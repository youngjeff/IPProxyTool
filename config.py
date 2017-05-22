# coding=utf-8
import os
# local
MYSQL_HOSTS = os.environ.get("MYSQL_HOSTS")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_PORT = os.environ.get("MYSQL_PORT")
MYSQL_DB = os.environ.get("MYSQL_DB")
MYSQL_utf8 = os.environ.get("MYSQL_utf8")

database_config = {
    'host': MYSQL_HOSTS,
    'port': MYSQL_PORT,
    'user': MYSQL_USER,
    'password': MYSQL_PASSWORD,
    'charset': MYSQL_utf8,
}

database = 'ipproxy'
free_ipproxy_table = 'free_ipproxy'
httpbin_table = 'httpbin'

data_port = '8000'
