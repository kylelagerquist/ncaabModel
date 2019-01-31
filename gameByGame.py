import pandas as pd
pd.set_option('display.max_columns', 500)

# data = pd.read_csv(r"/Users/kylelagerquist/PycharmProjects/NCAAB/ncaaBallGames", sep=",")
data = pd.read_csv(r"C:\Users\klagerquist\PycharmProjects\FrontView-Hit-List\ncaa.csv", sep=",",)
data.gametime = data.gametime.str[:10]
data = data.sort_values(by=['gametime'])
data = data[-(data['season'] == 2013)]
bigDict = {}


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
        self.three_points_made = three_points_made
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

    def update(self,points,games,field_goals_made,field_goals_att,three_points_made,three_points_att,
                 two_points_made,two_points_att,free_throws_made,free_throws_att,offensive_rebounds,defensive_rebounds,
                 assists,turnovers,steals,blocks,personal_fouls,opp_points,opp_field_goals_made,opp_field_goals_att,
                 opp_three_points_made,opp_three_points_att,opp_two_points_made,opp_two_points_att,
                 opp_free_throws_made,opp_free_throws_att,opp_offensive_rebounds,opp_defensive_rebounds,opp_assists,
                 opp_turnovers,opp_steals,opp_blocks,opp_personal_foul):
        self.points += points
        self.games += games
        self.field_goals_made += field_goals_made
        self.field_goals_att += field_goals_att
        self.three_points_made += three_points_made
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
        self.opp_personal_foul += opp_personal_foul


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
h_field_goals_percent = []
h_three_points_percent = []
h_two_points_percent = []
h_free_throws_percent = []
h_opp_points_per_game = []
h_opp_field_goals_made_per_game = []
h_opp_field_goals_att_per_game = []
h_opp_three_points_made_per_game = []
h_opp_three_points_att_per_game = []
h_opp_two_points_made_per_game = []
h_opp_two_points_att_per_game = []
h_opp_free_throws_made_per_game = []
h_opp_free_throws_att_per_game = []
h_opp_offensive_rebounds_per_game = []
h_opp_defensive_rebounds_per_game = []
h_opp_assists_per_game = []
h_opp_turnovers_per_game = []
h_opp_steals_per_game = []
h_opp_blocks_per_game = []
h_opp_personal_fouls_per_game = []
h_opp_field_goals_percent = []
h_opp_three_points_percent = []
h_opp_two_points_percent = []
h_opp_free_throws_percent = []
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
a_field_goals_percent = []
a_three_points_percent = []
a_two_points_percent = []
a_free_throws_percent = []
a_opp_points_per_game = []
a_opp_field_goals_made_per_game = []
a_opp_field_goals_att_per_game = []
a_opp_three_points_made_per_game = []
a_opp_three_points_att_per_game = []
a_opp_two_points_made_per_game = []
a_opp_two_points_att_per_game = []
a_opp_free_throws_made_per_game = []
a_opp_free_throws_att_per_game = []
a_opp_offensive_rebounds_per_game = []
a_opp_defensive_rebounds_per_game = []
a_opp_assists_per_game = []
a_opp_turnovers_per_game = []
a_opp_steals_per_game = []
a_opp_blocks_per_game = []
a_opp_personal_fouls_per_game = []
a_opp_field_goals_percent = []
a_opp_three_points_percent = []
a_opp_two_points_percent = []
a_opp_free_throws_percent = []




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
        awayName = str(row['a_market']) + ' ' + str(row['a_name'])
        homeName = str(row['a_market']) + ' ' + str(row['h_name'])
        first_for_away = False
        first_for_home = False

        if homeName not in seasonDict:
            seasonDict[homeName] = team(homeName,
                                        row['h_points'],
                                        1,
                                        row['h_field_goals_made'],
                                        row['h_field_goals_att'],
                                        row['h_three_points_made'],
                                        row['h_three_points_att'],
                                        row['h_two_points_made'],
                                        row['h_two_points_att'],
                                        row['h_free_throws_made'],
                                        row['h_free_throws_att'],
                                        row['h_offensive_rebounds'],
                                        row['h_defensive_rebounds'],
                                        row['h_assists'],
                                        row['h_turnovers'],
                                        row['h_steals'],
                                        row['h_blocks'],
                                        row['h_personal_fouls'],
                                        row['a_points'],
                                        row['a_field_goals_made'],
                                        row['a_field_goals_att'],
                                        row['a_three_points_made'],
                                        row['a_three_points_att'],
                                        row['a_two_points_made'],
                                        row['a_two_points_att'],
                                        row['a_free_throws_made'],
                                        row['a_free_throws_att'],
                                        row['a_offensive_rebounds'],
                                        row['a_defensive_rebounds'],
                                        row['a_assists'],
                                        row['a_turnovers'],
                                        row['a_steals'],
                                        row['a_blocks'],
                                        row['a_personal_fouls'])
            first_for_home = True

        if awayName not in seasonDict:
            seasonDict[awayName] = team(awayName,
                                        row['a_points'],
                                        1,
                                        row['a_field_goals_made'],
                                        row['a_field_goals_att'],
                                        row['a_three_points_made'],
                                        row['a_three_points_att'],
                                        row['a_two_points_made'],
                                        row['a_two_points_att'],
                                        row['a_free_throws_made'],
                                        row['a_free_throws_att'],
                                        row['a_offensive_rebounds'],
                                        row['a_defensive_rebounds'],
                                        row['a_assists'],
                                        row['a_turnovers'],
                                        row['a_steals'],
                                        row['a_blocks'],
                                        row['a_personal_fouls'],
                                        row['h_points'],
                                        row['h_field_goals_made'],
                                        row['h_field_goals_att'],
                                        row['h_three_points_made'],
                                        row['h_three_points_att'],
                                        row['h_two_points_made'],
                                        row['h_two_points_att'],
                                        row['h_free_throws_made'],
                                        row['h_free_throws_att'],
                                        row['h_offensive_rebounds'],
                                        row['h_defensive_rebounds'],
                                        row['h_assists'],
                                        row['h_turnovers'],
                                        row['h_steals'],
                                        row['h_blocks'],
                                        row['h_personal_fouls'])
            first_for_away = True

        awayTeam = seasonDict[awayName]
        homeTeam = seasonDict[homeName]

        append_to_columns(awayTeam, homeTeam)

        if not first_for_home:
            homeTeam.update(row['h_points'],
                                        1,
                                        row['h_field_goals_made'],
                                        row['h_field_goals_att'],
                                        row['h_three_points_made'],
                                        row['h_three_points_att'],
                                        row['h_two_points_made'],
                                        row['h_two_points_att'],
                                        row['h_free_throws_made'],
                                        row['h_free_throws_att'],
                                        row['h_offensive_rebounds'],
                                        row['h_defensive_rebounds'],
                                        row['h_assists'],
                                        row['h_turnovers'],
                                        row['h_steals'],
                                        row['h_blocks'],
                                        row['h_personal_fouls'],
                                        row['a_points'],
                                        row['a_field_goals_made'],
                                        row['a_field_goals_att'],
                                        row['a_three_points_made'],
                                        row['a_three_points_att'],
                                        row['a_two_points_made'],
                                        row['a_two_points_att'],
                                        row['a_free_throws_made'],
                                        row['a_free_throws_att'],
                                        row['a_offensive_rebounds'],
                                        row['a_defensive_rebounds'],
                                        row['a_assists'],
                                        row['a_turnovers'],
                                        row['a_steals'],
                                        row['a_blocks'],
                                        row['a_personal_fouls'])

        if not first_for_away:
            awayTeam.update(row['a_points'],
                                        1,
                                        row['a_field_goals_made'],
                                        row['a_field_goals_att'],
                                        row['a_three_points_made'],
                                        row['a_three_points_att'],
                                        row['a_two_points_made'],
                                        row['a_two_points_att'],
                                        row['a_free_throws_made'],
                                        row['a_free_throws_att'],
                                        row['a_offensive_rebounds'],
                                        row['a_defensive_rebounds'],
                                        row['a_assists'],
                                        row['a_turnovers'],
                                        row['a_steals'],
                                        row['a_blocks'],
                                        row['a_personal_fouls'],
                                        row['h_points'],
                                        row['h_field_goals_made'],
                                        row['h_field_goals_att'],
                                        row['h_three_points_made'],
                                        row['h_three_points_att'],
                                        row['h_two_points_made'],
                                        row['h_two_points_att'],
                                        row['h_free_throws_made'],
                                        row['h_free_throws_att'],
                                        row['h_offensive_rebounds'],
                                        row['h_defensive_rebounds'],
                                        row['h_assists'],
                                        row['h_turnovers'],
                                        row['h_steals'],
                                        row['h_blocks'],
                                        row['h_personal_fouls'])


def append_to_columns(awayTeam,homeTeam):
    h_points_per_game.append(homeTeam.points / homeTeam.games)
    h_field_goals_made_per_game.append(homeTeam.field_goals_made / homeTeam.games)
    h_field_goals_att_per_game.append(homeTeam.field_goals_att / homeTeam.games)
    h_three_points_made_per_game.append(homeTeam.three_points_made / homeTeam.games)
    h_three_points_att_per_game.append(homeTeam.three_points_att / homeTeam.games)
    h_two_points_made_per_game.append(homeTeam.two_points_made / homeTeam.games)
    h_two_points_att_per_game.append(homeTeam.two_points_att / homeTeam.games)
    h_free_throws_made_per_game.append(homeTeam.free_throws_made / homeTeam.games)
    h_free_throws_att_per_game.append(homeTeam.free_throws_att / homeTeam.games)
    h_offensive_rebounds_per_game.append(homeTeam.offensive_rebounds / homeTeam.games)
    h_defensive_rebounds_per_game.append(homeTeam.defensive_rebounds / homeTeam.games)
    h_assists_per_game.append(homeTeam.assists / homeTeam.games)
    h_turnovers_per_game.append(homeTeam.turnovers / homeTeam.games)
    h_steals_per_game.append(homeTeam.steals / homeTeam.games)
    h_blocks_per_game.append(homeTeam.blocks / homeTeam.games)
    h_personal_fouls_per_game.append(homeTeam.personal_fouls / homeTeam.games)

    h_field_goals_percent.append(divide(homeTeam.field_goals_made, homeTeam.field_goals_att))
    h_three_points_percent.append(divide(homeTeam.three_points_made, homeTeam.three_points_att))
    h_two_points_percent.append(divide(homeTeam.two_points_made, homeTeam.two_points_att))
    h_free_throws_percent.append(divide(homeTeam.free_throws_made, homeTeam.free_throws_att))

    h_opp_points_per_game.append(homeTeam.opp_points / homeTeam.games)
    h_opp_field_goals_made_per_game.append(homeTeam.opp_field_goals_made / homeTeam.games)
    h_opp_field_goals_att_per_game.append(homeTeam.opp_field_goals_att / homeTeam.games)
    h_opp_three_points_made_per_game.append(homeTeam.opp_three_points_made / homeTeam.games)
    h_opp_three_points_att_per_game.append(homeTeam.opp_three_points_att / homeTeam.games)
    h_opp_two_points_made_per_game.append(homeTeam.opp_two_points_made / homeTeam.games)
    h_opp_two_points_att_per_game.append(homeTeam.opp_two_points_att / homeTeam.games)
    h_opp_free_throws_made_per_game.append(homeTeam.opp_free_throws_made / homeTeam.games)
    h_opp_free_throws_att_per_game.append(homeTeam.opp_free_throws_att / homeTeam.games)
    h_opp_offensive_rebounds_per_game.append(homeTeam.opp_offensive_rebounds / homeTeam.games)
    h_opp_defensive_rebounds_per_game.append(homeTeam.opp_defensive_rebounds / homeTeam.games)
    h_opp_assists_per_game.append(homeTeam.opp_assists / homeTeam.games)
    h_opp_turnovers_per_game.append(homeTeam.opp_turnovers / homeTeam.games)
    h_opp_steals_per_game.append(homeTeam.opp_steals / homeTeam.games)
    h_opp_blocks_per_game.append(homeTeam.opp_blocks / homeTeam.games)
    h_opp_personal_fouls_per_game.append(homeTeam.opp_personal_foul / homeTeam.games)

    h_opp_field_goals_percent.append(divide(homeTeam.opp_field_goals_made, homeTeam.opp_field_goals_att))
    h_opp_three_points_percent.append(divide(homeTeam.opp_three_points_made, homeTeam.opp_three_points_att))
    h_opp_two_points_percent.append(divide(homeTeam.opp_two_points_made, homeTeam.opp_two_points_att))
    h_opp_free_throws_percent.append(divide(homeTeam.opp_free_throws_made, homeTeam.opp_free_throws_att))

    a_points_per_game.append(awayTeam.points / awayTeam.games)
    a_field_goals_made_per_game.append(awayTeam.field_goals_made / awayTeam.games)
    a_field_goals_att_per_game.append(awayTeam.field_goals_att / awayTeam.games)
    a_three_points_made_per_game.append(awayTeam.three_points_made / awayTeam.games)
    a_three_points_att_per_game.append(awayTeam.three_points_att / awayTeam.games)
    a_two_points_made_per_game.append(awayTeam.two_points_made / awayTeam.games)
    a_two_points_att_per_game.append(awayTeam.two_points_att / awayTeam.games)
    a_free_throws_made_per_game.append(awayTeam.free_throws_made / awayTeam.games)
    a_free_throws_att_per_game.append(awayTeam.free_throws_att / awayTeam.games)
    a_offensive_rebounds_per_game.append(awayTeam.offensive_rebounds / awayTeam.games)
    a_defensive_rebounds_per_game.append(awayTeam.defensive_rebounds / awayTeam.games)
    a_assists_per_game.append(awayTeam.assists / awayTeam.games)
    a_turnovers_per_game.append(awayTeam.turnovers / awayTeam.games)
    a_steals_per_game.append(awayTeam.steals / awayTeam.games)
    a_blocks_per_game.append(awayTeam.blocks / awayTeam.games)
    a_personal_fouls_per_game.append(awayTeam.personal_fouls / awayTeam.games)

    a_field_goals_percent.append(divide(awayTeam.field_goals_made, awayTeam.field_goals_att))
    a_three_points_percent.append(divide(awayTeam.three_points_made, awayTeam.three_points_att))
    a_two_points_percent.append(divide(awayTeam.two_points_made, awayTeam.two_points_att))
    a_free_throws_percent.append(divide(awayTeam.free_throws_made, awayTeam.free_throws_att))

    a_opp_points_per_game.append(awayTeam.opp_points / awayTeam.games)
    a_opp_field_goals_made_per_game.append(awayTeam.opp_field_goals_made / awayTeam.games)
    a_opp_field_goals_att_per_game.append(awayTeam.opp_field_goals_att / awayTeam.games)
    a_opp_three_points_made_per_game.append(awayTeam.opp_three_points_made / awayTeam.games)
    a_opp_three_points_att_per_game.append(awayTeam.opp_three_points_att / awayTeam.games)
    a_opp_two_points_made_per_game.append(awayTeam.opp_two_points_made / awayTeam.games)
    a_opp_two_points_att_per_game.append(awayTeam.opp_two_points_att / awayTeam.games)
    a_opp_free_throws_made_per_game.append(awayTeam.opp_free_throws_made / awayTeam.games)
    a_opp_free_throws_att_per_game.append(awayTeam.opp_free_throws_att / awayTeam.games)
    a_opp_offensive_rebounds_per_game.append(awayTeam.opp_offensive_rebounds / awayTeam.games)
    a_opp_defensive_rebounds_per_game.append(awayTeam.opp_defensive_rebounds / awayTeam.games)
    a_opp_assists_per_game.append(awayTeam.opp_assists / awayTeam.games)
    a_opp_turnovers_per_game.append(awayTeam.opp_turnovers / awayTeam.games)
    a_opp_steals_per_game.append(awayTeam.opp_steals / awayTeam.games)
    a_opp_blocks_per_game.append(awayTeam.opp_blocks / awayTeam.games)
    a_opp_personal_fouls_per_game.append(awayTeam.opp_personal_foul / awayTeam.games)

    a_opp_field_goals_percent.append(divide(awayTeam.opp_field_goals_made, awayTeam.opp_field_goals_att))
    a_opp_three_points_percent.append(divide(awayTeam.opp_three_points_made, awayTeam.opp_three_points_att))
    a_opp_two_points_percent.append(divide(awayTeam.opp_two_points_made, awayTeam.opp_two_points_att))
    a_opp_free_throws_percent.append(divide(awayTeam.opp_free_throws_made, awayTeam.opp_free_throws_att))


add_stats()


data['h_points_per_game'] = h_points_per_game
data['h_field_goals_made_per_game'] = h_field_goals_made_per_game
data['h_field_goals_att_per_game'] = h_field_goals_att_per_game
data['h_three_points_made_per_game'] = h_three_points_made_per_game
data['h_three_points_att_per_game'] = h_three_points_att_per_game
data['h_two_points_made_per_game'] = h_two_points_made_per_game
data['h_two_points_att_per_game'] = h_two_points_att_per_game
data['h_free_throws_made_per_game'] = h_free_throws_made_per_game
data['h_free_throws_att_per_game'] = h_free_throws_att_per_game
data['h_offensive_rebounds_per_game'] = h_offensive_rebounds_per_game
data['h_defensive_rebounds_per_game'] = h_defensive_rebounds_per_game
data['h_assists_per_game'] = h_assists_per_game
data['h_turnovers_per_game'] = h_turnovers_per_game
data['h_steals_per_game'] = h_steals_per_game
data['h_blocks_per_game'] = h_blocks_per_game
data['h_personal_fouls_per_game'] = h_personal_fouls_per_game
data['h_field_goals_percent'] = h_field_goals_percent
data['h_three_points_percent'] = h_three_points_percent
data['h_two_points_percent'] = h_two_points_percent
data['h_free_throws_percent'] = h_free_throws_percent
data['h_opp_points_per_game'] = h_opp_points_per_game
data['h_opp_field_goals_made_per_game'] = h_opp_field_goals_made_per_game
data['h_opp_field_goals_att_per_game'] = h_opp_field_goals_att_per_game
data['h_opp_three_points_made_per_game'] = h_opp_three_points_made_per_game
data['h_opp_three_points_att_per_game'] = h_opp_three_points_att_per_game
data['h_opp_two_points_made_per_game'] = h_opp_two_points_made_per_game
data['h_opp_two_points_att_per_game'] = h_opp_two_points_att_per_game
data['h_opp_free_throws_made_per_game'] = h_opp_free_throws_made_per_game
data['h_opp_free_throws_att_per_game'] = h_opp_free_throws_att_per_game
data['h_opp_offensive_rebounds_per_game'] = h_opp_offensive_rebounds_per_game
data['h_opp_defensive_rebounds_per_game'] = h_opp_defensive_rebounds_per_game
data['h_opp_assists_per_game'] = h_opp_assists_per_game
data['h_opp_turnovers_per_game'] = h_opp_turnovers_per_game
data['h_opp_steals_per_game'] = h_opp_steals_per_game
data['h_opp_blocks_per_game'] = h_opp_blocks_per_game
data['h_opp_personal_fouls_per_game'] = h_opp_personal_fouls_per_game
data['h_opp_field_goals_percent'] = h_opp_field_goals_percent
data['h_opp_three_points_percent'] = h_opp_three_points_percent
data['h_opp_two_points_percent'] = h_opp_two_points_percent
data['h_opp_free_throws_percent'] = h_opp_free_throws_percent
data['a_points_per_game'] = a_points_per_game
data['a_field_goals_made_per_game'] = a_field_goals_made_per_game
data['a_field_goals_att_per_game'] = a_field_goals_att_per_game
data['a_three_points_made_per_game'] = a_three_points_made_per_game
data['a_three_points_att_per_game'] = a_three_points_att_per_game
data['a_two_points_made_per_game'] = a_two_points_made_per_game
data['a_two_points_att_per_game'] = a_two_points_att_per_game
data['a_free_throws_made_per_game'] = a_free_throws_made_per_game
data['a_free_throws_att_per_game'] = a_free_throws_att_per_game
data['a_offensive_rebounds_per_game'] = a_offensive_rebounds_per_game
data['a_defensive_rebounds_per_game'] = a_defensive_rebounds_per_game
data['a_assists_per_game'] = a_assists_per_game
data['a_turnovers_per_game'] = a_turnovers_per_game
data['a_steals_per_game'] = a_steals_per_game
data['a_blocks_per_game'] = a_blocks_per_game
data['a_personal_fouls_per_game'] = a_personal_fouls_per_game
data['a_field_goals_percent'] = a_field_goals_percent
data['a_three_points_percent'] = a_three_points_percent
data['a_two_points_percent'] = a_two_points_percent
data['a_free_throws_percent'] = a_free_throws_percent
data['a_opp_points_per_game'] = a_opp_points_per_game
data['a_opp_field_goals_made_per_game'] = a_opp_field_goals_made_per_game
data['a_opp_field_goals_att_per_game'] = a_opp_field_goals_att_per_game
data['a_opp_three_points_made_per_game'] = a_opp_three_points_made_per_game
data['a_opp_three_points_att_per_game'] = a_opp_three_points_att_per_game
data['a_opp_two_points_made_per_game'] = a_opp_two_points_made_per_game
data['a_opp_two_points_att_per_game'] = a_opp_two_points_att_per_game
data['a_opp_free_throws_made_per_game'] = a_opp_free_throws_made_per_game
data['a_opp_free_throws_att_per_game'] = a_opp_free_throws_att_per_game
data['a_opp_offensive_rebounds_per_game'] = a_opp_offensive_rebounds_per_game
data['a_opp_defensive_rebounds_per_game'] = a_opp_defensive_rebounds_per_game
data['a_opp_assists_per_game'] = a_opp_assists_per_game
data['a_opp_turnovers_per_game'] = a_opp_turnovers_per_game
data['a_opp_steals_per_game'] = a_opp_steals_per_game
data['a_opp_blocks_per_game'] = a_opp_blocks_per_game
data['a_opp_personal_fouls_per_game'] = a_opp_personal_fouls_per_game
data['a_opp_field_goals_percent'] = a_opp_field_goals_percent
data['a_opp_three_points_percent'] = a_opp_three_points_percent
data['a_opp_two_points_percent'] = a_opp_two_points_percent
data['a_opp_free_throws_percent'] = a_opp_free_throws_percent

# data.to_csv('ncaaBallGamesUpdated', sep=',', encoding='utf-8')




homeDF = data.filter([
'h_points',
'h_points_per_game',
'h_field_goals_made_per_game',
'h_field_goals_att_per_game',
'h_three_points_made_per_game',
'h_three_points_att_per_game',
'h_two_points_made_per_game',
'h_two_points_att_per_game',
'h_free_throws_made_per_game',
'h_free_throws_att_per_game',
'h_offensive_rebounds_per_game',
'h_defensive_rebounds_per_game',
'h_assists_per_game',
'h_turnovers_per_game',
'h_steals_per_game',
'h_blocks_per_game',
'h_personal_fouls_per_game',
'h_field_goals_percent',
'h_three_points_percent',
'h_two_points_percent',
'h_free_throws_percent',
'a_opp_points_per_game',
'a_opp_field_goals_made_per_game',
'a_opp_field_goals_att_per_game',
'a_opp_three_points_made_per_game',
'a_opp_three_points_att_per_game',
'a_opp_two_points_made_per_game',
'a_opp_two_points_att_per_game',
'a_opp_free_throws_made_per_game',
'a_opp_free_throws_att_per_game',
'a_opp_offensive_rebounds_per_game',
'a_opp_defensive_rebounds_per_game',
'a_opp_assists_per_game',
'a_opp_turnovers_per_game',
'a_opp_steals_per_game',
'a_opp_blocks_per_game',
'a_opp_personal_fouls_per_game',
'a_opp_field_goals_percent',
'a_opp_three_points_percent',
'a_opp_two_points_percent',
'a_opp_free_throws_percent'], axis=1)

awayDF = data.filter([
'a_points',
'a_points_per_game',
'a_field_goals_made_per_game',
'a_field_goals_att_per_game',
'a_three_points_made_per_game',
'a_three_points_att_per_game',
'a_two_points_made_per_game',
'a_two_points_att_per_game',
'a_free_throws_made_per_game',
'a_free_throws_att_per_game',
'a_offensive_rebounds_per_game',
'a_defensive_rebounds_per_game',
'a_assists_per_game',
'a_turnovers_per_game',
'a_steals_per_game',
'a_blocks_per_game',
'a_personal_fouls_per_game',
'a_field_goals_percent',
'a_three_points_percent',
'a_two_points_percent',
'a_free_throws_percent',
'h_opp_points_per_game',
'h_opp_field_goals_made_per_game',
'h_opp_field_goals_att_per_game',
'h_opp_three_points_made_per_game',
'h_opp_three_points_att_per_game',
'h_opp_two_points_made_per_game',
'h_opp_two_points_att_per_game',
'h_opp_free_throws_made_per_game',
'h_opp_free_throws_att_per_game',
'h_opp_offensive_rebounds_per_game',
'h_opp_defensive_rebounds_per_game',
'h_opp_assists_per_game',
'h_opp_turnovers_per_game',
'h_opp_steals_per_game',
'h_opp_blocks_per_game',
'h_opp_personal_fouls_per_game',
'h_opp_field_goals_percent',
'h_opp_three_points_percent',
'h_opp_two_points_percent',
'h_opp_free_throws_percent'], axis=1)


def get_colnames():
    for name in list(awayDF):
        if name

print(list(awayDF))
print(list(homeDF))
