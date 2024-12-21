from datetime import datetime
from dateutil.relativedelta import relativedelta

# datePlus1Month takes datetime.datetime type `date` and returns new object of type datetime.datetime with 1 month added,
# returned object has minute variable changed to try to keep same day on next call of datePlus1Month with that new object
def datePlus1Month(date):
	if date.day < 28:
		dateAndMonth = date + relativedelta(months=1)
		# cast to datetime.datetime object so this function returns that object type instead of sometimes returning datetime.date and sometimes datetime.datetime
		return datetime(year=dateAndMonth.year, month=dateAndMonth.month, day=dateAndMonth.day, hour=dateAndMonth.hour, minute=dateAndMonth.minute)

	next_month_lst_day =	((date + relativedelta(months=1))+relativedelta(day=31)).day
	
	if date.day != (date + relativedelta(months=1)).day and date.day == 31 and next_month_lst_day == 30:
		dateAndMonth = date + relativedelta(months=1) + relativedelta(minute=3)
		return datetime(year=dateAndMonth.year, month=dateAndMonth.month, day=dateAndMonth.day, hour=dateAndMonth.hour, minute=dateAndMonth.minute)
		
	isLeapYear = 0
	if (date.year % 4 == 0 and date.year % 100 != 0) or date.year % 400 == 0: isLeapYear = 1

	if date.minute == 3:
		dateAndMonth = date + relativedelta(months=1) + relativedelta(days=1)  + relativedelta(minute=0)
		return datetime(year=dateAndMonth.year, month=dateAndMonth.month, day=dateAndMonth.day, hour=dateAndMonth.hour, minute=dateAndMonth.minute)
	if date.minute == 2:
		dateAndMonth = date + relativedelta(months=1) + relativedelta(days=2)  + relativedelta(minute=0)
		return datetime(year=dateAndMonth.year, month=dateAndMonth.month, day=dateAndMonth.day, hour=dateAndMonth.hour, minute=dateAndMonth.minute)
	if date.minute == 1:
		dateAndMonth = date + relativedelta(months=1) + relativedelta(days=3) + relativedelta(minute=0)
		return datetime(year=dateAndMonth.year, month=dateAndMonth.month, day=dateAndMonth.day, hour=dateAndMonth.hour, minute=dateAndMonth.minute)
	if date.day != (date + relativedelta(months=1)).day:
		dateAndMonth = date + relativedelta(months=1) + relativedelta(minute=32 - date.day + isLeapYear)
		return datetime(year=dateAndMonth.year, month=dateAndMonth.month, day=dateAndMonth.day, hour=dateAndMonth.hour, minute=dateAndMonth.minute)
	
	dateAndMonth = date + relativedelta(months=1)
	return datetime(year=dateAndMonth.year, month=dateAndMonth.month, day=dateAndMonth.day, hour=dateAndMonth.hour, minute=dateAndMonth.minute)

def showDiff(s):
	startDate = datetime.strptime(s, '%d.%m.%Y')

	date = startDate
	myDate = startDate
	d = 0
	while d<16:
		print(date, '\t', myDate)
		date = datePlus1Month(date)
		myDate = myDate + relativedelta(months=1)
		d+=1


s='31.12.2019'
print('\n\tFor start date', s)
showDiff(s)

s='30.12.2019'
print('\n\tFor start date', s)
showDiff(s)

print('\nCompare dates only using d1_after_d2(d1, d2)')
def d1_after_d2(d1, d2):
	return datetime(year=d1.year, month=d1.month, day=d1.day, hour=d1.hour) > datetime(year=d2.year, month=d2.month, day=d2.day, hour=d2.hour)
	
s='31.1.2020'
s2='29.2.2020'
d1_after_d2(datePlus1Month(datetime.strptime(s, '%d.%m.%Y')), datetime.strptime(s2, '%d.%m.%Y'))# False
