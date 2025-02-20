from datetime import datetime, timedelta

today = datetime.now()
new_date = today - timedelta(days = 5)

print("Current Date:", today)
print("Date 5 days ago:",new_date)