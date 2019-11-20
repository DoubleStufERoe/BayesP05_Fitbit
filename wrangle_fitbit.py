from debug import local_settings, timeifdebug, timeargsifdebug, frame_splain
import pandas as pd
import numpy as np
from datetime import timedelta, datetime
from acquire import check_df
import csv
from os import walk


def acquire_fitbit_daily(directory='fitbit', splain=False):
    rows = []
    file_list = []
    for (dirpath,dirnames,filenames) in walk(directory):
        file_list.extend(filenames)
    
    for i in file_list:
        filename = directory + '/' + i
    
        with open(filename) as f:
            cr = csv.reader(f)
            for row in cr:
                if len(row)> 8:
                    rows.append(row)
    
    df = pd.DataFrame(rows[1:],columns=rows[0])
    df = df[df.Date != 'Date']
    df.Date = pd.to_datetime(df.Date, format='%Y-%m-%d')
    df = df.sort_values(by='Date')
    df = df.rename(columns={'Date': 'date'})
    
    return check_df(df, splain=splain)


def get_activities_data(directory='fitbit', splain=local_settings.splain):
    df = acquire_fitbit_daily(directory=directory)
    df = prep_activities_data(df, splain=splain)

    return check_df(df, splain=splain)


def prep_activities_data(df, splain=local_settings.splain):
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
    #df.date=pd.to_datetime(df.date, format='%Y-%m-%d')
    df = df.set_index('date')
    for col in df.columns[df.dtypes == 'object']:
        df[col] = df[col].str.replace(',','').astype('float')
    df['mins_tot'] = df.mins_sed + df.mins_light + df.mins_mod + df.mins_heavy
    df['mins_off'] = 1440 - df.mins_tot
    df['week_day'] = df.index.strftime('%w-%a')
    df['cals_idle'] = df.cals_burned - df.activity_cals
    df['mins_idle'] = df.mins_sed + df.mins_off
    df['idle_cals_per_min'] = df.cals_idle/(df.mins_idle)
    df['daily_rest_cals'] = df.idle_cals_per_min * 1440

    return check_df(df, splain=splain)


def predict_missing(df, to_csv=True, csv_name=r'missing_data_predicted.csv'):
    new_df = df[df.index < '2018-07-07'].drop(columns='week_day')
    df_early = df[(df.steps > 0) & (df.index < '2018-07-07')]
    df_missing = df[(df.steps == 0) & (df.index < '2018-07-07')]
    df_early.drop(columns='week_day',inplace=True)
    df_missing.drop(columns='week_day',inplace=True)

    for col in df_missing.columns:
        df_missing[col]= round(df_early[col].mean(),2)

    if to_csv: 
        export_csv = df_missing.to_csv(csv_name,header=True)
    return df_missing
    
    
def merge_imputed(df, df_mask, imputed_df, agg_fn='mean'):
    new_df = df.copy()
    for col in imputed_df.columns:
        df[col] = np.where(df_mask, imputed_df[col].agg(agg_fn), df[col])
    return df
 


if __name__ == '__main__':
    get_activities_data(splain=True)

