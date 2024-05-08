import psycopg2
from psycopg2 import sql
# not used still wokting on sqlite
def create_database():
    conn = psycopg2.connect(
        dbname="postgres",
        user="shankarramnr",
        password="dbPassword@1234",
        host="localhost",
        port="5432"
    )

    conn.autocommit = True

    cursor = conn.cursor()

    cursor.execute(sql.SQL("CREATE DATABASE {}").format(
        sql.Identifier('Mess_database'))
    )

    cursor.close()
    conn.close()