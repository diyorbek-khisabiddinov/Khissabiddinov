from datetime import datetime, timedelta

current_time = datetime.now()  
x_date = datetime.now() - timedelta(days = 2)


difference = (current_time - x_date).total_seconds()   #difference between date1,date2

print(f"Difference in seconds: {difference}")
