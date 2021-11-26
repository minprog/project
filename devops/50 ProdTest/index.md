# Your First App (continued)

Now that we have a reverse proxy able to relay requests to our containerized applications running behind it, it's time to put it to the test. 

Configure your webserver to relay requests to the port that your application is listening on. 
  * For Apache [vhost setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-ubuntu-18-04-quickstart) and [reverse proxy](https://limeproxies.netlify.app/blog/step-by-step-guide-to-configure-apache-reverse-proxy/) 
  
  * For Nginx [vhost setup](https://www.tecmint.com/create-nginx-server-blocks-in-ubuntu/) and [reverse proxy](https://bitlaunch.io/blog/how-to-use-nginx-as-a-reverse-proxy-on-ubuntu-20-04/)