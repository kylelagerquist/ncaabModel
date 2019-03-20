import pandas as pd
import statsmodels.api as sm
import numpy as np
from sklearn import datasets

out = {'Charlotte': 'CHA', 'Oklahoma City': 'OKC', 'Denver': 'DEN', 'New Orleans': 'NO', 'Phoenix': 'PHO', 'Indiana': 'IND',
       'Cleveland': 'CLE', 'Brooklyn': 'BKN', 'Washington': 'WAS', 'Orlando': 'ORL', 'San Antonio': 'SA', 'Utah': 'UTA',
       'Houston': 'HOU', 'Toronto': 'TOR', 'Detroit': 'DET', 'Dallas': 'DAL', 'Minnesota': 'MIN', 'Chicago': 'CHI', 'Boston': 'BOS',
       'Miami': 'MIA', 'Milwaukee': 'MIL', 'L.A. Clippers': 'LAC', 'Atlanta': 'ATL', 'New York': 'NY', 'Sacramento': 'SAC',
       'L.A. Lakers': 'LAL', 'Golden State': 'GS', 'Memphis': 'MEM', 'Portland': 'POR', 'Philadelphia': 'PHI', 'East': np.nan,
       'World All Stars': np.nan, 'USA All Stars': np.nan, 'West': np.nan, 'Team LeBron':np.nan, 'Team World':np.nan,
       'Team Stephen':np.nan, 'Team USA':np.nan}
cols = ['oppt2PA-pg', 'oppt2PM-pg', 'oppt3PA-pg', 'oppt3PM-pg', 'opptAR-pg',
        'opptAST-pg', 'opptBLK-pg', 'opptBLKR-pg', 'opptDRB-pg', 'opptDrtg-pg', 'opptEDiff-pg', 'opptFGA-pg', 'opptFGM-pg',
        'opptFIC-pg', 'opptFIC40-pg', 'opptFTA-pg', 'opptFTM-pg', 'opptMin-pg', 'opptORB-pg', 'opptOrtg-pg', 'opptPF-pg',
        'opptPPS-pg', 'opptPTS-pg', 'opptSTL-pg', 'opptTO-pg', 'opptTRB-pg','team2PA-pg', 'team2PM-pg',
        'team3PA-pg', 'team3PM-pg', 'teamAR-pg', 'teamAST-pg', 'teamBLK-pg', 'teamBLKR-pg', 'teamDRB-pg',
        'teamDayOff', 'teamDrtg-pg', 'teamEDiff-pg', 'teamFGA-pg', 'teamFGM-pg', 'teamFIC-pg', 'teamFIC40-pg', 'teamFTA-pg',
        'teamFTM-pg', 'teamMin-pg', 'teamORB-pg', 'teamOrtg-pg', 'teamPF-pg', 'teamPPS-pg', 'teamPTS-pg',
        'teamPace-pg', 'teamPoss-pg', 'teamSTL-pg', 'teamTO-pg', 'teamTRB-pg', 'oppt2PA-pg_x',
        'oppt2PM-pg_x', 'oppt3PA-pg_x', 'oppt3PM-pg_x', 'opptAR-pg_x', 'opptAST-pg_x', 'opptBLK-pg_x', 'opptBLKR-pg_x',
        'opptDRB-pg_x', 'opptDrtg-pg_x', 'opptEDiff-pg_x', 'opptFGA-pg_x', 'opptFGM-pg_x', 'opptFIC-pg_x', 'opptFIC40-pg_x',
        'opptFTA-pg_x', 'opptFTM-pg_x', 'opptMin-pg_x', 'opptORB-pg_x', 'opptOrtg-pg_x', 'opptPF-pg_x', 'opptPPS-pg_x',
        'opptPTS-pg_x', 'opptSTL-pg_x', 'opptTO-pg_x', 'opptTRB-pg_x', 'team2PA-pg_x', 'team2PM-pg_x',
        'team3PA-pg_x', 'team3PM-pg_x', 'teamAR-pg_x', 'teamAST-pg_x', 'teamBLK-pg_x', 'teamBLKR-pg_x',
        'teamDRB-pg_x', 'teamDayOff_x', 'teamDrtg-pg_x', 'teamEDiff-pg_x', 'teamFGA-pg_x', 'teamFGM-pg_x', 'teamFIC-pg_x',
        'teamFIC40-pg_x', 'teamFTA-pg_x', 'teamFTM-pg_x', 'teamMin-pg_x', 'teamORB-pg_x', 'teamOrtg-pg_x', 'teamPF-pg_x',
        'teamPPS-pg_x', 'teamPTS-pg_x', 'teamPace-pg_x', 'teamPoss-pg_x', 'teamSTL-pg_x', 'teamTO-pg_x',
        'teamTRB-pg_x']

historic = pd.read_csv(r'C:\Users\klagerquist\PycharmProjects\FrontView-Hit-List\nba_historic.csv')
odds2016 = pd.read_csv(r'C:\Users\klagerquist\PycharmProjects\FrontView-Hit-List\nba_od_2016.csv')
odds2017 = pd.read_csv(r'C:\Users\klagerquist\PycharmProjects\FrontView-Hit-List\nba_od_2017.csv')
# odds2016['key'] = odds2016['key'].str[4:6] + odds2016['key'].str[6:8] + odds2016['key'].str[:4] + odds2016['key'].str[8:]
# odds2017['key'] = odds2017['key'].str[4:6] + odds2017['key'].str[6:8] + odds2017['key'].str[:4] + odds2017['key'].str[8:]

historic['finalTotal'] = historic['teamPTS']+historic['teamPTS_x']
new = pd.merge(historic,odds2016,how='inner',left_on='key',right_on='key')
print(list(historic))
print(list(new))
# 2016: o585, u585, p19
# 2017: o624, u574, p16


def totals_eval(actual, pred, odds):
    win = 0
    loss = 0
    push = 0
    for x in range(0,len(actual)):
        a = actual[x]
        p = pred[x]
        o = odds[x]
        if a == o:
            push += 1
        elif p > o:
            if p > a:
                win += 1
            else:
                loss += 1
        else:
            if p < a:
                win += 1
            else:
                loss += 1
    print(win,loss,push,win/(win+loss))







def using_statsmodels(df,features,target,with_coef,testDF):
    X = df[features]
    y = df[target]
    if with_coef:
        X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    print(df.shape,testDF.shape)
    predictions = model.predict(testDF[features])
    # totals_eval(testDF['finalTotal'], predictions, testDF['total'])
    return model


def optimizer(df,features,target,with_coef,testDf):
    attempt = using_statsmodels(df,features,target,with_coef,testDf)
    pvals = attempt.pvalues.tolist()
    cols = attempt.pvalues.index.tolist()
    worst = max(pvals)
    ind = pvals.index(worst)
    bad_col = cols[ind]
    cols.remove(bad_col)
    # if len(cols) > 0:
    #     optimizer(df, cols, target, with_coef)



a = historic[historic['season'].isin(['2013','2014','2015'])]
optimizer(a,cols,'finalTotal',True, new)



