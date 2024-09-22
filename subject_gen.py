import datetime as dt
start_date = dt.date(2024, 9, 23)
end_date = dt.date(2024, 12, 13)

start_dates = [
    dt.date(2024, 9, 23),
    dt.date(2024, 9, 24),
    ]

breaks = [
    [dt.date(2024, 10, 28), dt.date(2024, 11, 3)],
    ]

name = "Groups and Symmetries"
tag = "grp_sym1"

def next_event(start, end, starts, breaks):
    current = start
    week = 0
    while current <= end:
        diff = dt.timedelta(days=7 * week)
        for date in starts:
            lec = date + diff
            for brek in breaks:
                if brek[0] <= lec <= brek[1]:
                    break
            else:
                current = lec
                yield lec

        week += 1

for i in next_event(start_date, end_date, start_dates, breaks):
    print(i)
