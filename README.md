Visualizing my openPaths Data
===

Used the app Open Paths (http://openpaths.cc) and tracked my movements for a month.
The data obtained had the following features:

- Lat-Long coordinates
- Altitide
- Date & Time
- Device I'm using
- os & version

In order to get more info from my data I ended up doing some feature engineering using python (refer to openPaths.py). Thus I ended up creating the following 3 categories:

- Time of the day (Day/Night)
- Day type (Weekday/Weekend)
- Week #