day, month, year = map(int, input().strip().split())
day1, month1, year1 = map(int, input().strip().split())

month_late = month - month1
day_late = day - day1
year_late = year - year1

fine = 0
if year_late < 0:
    pass
elif year_late >= 1:
    fine = 10000
elif month_late >= 1:
    fine = 500 * month_late
elif day_late >= 1:
    fine = 15 * day_late

print(fine)
