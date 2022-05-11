import datetime

year = datetime.datetime.now().year
month = datetime.datetime.now().month

print(year)
print(month)

ytd = list(range(1, month+1))
fy = list(range(1, 13))

print( [f"{year}-{i:02d}" for i in ytd])
print( [f"{year}-{i:02d}" for i in fy])