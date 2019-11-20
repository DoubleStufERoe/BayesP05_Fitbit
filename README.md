##README Time Series Fitbit Project


#### Data Dictionary

'cals_burned', 'steps', 'dist', 'flrs', 'mins_sed', 'mins_light',
       'mins_mod', 'mins_heavy', 'activity_cals', 'mins_tot', 'mins_off',
       'week_day', 'cals_idle', 'mins_idle', 'idle_cals_per_min'

- cals_burned: calories burned in 24 hour period
- steps: number of steps taken in 24 hour period (running, walking, etc)
- activity_cals: The number of calories burned during the day when the user was active above sedentary level. This value is calculated minute by minute. This includes BMR for those minutes as well as activity burned calories.
- flrs: 1 flrs is equal to an elevation change of ten feet.
- dist: Distance traveled in kilometers in one 24 hour period.
- mins_sed: Minutes at rest, not counted towards active minutes.
- mins_light: Metabolic equivalents (MET) rate below 3 but not sedentary (walking, making the bed, etc)
- mins_mod: MET rate between 3 and 5 (brisk walking, water aerobics, etc)
- mins_heavy: MET rate 6 or greater. (lifting weights, running, etc)
- activity_cals: Calories burned during activity (not including BMR)
- mins_tot: Total minutes recorded by fitbit in 24 hour period.
- mins_off: Total minutes not recorded by fitbit in 24 hour period.
- week_day: Day of week
- cals_idle: Idle calories burned excluding activity calories
- mins_idle: Idle minutes in 24 hour period.
- idle_cals_per_min: Idle calories burned per minute.


sources: 
https://www.awpnow.com/main/2018/01/16/why-your-fitbit-active-minutes-mean-more-than-your-steps/

https://help.fitbit.com/articles/en_US/Help_article/1379/?q=active+minutes&l=en_US&fs=Search&pn=1

https://dev.fitbit.com/build/reference/web-api/activity/

https://www.fitabase.com/media/1748/fitabasedatadictionary.pdf