import math
import random
import datetime

points = [(0, 0), (3, 4), (6, 8)]
for p in points:
    distance = math.hypot(p[0], p[1])
    print("Distance of", p, "from origin:", distance)

print()

options = ["Rock", "Paper", "Scissors"]
cpu_choice = random.choice(options)
print("CPU move:", cpu_choice)

sample_pool = list(range(10, 100, 10))
sample_pick = random.sample(sample_pool, 3)
print("Random sample of 3 from pool:", sample_pick)

print()

current_time = datetime.datetime.now()
print("Formatted now:", current_time.strftime("%d/%m/%Y, %H:%M"))

ten_days_later = current_time + datetime.timedelta(days=10)
print("Date after 10 days:", ten_days_later.strftime("%Y-%m-%d"))

birthday = datetime.date(2004, 8, 15)
age_days = (datetime.date.today() - birthday).days
print("Days since 2004-08-15:", age_days)
