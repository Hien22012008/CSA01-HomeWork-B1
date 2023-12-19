from datetime import datetime


class DateHandler:
    def __init__(self):
        pass

    def format_date(date):
        return date.strftime("%d/%m/%Y")

    def get_days_between(date1, date2):
        return (date2 - date1).days


start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 1, 1)

date_handler = DateHandler()

print("Start:", date_handler.format_date(start_date))
print("End:", date_handler.format_date(end_date))
print("Days between:", date_handler.get_days_between(start_date, end_date))
