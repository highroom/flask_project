import sqlite3
from settings import Config


def db_connect():
    conn = Config.POOL.connection()
    cursor = conn.cursor()
    return conn, cursor


def db_close(conn, cursor):
    cursor.close()
    conn.close()


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def fetch_one(sql, args):
    conn, cursor = db_connect()
    cursor.execute(sql, args)
    row = cursor.fetchone()
    data = dict_factory(cursor, row) if row else None
    db_close(conn, cursor)
    return data


def fetch_all(sql, args):
    conn, cursor = db_connect()
    cursor.execute(sql, args)
    rows = cursor.fetchall()
    ret = []
    if rows:
        for row in rows:
            data = dict_factory(cursor, row)
            ret.append(data)
    db_close(conn, cursor)
    return ret


def insert(sql, args):
    conn, cursor = db_connect()
    row = cursor.execute(sql, args)
    conn.commit()
    db_close(conn, cursor)
    return row
