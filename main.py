import sqlite3
import time

from tasks import add
from tasks import r

add.delay(3, 4)


def get_from_redis():
    time.sleep(2)
    print(r.get('value'))


get_from_redis()
#
# conn = sqlite3.connect('db.sqlite3')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS Myresults (id INT PRIMARY KEY, val INT)''')

