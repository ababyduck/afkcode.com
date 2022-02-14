import os

# Users in this list will always see debug messages even if DEBUG is False
admins = [('name', 'email')]


def set_environment_variables():
    # Enables debug mode, which gives detailed code error info for all users. Disable for production
    os.environ['DJANGO_DEBUG'] = 'False'
    # Switches between development and production database. Disable for production
    os.environ['DJANGO_DEVELOPMENT'] = 'False'
    # Django uses this for crypto signatures, just make sure it's set
    os.environ['DJANGO_SECRET_KEY'] = 'your secret here'
    # Database URL, will be parsed by dj-database-url on import
    os.environ['DATABASE_URL'] = 'postgres://user:pass@localhost:5432/dbname'
    # Hosts that django is allowed to run on
    os.environ['DJANGO_ALLOWED_HOSTS'] = '127.0.0.1,localhost'
