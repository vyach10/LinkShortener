import psycopg2
import config

def create_table():
    conn = psycopg2.connect(host = config.host, database = config.database, user = config.user, password = config.password)

    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS links ( id SERIAL UNIQUE, full_link VARCHAR(256), short_link VARCHAR(20) )")

    conn.commit()

    cur.close()

    conn.close()