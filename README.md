# afkcode.com
This project will contain my personal portfolio website, which is primarily intended for school projects for now.

## Goals
- Create a self-contained [Django](https://www.djangoproject.com/) based portfolio website that can be easily deployed to an inexpensive VPS
- Showcase projects from each of my classes as I progress through my [Computer Science undergrad at CSUMB](https://csumb.edu/csonline/).
- Migrate my existing Learning Journal content from Blogger and post all future content on this new project

## What I learned
- **DigitalOcean Droplets:** Droplets are awesome. $5/month to host my Django app is hard to pass up, especially when [GitHub's student developer pack](https://education.github.com/pack) comes with a $100 DigitalOcean credit.  DigitalOcean's "App Platform" is also very compelling since it can link directly to GitHub or Gitlab and update itself whenever you push new changes, but unfortunately they want an additional $7/month just to host your database if you go this route.
- **Dokku**: Dokku is a PaaS service similar to heroku, except that it's self-hosted.  By installing Dokku on a cheap droplet, we gain the convenience of heroku's time-saving deployment features without the high price tag. 
- **Django:** Initially I followed [this excellent tutorial by Jasmine Finer](https://realpython.com/get-started-with-django-1/) for creating basic versions of the blog and projects apps before building the rest on my own. This was an excellent starter project that helped me understand the Django workflow just enough to get begin building what I want on a foundation of two very practical and usable examples.
- **Bootstrap 5:** I was hesitant to give up total control and embrace Bootstrap's class library, but it's hard to argue with the value of time saved creating a page that looks familiar to users, especially on a tight deadline for school.
- **PostgreSQL:** Django's ORM handles the queries, but I still had to install and configure it. This project uses SQLite for development and PostgreSQL for  production.
