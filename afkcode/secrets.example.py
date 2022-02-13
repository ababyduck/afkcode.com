from dj_database_url import parse

# Important: All of these must be updated for deployment
secret_key = ''
allowed_hosts = '127.0.0.1,localhost'.split(',')
admins = [('Your django admin username', 'Your django admin email address')]
prod_db_info = parse('postgres://user:pass@localhost:5432/dbname')
