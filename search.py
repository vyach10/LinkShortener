import psycopg2
import config

def search_by_full_link(full_link):
    conn = psycopg2.connect(host = config.host, database = config.database, user = config.user, password = config.password)
    cur = conn.cursor()
    cur.execute("SELECT short_link FROM LINKS WHERE full_link in (%s);", (full_link,))

    conn.commit()

    short_link = cur.fetchone()

    cur.close()

    conn.close()

    if (short_link == [] or short_link is None):
        return False
    else:
        return short_link

def search_by_short_link(short_link):
    conn = psycopg2.connect(host = config.host, database = config.database, user = config.user, password = config.password)

    cur = conn.cursor()

    cur.execute("SELECT full_link FROM LINKS WHERE short_link in (%s);", (short_link,))

    conn.commit()

    full_link = cur.fetchone()

    cur.close()

    conn.close()

    if (full_link == [] or full_link is None):
        return False
    else:
        return full_link