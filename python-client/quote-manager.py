import mysql.connector
import json

filename = 'config.json'

with open(filename) as f:
    data = json.load(f)
    port = data['port']
    ipaddr = data['ipaddr']
    user = data['user']
    password = data['pass']
    database = data['database']


def connectToDb(usr, pss, ip, db):
    conn = mysql.connector.connect(user=usr, password=pss,
                                        host=ip, database=db,
                                        auth_plugin='mysql_native_password')
    return conn

def checkTables(cursor):
    cursor.execute("SHOW TABLES")
    return cursor.fetchall()

def addClip(link, title, cursor):
    add_clip = ("INSERT INTO links (linkscol, title) VALUES ({}, {})")

def selectAll(table, cursor):
    query = "SELECT * FROM {}".format(table)
    cursor.execute(query)
    return cursor.fetchall()

def main():
    conn = connectToDb(user, password, ipaddr, database)
    cursor = conn.cursor()

    print(checkTables(cursor))
    print(selectAll('links',cursor))

if __name__=='__main__':
    main()
