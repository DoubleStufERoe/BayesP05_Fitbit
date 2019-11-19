from debug import local_settings, timeifdebug, timeargsifdebug, frame_splain
import pandas as pd
from datetime import timedelta, datetime

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
    for col in df.columns[df.dtypes == 'object']:
        df[col] = df[col].str.replace(',','').astype(int)
    df['mins_tot'] = df.mins_sed + df.mins_light + df.mins_mod + df.mins_heavy
    df['mins_off'] = 1440 - df.mins_tot

    return df


if __name__ == '__main__':
    frame_splain(get_activities_data(), splain=True)
