from datetime import datetime

now = datetime.now()

print("Method 1")
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%H:%M:%S"))

print("\nMethod 2")
print(f"{now.day:02d}/{now.month:02d}/{now.year:04d}")
print(f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}")


class CustomDate:
    def __init__(self):
        self.now = datetime.now()

    def get_date(self):
        return f"{self.now.day:02d}/{self.now.month:02d}/{self.now.year:04d}"

    def get_time(self):
        return f"{self.now.hour:02d}:{self.now.minute:02d}:{self.now.second:02d}"


custom_date = CustomDate()

custom_date.get_date()
custom_date.get_time()
