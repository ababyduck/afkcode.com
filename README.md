# afkcode.com
This project will contain my personal portfolio website, which is primarily intended for school projects for now.

## Goals
- [x] Create a self-contained portfolio website using [Django](https://www.djangoproject.com/) that can be easily deployed to an inexpensive VPS
- [ ] Showcase projects from each of my classes as I progress through my [Computer Science undergrad at CSUMB](https://csumb.edu/csonline/).
- [ ] Migrate my existing Learning Journal content from Blogger and post all future content on this new project

## Tech Stack
- Services: 
  - CloudFlare nameservers and proxy
  - LetsEncrypt SSL cert
  - DigitalOcean Droplet (Ubuntu VPS)
  - Dokku-managed container
- Web servers: nginx handles static data, reverse proxies the rest to gunicorn
- Databases: SQLite for local development, PostgreSQL for production
- Frameworks: Django 4, Bootstrap 5
- Languages: Python, HTML, CSS


## What I learned 

### Django
Initially I followed [this excellent tutorial by Jasmine Finer](https://realpython.com/get-started-with-django-1/) for creating basic versions of the blog and projects apps before building the rest on my own. This was an excellent starter project that helped me understand Django's MVC workflow just enough to start building what I want on a foundation of two very practical and usable examples. It also casually ignored some problems that you're bound to run into if you continue to build on those projects, but I learned a lot by banging my head against those. No spoilers.
 
### Bootstrap
I was hesitant to embrace Bootstrap's class library because it feels like giving up some design control to learn another framework that I don't *need*, but it's hard to argue with the value of time saved creating a responsive page that looks familiar to users, especially on a school assignment deadline. 

### PostgreSQL
Django's ORM handles the queries, but I had to install and configure the database first. (While I *could* write the SQL myself, I'm actually looking forward to a more maintainable project without a bunch of stringified queries, which is also a huge benefit if I ever want to change database servers in the future.)  I did eventually start using Dokku, which automates most of the database setup. More on that below.

### DigitalOcean
Droplets are awesome. $5/month to host my Django app is hard to pass up, especially when [GitHub's student developer pack](https://education.github.com/pack) comes with a $100 DigitalOcean credit that should cover this site for most of my undergrad.  DigitalOcean's "App Platform" is another very compelling deployment option since it can link directly to GitHub or Gitlab and update itself whenever you push new changes, but unfortunately they want an additional $7/month just to host your database if you go this route. (More on git deployment in the next heading.)

### Dokku / Heroku commands
[Dokku](https://dokku.com/) is a PaaS service that is very similar to [Heroku](https://www.heroku.com/), except that it's self-hosted.  By installing Dokku on a cheap droplet, we gain the convenience of Heroku's time-saving deployment features without the high price tag. Dokku handles configuring a few things for us and exposes a nice API for others, including:
- Building directly from a remote git repo to a [Docker](https://www.docker.com/) container
- Automatically configuring [nginx](https://www.nginx.com/) with a reverse proxy to [gunicorn](https://gunicorn.org/)
- Managing project-specific environment variables
- Managing SSL certs, including a cron job for auto-renewal ([requires a plugin](https://github.com/dokku/dokku-letsencrypt))

### CloudFlare
Pointing my domain registrar to CloudFlare's nameservers provides a nicer interface for managing DNS records and an easy-to-use proxy server with lots of additional functionality including caching, DDoS protection, and some basic monitoring that lets me easily see if my webserver's returning any error codes on incoming traffic.