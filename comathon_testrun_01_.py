import pyupbit
import time
import pymysql
import re

host = 'leaderboard.cten39djs6f8.ap-northeast-2.rds.amazonaws.com'
username = 'admin'
password = 'comathon0123'
database = 'leaderboarddb'

db = pymysql.connect(host=host, user=username, password=password, database=database)
cur = db.cursor()

### EMAIL list
cur.execute("SELECT email FROM users")
emaillist = cur.fetchall()
emailstr = str(emaillist)
user_email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", emailstr)
print(user_email)

email = user_email[0]

### SelectedBot
cur.execute("SELECT selectedbot FROM users WHERE email=%s", [email])
selectedbot1 = cur.fetchone()
selectedbot = selectedbot1[0]
# print(selectedbot)

### APIKey
cur.execute("SELECT apikey FROM users WHERE email=%s", [email])
apikeyget = cur.fetchone()
api = apikeyget[0]
# print(api)

### SecretKey
cur.execute("SELECT secretkey FROM users WHERE email=%s", [email])
secretkeyget = cur.fetchone()
secretkey = secretkeyget[0]
# print(secretkey)

### 매수금액
cur.execute("SELECT tradingamount FROM users WHERE email=%s", [email])
trdamtget = cur.fetchone()
trdamt = trdamtget[0]
# print(trdamt)

cur.close()
