import numpy as np
import pandas as pd
data=pd.read_excel("data_raw.xlsx")

data['Tbar']=[i/1.15/1.05 for i in data['TP']]



data_preprocessed=data[['CCYYMM','DDHHmm','WD','WS','TP','Tbar','HS','DMDIR']]



time_ym=[str(i) for i in data_preprocessed['CCYYMM']]
time_dh=[str(i) for i in data_preprocessed['DDHHmm']]
for i in range(len(time_dh)):
    if len(time_dh[i])==5:
        time_dh[i]='0'+time_dh[i]
time_concat=pd.Series([time_ym[i]+time_dh[i] for i in range(len(time_ym))])
data_preprocessed.insert(loc=0, column='TIME', value=time_concat)

def direction(deg):
    if deg >=348.75:
        deg-=360
    if deg>=-11.25 and deg<11.25:
        return 'N'
    if deg>=11.25 and deg<33.75:
        return 'NNE'
    if deg>=33.75 and deg<56.25:
        return 'NE'
    if deg>=56.25 and deg<78.75:
        return 'ENE'
    if deg>=78.75 and deg<101.25:
        return 'E'
    if deg>=101.25 and deg<123.75:
        return 'ESE'
    if deg>=123.75 and deg<146.25:
        return 'SE'
    if deg>=146.25 and deg<168.75:
        return 'SSE'
    if deg>=168.75 and deg<191.25:
        return 'S'
    if deg>=191.25 and deg<213.75:
        return 'SSW'
    if deg>=213.75 and deg<236.25:
        return 'SW'
    if deg>=236.25 and deg<258.75:
        return 'WSW'
    if deg>=258.75 and deg<281.25:
        return 'W'
    if deg>=281.25 and deg<303.75:
        return 'WNW'
    if deg>=303.75 and deg<326.25:
        return 'NW'
    if deg>=326.25 and deg<348.75:
        return 'NNW'

dmdir_cache=data_preprocessed.loc[0:,'DMDIR']
dmdir_trans=[i+180 for i in dmdir_cache]
data_preprocessed.loc[0:,'DMDIR']=dmdir_trans
winddir_tran=[i for i in data_preprocessed.loc[0:,'WD']]
wavedir_tran=[i for i in data_preprocessed.loc[0:,'DMDIR']]

WAVEDIR=[direction(i) for i in wavedir_tran]
data_preprocessed.insert(loc=9, column='WAVEDIR', value=WAVEDIR)
WINDDIR=[direction(i) for i in winddir_tran]
data_preprocessed.insert(loc=4, column='WINDDIR', value=WINDDIR)

year_tran=[int(i[0:4]) for i in data_preprocessed['TIME']]
data_preprocessed.insert(loc=1, column='YEAR', value=year_tran)

month_tran=[int(i[4:6])-1 for i in data_preprocessed['TIME']]
data_preprocessed.insert(loc=2, column='MONTH', value=month_tran)

season_tran=[i[4:6] for i in data_preprocessed['TIME']]
def seasons(month):
    if month=='12' or month=='01' or month=='02':
        return 0
    if month=='03' or month=='04' or month=='05':
        return 1
    if month=='06' or month=='07' or month=='08':
        return 2
    if month=='09' or month=='10' or month=='11':
        return 3
SEASONS=[seasons(i) for i in season_tran]
data_preprocessed.insert(loc=3, column='SEASON', value=SEASONS)

data_preprocessed.reindex(['TIME','YEAR','SEASON','TP','Tbar','HS','DMDIR','DIRECTION'])

del data_preprocessed['CCYYMM']
del data_preprocessed['DDHHmm']

with pd.ExcelWriter('data_preprocessed.xlsx') as writer:
    data_preprocessed.to_excel(writer,sheet_name='Sheet 1')

