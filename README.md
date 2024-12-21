# python dateutil relativedelta add month keep same day

This repo uses [https://github.com/ehiggs/python-dateutil](https://github.com/dateutil/dateutil) to allow looping via +1 month increments and keep same day in month whenever possible (by storing in minutes of datetime.datetime information when to go back to same day as day in starting date)

## Note:
```diff
- Compare dates only using d1_after_d2(d1, d2)
```
> and 
```diff
- Do not use datetime.datetime.minutes
```

#
This repo offers add month fix for https://stackoverflow.com/questions/77872779/unexpected-behavior-from-pythons-relativedelta-and-datetime-libraries

the left column is loop of `date + relativedelta(months=1)`; while the right column is loop of `datePlus1Month(date)`
```
        For start date 31.12.2019
2019-12-31 00:00:00      2019-12-31 00:00:00
2020-01-31 00:00:00      2020-01-31 00:00:00
2020-02-29 00:02:00      2020-02-29 00:00:00
2020-03-31 00:00:00      2020-03-29 00:00:00
2020-04-30 00:03:00      2020-04-29 00:00:00
2020-05-31 00:00:00      2020-05-29 00:00:00
2020-06-30 00:03:00      2020-06-29 00:00:00
2020-07-31 00:00:00      2020-07-29 00:00:00
2020-08-31 00:00:00      2020-08-29 00:00:00
2020-09-30 00:03:00      2020-09-29 00:00:00
2020-10-31 00:00:00      2020-10-29 00:00:00
2020-11-30 00:03:00      2020-11-29 00:00:00
2020-12-31 00:00:00      2020-12-29 00:00:00
2021-01-31 00:00:00      2021-01-29 00:00:00
2021-02-28 00:01:00      2021-02-28 00:00:00
2021-03-31 00:00:00      2021-03-28 00:00:00

        For start date 30.12.2019
2019-12-30 00:00:00      2019-12-30 00:00:00
2020-01-30 00:00:00      2020-01-30 00:00:00
2020-02-29 00:03:00      2020-02-29 00:00:00
2020-03-30 00:00:00      2020-03-29 00:00:00
2020-04-30 00:00:00      2020-04-29 00:00:00
2020-05-30 00:00:00      2020-05-29 00:00:00
2020-06-30 00:00:00      2020-06-29 00:00:00
2020-07-30 00:00:00      2020-07-29 00:00:00
2020-08-30 00:00:00      2020-08-29 00:00:00
2020-09-30 00:00:00      2020-09-29 00:00:00
2020-10-30 00:00:00      2020-10-29 00:00:00
2020-11-30 00:00:00      2020-11-29 00:00:00
2020-12-30 00:00:00      2020-12-29 00:00:00
2021-01-30 00:00:00      2021-01-29 00:00:00
2021-02-28 00:02:00      2021-02-28 00:00:00
2021-03-30 00:00:00      2021-03-28 00:00:00
```
***
***
*** 
### Also dateutil.rrule failes because

from https://datatracker.ietf.org/doc/html/rfc5545#section-3.3.10
```
      Recurrence rules may generate recurrence instances with an invalid
      date (e.g., February 30) or nonexistent local time (e.g., 1:30 AM
      on a day where the local time is moved forward by an hour at 1:00
      AM).  Such recurrence instances MUST be ignored and MUST NOT be
      counted as part of the recurrence set.
```
although following may be usefull
```
from dateutil.rrule import rrule, MONTHLY
# Generate a list of the last day for 16 months from the calculated date
list(rrule(freq=MONTHLY, count=16, dtstart=datetime(2019,12,31), bymonthday=(-1,)))
```
