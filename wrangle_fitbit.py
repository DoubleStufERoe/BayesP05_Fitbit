from debug import local_settings, timeifdebug, timeargsifdebug, frame_splain
import pandas as pd
from datetime import timedelta, datetime


def acquire_fitbit_daily():
    rows = []
    file_list = []
    for (dirpath,dirnames,filenames) in walk('fitbit'):
        file_list.extend(filenames)
    
    for i in file_list:
        filename = 'fitbit/' + i
    
        with open(filename) as f:
            cr = csv.reader(f)
            for row in cr:
                if len(row)> 8:
                    rows.append(row)
    
    df = pd.DataFrame(rows[1:],columns=rows[0])
    df = df[df.Date != 'Date']
    return df

def get_activities_data():
    df = pd.read_csv('activities.csv')
    df = df.rename(columns={
        'Date': 'date',
        'Calories Burned': 'cals_burned',
        'Steps': 'steps',
        'Distance': 'dist',
        'Floors': 'flrs',
        'Minutes Sedentary': 'mins_sed',
        'Minutes Lightly Active': 'mins_light',
        'Minutes Fairly Active': 'mins_mod',
        'Minutes Very Active': 'mins_heavy',
        'Activity Calories': 'activity_cals',
    })
    df.date=pd.to_datetime(df.date, format='%m/%d/%y')
    df = df.set_index('date')
    for col in df.columns[df.dtypes == 'object']:
        df[col] = df[col].str.replace(',','').astype(int)
    df['mins_tot'] = df.mins_sed + df.mins_light + df.mins_mod + df.mins_heavy
    df['mins_off'] = 1440 - df.mins_tot
    df['weekday'] = df.index.strftime('%w-%a')


    return df


if __name__ == '__main__':
    frame_splain(get_activities_data(), splain=True)
