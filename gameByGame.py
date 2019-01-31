import pandas as pd
pd.set_option('display.max_columns', 500)

data = pd.read_csv(r"/Users/kylelagerquist/PycharmProjects/NCAAB/ncaaBallGames", sep=",")
data.gametime = data.gametime.str[:10]
data = data.sort_values(by=['gametime'])
bigDict = {}

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

class team:
    def __init__(self, name,points,games,field_goals_made,field_goals_att,three_points_made,three_points_att,
                 two_points_made,two_points_att,free_throws_made,free_throws_att,offensive_rebounds,defensive_rebounds,
                 assists,turnovers,steals,blocks,personal_fouls,opp_points,opp_field_goals_made,opp_field_goals_att,
                 opp_three_points_made,opp_three_points_att,opp_two_points_made,opp_two_points_att,
                 opp_free_throws_made,opp_free_throws_att,opp_offensive_rebounds,opp_defensive_rebounds,opp_assists,
                 opp_turnovers,opp_steals,opp_blocks,opp_personal_foul):
        self.name = name
        self.points = points
        self.games = games
        self.field_goals_made = field_goals_made
        self.field_goals_att = field_goals_att
        self.opp_three_points_made = three_points_made
        self.three_points_att = three_points_att
        self.two_points_made = two_points_made
        self.two_points_att = two_points_att
        self.free_throws_made = free_throws_made
        self.free_throws_att = free_throws_att
        self.offensive_rebounds = offensive_rebounds
        self.defensive_rebounds = defensive_rebounds
        self.assists = assists
        self.turnovers = turnovers
        self.steals = steals
        self.blocks = blocks
        self.personal_fouls = personal_fouls
        self.opp_points = opp_points
        self.opp_field_goals_made = opp_field_goals_made
        self.opp_field_goals_att = opp_field_goals_att
        self.opp_three_points_made = opp_three_points_made
        self.opp_three_points_att = opp_three_points_att
        self.opp_two_points_made = opp_two_points_made
        self.opp_two_points_att = opp_two_points_att
        self.opp_free_throws_made = opp_free_throws_made
        self.opp_free_throws_att = opp_free_throws_att
        self.opp_offensive_rebounds = opp_offensive_rebounds
        self.opp_defensive_rebounds = opp_defensive_rebounds
        self.opp_assists = opp_assists
        self.opp_turnovers = opp_turnovers
        self.opp_steals = opp_steals
        self.opp_blocks = opp_blocks
        self.opp_personal_foul = opp_personal_foul

    def update(self, name,points,games,field_goals_made,field_goals_att,three_points_made,three_points_att,
                 two_points_made,two_points_att,free_throws_made,free_throws_att,offensive_rebounds,defensive_rebounds,
                 assists,turnovers,steals,blocks,personal_fouls,opp_points,opp_field_goals_made,opp_field_goals_att,
                 opp_three_points_made,opp_three_points_att,opp_two_points_made,opp_two_points_att,
                 opp_free_throws_made,opp_free_throws_att,opp_offensive_rebounds,opp_defensive_rebounds,opp_assists,
                 opp_turnovers,opp_steals,opp_blocks,opp_personal_foul):
        self.name += name
        self.points += points
        self.games += games
        self.field_goals_made += field_goals_made
        self.field_goals_att += field_goals_att
        self.opp_three_points_made += three_points_made
        self.three_points_att += three_points_att
        self.two_points_made += two_points_made
        self.two_points_att += two_points_att
        self.free_throws_made += free_throws_made
        self.free_throws_att += free_throws_att
        self.offensive_rebounds += offensive_rebounds
        self.defensive_rebounds += defensive_rebounds
        self.assists += assists
        self.turnovers += turnovers
        self.steals += steals
        self.blocks += blocks
        self.personal_fouls += personal_fouls
        self.opp_points += opp_points
        self.opp_field_goals_made += opp_field_goals_made
        self.opp_field_goals_att += opp_field_goals_att
        self.opp_three_points_made += opp_three_points_made
        self.opp_three_points_att += opp_three_points_att
        self.opp_two_points_made += opp_two_points_made
        self.opp_two_points_att += opp_two_points_att
        self.opp_free_throws_made += opp_free_throws_made
        self.opp_free_throws_att += opp_free_throws_att
        self.opp_offensive_rebounds += opp_offensive_rebounds
        self.opp_defensive_rebounds += opp_defensive_rebounds
        self.opp_assists += opp_assists
        self.opp_turnovers += opp_turnovers
        self.opp_steals += opp_steals
        self.opp_blocks += opp_blocks
        self.opp_personal_foul += opp_personal_fou
    allColsseason





h_points_per_game = []
h_field_goals_made_per_game = []
h_field_goals_att_per_game = []
h_three_points_made_per_game = []
h_three_points_att_per_game = []
h_two_points_made_per_game = []
h_two_points_att_per_game = []
h_free_throws_made_per_game = []
h_free_throws_att_per_game = []
h_offensive_rebounds_per_game = []
h_defensive_rebounds_per_game = []
h_assists_per_game = []
h_turnovers_per_game = []
h_steals_per_game = []
h_blocks_per_game = []
h_personal_fouls_per_game = []
a_points_per_game = []
a_field_goals_made_per_game = []
a_field_goals_att_per_game = []
a_three_points_made_per_game = []
a_three_points_att_per_game = []
a_two_points_made_per_game = []
a_two_points_att_per_game = []
a_free_throws_made_per_game = []
a_free_throws_att_per_game = []
a_offensive_rebounds_per_game = []
a_defensive_rebounds_per_game = []
a_assists_per_game = []
a_turnovers_per_game = []
a_steals_per_game = []
a_blocks_per_game = []
a_personal_fouls_per_game = []


ppg = []
apg = []
opp_blk_pg = []
blk_pg = []
def_rb_pg = []
fg_att_pg = []
ft_pg = []
off_rb_pg_ = []
fls_pg = []
stls_pg = []
thr_att_pg = []
thr_pg = []
tpg = []
two_att_pg = []
twos_pg = []
ft_per = []
fg_per = []
thr_per = []
two_per = []
total_rb = []
opp_ppg = []
opp_apg = []
opp_def_rb_pg = []
opp_fg_att_pg = []
opp_ft_pg = []
opp_off_rb_pg_ = []
opp_fls_pg = []
opp_stls_pg = []
opp_thr_att_pg = []
opp_thr_pg = []
opp_tpg = []
opp_two_att_pg = []
opp_twos_pg = []
opp_ft_per = []
opp_fg_per = []
opp_thr_per = []
opp_two_per = []
opp_total_rb = []


def divide(num, den):
    if den != 0:
        return num / den
    else:
        return 0


def add_stats():
    for index, row in data.iterrows():
        season = str(row['season'])
        if season not in bigDict:
            bigDict[season] = {}

        seasonDict = bigDict[season]
        awayName = str(row['market']) + ' ' + str(row['name'])
        homeName = str(row['opp_market']) + ' ' + str(row['opp_name'])
        if awayName not in seasonDict:
            seasonDict[awayName] = team(awayName, row['points'], 1, row['assists'], row['blocked_att'],
                                    row['blocks'], row['defensive_rebounds'], row['field_goals_att'],
                                    row['field_goals_made'], row['free_throws_att'], row['free_throws_made'],
                                    row['offensive_rebounds'], row['personal_fouls'],
                                    row['steals'], row['three_points_att'], row['three_points_made'], row['turnovers'],
                                    row['two_points_att'], row['two_points_pct'], row['opp_points_game'],
                                    row['opp_field_goals_made'], row['opp_field_goals_att'],
                                    row['opp_three_points_made'],
                                    row['opp_three_points_att'], row['opp_two_points_made'], row['opp_two_points_att'],
                                    row['opp_free_throws_made'], row['opp_free_throws_att'],
                                    row['opp_offensive_rebounds'],
                                    row['opp_defensive_rebounds'], row['opp_assists'], row['opp_turnovers'],
                                    row['opp_steals'],
                                    row['opp_personal_fouls'])

            seasonDict[awayName] = team({"name":awayName,
                                         "points":row['points'],
                                         "games":1,
                                         "assists":row['assists'],
                                         "defensive_rebounds":row['defensive_rebounds'],
                                         "field_goals_att":row['field_goals_att'],
                                        "field_goals_made":row['field_goals_made'],
                                         "free_throws_att":row['free_throws_att'],
                                         'free_throws_made':row['free_throws_made'],
                                        'offensive_rebounds':row['offensive_rebounds'],
                                         'personal_fouls':row['personal_fouls'],
                                        'steals':row['steals'],
                                         'three_points_att':row['three_points_att'],
                                         'three_points_made':row['three_points_made'],
                                        'turnovers':row['turnovers'],
                                        'two_points_att':row['two_points_att'],
                                         'two_points_pct':row['two_points_pct'],
                                         'opp_points_game':row['opp_points_game'],
                                        'opp_field_goals_made':row['opp_field_goals_made'],
                                         'opp_field_goals_att':row['opp_field_goals_att'],
                                        'opp_three_points_made':row['opp_three_points_made'],
                                        'opp_three_points_att':row['opp_three_points_att'],
                                         'opp_two_points_made':row['opp_two_points_made'],
                                        'opp_two_points_att':row['opp_two_points_att'],
                                        'opp_free_throws_made':row['opp_free_throws_made'],
                                         'opp_free_throws_att':row['opp_free_throws_att'],
                                        'opp_offensive_rebounds':row['opp_offensive_rebounds'],
                                        'opp_defensive_rebounds':row['opp_defensive_rebounds'],
                                         'opp_assists':row['opp_assists'],
                                         'opp_turnovers':row['opp_turnovers'],
                                        'opp_steals':row['opp_steals'],
                                        'opp_personal_fouls':row['opp_personal_fouls']})



            curr = seasonDict[name]
            print(type(curr.points),curr.points)
            ppg.append(curr.points)
            apg.append(curr.assists)
            opp_blk_pg.append(curr.opp_blocks)
            blk_pg.append(curr.blocks)
            def_rb_pg.append(curr.dfsn_rb)
            fg_att_pg.append(curr.fg_att)
            ft_pg.append(curr.ft)
            off_rb_pg_.append(curr.ofsn_rb)
            fls_pg.append(curr.pr_fls)
            stls_pg.append(curr.steals)
            thr_att_pg.append(curr.three_att)
            thr_pg.append(curr.threes)
            tpg.append(curr.turnovr)
            two_att_pg.append(curr.two_att)
            twos_pg.append(curr.twos)
            ft_per.append(divide(curr.ft, curr.ft_att))
            fg_per.append(divide(curr.fg, curr.fg_att))
            thr_per.append(divide(curr.threes, curr.three_att))
            two_per.append(divide(curr.twos, curr.two_att))
            total_rb.append(curr.ofsn_rb + curr.dfsn_rb)
            opp_ppg.append(curr.opp_points_game)
            opp_apg.append(curr.opp_assists)
            opp_def_rb_pg.append(curr.opp_defensive_rebounds)
            opp_fg_att_pg.append(curr.opp_field_goals_att)
            opp_ft_pg.append(curr.opp_free_throws_made)
            opp_off_rb_pg_.append(curr.opp_defensive_rebounds)
            opp_fls_pg.append(curr.opp_personal_fouls)
            opp_stls_pg.append(curr.opp_steals)
            opp_thr_att_pg.append(curr.opp_three_points_att)
            opp_thr_pg.append(curr.opp_three_points_made)
            opp_tpg.append(curr.opp_turnovers)
            opp_two_att_pg.append(curr.opp_two_points_att)
            opp_twos_pg.append(curr.opp_two_points_made)
            opp_ft_per.append(divide(curr.opp_free_throws_made, curr.opp_free_throws_att))
            opp_fg_per.append(divide(curr.opp_field_goals_made, curr.opp_field_goals_att))
            opp_thr_per.append(divide(curr.opp_three_points_made, curr.opp_two_points_att))
            opp_two_per.append(divide(curr.opp_two_points_made, curr.opp_three_points_att))
            opp_total_rb.append(curr.opp_offensive_rebounds + curr.opp_defensive_rebounds)
        else:
            curr = seasonDict[name]

            ppg.append(curr.points / curr.games)
            apg.append(curr.assists / curr.games)
            opp_blk_pg.append(curr.opp_blocks / curr.games)
            blk_pg.append(curr.blocks / curr.games)
            def_rb_pg.append(curr.dfsn_rb / curr.games)
            fg_att_pg.append(curr.fg_att / curr.games)
            ft_pg.append(curr.ft / curr.games)
            off_rb_pg_.append(curr.ofsn_rb / curr.games)
            fls_pg.append(curr.pr_fls / curr.games)
            stls_pg.append(curr.steals / curr.games)
            thr_att_pg.append(curr.three_att / curr.games)
            thr_pg.append(curr.threes / curr.games)
            tpg.append(curr.turnovr / curr.games)
            two_att_pg.append(curr.two_att / curr.games)
            twos_pg.append(curr.twos / curr.games)
            ft_per.append(divide(curr.ft , curr.ft_att))
            fg_per.append(divide(curr.fg , curr.fg_att))
            thr_per.append(divide(curr.threes , curr.three_att))
            two_per.append(divide(curr.twos , curr.two_att))
            total_rb.append((curr.ofsn_rb + curr.dfsn_rb) / curr.games)
            opp_ppg.append(curr.opp_points_game / curr.games)
            opp_apg.append(curr.opp_assists / curr.games)
            opp_def_rb_pg.append(curr.opp_defensive_rebounds / curr.games)
            opp_fg_att_pg.append(curr.opp_field_goals_att / curr.games)
            opp_ft_pg.append(curr.opp_free_throws_made / curr.games)
            opp_off_rb_pg_.append(curr.opp_defensive_rebounds / curr.games)
            opp_fls_pg.append(curr.opp_personal_fouls / curr.games)
            opp_stls_pg.append(curr.opp_steals / curr.games)
            opp_thr_att_pg.append(curr.opp_three_points_att / curr.games)
            opp_thr_pg.append(curr.opp_three_points_made / curr.games)
            opp_tpg.append(curr.opp_turnovers / curr.games)
            opp_two_att_pg.append(curr.opp_two_points_att / curr.games)
            opp_twos_pg.append(curr.opp_two_points_made / curr.games)
            opp_ft_per.append(divide(curr.opp_free_throws_made , curr.opp_free_throws_att))
            opp_fg_per.append(divide(curr.opp_field_goals_made , curr.opp_free_throws_att))
            opp_thr_per.append(divide(curr.opp_three_points_made , curr.opp_three_points_att))
            opp_two_per.append(divide(curr.opp_two_points_made , curr.opp_two_points_att))
            opp_total_rb.append((curr.opp_offensive_rebounds + curr.opp_defensive_rebounds) / curr.games)

            seasonDict[name].update(row['points'], 1, row['assists'], row['blocked_att'],
                                    row['blocks'], row['defensive_rebounds'], row['field_goals_att'],
                                    row['field_goals_made'], row['free_throws_att'], row['free_throws_made'],
                                    row['offensive_rebounds'], row['personal_fouls'],
                                    row['steals'], row['three_points_att'], row['three_points_made'], row['turnovers'],
                                    row['two_points_att'], row['two_points_pct'], row['opp_points_game'],
                                    row['opp_field_goals_made'], row['opp_field_goals_att'],
                                    row['opp_three_points_made'],
                                    row['opp_three_points_att'], row['opp_two_points_made'], row['opp_two_points_att'],
                                    row['opp_free_throws_made'], row['opp_free_throws_att'],
                                    row['opp_offensive_rebounds'],
                                    row['opp_defensive_rebounds'], row['opp_assists'], row['opp_turnovers'],
                                    row['opp_steals'],
                                    row['opp_personal_fouls'])


add_stats()

data['ppg'] = ppg
data['apg'] = apg
data['opp_blk_pg'] = opp_blk_pg
data['blk_pg'] = blk_pg
data['def_rb_pg'] = def_rb_pg
data['fg_att_pg'] = fg_att_pg
data['ft_pg'] = ft_pg
data['off_rb_pg_'] = off_rb_pg_
data['fls_pg'] = fls_pg
data['stls_pg'] = stls_pg
data['thr_att_pg'] = thr_att_pg
data['thr_pg'] = thr_pg
data['tpg'] = tpg
data['two_att_pg'] = two_att_pg
data['twos_pg'] = twos_pg
data['ft_per'] = ft_per
data['fg_per'] = fg_per
data['thr_per'] = thr_per
data['two_per'] = two_per
data['total_rb'] = total_rb
data['opp_ppg'] = opp_ppg
data['opp_apg'] = opp_apg
data['opp_def_rb_pg'] = opp_def_rb_pg
data['opp_fg_att_pg'] = opp_fg_att_pg
data['opp_ft_pg'] = opp_ft_pg
data['opp_off_rb_pg_'] = opp_off_rb_pg_
data['opp_fls_pg'] = opp_fls_pg
data['opp_stls_pg'] = opp_stls_pg
data['opp_thr_att_pg'] = opp_thr_att_pg
data['opp_thr_pg'] = opp_thr_pg
data['opp_tpg'] = opp_tpg
data['opp_two_att_pg'] = opp_two_att_pg
data['opp_twos_pg'] = opp_twos_pg
data['opp_ft_per'] = opp_ft_per
data['opp_fg_per'] = opp_fg_per
data['opp_thr_per'] = opp_thr_per
data['opp_two_per'] = opp_two_per
data['opp_total_rb'] = opp_total_rb

data.to_csv('ncaaBallGamesUpdated', sep=',', encoding='utf-8')


