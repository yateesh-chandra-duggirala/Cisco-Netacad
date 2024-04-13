from datetime import datetime

wish = datetime(2024, 3, 1, 14, 26, 23)

print(wish)
print(wish.date())
print(wish.time())
print(wish.timestamp())

print("time : ", datetime.today())
print("now : ", datetime.now())
print("utcnow : ", datetime.utcnow())

print(datetime.today().timestamp())