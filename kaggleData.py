from google.cloud import bigquery
import pandas as pd
from google.oauth2 import service_account
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/kylelagerquist/PycharmProjects/NCAAB/bigQueryCredentials.json"
client = bigquery.Client()

def get_data_table():
    kaggle_ncaa = client.dataset('ncaa_basketball', project='bigquery-public-data')
    retrievedData = client.get_dataset(kaggle_ncaa)
    singleGameTable = client.get_table(retrievedData.table('mbb_games_sr'))
    return get_wanted_columns(singleGameTable)

def get_wanted_columns(table):
    allCols = ('season',
               'gametime',
               'h_name',
               'h_market',
               'a_name',
               'a_market',
               'h_points',
               'a_points',
               'h_field_goals_made',
               'h_field_goals_att',
               'h_three_points_made',
               'h_three_points_att',
               'h_two_points_made',
               'h_two_points_att',
               'h_free_throws_made',
               'h_free_throws_att',
               'h_offensive_rebounds',
               'h_defensive_rebounds',
               'h_assists',
               'h_turnovers',
               'h_steals',
               'h_blocks',
               'h_personal_fouls',
               'a_field_goals_made',
               'a_field_goals_att',
               'a_three_points_made',
               'a_three_points_att',
               'a_two_points_made',
               'a_two_points_att',
               'a_free_throws_made',
               'a_free_throws_att',
               'a_offensive_rebounds',
               'a_defensive_rebounds',
               'a_assists',
               'a_turnovers',
               'a_steals',
               'a_blocks',
               'a_personal_fouls')

    table_subset = [col for col in table.schema if col.name in allCols]
    rows = [x for x in client.list_rows(table, start_index=0, selected_fields=table_subset, max_results=100000)]

    return rows_to_df(rows)


def rows_to_df(rows):
    rowsArray = []
    for i in rows:
        rowsArray.append(dict(i))

    df = pd.DataFrame(rowsArray)
    return df


def create_csv():
    newDF = get_data_table()
    newDF.to_csv('ncaaBallGames', sep=',', encoding='utf-8')

create_csv()

