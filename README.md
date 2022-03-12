# afkcode.com
This project will contain my personal portfolio website, which is primarily intended for school projects for now.

## Project Goals
- [x] Create a self-contained portfolio website using [Django](https://www.djangoproject.com/) that can be easily deployed to an inexpensive VPS
- [ ] Showcase projects from each of my classes as I progress through my [Computer Science undergrad at CSUMB](https://csumb.edu/csonline/).
- [ ] Migrate my existing Learning Journal content from Blogger and post all future content on this new project

## Tech Stack
- Services: 
  - CloudFlare nameservers and proxy
  - DigitalOcean Droplet (Ubuntu VPS)
  - Dokku-managed Docker container
  - LetsEncrypt SSL cert
- Web server: nginx reverse proxy to gunicorn
- Databases: SQLite for local development, PostgreSQL for production
- Frameworks: Django 4, Bootstrap 5
- Languages: Python, HTML, CSS, JavaScript


## What I learned 

### Django
Initially I followed [this excellent tutorial by Jasmine Finer](https://realpython.com/get-started-with-django-1/) for creating basic versions of the blog and projects apps before building the rest on my own. This was an excellent starter project that helped me understand Django's MVC workflow just enough to start building what I want on a foundation of two very practical and usable examples. It also casually ignored some problems that you're bound to run into if you continue to build on those projects, but I learned a lot by banging my head against those. No spoilers.
 
### CSS Libraries
I was initially hesitant to embrace [Bootstrap](https://getbootstrap.com/) because it felt like giving up a lot of control over my own design in order to learn a framework I don't really need, but it's hard not to appreciate how much time you save and how little code it requires to create attractive and responsive pages, especially on a school assignment deadline.

At one point I got frustrated with Bootstrap and switched to [Tailwind](https://tailwindcss.com/), but found that the build process did not fit into my workflow as nicely as I'd hoped. Deploying to Django and dokku requires a specific project structure that is not compatible with PyCharm's code completion for Tailwind, and I didn't want to have to switch the project to VS Code and lose PyCharm's other handy features (especially the debugger!).  

### PostgreSQL
Django's ORM handles the queries, but I had to install and configure the database first. (While I *could* write the SQL myself, I'm actually looking forward to a more maintainable project without a bunch of stringified queries, which is also a huge benefit if I ever want to change database servers in the future.)  Eventually I switched to a Dokku build process, which automates most of the database setup. More on that below.

### DigitalOcean
Droplets are awesome. $5/month to host my Django app is hard to pass up, especially when [GitHub's student developer pack](https://education.github.com/pack) comes with a $100 DigitalOcean credit that should cover this site for most of my undergrad.

DigitalOcean's "App Platform" is another very compelling deployment option since it can link directly to GitHub or Gitlab and update itself whenever you push new changes, but unfortunately they want an additional $7/month just to host your database if you go this route. (More on git deployment in the next heading.)

### Dokku / Heroku commands
[Dokku](https://dokku.com/) is a PaaS service that is very similar to [Heroku](https://www.heroku.com/), except that it's self-hosted.  By installing Dokku on a cheap droplet, we gain the convenience of Heroku's time-saving deployment features without the high price tag. Dokku handles configuring a few things for us and exposes a nice API for others, including:
- Building directly from a remote git repo to a [Docker](https://www.docker.com/) container
- Automatically configuring [nginx](https://www.nginx.com/) with a reverse proxy to [gunicorn](https://gunicorn.org/)
- Managing project-specific environment variables
- Managing SSL certs, including a cron job for auto-renewal ([requires a plugin](https://github.com/dokku/dokku-letsencrypt))

### CloudFlare
Pointing my domain registrar to CloudFlare's nameservers provides a nicer interface for managing DNS records and an easy-to-use proxy server with lots of additional functionality including caching, DDoS protection, and some basic monitoring that lets me easily see if my webserver's returning errors.

### DevOps is hard
I spent almost 4 days just getting static images to work in production.  I tore my hair out and nearly swore off Django because of how frustrating the deployment process was initially, but fixing it forced me to learn a lot about every layer of the tech stack that I'm using.

The solution I settled on involves adding the [whitenoise](http://whitenoise.evans.io/en/stable/) module to my Django config to allow it to serve static files directly to the gunicorn webserver from inside the container. The whitenoise docs have a nice writeup on [why this is actually a preferable solution to something like S3](http://whitenoise.evans.io/en/stable/#shouldn-t-i-be-pushing-my-static-files-to-s3-using-something-like-django-storages). The other option would have been to write an nginx [sigil template](https://dokku.com/docs/configuration/nginx/#customizing-the-nginx-configuration) and then add a post-build script to copy all of my files outside of the container so that nginx can serve them directly.

## Recommendations

To anyone looking to tackle a similar project, [this is the tutorial I wish I had when I started the deployment process](https://www.accordbox.com/blog/how-deploy-django-project-dokku/). It's not super in-depth, but there are so many pearls of knowledge here, some of which took me a lot of time to find by digging through documentation and stackoverflow searches.