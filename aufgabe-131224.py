# holiday plan 2025
from datetime import datetime

# Holiday plan
holidays = dict(
    Christmas_2025=(datetime(2024, 12, 24), datetime(2025, 1, 2)),
    Easter_2025=(datetime(2025, 4, 18), datetime(2024, 4, 21)),
    Sommerferien_2025=(datetime(2025, 8, 11), datetime(2025, 8, 19)),
    Winterferien_2025=(datetime(2025, 12, 24), datetime(2026, 1, 2)),
    Christi_Himmelfahrt=(datetime(2025, 5, 29), datetime(2025, 5, 29)),
    Pfingstmontag=(datetime(2025, 6, 9), datetime(2025, 6, 9)),
    Tag_der_deutschen_Einheit=(datetime(2025, 10, 3), datetime(2025, 10, 3)),
    Reformationstag=(datetime(2025, 10, 31), datetime(2025, 10, 31)),
)

# enter a Date
input_date_str = input("Pleace enter a Date (YYYY.MM.DD): ")
input_date = datetime.strptime(input_date_str, "%Y.%m.%d")

# try:
#    input_date = datetime.strptime(input_date_str, "%Y.%m.%d")
# except ValueError:
#    print("Pleace enter a Date (YYYY.MM.DD):")
#    exit(1)

# Check if the input date ist within any holyday interval
holiday_found = False
for holiday, (start, end) in holidays.items():
    if start <= input_date <= end:
        print(f"{input_date_str} is {holiday} in vacation")
        holiday_found = True
        break

if not holiday_found:
    print(f"{input_date_str} is in business!")
