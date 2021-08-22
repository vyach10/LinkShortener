import psycopg2
import config
from hash import hash_link

def insert(full_link):
    conn = psycopg2.connect(config.host, config.database, config.user, config.password)

    cur = conn.cursor()

    short_link = str(hash(full_link))

    cur.execute("INSERT INTO LINKS (full_link, short_link) VALUES (%s, %s) ;", (full_link, short_link[1:]))

    conn.commit()

    cur.close()

    conn.close()

    return(short_link[1:])