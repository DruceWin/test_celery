import sqlite3
import time

from tasks import add
from tasks import r

add.delay(3, 2)

def get_from_redis():
    time.sleep(1)
    print(r.get('value'))


get_from_redis()

conn = sqlite3.connect('db.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS reusts(id INT PRIMARY KEY''')