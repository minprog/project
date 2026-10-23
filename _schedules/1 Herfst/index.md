# Programmeerproject <br><small>Studiewijzer Herfst 2026*</small>

> Binnen twee maanden vorm je van begin tot eind een eigen idee tot een ontwerp en vervolgens implementeer je een eigen applicatie in een modern software-framework. Je doet ervaring op met systematisch werken en documenteren van zo'n project en het uitzoeken van de kennis die je nodig hebt om het tot een succes te maken. Hierbij beperkt de staf zich tot het geven van feedback op de ideeën en het helpen oplossen van technische blokkades.

> *) **Let op!** Deze studiewijzer is nog niet definitief. Er kunnen nog een paar activiteiten wijzigen voordat het vak begint.

## Voorkennis

De vakken Programmeren 1 en Datarepresentaties, of Programmeren 1 en 2, moet je helemaal gehaald hebben vóór je deze cursus start.

## Kalender

<div markdown="1">
<ul class="nav nav-tabs" id="rooster-tabs" role="tablist">
<li class="nav-item" role="presentation"><button class="nav-link" id="tab-parttime" data-bs-toggle="tab" data-bs-target="#panel-parttime" type="button" role="tab" aria-controls="panel-parttime" aria-selected="false">Parttime</button></li>
<li class="nav-item" role="presentation"><button class="nav-link active" id="tab-fulltime" data-bs-toggle="tab" data-bs-target="#panel-fulltime" type="button" role="tab" aria-controls="panel-fulltime" aria-selected="true">Fulltime</button></li>
</ul>

<div class="tab-content rooster-box" markdown="1">

<div class="tab-pane fade" role="tabpanel" id="panel-parttime" aria-labelledby="tab-parttime" tabindex="0" markdown="1">

<div class="cal" data-track="Parttime"></div>

Volg je alleen het programmeerproject en niet Programmeren 2? Dan ga je tijdens de **eerste drie weken** aan de slag met de voorbereiding: het leren kennen van het platform waarmee je gaat werken.

Het project wordt gedaan volgens een aantal **milestones**. Na elke milestone bespreek je met je begeleider hoe je ervoor staat en hoe je verder kunt. De deadlines van versie 1 t/m 3 mag je met enkele dagen verschuiven als het strikt nodig is.

En de **afsluiting** vindt plaats met het opleveren van je definitieve project en de eindpresentaties. Deze data staan helemaal vast en kunnen niet aangepast worden.

| Onderdeel        | Tijdsbesteding |
| ---------------- | -------------: |
| Voorbereiding    |        ~40 uur |
| Projectvoorstel  |         ~8 uur |
| Projectvalidatie |        ~10 uur |
| Versie 1         |        ~20 uur |
| Versie 2         |        ~20 uur |
| Versie 3         |        ~20 uur |

</div>

<div class="tab-pane fade show active" role="tabpanel" id="panel-fulltime" aria-labelledby="tab-fulltime" tabindex="0" markdown="1">

<div class="cal" data-track="Fulltime"></div>

Volg je tegelijkertijd Programmeren 2 en het programmeerproject? Dan doe je de minor programmeren in fulltime. Je doet eerst grotendeels Programmeren 2, met daartussen de voorbereiding op het project (Finance en Books), en daarna werk je aan het programmeerproject. Voor een schema per dag voor de hele periode zie de [studiewijzer van Programmeren 2](https://prog2.proglab.nl/syllabus). Het programmeerproject start na de meesterproef op **vrijdag 27 november**.

Het project wordt gedaan volgens een aantal **milestones**. Na elke milestone ga je bespreken met je begeleider hoe je ervoor staat en hoe je verder kunt. De deadlines van versie 1 t/m 3 mag je met enkele dagen verschuiven als het strikt nodig is.

En de **afsluiting** vindt plaats met het opleveren van je definitieve project en de eindpresentaties. Deze data staan helemaal vast en kunnen niet aangepast worden.

| Onderdeel        | Tijdsbesteding |
| ---------------- | -------------: |
| Voorbereiding    |        ~40 uur |
| Projectvoorstel  |         ~8 uur |
| Projectvalidatie |        ~10 uur |
| Versie 1         |        ~20 uur |
| Versie 2         |        ~20 uur |
| Versie 3         |        ~20 uur |

</div>
</div>
</div>

<style>
#rooster-tabs .nav-item { margin-bottom: 0; }
.cal { margin: 0.75rem 0 1.5rem; --cal-grid: rgba(127,127,127,.3); --cal-prep: #5b6b8c; --cal-start: #0f766e; --cal-mile: #1d6fb8; --cal-end: #7a3fb0; }
.cal-row { position: relative; isolation: isolate; margin-bottom: 1.75rem; }
.cal-markers { position: relative; height: var(--mh); }
.cal-marker { position: absolute; bottom: calc(2px - var(--barh) - 18px); width: 0; border-left: 2px solid var(--c); z-index: 0; pointer-events: none; }
.cal-marker span { position: absolute; top: 0; left: 4px; white-space: nowrap; font-size: 12px; font-weight: 600; color: var(--c); line-height: 1.2; }
.cal-marker.right span { left: auto; right: 4px; text-align: right; }
.cal-weeks { height: 18px; display: grid; grid-template-columns: repeat(4, 1fr); font-size: 11px; opacity: .65; }
.cal-weeks div { padding: 0 0 2px 4px; border-left: 1px solid var(--cal-grid); }
.cal-bar { position: relative; height: var(--barh); border-bottom: 1px solid var(--cal-grid); }
.cal-day { position: absolute; top: 0; bottom: 0; border-left: 1px dotted var(--cal-grid); }
.cal-day.wk { border-left: 1px solid var(--cal-grid); }
.cal-seg { position: absolute; z-index: 1; top: 0; height: 52px; border-radius: 4px; color: #fff; overflow: hidden; padding: 3px 5px; display: flex; flex-direction: column; justify-content: space-between; font-size: 12px; line-height: 1.15; border: 1px solid #fff; }
.cal-seg b { font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.cal-seg .d { flex: 1; white-space: nowrap; display: flex; justify-content: space-between; font-size: 10px; opacity: .92; gap: 2px; }
.cal-seg.cl-l { border-top-left-radius: 0; border-bottom-left-radius: 0; }
.cal-seg.cl-r { border-top-right-radius: 0; border-bottom-right-radius: 0; }
.cal-seg.t-prep { background: var(--cal-prep); }
.cal-seg.t-start { background: var(--cal-start); }
.cal-seg.t-mile { background: var(--cal-mile); }
.cal-seg.t-end { background: var(--cal-end); }
.cal-seg.t-prog2 { background: #e3e5ea; color: #555; }
</style>
<script>
(function () {
  var START = '2026-10-26', WEEKS_PER_ROW = 4, ROWS = 2, PER_ROW = WEEKS_PER_ROW * 5, BAR_HEIGHT = 52;
  var PREP = 'var(--cal-prep)', MILE = 'var(--cal-mile)', END = 'var(--cal-end)';
  var closing = [
    { name: 'Definitieve versie', from: '2026-12-14', to: '2026-12-17', type: 'end', hideEnd: true },
    { name: 'Pr', from: '2026-12-18', to: '2026-12-18', type: 'end', hideEnd: true }
  ];
  var tracks = {
    Parttime: {
      segs: [
        { name: 'Finance', from: '2026-10-27', to: '2026-10-30', type: 'prep' },
        { name: 'Books', from: '2026-11-02', to: '2026-11-05', type: 'prep' },
        { name: 'Voorstel', from: '2026-11-06', to: '2026-11-10', type: 'start' },
        { name: 'Validatie', from: '2026-11-11', to: '2026-11-20', type: 'mile' },
        { name: 'Versie 1', from: '2026-11-23', to: '2026-11-27', type: 'mile' },
        { name: 'Versie 2', from: '2026-11-30', to: '2026-12-04', type: 'mile' },
        { name: 'Versie 3', from: '2026-12-07', to: '2026-12-11', type: 'mile' }
      ].concat(closing),
      markers: [
        { name: 'Intake, di 10:00', at: '2026-11-03', frac: .2, color: PREP, level: 0 },
        { name: 'Introductie, 11:00', at: '2026-10-27', frac: .3, color: PREP, level: 1, align: 'left' },
        { name: 'Walkthrough, vr 11-15', at: '2026-12-04', frac: .5, color: MILE, level: 0 },
        { name: 'Groepseval., vr 11-15', at: '2026-12-11', frac: .12, color: MILE, level: 0 },
        { name: 'Def. versie, do 20:00', at: '2026-12-17', frac: .83, color: END, level: 1 },
        { name: 'Eindpresentaties, vr 10-18', at: '2026-12-18', frac: .9, color: END, level: 0 }
      ]
    },
    Fulltime: {
      fill: 'Prog2',
      segs: [
        { name: 'Finance', from: '2026-11-04', to: '2026-11-05', type: 'prep' },
        { name: 'Books', from: '2026-11-17', to: '2026-11-19', type: 'prep' },
        { name: 'Voorstel', from: '2026-11-27', to: '2026-11-30', type: 'start' },
        { name: 'Validatie', from: '2026-12-01', to: '2026-12-02', type: 'mile' },
        { name: 'Versie 1', from: '2026-12-03', to: '2026-12-04', type: 'mile' },
        { name: 'Versie 2', from: '2026-12-07', to: '2026-12-08', type: 'mile' },
        { name: 'Versie 3', from: '2026-12-09', to: '2026-12-11', type: 'mile' }
      ].concat(closing),
      markers: [
        { name: 'Introductie, ma 10:00', at: '2026-10-26', frac: .3, color: PREP, level: 0, align: 'left' },
        { name: 'Intake, do 18:00', at: '2026-11-12', frac: .75, color: PREP, level: 0 },
        { name: 'Walkthrough, ma-di', at: '2026-12-08', frac: .12, color: MILE, level: 1 },
        { name: 'Groepseval., do 11-15', at: '2026-12-11', frac: .12, color: MILE, level: 0 },
        { name: 'Def. versie, do 20:00', at: '2026-12-17', frac: .83, color: END, level: 1 },
        { name: 'Eindpresentaties, vr 10-18', at: '2026-12-18', frac: .9, color: END, level: 0 }
      ]
    }
  };
  function parse(s) { return new Date(s + 'T00:00:00'); }
  function short(s) { var d = parse(s); return d.getDate() + '/' + (d.getMonth() + 1); }
  // Counts workdays (mon-fri) from START; weekends have no width.
  function workday(s) {
    var days = Math.round((parse(s) - parse(START)) / 864e5);
    return Math.floor(days / 7) * 5 + Math.min(days % 7, 5);
  }
  function pct(i) { return (i / PER_ROW * 100) + '%'; }
  // Returns boxes for the workdays that no segment covers.
  function gaps(t) {
    var covered = [], out = [], start = null, n = ROWS * PER_ROW, i;
    t.segs.forEach(function (s) { for (i = workday(s.from); i <= workday(s.to); i++) covered[i] = true; });
    for (i = 0; i <= n; i++) {
      if (i < n && !covered[i]) { if (start === null) start = i; }
      else if (start !== null) { out.push({ name: t.fill, a: start, b: i, type: 'prog2', noDates: true }); start = null; }
    }
    return out;
  }
  function renderRow(t, r) {
    var lo = r * PER_ROW, hi = lo + PER_ROW, h = '';
    var ms = t.markers.map(function (m) { return Object.assign({}, m, { x: workday(m.at) + m.frac }); })
      .filter(function (m) { return m.x >= lo && m.x <= hi; });
    var mh = ms.length ? 20 + 20 * (1 + Math.max.apply(null, ms.map(function (m) { return m.level; }))) : 8;
    h += '<div class="cal-row" style="--barh:' + BAR_HEIGHT + 'px;--mh:' + mh + 'px"><div class="cal-markers">';
    ms.forEach(function (m) {
      h += '<div class="cal-marker' + (m.align === 'left' ? '' : ' right') + '" style="left:' + (m.x - lo) / PER_ROW * 100 + '%;--c:' + m.color + ';top:' + m.level * 18 + 'px"><span>' + m.name + '</span></div>';
    });
    h += '</div><div class="cal-weeks">';
    for (var w = 0; w < WEEKS_PER_ROW; w++) h += '<div>wk ' + (r * WEEKS_PER_ROW + w + 1) + '</div>';
    h += '</div><div class="cal-bar">';
    for (var i = 0; i < PER_ROW; i++) h += '<div class="cal-day' + (i % 5 ? '' : ' wk') + '" style="left:' + pct(i) + '"></div>';
    t.segs.concat(t.fill ? gaps(t) : []).forEach(function (s) {
      var a = s.noDates ? s.a : workday(s.from), b = s.noDates ? s.b : workday(s.to) + 1;
      if (b <= lo || a >= hi) return;
      var l = Math.max(a, lo), e = Math.min(b, hi);
      h += '<div class="cal-seg t-' + s.type + (a < lo ? ' cl-l' : '') + (b > hi ? ' cl-r' : '') + '" title="' + s.name + (s.noDates ? '' : ': ' + short(s.from) + ' - ' + short(s.to)) + '" style="left:' + pct(l - lo) + ';width:' + (e - l) / PER_ROW * 100 + '%">' +
        '<b>' + (s.noDates && e - l < 2 ? '' : s.name) + '</b>' + (s.noDates ? '' : '<span class="d"><span>' + (a < lo ? '' : short(s.from)) + '</span><span>' + (b > hi || s.hideEnd ? '' : short(s.to)) + '</span></span>') + '</div>';
    });
    return h + '</div></div>';
  }
  document.querySelectorAll('.cal[data-track]').forEach(function (el) {
    var t = tracks[el.dataset.track], h = '';
    for (var r = 0; r < ROWS; r++) h += renderRow(t, r);
    el.innerHTML = h;
  });
})();
</script>

## Staff

Jelle van Assema en Martijn Stegeman zijn de docenten bij het vak. Je kan ze via e-mail bereiken op <help@mprog.nl>.

## Contact

Tijdens dit vak zul je regelmatig de hulp inroepen van de staff en medestudenten. Er zijn diverse opties voor het stellen van vragen. De beste optie hangt af van het soort vraag dat je wil stellen.

**Werkcolleges en assistentie:** direct contact voor hulp bij programmeren.

- hulp op locatie
- je weet niet waar te beginnen of je zit met een onvindbare bug
- je hebt moeite met het verzinnen van een oplossing
- kwestie van binnenlopen!

**E-mail:** contact met de docent.

- maken van persoonlijke planningsafspraken
- meedenken over grote problemen met het vak
- andere officiële zaken
- administratie na afloop van het vak
- mail naar <help@mprog.nl>

## Minimumeisen

Om de cursus tot een goed einde te brengen, verwachten we dat je:

1. wekelijks contact hebt met je begeleider,
1. een interessant en voor jou leerzaam project implementeert en inlevert,
1. goed werk steekt in de milestones voor je project,
1. gebruik maakt van git en dagelijks je voortgang pusht naar github,
1. regelmatig vragen stelt.

Let op dat je minimaal aan bovenstaande verwachtingen moet voldoen om een eindcijfer te kunnen halen.

## Beoordeling

Naast de minimumeisen hierboven moet je project op GitHub staan. In de repository staat de code voor het project en de bijbehorende documentatie. Er moet een zodanige hoeveelheid code en documentatie zijn dat beoordeling goed mogelijk is (naar oordeel van de docent).


* Cijfer 5: een onvoldoende afgerond project waar aantoonbaar wel flink werk in is gestoken, zoals ook aangetoond door reflectie bij de milestones en commits op GitHub; zo'n project zou in een later semester zonder al te veel inzet afgerond kunnen worden.
* Cijfer 6: een basisproject waar duidelijk inzet in zit, zoals aangetoond door de reflecties bij de milestones en commits; er is weinig diepgang ten opzichte van tutorials of de gedane oefenprojecten; er is voldoende aandacht voor nette code, repository, en documentatie.
* Cijfer 7: een eigen project dat stevig leunt op tutorials, voorbeelden of de gedane oefenprojecten (bijvoorbeeld door hergebruik van code); voldoende inzet in uitzoeken van leerzame dingen, zoals aangetoond door reflectie en commits; zichtbare aandacht voor nette code, repository, en documentatie van zowel het project als de code met een voldoende resultaat.
* Cijfer 8: een eigen project waarvoor enkele technieken uitgezocht zijn die niet als zodanig aangeboden worden in tutorials of eerder werk, en waarvoor dus leerzame ontwerp-uitdagingen zijn aangegaan, zoals aangetoond door reflectie en commits; zichtbare aandacht voor nette code, repository en documentatie van zowel het project als de code met een goed resultaat.
* Cijfer 9: een eigen project met een creatieve eigen insteek, waarvoor diverse technieken zijn uitgezocht die niet als zodanig aangeboden worden in tutorials of eerder werk, en waarvoor dus flinke ontwerp-uitdagingen zijn aangegaan, zoals aangetoond door reflectie en commits; zeer nette code, repository en documentatie van zowel het project als de code. Daardoor is het project goed over te nemen door een andere programmeur om verder te ontwikkelen.
* Cijfer 10: een zelfgedefinieerd project dat uitblinkt in originaliteit en complexiteit, waarvoor grote ontwerp-uitdagingen zijn aangegaan die niet in het verlengde liggen van tutorials of eerder uitgewerkte projecten, zoals aangetoond door reflectie en commits; het project zou zonder grote wijzigingen kunnen worden gepubliceerd als website, paper of onderzoeksresultaat; de code, repository en documentatie zijn daarom ook uitstekend en specifiek gericht op verder ontwikkelen en hergebruik.

In de beschrijving hierboven staan de **minimumeisen** voor elk cijfer: al deze eisen moeten dus gehaald worden om in aanmerking te komen voor het genoemde cijfer. Voor een 8 moet er project staan op basis van zelf-uitgezochte technieken, en ook duidelijke aandacht voor nette code, repo en docs. Stel dat het project uitdagend is, de code netjes, maar de documentatie is niet voldoende, dan past daar niet het cijfer 8 bij.

## Samenwerken

Al het werk dat je doet om aan bovenstaande verwachtingen te voldoen moet je eigen werk zijn.

- Ideeën en technieken die je kent uit de reviews van andermans code en uit de feedback die je krijgt van anderen mag je gerust gebruiken, als je maar duidelijk de ideeën toeschrijft via comments in je code.

- Je mag ideeën voor projecten, inclusief designs, bespreken met anderen, om feedback te verkrijgen en te geven, maar je mag geen _code_ delen met anderen.

In andere woorden: je mag met je medestudenten (en anderen) communiceren in het Nederlands of Engels over je werk in deze cursus, maar niet in de vorm van meer dan een paar regels Python, JavaScript, HTML en dergelijke talen. Als je twijfelt of je manier van werken in deze correct is, neem gerust contact op met de docent.

### Citeren en hulpbronnen

Je mag gerust op het web zoeken naar uitleg die verder gaat dan de colleges en andere materialen die in de cursus bijgeleverd zijn, en je mag op zoek naar oplossingen voor technische problemen waar je tegenaan loopt, maar je mag zeker geen oplossingen voor deelproblemen van de opdrachten overnemen om aan de eisen te voldoen. Daarnaast moet je bij het geheel of gedeeltelijk overnemen van codefragmenten of werken via tutorials en dergelijke altijd een precieze bronvermelding doen.

### Officiële regels

Wat betreft fraude en plagiaat volgen we in deze cursus de richtlijnen van de Universiteit van Amsterdam en de werkwijze van de bachelor Informatica. De richtlijnen kun je [hier vinden](http://student.uva.nl/az/a-z-lijst/a-z-lijst/content/folder/fraude-plagiaat-en-bronvermelding/plagiaat-en-fraude.html).

## Herkansen

Het vak bestaat uit een hoeveelheid projecten die binnen de gestelde tijd afgemaakt moeten worden. Red je het niet binnen de tijd, dan kun je doorgaans het vak afmaken in een later semester. De projecten worden echter niet _standaard_ overgezet. Je moet altijd zelf contact opnemen vóór de start van een nieuwe editie van het vak om afspraken te maken over het meenemen van de oude opdrachten en het verder afmaken van de resterende. Het overzetten is afhankelijk van de beschikbaarheid van expertise en de mate waarin je project al was afgerond.

## Dankbetuiging/Acknowledgements

Some of the materials in this course have been based on other courses that were generously published under a creative commons license. Many thanks to:

- Brian Yu and David Malan, [CSCI S-33a at Harvard](https://cs50.harvard.edu/extension/web/2019/spring/syllabus/), published 2019 under a Creative Commons Attribution-Noncommercial-Share Alike 3.0 Unported license.

- David Malan, [CS164 at Harvard](http://cs164.tv/2012/spring/), published 2012 under a Creative Commons Attribution-Noncommercial-Share Alike 3.0 Unported license.
