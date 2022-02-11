# afkcode.com
This project will contain my personal website, which is primarily intended for school projects for now.

## Planned features:
- Self-contained website based on the [Django](https://www.djangoproject.com/) web framework for Python, to be hosted within a DigitalOcean droplet
- Portfolio page to showcase projects from each of my classes as I progress through my [Computer Science undergrad at CSUMB](https://csumb.edu/csonline/).
- Learning blog: Will migrate my existing content from Blogger and post all future content here

## What I learned:
- **Deploying to a DigitalOcean "droplet":** Droplets are awesome. $5/month to host my django app is hard to pass up, especially when [GitHub's student developer pack](https://education.github.com/pack) comes with a $100 DigitalOcean credit.  DigitalOcean's "App Platform" is also very compelling since it can link directly to GitHub or Gitlab and update itself whenever you push new changes, but unfortunately they want an additional $7/month just to host your database if you go this route.
- **Django:** Created the initial portfolio and a blog by following [this excellent tutorial by Jasmine Finer](https://realpython.com/get-started-with-django-1/).
- **Bootstrap 5:** I was hesitant to give up total control and embrace Bootstrap's class library, but it's hard to argue with the value of time saved creating a page that looks familiar to users.
- **PostgreSQL:** Django's ORM handles the queries, but I still had to install and configure it.
