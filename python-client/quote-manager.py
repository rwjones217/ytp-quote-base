import mysql.connector
import json


with open('config.json') as f:
    data = json.load(f)
    port = data['port']
    ipaddr = data['ipaddr']
    user = data['user']
    password = data['pass']


def main():
    pass


if __name__=='__main__':
    main()
