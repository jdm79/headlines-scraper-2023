import database
import psycopg2

db_url = "postgres://oxbvadmp:3g1tL7uVL15a1qb_5l-x81jDlxp2X-fr@rogue.db.elephantsql.com/oxbvadmp"

connection = psycopg2.connect(db_url)


database.create_tables(connection)
database.drop_tables(connection)