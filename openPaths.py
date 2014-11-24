__author__ = 'Anuj'

import pandas as pd
import numpy as np
from datetime import datetime
from dateutil import tz


dfr = pd.read_csv("openpaths_anujsaxenaa.csv")

# print dfr.head()
# print dfr.shape
dfr = dfr.loc[(dfr.os == '8.1.1')]
# print dfr.head()
# print dfr.shape


dfr = dfr.rename(columns={'alt': 'Altitude'})

dfr['Date'] = dfr['date'].map(lambda x: x.strip(' ')[0:10])

dfr['dW'] = pd.to_datetime(np.array(dfr['date'])).dayofweek

dfr.loc[(dfr.dW == 5) | (dfr.dW == 6), 'WeekDayType'] = "WeekEnd"
dfr.loc[(dfr.dW == 5) | (dfr.dW == 6), 'WeekDayTypeColor'] = "#4ab1eb"

dfr.loc[(dfr.dW == 0) | (dfr.dW == 1) | (dfr.dW == 2) | (dfr.dW == 3) | (dfr.dW == 4), 'WeekDayType'] = "WeekDay"
dfr.loc[(dfr.dW == 0) | (dfr.dW == 1) | (dfr.dW == 2) | (dfr.dW == 3) | (dfr.dW == 4), 'WeekDayTypeColor'] = "#e22c56"


dfr = dfr.drop('dW', 1)
# print dfr.date
# print pd.to_datetime(np.array(dfr['date'])).hour
dfr = dfr.rename(columns={'date': 'DateTime'})
# print dfr.head()
# print dfr.dtypes

from_zone = tz.tzutc()
to_zone = tz.gettz('America/New_York')
# to_zone = tz.tzlocal()

dt = np.array(dfr.DateTime)
dt2 = []
hrs = []
for vals in dt:
    date_object = datetime.strptime(vals, "%Y-%m-%d %H:%M:%S")
    date_object2 = date_object.replace(tzinfo=from_zone)
    central = date_object2.astimezone(to_zone)
    dt2.append(central)
    hrs.append(int(str(central).split(':')[0][-3:]))

    # print str(central).split(':')[0][-3:], "HI!", central


dfr['DateTimeEST'] = np.array(dt2)
dfr['Hrs'] = np.array(hrs)
# print dfr.Hrs.unique()
dfr.loc[(dfr.Hrs > 7) & (dfr.Hrs < 17), 'TimeOfDay'] = "Day"
dfr.loc[(dfr.Hrs > 7) & (dfr.Hrs < 17), 'DayColor'] = "#fdb863"
dfr.loc[(dfr.Hrs <= 7) | (dfr.Hrs >= 17), 'TimeOfDay'] = "Night"
dfr.loc[(dfr.Hrs <= 7) | (dfr.Hrs >= 17), 'DayColor'] = "#b2abd2"
# dfr.loc[(dfr.Hrs >= 21) | (dfr.Hrs <= 7), 'TimeOfDay'] = "Night"
# dfr.loc[(dfr.Hrs >= 21) | (dfr.Hrs <= 7), 'DayColor'] = "#5e3c99"


dfr = dfr.drop('DateTime', 1)
dfr = dfr.drop('DateTimeEST', 1)
# dfr = dfr.drop('Date', 1)
# print dfr.dtypes
dfr.Date = pd.to_datetime(dfr.Date, format="%Y-%m-%d")
print min(dfr.Date)
print max(dfr.Date)
# print sorted(dfr.Date.tail(40))
print dfr.Date.unique()

# creating week indicators

dfr.loc[(dfr.Date < '2014-10-31 00:00:00'), "Week"] = "Week 1"
dfr.loc[(dfr.Date < '2014-10-31 00:00:00'), "WeekColor"] = "#bdc9e1"
dfr.loc[(dfr.Date >= '2014-10-31 00:00:00') & (dfr.Date < '2014-11-07 00:00:00'), "Week"] = "Week 2"
dfr.loc[(dfr.Date >= '2014-10-31 00:00:00') & (dfr.Date < '2014-11-07 00:00:00'), "WeekColor"] = "#74a9cf"
dfr.loc[(dfr.Date >= '2014-11-07 00:00:00') & (dfr.Date < '2014-11-14 00:00:00'), "Week"] = "Week 3"
dfr.loc[(dfr.Date >= '2014-11-07 00:00:00') & (dfr.Date < '2014-11-14 00:00:00'), "WeekColor"] = "#2b8cbe"
dfr.loc[(dfr.Date >= '2014-11-14 00:00:00'), "Week"] = "Week 4"
dfr.loc[(dfr.Date >= '2014-11-14 00:00:00'), "WeekColor"] = "#045a8d"
print dfr.shape
print dfr.head()
dfr.to_csv('paths2.csv', index=False)
# print dfr.DateTimeEST.map(lambda x: x.strip(' ')[11:13])
# dfr.to_csv('testspit.csv', index=None)
