from datetime import datetime
from dateutil.relativedelta import relativedelta

class WrappedDatetime(datetime):
    
    def __eq__(self, other):
        if isinstance(other, WrappedDatetime):
            return datetime(year=self.year, month=self.month, day=self.day, hour=self.hour) == datetime(year=other.year, month=other.month, day=other.day, hour=other.hour)
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, WrappedDatetime):
            self_datetime = datetime(year=self.year, month=self.month, day=self.day, hour=self.hour)
            other_datetime = datetime(year=other.year, month=other.month, day=other.day, hour=other.hour)
            return self_datetime < other_datetime
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, WrappedDatetime):
            self_datetime = datetime(year=self.year, month=self.month, day=self.day, hour=self.hour)
            other_datetime = datetime(year=other.year, month=other.month, day=other.day, hour=other.hour)
            return self_datetime <= other_datetime
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, WrappedDatetime):
            self_datetime = datetime(year=self.year, month=self.month, day=self.day, hour=self.hour)
            other_datetime = datetime(year=other.year, month=other.month, day=other.day, hour=other.hour)
            return self_datetime > other_datetime
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, WrappedDatetime):
            self_datetime = datetime(year=self.year, month=self.month, day=self.day, hour=self.hour)
            other_datetime = datetime(year=other.year, month=other.month, day=other.day, hour=other.hour)
            return self_datetime >= other_datetime
        return NotImplemented
    
    def __ne__(self, other):
        if isinstance(other, WrappedDatetime):
            self_datetime = datetime(year=self.year, month=self.month, day=self.day, hour=self.hour)
            other_datetime = datetime(year=other.year, month=other.month, day=other.day, hour=other.hour)
            return self_datetime != other_datetime
        return NotImplemented
    
    @classmethod
    def from_datetime(cls, dt):
        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond)
    
    # datePlus1Month returns new object of type datetime.datetime with 1 month added while trying to keep same day,
    # returned object has minute variable changed to try to keep same day on next call of datePlus1Month on that new object
    def datePlus1Month(self):
        if self.day < 28:
            dateAndMonth = self + relativedelta(months=1)
            return WrappedDatetime.from_datetime(dateAndMonth)

        next_month_lst_day =    ((self + relativedelta(months=1))+relativedelta(day=31)).day

        if self.day != (self + relativedelta(months=1)).day and self.day == 31 and next_month_lst_day == 30:
            dateAndMonth = self + relativedelta(months=1) + relativedelta(minute=3)
            return WrappedDatetime.from_datetime(dateAndMonth)
            
        isLeapYear = 0
        if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0: isLeapYear = 1

        if self.minute == 3:
            dateAndMonth = self + relativedelta(months=1) + relativedelta(days=1)  + relativedelta(minute=0)
            return WrappedDatetime.from_datetime(dateAndMonth)
        if self.minute == 2:
            dateAndMonth = self + relativedelta(months=1) + relativedelta(days=2)  + relativedelta(minute=0)
            return WrappedDatetime.from_datetime(dateAndMonth)
        if self.minute == 1:
            dateAndMonth = self + relativedelta(months=1) + relativedelta(days=3) + relativedelta(minute=0)
            return WrappedDatetime.from_datetime(dateAndMonth)
        if self.day != (self + relativedelta(months=1)).day:
            dateAndMonth = self + relativedelta(months=1) + relativedelta(minute=32 - self.day + isLeapYear)
            return WrappedDatetime.from_datetime(dateAndMonth)

        dateAndMonth = self + relativedelta(months=1)
        return WrappedDatetime.from_datetime(dateAndMonth)


startDateStr = '31.12.2019'
startDate = datetime.strptime(startDateStr, '%d.%m.%Y')
date = WrappedDatetime.from_datetime(startDate)

d = 0
while d<16:
	
    print(date, date <= WrappedDatetime.from_datetime(datetime.strptime('30.4.2020', '%d.%m.%Y')), date < WrappedDatetime.from_datetime(datetime.strptime('30.4.2020', '%d.%m.%Y')))
	
    date = date.datePlus1Month()
	
    d+=1
'''
date op 30.4.2020   op:<= op:<
2019-12-31 00:00:00 True True
2020-01-31 00:00:00 True True
2020-02-29 00:02:00 True True
2020-03-31 00:00:00 True True
2020-04-30 00:03:00 True False
2020-05-31 00:00:00 False False
2020-06-30 00:03:00 False False
2020-07-31 00:00:00 False False
2020-08-31 00:00:00 False False
2020-09-30 00:03:00 False False
2020-10-31 00:00:00 False False
2020-11-30 00:03:00 False False
2020-12-31 00:00:00 False False
2021-01-31 00:00:00 False False
2021-02-28 00:01:00 False False
2021-03-31 00:00:00 False False
'''
