# Webservers: Reverse Proxy
To handle requests from the web you'll need a dedicated program that listens on specified ports (80 for http and 443 for https) and that can redirect those requests to designated end-points.

Two of the most popular options to do this are Apache and NGINX. They will act as a reverse proxy server, intercepting requests from the web and relaying those requests to your application(s) running behind it. This is because when you have multiple applications running behind your reverse proxy, you need some sort of specialized technology to divert all those requests to the correct application. 

You can find out more about reverse proxies [here](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/). 

## Apache vs NGINX

Both Apache and NGINX are more than up to the task of handling requests on our VPS. If you'd like some help choosing which one to use, check out [this](https://kinsta.com/blog/nginx-vs-apache/) article on their differences.

Do note that they are very different in configuration and use, and once you've got one setup with your application, it is not easy to migrate to the other.
* Installing [Apache](https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04)
* Installing [Nginx](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04)