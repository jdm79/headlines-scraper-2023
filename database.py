from psycopg2.extras import execute_values

DROP_TABLE = "DROP TABLE IF EXISTS headlines;"

CREATE_HEADLINES = """CREATE TABLE IF NOT EXISTS headlines (
    id SERIAL, 
    headline TEXT,
    url TEXT,
    paper TEXT,
    timestamp TEXT,
    paper_id TEXT,
    css_name TEXT
    );"""
INSERT_HEADLINE = "INSERT INTO headlines (headline, url, paper, timestamp, paper_id, css_name) VALUES (%s, %s, %s, %s, %s, %s);"
SELECT_ALL_HEADLINES = "SELECT * FROM headlines;"

# https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-add-column/
ADD_COLUMNS = """ALTER TABLE headlines
ADD COLUMN css_name TEXT
;"""

ADD_UNIQUE = "ALTER TABLE headlines ADD CONSTRAINT constraintname UNIQUE (headline)"
def drop_tables(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(DROP_TABLE)

def create_tables(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_HEADLINES)

def add_unique(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(ADD_UNIQUE)

def add_columns(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(ADD_COLUMNS)


def add_headline(connection, headline, url, paper, timestamp, paper_id, css_name):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_HEADLINE, (headline, url, paper, timestamp, paper_id, css_name))        

def get_headlines(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_HEADLINES)
            return cursor.fetchall()
