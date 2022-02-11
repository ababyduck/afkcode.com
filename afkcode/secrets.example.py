from dj_database_url import parse

db_info = parse('postgres://user:pass@localhost:5432/dbname')
