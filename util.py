import pendulum
from pendulum.date import Date
import logging
import pandas as pd

listOfNseHolidays = set([
Date(2011,1,26),
Date(2011,3,2),
Date(2011,4,12),
Date(2011,4,14),
Date(2011,4,22),
Date(2011,8,15),
Date(2011,8,31),
Date(2011,9,1),
Date(2011,10,6),
Date(2011,10,26),
Date(2011,10,27),
Date(2011,11,7),
Date(2011,11,10),
Date(2011,12,6),
Date(2012,1,26),
Date(2012,2,20),
Date(2012,3,8),
Date(2012,4,5),
Date(2012,4,6),
Date(2012,5,1),
Date(2012,8,15),
Date(2012,8,20),
Date(2012,9,19),
Date(2012,10,2),
Date(2012,10,24),
Date(2012,10,26),
Date(2012,11,13),
Date(2012,11,14),
Date(2012,11,28),
Date(2012,12,25),
Date(2013,1,26),
Date(2013,3,27),
Date(2013,3,29),
Date(2013,4,19),
Date(2013,4,24),
Date(2013,5,1),
Date(2013,8,9),
Date(2013,8,15),
Date(2013,9,9),
Date(2013,10,2),
Date(2013,10,16),
Date(2013,11,4),
Date(2013,11,14),
Date(2013,12,25), 
Date(2014,2,27),
Date(2014,3,17),
Date(2014,4,8),
Date(2014,4,14),
Date(2014,4,18),
Date(2014,4,24),
Date(2014,5,1),
Date(2014,7,29),
Date(2014,10,2),
Date(2014,10,3),
Date(2014,10,6),
Date(2014,10,15),
Date(2014,10,23),
Date(2014,10,24),
Date(2014,11,4),
Date(2014,11,6),
Date(2014,12,25),
Date(2015,1,26),
Date(2015,2,17),
Date(2015,3,6),
Date(2015,4,2),
Date(2015,4,3),
Date(2015,4,14),
Date(2015,5,1),
Date(2015,9,17),
Date(2015,9,25),
Date(2015,10,2),
Date(2015,10,22),
Date(2015,11,11),
Date(2015,11,23),
Date(2015,11,25),
Date(2015,12,25),
Date(2016,1,26),
Date(2016,3,7),
Date(2016,3,24),
Date(2016,3,25),
Date(2016,4,14),
Date(2016,4,15),
Date(2016,4,19),
Date(2016,7,6),
Date(2016,8,15),
Date(2016,9,5),
Date(2016,9,13),
Date(2016,10,11),
Date(2016,10,23),
Date(2016,10,31),
Date(2016,11,14),
Date(2017,1,26),
Date(2017,2,24),
Date(2017,3,13),
Date(2017,4,4),
Date(2017,4,14),
Date(2017,5,1),
Date(2017,6,26),
Date(2017,8,15),
Date(2017,8,25),
Date(2017,10,2),
Date(2017,10,19),
Date(2017,10,20),
Date(2017,12,25),   
Date(2018,1,26),    
Date(2018,2,13),
Date(2018,3,2),
Date(2018,3,29),
Date(2018,3,30),
Date(2018,5,1),
Date(2018,8,15),
Date(2018,8,22),
Date(2018,9,13),
Date(2018,9,20),
Date(2018,10,2),
Date(2018,10,18),
Date(2018,11,7),
Date(2018,11,8),
Date(2018,11,23),
Date(2018,12,25),   
Date(2019,3,4),
Date(2019,3,21),
Date(2019,4,17),
Date(2019,4,19),
Date(2019,5,1),
Date(2019,6,5),
Date(2019,8,12),
Date(2019,8,15),
Date(2019,9,2),
Date(2019,9,10),
Date(2019,10,2),
Date(2019,10,8),
Date(2019,10,28),
Date(2019,11,12),
Date(2019,12,25),
Date(2020,2,21),
Date(2020,3,10),
Date(2020,4,2),
Date(2020,4,6),
Date(2020,4,10),
Date(2020,4,14),
Date(2020,5,1),
Date(2020,5,25),
Date(2020,10,2),
Date(2020,11,16),
Date(2020,11,30),
Date(2020,12,25),
Date(2021,1,26),
Date(2021,3,11),
Date(2021,3,29),
Date(2021,4,2),
Date(2021,4,14),
Date(2021,4,21),
Date(2021,5,13),
Date(2021,7,21),
Date(2021,8,19),
Date(2021,9,10),
Date(2021,10,15),
Date(2021,11,4),
Date(2021,11,5),
Date(2021,11,19),
Date(2022,1,26),
Date(2022,3,1),
Date(2022,3,18),
Date(2022,4,14),
Date(2022,4,15),
Date(2022,5,3),
Date(2022,8,9),
Date(2022,8,15),
Date(2022,8,31),
Date(2022,10,5),
Date(2022,10,24),
Date(2022,10,26),
Date(2022,11,8),
Date(2023,1,26),
Date(2023,3,7),
Date(2023,3,22),
Date(2023,3,30),
Date(2023,4,4),
Date(2023,4,7),
Date(2023,4,14),
Date(2023,5,1),
Date(2023,5,5),
Date(2023,6,29),
Date(2023,8,15),
Date(2023,8,16),
Date(2023,9,19),
Date(2023,9,28),
Date(2023,10,2),
Date(2023,10,24),
Date(2023,11,14),
Date(2023,11,27),
Date(2023,12,25)

])


# utility method to be used only by this module
def __considerHolidayList(expiryDate: Date):
    if(expiryDate.date() in listOfNseHolidays):
        return __considerHolidayList(expiryDate.subtract(days=1))
    else:
        return expiryDate

def getNearestWeeklyExpiryDate(cob_):
    expiryDate = None
    if(pendulum.local(cob_.year, cob_.month,cob_.day).date().day_of_week is pendulum.THURSDAY):
        expiryDate = pendulum.local(cob_.year, cob_.month,cob_.day)
    else:
        expiryDate = pendulum.local(cob_.year, cob_.month,cob_.day).next(pendulum.THURSDAY)
    return __considerHolidayList(expiryDate).date()

#print('nearest weekly exp is '+str(getNearestWeeklyExpiryDate(cob)))

def getNearestMonthlyExpiryDate(cob_):
    expiryDate = pendulum.local(cob_.year, cob_.month,cob_.day).last_of('month', pendulum.THURSDAY)
    if(pendulum.local(cob_.year, cob_.month,cob_.day).date() > expiryDate.date()):
        expiryDate = pendulum.local(cob_.year, cob_.month,cob_.day).add(months=1).last_of('month', pendulum.THURSDAY)
    return __considerHolidayList(expiryDate).date()

#print('nearest monthly exp is '+str(getNearestMonthlyExpiryDate(cob)))



def getNextWeeklyExpiryDate(cob_):
    expiryDate = None
    if(pendulum.local(cob_.year, cob_.month,cob_.day).date().day_of_week is pendulum.THURSDAY):
        expiryDate = pendulum.local(cob_.year, cob_.month,cob_.day).next(pendulum.THURSDAY)
    else:
        expiryDate = pendulum.local(cob_.year, cob_.month,cob_.day).next(pendulum.THURSDAY).next(pendulum.THURSDAY)
    return __considerHolidayList(expiryDate).date()

#print('next weekly exp is '+str(getNextWeeklyExpiryDate(cob)))

def getNextMonthlyExpiryDate(cob_):
    expiryDate = pendulum.local(cob_.year, cob_.month,cob_.day).last_of('month', pendulum.THURSDAY)
    if(pendulum.local(cob_.year, cob_.month,cob_.day).date() > expiryDate.date()):
        expiryDate = pendulum.local(cob_.year, cob_.month,cob_.day).add(months=2).last_of('month', pendulum.THURSDAY)
    else:
        expiryDate = pendulum.local(cob_.year, cob_.month,cob_.day).add(months=1).last_of('month', pendulum.THURSDAY)
    return __considerHolidayList(expiryDate).date()

#print('next month exp is '+str(getNextMonthlyExpiryDate(cob)))

#############################



def getNearestMonthlyExpiryDate(cob_):
    expiryDate = pendulum.local(cob_.year, cob_.month,cob_.day).last_of('month', pendulum.THURSDAY)
    if(pendulum.local(cob_.year, cob_.month,cob_.day).date() > expiryDate.date()):
        expiryDate = pendulum.local(cob_.year, cob_.month,cob_.day).add(months=1).last_of('month', pendulum.THURSDAY)
    return __considerHolidayList(expiryDate).date()




# print('today is '+str(pendulum.now().date()))
# print('nearest weekly exp is '+str(getNearestWeeklyExpiryDate()))
# print('next weekly exp is '+str(getNextWeeklyExpiryDate()))
# print('nearest monthly exp is '+str(getNearestMonthlyExpiryDate()))
# print('next month exp is '+str(getNextMonthlyExpiryDate()))