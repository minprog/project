
# Health code inspections

> Deze opdracht gaat door op yelp deel 1. Zorg dat je die opdracht in ieder geval hebt doorgelezen voordat je aan deze opdracht begint. Heb je het eerste deel niet gemaakt, download dan [hier](data/Seattle_Health_Code.zip) de notebook en [hier](data/transformation_YELP.ipynb) de data voor dat deel. Zorg dat je de code runt en begrijpt voordat je verder gaat met het tweede deel. Let op! Deze notebook heeft bij het samenvoegen van de restaurants en de reviews een iets andere methode gebruikt dan omschreven in de opdracht. Zorg dat je begrijpt hoe beide manieren werken en zorgen voor hetzelfde resultaat.

The second part of this exercise continues upon the first part, and will be programmed in the same Jupyter Notebook: `transformation_YELP.ipynb`.

## Processing the combined data

Now that we have all the data combined in a single structure, we can finally
start processing it. As the reviews are all just raw text data, we'll
definitely need to do some processing. For this we'll use the `nltk`
package, which stands for Natural Language ToolKit. Try to import the package
and see if it is already installed on your machine. If not, follow the
instructions [here](https://www.nltk.org/install.html).

We'll use a couple of very basic `nltk` features for processing the text;
tokenization and stop words. Tokenization splits the text into words, which is
essentially splitting on *spaces*, but also takes things like punctuation into
account. Also, some words are so common that we want to filter them from
processing altogether, like the word *"the"*. These words are called
*stopwords* and `nltk` has standard lists for many languages. Include the
following code to load the list for English:

    import nltk

    nltk.download('punkt')
    nltk.download('stopwords')

    stop_words = set(nltk.corpus.stopwords.words("english"))


> #### Sidenote: Sets
>
> Since we only want to search if each word is contained in the list of
> stopwords, we'll use a **set** instead of a list. Using a set here converts
> each search from $$O(N)$$ to $$O(1)$$.

No need to write any further code for this step, here we've just set up the
tools we'll be needing for the next steps.

### Processing the violations

To answer our research question *"Are there any words whose presence in a Yelp
review might indicate that there is a serious health code violation present at
a restaurant?"*, we'll need to distinguish between restaurants that are
generally clean and ones that have serious health code violations. These
restaurants are most likely to have reviews with distinguishing words, as
something like unlabeled food in the fridge is unlikely to directly affect the
customer reviews. Take a look at the data containing the inspection results and
see if you can come up with any good criteria for filtering these results.

While defining your own criteria is a useful exercise, let's start out with
using a predefined set, so we can refer to the same results for the next few
steps. What I ended up selecting was just filtering on `'Inspection Score'`,
which seemed descriptive on how good or bad the inspection was, and also easy
enough to filter. If a restaurant has had several inspections, I just used the
maximum score, so the worst inspection the restaurant has ever gotten, as that
seemed like it would give the best indication of health code standards.

Looking at the type of violations listed in the inspection results, I ended up
settling on the following criteria: any restaurant with a maximum score under $$20$$ is a generally
clean restaurant, while a maximum score over $$70$$ indicates serious health
code violations. This also results in a nice distribution of approximately 120
restaurants labeled as clean and 120 as serious violations.

Loop over the dictionary containing all the data and divide the businesses and
their reviews into two lists; one list containing all the businesses considered
clean and one with businesses who had serious violations. You can ignore the
businesses that do not meet either criteria or do not have any inspection
results for now. You should end up with approximately 120 businesses in each
list.

### Processing the reviews

Next, we'll actually process those reviews in both lists. Use the `nltk`
function [word_tokenize()](https://www.nltk.org/api/nltk.tokenize.html#module-nltk.tokenize)
to split the text of each review into words. Convert all words to lowercase and
remove any "words" that contain non-alphabetic characters (e.g. punctuation) or
words that are a part of the set of stopwords.

The processed result should still consist of 2 lists, 1 for clean restaurants
and 1 for those with violations. Within both these lists, all the processed
words for a one business should be merged into a single list. So, *both lists
should consist of multiple lists of words, each containing all the processed
words in all reviews for one specific restaurant.*

### Counting word occurrences

Now, let's start with simply counting how often words occur in the clean
restaurant reviews and how often they occur in the reviews of those with
violations. Start out by combining all the lists with words for each business
to a single list, which is called flattening the list. There are many ways to
flatten a list in Python, I prefer using the [chain()](https://docs.python.org/3/library/itertools.html#itertools.chain)
function, but any flattening method will do. Do not discard/overwrite the
unflattened versions of the lists, as we *might* need them later on. The end
result of this transformation should be two massive flat lists of words, one
for each type of restaurant.

Next, use the built-in [Counter](https://docs.python.org/3/library/collections.html#counter-objects)
object to count how often elements occur in a list. Then, select the 25
[most_common()](https://docs.python.org/3/library/collections.html#collections.Counter.most_common)
words for both lists and print them.

### Defining some better metrics

It seems as though there is a pretty generic formula for Yelp reviews, as the set
of most common words appears to be nearly *identical* in both cases. This could
have quite a few different causes; it could be because we're not filtering for
the serious violations correctly, or that a single serious violation does not
imply all bad reviews. For now, we'll assume both of those are *not* the issue
and that some people (or bots) writing Yelp reviews are just not that creative.
So, instead, we will define a better ordering metric than just the most common
word and try to distinguish the two types of restaurant that way.

As there are so many commonalities between the word lists, a logical next step
would be to try to find words that are common in reviews of restaurants with violations,
but uncommon in reviews of clean restaurants. For now, we'll just focus on the
words that *do* actually occur in *both* lists, so we'll need to construct a
set containing these common words. As you may have already noticed, `Counter`
objects are actually just dictionaries with a couple extra features.
Additionally, the `.keys()` function returns a set-like [view of the dictionary](https://docs.python.org/release/3.3.0/library/stdtypes.html#dict-views),
so computing the [intersection()](https://docs.python.org/3/library/stdtypes.html#frozenset.intersection)
of words occurring in both *key-sets* should actually be pretty easy.

Using this set of words occurring in both `Counter` objects, we'll build a new
dictionary where we normalize the count of every word by dividing it by the
total count for that type of restaurant, making the values for both types
more comparable. Then, we'll use the ratio between the normalized counts of both
types to assign a final score to each word.

$$score\_word = \dfrac{\frac{violations\_word\_count}{total\_violations\_count}}{\frac{clean\_word\_count}{total\_clean\_count}}$$

Dividing by the normalized count of how often a word occurs in reviews of
restaurants with *clean* inspection results should give words that occur
in those restaurants *less* a higher score. This combined rating for each word,
based on the counts for both lists, can then be sorted to find the top 50 words
with the highest score. Use the built-in function [sorted()](https://docs.python.org/3/library/functions.html#sorted)
to construct this top 50 of words and print the results.

> #### Sidenote: Origins of this metric
>
> Dividing by the normalized count of how often a word occurs in reviews of
> restaurants with *clean* inspection results, might seem like a somewhat
> arbitrary way to filter out common words. In essence, it is, and the only
> real indication we have of it making any sense, is if it actually produces a
> better list of words. However, it does also have some theoretical foundation,
> which might be interesting to note. The metric was heavily inspired by
> [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf), which is a widely
> used metric in information retrieval for improving search results.

### Tweaking the metric further

The results from this metric seem to mostly produce names of dishes or even
specific restaurants that correspond to serious violations. What we would
actually like in our top 50 words are general trends among the *different*
restaurants. For this new metric we can reuse most of the code from the
previous metric, we'll only need to adjust how exactly words are counted.

So, instead of counting how many times a word occurs overall in either list, we
should *count in how many of the different business reviews it occurs*. The
easiest way to do that is to take the *unflattened* list of reviews, remove
duplicate words for each business, and then flatten the results. Applying a
`Counter` to this flattened list should return in how many different
restaurants' reviews this word is mentioned. The rest of the metric can be left
exactly as is, just use this new count dictionary to compute the score for each
word, sort and print the top 50 words.

### Final improvements

This metric definitely isn't perfect, but it produces some interesting words in
the top 50 list, most notably *inspector/inspection* and *cockroach/roach*.
There are plenty more improvements possible to get the list of words even more
representative:

* Improve the definition of *clean* and *severe violations*, so the reviews are
separated more accurately.

* Create a general model for common food terms or specific dishes, so those can
be filtered from the top 50 distinguishing words.

* Use the exact time window of the inspection to filter reviews that are more
likely to be related to results of the inspection.

* Tweak the word scoring in some other way and see if this improves the results.

Implement _at least two_ of these extensions or come up with your own improvements
and print the final top 50 of most indicative words.

**In your notebook, clearly state for each of your extensions what you did to improve your top 50, and whether your extension truly improved it.** Finally, compare your different extensions. You could, for
example, list advantages and disadvantages of each of your methods, and explain
why you would use a specific extension over another in specific situations.

> Disclaimer: not having "cockroach/roach" and/or "inspection/inspection" does not _immediately_ mean that something's wrong with your code. Try checking with your TA if you're not sure.

<!--
## Yelp API

Now that you have a good list of words to monitor for in *Yelp* reviews, you
can build a program that does exactly that! Yelp also offers *API* end points
where you can just send requests for specific data and get some *JSON* data
back. From there, building a monitoring system is quite straightforward,
especially considering you already wrote code to load the JSON objects and
process the review text.

For a general introduction on what an API is and how to use it, read the blog
post [here](https://www.dataquest.io/blog/python-api-tutorial/). Note that the
`requests` library should already be installed for you, so there is no need to
install it again.

Then, take a look at the documentation for the Yelp [api](https://docs.developer.yelp.com/),
specifically the end points [search](https://docs.developer.yelp.com/reference/v3_business_search)
and [reviews](https://docs.developer.yelp.com/reference/v3_business_reviews).

In addition, you will need to provide the API with an API key. To get the API key, register
[here](https://www.yelp.com/login?return_url=%2Fdevelopers%2Fv3%2Fmanage_app).
In the create new app form, enter information about your app, then agree to the
"Yelp API Terms of Use and Display Requirements". You can then use this key as
follows:

    api_key = 'copy_your_api_key_here'
    headers = {'Authorization': f'Bearer {api_key}'}
    req = requests.get(url, params=params, headers=headers)

> Note that most APIs only allow you to send a limited amount of requests every
day (in this case 500 every day). Instead of re-running the code every time you
change or add something, try to create separate cells that you only have to
run once. This will prevent you from accidentally getting blocked for the rest
of the day.

Write a program to actively monitor Yelp for **50** new restaurants in Seattle
which get reviews that contain words from your top most indicative words for
health code violations and add these to a list for future inspections by the
*Washington State Department of Health*. Print the names of these restaurants
and the words that indicated a violation for these restaurants.

> It is entirely possible that there are no restaurants that have reviews that
contain one or more of the words in your top 50 indicative words at all. In
that case, include a word of which you are sure that it is in one of the
reviews as a proof of concept. -->
