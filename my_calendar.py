# import datetime as dt

# from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, nearest_workday
    


# class USTradingCalendar(AbstractHolidayCalendar):
#     rules = [
#         Holiday('NewYearsDay', month=1, day=1, observance=nearest_workday),
#         Holiday('USIndependenceDay', month=7, day=4, observance=nearest_workday),
        
#         Holiday('Christmas', month=12, day=25, observance=nearest_workday)
#     ]


# def get_trading_close_holidays(year):
#     inst = USTradingCalendar()

#     return inst.holidays(dt.datetime(year-1, 12, 31), dt.datetime(year, 12, 31))


# if __name__ == '__main__':
#     print(get_trading_close_holidays(2016))
    #    DatetimeIndex(['2016-01-01', '2016-01-18', '2016-02-15', '2016-03-25',
    #                   '2016-05-30', '2016-07-04', '2016-09-05', '2016-11-24',
    #                   '2016-12-26'],
    #                  dtype='datetime64[ns]', freq=None)


from pandas.tseries.holiday import (
    AbstractHolidayCalendar, DateOffset, EasterMonday,
    GoodFriday, Holiday, MO,
    next_monday, next_monday_or_tuesday)
from datetime import date, datetime, timedelta
from pandas.tseries.offsets import CDay
import time
class MyIsraelHolidayCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday('New Years Day', month=1, day=1, observance=next_monday),
        GoodFriday,
        EasterMonday,
        Holiday('Early May bank holiday',
                month=5, day=1, offset=DateOffset(weekday=MO(1))),
        Holiday('Spring bank holiday',
                month=5, day=31, offset=DateOffset(weekday=MO(-1))),
        Holiday('Summer bank holiday',
                month=8, day=31, offset=DateOffset(weekday=MO(-1))),
        Holiday('Christmas Day', month=12, day=25, observance=next_monday),
        Holiday('Boxing Day',
                month=12, day=26, observance=next_monday_or_tuesday)
    ]  
weekmask_israel = 'Sun Mon Tue Wed Thu'   
business = CDay(calendar=MyIsraelHolidayCalendar(), weekmask = weekmask_israel)
 

print (business)
today = date.today()+ 2*business 
five_business_days_later = date.today() + 5 * business 

print(today) 
print(five_business_days_later)
# holidays = MyIsraelHolidayCalendar().holidays(
#     start=date(2018, 1, 1),
#     end=date(2018, 12, 31))
d = datetime(2018, 3, 10)
d1 = datetime(2018,4,22)
print (business(d))
print (d1.weekday())

if d.weekday() in [5, 6]:
    print ('YIIII')

if  d in business.holidays: 
    print ("true")
else: print('false')  
print(repr(business))
# print(holidays.__dict__)
# print(holidays.tolist)
# print(business.__dict__)
# print(business.calendar)
