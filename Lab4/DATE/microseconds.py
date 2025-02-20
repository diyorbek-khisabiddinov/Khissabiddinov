from datetime import datetime

current_time = datetime.now()
microseconds = current_time.replace(microsecond = 0)

print("Datetime:", current_time)
print("Without microseconds:", microseconds)