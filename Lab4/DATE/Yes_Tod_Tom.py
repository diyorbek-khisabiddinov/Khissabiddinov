from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)

print("Yesterday is date:", yesterday)
print("Today is date:",today)
print("Tomorrow is date:", tomorrow)