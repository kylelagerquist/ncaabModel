from datetime import datetime, timedelta
from sportsreference.ncaab.teams import Teams
from sportsreference.ncaab.boxscore import Boxscores
import pandas as pd
import to_database as td


points_per_game = 0.37678095290479685
field_goals_made_per_game = 0.8633446291420521
field_goals_att_per_game = -0.20537280030155183
three_points_made_per_game = 0.5960540359868984
three_points_att_per_game = -0.12110562220840851
two_points_made_per_game = 0.2672905931552056
two_points_att_per_game = -0.08426717809365507
free_throws_made_per_game = 0.5360480209780171
free_throws_att_per_game = -0.21940833901567686
offensive_rebounds_per_game = -0.046374148744446
defensive_rebounds_per_game = -0.07005016035174176
assists_per_game = 0.039563772060962524
turnovers_per_game = 0.034712762620641595
steals_per_game = -0.03124236227161787
field_goals_percent = -41.25519584980158
free_throws_percent = -5.932001240803108
opp_points_per_game_allowed = 0.7004705674048275
opp_field_goals_made_per_game_allowed = -0.5034609271205643
opp_field_goals_att_per_game_allowed = 0.10384905362167636
opp_three_points_made_per_game_allowed = -0.1877727830493967
opp_two_points_made_per_game_allowed = -0.31568814407060924
opp_two_points_att_per_game_allowed = 0.12420903140989135
opp_free_throws_made_per_game_allowed = -0.19408071849980985
opp_free_throws_att_per_game_allowed = 0.02563362849346587
opp_defensive_rebounds_per_game_allowed = -0.06664744850220218
opp_assists_per_game_allowed = -0.13333565997904304
opp_turnovers_per_game_allowed = -0.018378934609531442
opp_steals_per_game_allowed = -0.08310069196147381
opp_blocks_per_game_allowed = -0.12845173719888855
opp_personal_fouls_per_game_allowed = 0.09771865234963091
opp_field_goals_percent_allowed = 34.112545610610304
opp_three_points_percent_allowed = -1.58611544389508
opp_free_throws_percent_allowed = 1.543097665857241

# points_per_game,
# field_goals_made_per_game,
# field_goals_att_per_game,
# three_points_made_per_game,
# three_points_att_per_game,
# two_points_made_per_game,
# two_points_att_per_game,
# free_throws_made_per_game,
# free_throws_att_per_game,
# offensive_rebounds_per_game,
# defensive_rebounds_per_game,
# assists_per_game,
# turnovers_per_game,
# steals_per_game,
# field_goals_percent,
# free_throws_percent,
# opp_points_per_game_allowed,
# opp_field_goals_made_per_game_allowed,
# opp_field_goals_att_per_game_allowed,
# opp_three_points_made_per_game_allowed,
# opp_two_points_made_per_game_allowed,
# opp_two_points_att_per_game_allowed,
# opp_free_throws_made_per_game_allowed,
# opp_free_throws_att_per_game_allowed,
# opp_defensive_rebounds_per_game_allowed,
# opp_assists_per_game_allowed,
# opp_turnovers_per_game_allowed,
# opp_steals_per_game_allowed,
# opp_blocks_per_game_allowed,
# opp_personal_fouls_per_game_allowed,
# opp_field_goals_percent_allowed,
# opp_three_points_percent_allowed,
# opp_free_throws_percent_allowed,


team_alt_names = {'Abilene Christian': 'Abilene Christian', 'Air Force': 'Air Force', 'Akron': 'Akron',
                  'Alabama A&M': 'Alabama A&M',
                  'Alabama-Birmingham': 'Alabama-Birmingham', 'Alabama State': 'Alabama State', 'Alabama': 'Alabama',
                  'Albany (NY)': 'Albany (NY)', 'Alcorn State': 'Alcorn State', 'American': 'American',
                  'Appalachian State': 'Appalachian State', 'Arizona State': 'Arizona State', 'Arizona': 'Arizona',
                  'Little Rock': 'Little Rock', 'Arkansas-Pine Bluff': 'Arkansas-Pine Bluff',
                  'Arkansas State': 'Arkansas State',
                  'Arkansas': 'Arkansas', 'Army': 'Army', 'Auburn': 'Auburn', 'Austin Peay': 'Austin Peay',
                  'Ball State': 'Ball State', 'Baylor': 'Baylor', 'Belmont': 'Belmont',
                  'Bethune-Cookman': 'Bethune-Cookman',
                  'Binghamton': 'Binghamton', 'Boise State': 'Boise State', 'Boston College': 'Boston College',
                  'Boston University': 'Boston University', 'Bowling Green State': 'Bowling Green State',
                  'Bradley': 'Bradley',
                  'BYU': 'Brigham Young', 'Brown': 'Brown', 'Bryant': 'Bryant', 'Bucknell': 'Bucknell',
                  'Buffalo': 'Buffalo', 'Butler': 'Butler', 'Cal Poly': 'Cal Poly',
                  'Cal State Bakersfield': 'Cal State Bakersfield',
                  'Cal State Fullerton': 'Cal State Fullerton', 'Cal State Northridge': 'Cal State Northridge',
                  'California Baptist': 'California Baptist', 'UC-Davis': 'UC-Davis', 'UC-Irvine': 'UC-Irvine',
                  'UC-Riverside': 'UC-Riverside', 'UCSB': 'UC-Santa Barbara',
                  'California': 'University of California', 'Campbell': 'Campbell',
                  'Canisius': 'Canisius',
                  'Central Arkansas': 'Central Arkansas', 'Central Connecticut': 'Central Connecticut State',
                  'UCF': 'Central Florida', 'Central Michigan': 'Central Michigan',
                  'Charleston Southern': 'Charleston Southern', 'Charlotte': 'Charlotte', 'Chattanooga': 'Chattanooga',
                  'Chicago State': 'Chicago State', 'Cincinnati': 'Cincinnati', 'Citadel': 'Citadel',
                  'Clemson': 'Clemson',
                  'Cleveland State': 'Cleveland State', 'Coastal Carolina': 'Coastal Carolina', 'Colgate': 'Colgate',
                  'College of Charleston': 'College of Charleston', 'Colorado State': 'Colorado State',
                  'Colorado': 'Colorado',
                  'Columbia': 'Columbia', 'UConn': 'Connecticut', 'Coppin State': 'Coppin State',
                  'Cornell': 'Cornell',
                  'Creighton': 'Creighton', 'Dartmouth': 'Dartmouth', 'Davidson': 'Davidson', 'Dayton': 'Dayton',
                  'Delaware State': 'Delaware State', 'Delaware': 'Delaware', 'Denver': 'Denver', 'DePaul': 'DePaul',
                  'Detroit': 'Detroit Mercy', 'Drake': 'Drake', 'Drexel': 'Drexel', 'Duke': 'Duke',
                  'Duquesne': 'Duquesne',
                  'East Carolina': 'East Carolina', 'ETSU': 'East Tennessee State',
                  'Eastern Illinois': 'Eastern Illinois', 'Eastern Kentucky': 'Eastern Kentucky',
                  'Eastern Michigan': 'Eastern Michigan', 'Eastern Washington': 'Eastern Washington', 'Elon': 'Elon',
                  'Evansville': 'Evansville', 'Fairfield': 'Fairfield', 'Fairleigh Dickinson': 'Fairleigh Dickinson',
                  'Florida A&M': 'Florida A&M', 'Florida Atlantic': 'Florida Atlantic',
                  'Florida Gulf Coast': 'Florida Gulf Coast',
                  'Florida International': 'Florida International', 'Florida State': 'Florida State',
                  'Florida': 'Florida',
                  'Fordham': 'Fordham', 'Fresno State': 'Fresno State', 'Furman': 'Furman',
                  'Gardner-Webb': 'Gardner-Webb',
                  'George Mason': 'George Mason', 'George Washington': 'George Washington', 'Georgetown': 'Georgetown',
                  'Georgia Southern': 'Georgia Southern', 'Georgia State': 'Georgia State',
                  'Georgia Tech': 'Georgia Tech',
                  'Georgia': 'Georgia', 'Gonzaga': 'Gonzaga', 'Grambling': 'Grambling', 'Grand Canyon': 'Grand Canyon',
                  'Green Bay': 'Green Bay', 'Hampton': 'Hampton', 'Hartford': 'Hartford', 'Harvard': 'Harvard',
                  'Hawaii': 'Hawaii',
                  'High Point': 'High Point', 'Hofstra': 'Hofstra', 'Holy Cross': 'Holy Cross',
                  'Houston Baptist': 'Houston Baptist',
                  'Houston': 'Houston', 'Howard': 'Howard', 'Idaho State': 'Idaho State', 'Idaho': 'Idaho',
                  'UIC': 'Illinois-Chicago', 'Illinois State': 'Illinois State', 'Illinois': 'Illinois',
                  'Incarnate Word': 'Incarnate Word', 'Indiana State': 'Indiana State', 'Indiana': 'Indiana',
                  'Iona': 'Iona',
                  'Iowa State': 'Iowa State', 'Iowa': 'Iowa', 'Purdue-Fort Wayne': 'Purdue-Fort Wayne',
                  'IUPUI': 'IUPUI',
                  'Jackson State': 'Jackson State', 'Jacksonville State': 'Jacksonville State',
                  'Jacksonville': 'Jacksonville',
                  'James Madison': 'James Madison', 'Kansas State': 'Kansas State', 'Kansas': 'Kansas',
                  'Kennesaw State': 'Kennesaw State', 'Kent State': 'Kent State', 'Kentucky': 'Kentucky',
                  'La Salle': 'La Salle',
                  'Lafayette': 'Lafayette', 'Lamar': 'Lamar', 'Lehigh': 'Lehigh', 'Liberty': 'Liberty',
                  'Lipscomb': 'Lipscomb',
                  'Long Beach State': 'Long Beach State', 'LIU-Brooklyn': 'Long Island University',
                  'Longwood': 'Longwood',
                  'Louisiana': 'Louisiana', 'Louisiana-Monroe': 'Louisiana-Monroe', 'LSU': 'Louisiana State',
                  'Louisiana Tech': 'Louisiana Tech', 'Louisville': 'Louisville', 'Loyola (IL)': 'Loyola (IL)',
                  'Loyola Marymount': 'Loyola Marymount', 'Loyola (MD)': 'Loyola (MD)', 'Maine': 'Maine',
                  'Manhattan': 'Manhattan',
                  'Marist': 'Marist', 'Marquette': 'Marquette', 'Marshall': 'Marshall',
                  'UMBC': 'Maryland-Baltimore County', 'Maryland-Eastern Shore': 'Maryland-Eastern Shore',
                  'Maryland': 'Maryland', 'UMass-Lowell': 'Massachusetts-Lowell', 'UMass': 'Massachusetts',
                  'McNeese State': 'McNeese State', 'Memphis': 'Memphis', 'Mercer': 'Mercer',
                  'Miami (FL)': 'Miami (FL)',
                  'Miami (OH)': 'Miami (OH)', 'Michigan State': 'Michigan State', 'Michigan': 'Michigan',
                  'Middle Tennessee': 'Middle Tennessee', 'Milwaukee': 'Milwaukee', 'Minnesota': 'Minnesota',
                  'Mississippi State': 'Mississippi State', 'Mississippi Valley State': 'Mississippi Valley State',
                  'Ole Miss': 'Mississippi', 'UMKC': 'Missouri-Kansas City',
                  'Missouri State': 'Missouri State',
                  'Missouri': 'Missouri', 'Monmouth': 'Monmouth', 'Montana State': 'Montana State',
                  'Montana': 'Montana',
                  'Morehead State': 'Morehead State', 'Morgan State': 'Morgan State',
                  "Mount St. Mary's": "Mount St. Mary's",
                  'Murray State': 'Murray State', 'Navy': 'Navy', 'Omaha': 'Omaha', 'Nebraska': 'Nebraska',
                  'UNLV': 'Nevada-Las Vegas', 'Nevada': 'Nevada', 'New Hampshire': 'New Hampshire',
                  'New Mexico State': 'New Mexico State', 'New Mexico': 'New Mexico', 'New Orleans': 'New Orleans',
                  'Niagara': 'Niagara', 'Nicholls State': 'Nicholls State', 'NJIT': 'NJIT',
                  'Norfolk State': 'Norfolk State',
                  'North Alabama': 'North Alabama', 'UNC Asheville': 'North Carolina-Asheville',
                  'North Carolina A&T': 'North Carolina A&T', 'North Carolina Central': 'North Carolina Central',
                  'UNC Greensboro': 'North Carolina-Greensboro',
                  'NC State': 'North Carolina State',
                  'UNC Wilmington': 'North Carolina-Wilmington', 'UNC': 'North Carolina',
                  'North Dakota State': 'North Dakota State', 'North Dakota': 'North Dakota',
                  'North Florida': 'North Florida',
                  'North Texas': 'North Texas', 'Northeastern': 'Northeastern', 'Northern Arizona': 'Northern Arizona',
                  'Northern Colorado': 'Northern Colorado', 'Northern Illinois': 'Northern Illinois',
                  'Northern Iowa': 'Northern Iowa', 'Northern Kentucky': 'Northern Kentucky',
                  'Northwestern State': 'Northwestern State', 'Northwestern': 'Northwestern',
                  'Notre Dame': 'Notre Dame',
                  'Oakland': 'Oakland', 'Ohio State': 'Ohio State', 'Ohio': 'Ohio', 'Oklahoma State': 'Oklahoma State',
                  'Oklahoma': 'Oklahoma', 'Old Dominion': 'Old Dominion', 'Oral Roberts': 'Oral Roberts',
                  'Oregon State': 'Oregon State', 'Oregon': 'Oregon', 'Pacific': 'Pacific', 'Penn State': 'Penn State',
                  'Penn': 'Pennsylvania', 'Pepperdine': 'Pepperdine', 'Pitt': 'Pittsburgh',
                  'Portland State': 'Portland State', 'Portland': 'Portland', 'Prairie View': 'Prairie View',
                  'Presbyterian': 'Presbyterian', 'Princeton': 'Princeton', 'Providence': 'Providence',
                  'Purdue': 'Purdue',
                  'Quinnipiac': 'Quinnipiac', 'Radford': 'Radford', 'Rhode Island': 'Rhode Island', 'Rice': 'Rice',
                  'Richmond': 'Richmond', 'Rider': 'Rider', 'Robert Morris': 'Robert Morris', 'Rutgers': 'Rutgers',
                  'Sacramento State': 'Sacramento State', 'Sacred Heart': 'Sacred Heart',
                  'Saint Francis (PA)': 'Saint Francis (PA)',
                  "Saint Joseph's": "Saint Joseph's", 'Saint Louis': 'Saint Louis',
                  "Saint Mary's": "Saint Mary's (CA)",
                  "St. Peter's": "Saint Peter's", 'Sam Houston State': 'Sam Houston State', 'Samford': 'Samford',
                  'San Diego State': 'San Diego State', 'San Diego': 'San Diego', 'San Francisco': 'San Francisco',
                  'San Jose State': 'San Jose State', 'Santa Clara': 'Santa Clara', 'Savannah State': 'Savannah State',
                  'Seattle': 'Seattle', 'Seton Hall': 'Seton Hall', 'Siena': 'Siena', 'South Alabama': 'South Alabama',
                  'South Carolina State': 'South Carolina State', 'USC Upstate': 'South Carolina Upstate',
                  'South Carolina': 'South Carolina', 'South Dakota State': 'South Dakota State',
                  'South Dakota': 'South Dakota',
                  'South Florida': 'South Florida', 'Southeast Missouri State': 'Southeast Missouri State',
                  'Southeastern Louisiana': 'Southeastern Louisiana', 'USC': 'Southern California',
                  'SIU-Edwardsville': 'SIU Edwardsville', 'Southern Illinois': 'Southern Illinois',
                  'SMU': 'Southern Methodist', 'Southern Miss': 'Southern Mississippi',
                  'Southern Utah': 'Southern Utah', 'Southern': 'Southern', 'St. Bonaventure': 'St. Bonaventure',
                  'St. Francis (NY)': 'St. Francis (NY)', "St. John's (NY)": "St. John's (NY)", 'Stanford': 'Stanford',
                  'Stephen F. Austin': 'Stephen F. Austin', 'Stetson': 'Stetson', 'Stony Brook': 'Stony Brook',
                  'Syracuse': 'Syracuse', 'Temple': 'Temple', 'UT-Martin': 'Tennessee-Martin',
                  'Tennessee State': 'Tennessee State', 'Tennessee Tech': 'Tennessee Tech', 'Tennessee': 'Tennessee',
                  'Texas A&M-Corpus Christi': 'Texas A&M-Corpus Christi', 'Texas A&M': 'Texas A&M',
                  'Texas-Arlington': 'Texas-Arlington', 'Texas Christian': 'Texas Christian',
                  'UTEP': 'Texas-El Paso',
                  'Texas-Rio Grande Valley': 'Texas-Rio Grande Valley', 'UTSA': 'Texas-San Antonio',
                  'Texas Southern': 'Texas Southern', 'Texas State': 'Texas State', 'Texas Tech': 'Texas Tech',
                  'Texas': 'Texas',
                  'Toledo': 'Toledo', 'Towson': 'Towson', 'Troy': 'Troy', 'Tulane': 'Tulane', 'Tulsa': 'Tulsa',
                  'UCLA': 'UCLA',
                  'Utah State': 'Utah State', 'Utah Valley': 'Utah Valley', 'Utah': 'Utah', 'Valparaiso': 'Valparaiso',
                  'Vanderbilt': 'Vanderbilt', 'Vermont': 'Vermont', 'Villanova': 'Villanova',
                  'VCU': 'Virginia Commonwealth', 'VMI': 'VMI', 'Virginia Tech': 'Virginia Tech',
                  'Virginia': 'Virginia', 'Wagner': 'Wagner', 'Wake Forest': 'Wake Forest',
                  'Washington State': 'Washington State',
                  'Washington': 'Washington', 'Weber State': 'Weber State', 'West Virginia': 'West Virginia',
                  'Western Carolina': 'Western Carolina', 'Western Illinois': 'Western Illinois',
                  'Western Kentucky': 'Western Kentucky', 'Western Michigan': 'Western Michigan',
                  'Wichita State': 'Wichita State',
                  'William & Mary': 'William & Mary', 'Winthrop': 'Winthrop', 'Wisconsin': 'Wisconsin',
                  'Wofford': 'Wofford',
                  'Wright State': 'Wright State', 'Wyoming': 'Wyoming', 'Xavier': 'Xavier', 'Yale': 'Yale',
                  'Youngstown State': 'Youngstown State'}


class ballgame:
    def __init__(self, name, points_per_game, field_goals_made_per_game, field_goals_att_per_game,
                 three_points_made_per_game, three_points_att_per_game, two_points_made_per_game,
                 two_points_att_per_game, free_throws_made_per_game, free_throws_att_per_game,
                 offensive_rebounds_per_game, defensive_rebounds_per_game, assists_per_game, turnovers_per_game,
                 steals_per_game, field_goals_percent, free_throws_percent, opp_points_per_game_allowed,
                 opp_field_goals_made_per_game_allowed, opp_field_goals_att_per_game_allowed,
                 opp_three_points_made_per_game_allowed, opp_two_points_made_per_game_allowed,
                 opp_two_points_att_per_game_allowed, opp_free_throws_made_per_game_allowed,
                 opp_free_throws_att_per_game_allowed, opp_defensive_rebounds_per_game_allowed,
                 opp_assists_per_game_allowed, opp_turnovers_per_game_allowed, opp_steals_per_game_allowed,
                 opp_blocks_per_game_allowed, opp_personal_fouls_per_game_allowed, opp_field_goals_percent_allowed,
                 opp_three_points_percent_allowed, opp_free_throws_percent_allowed,
                 ):
        self.name = name
        self.points_per_game = points_per_game
        self.field_goals_made_per_game = field_goals_made_per_game
        self.field_goals_att_per_game = field_goals_att_per_game
        self.three_points_made_per_game = three_points_made_per_game
        self.three_points_att_per_game = three_points_att_per_game
        self.two_points_made_per_game = two_points_made_per_game
        self.two_points_att_per_game = two_points_att_per_game
        self.free_throws_made_per_game = free_throws_made_per_game
        self.free_throws_att_per_game = free_throws_att_per_game
        self.offensive_rebounds_per_game = offensive_rebounds_per_game
        self.defensive_rebounds_per_game = defensive_rebounds_per_game
        self.assists_per_game = assists_per_game
        self.turnovers_per_game = turnovers_per_game
        self.steals_per_game = steals_per_game
        self.field_goals_percent = field_goals_percent
        self.free_throws_percent = free_throws_percent
        self.opp_points_per_game_allowed = opp_points_per_game_allowed
        self.opp_field_goals_made_per_game_allowed = opp_field_goals_made_per_game_allowed
        self.opp_field_goals_att_per_game_allowed = opp_field_goals_att_per_game_allowed
        self.opp_three_points_made_per_game_allowed = opp_three_points_made_per_game_allowed
        self.opp_two_points_made_per_game_allowed = opp_two_points_made_per_game_allowed
        self.opp_two_points_att_per_game_allowed = opp_two_points_att_per_game_allowed
        self.opp_free_throws_made_per_game_allowed = opp_free_throws_made_per_game_allowed
        self.opp_free_throws_att_per_game_allowed = opp_free_throws_att_per_game_allowed
        self.opp_defensive_rebounds_per_game_allowed = opp_defensive_rebounds_per_game_allowed
        self.opp_assists_per_game_allowed = opp_assists_per_game_allowed
        self.opp_turnovers_per_game_allowed = opp_turnovers_per_game_allowed
        self.opp_steals_per_game_allowed = opp_steals_per_game_allowed
        self.opp_blocks_per_game_allowed = opp_blocks_per_game_allowed
        self.opp_personal_fouls_per_game_allowed = opp_personal_fouls_per_game_allowed
        self.opp_field_goals_percent_allowed = opp_field_goals_percent_allowed
        self.opp_three_points_percent_allowed = opp_three_points_percent_allowed
        self.opp_free_throws_percent_allowed = opp_free_throws_percent_allowed

    def info(self):
        print(self.away + ' at ' + self.home)

    def predictScore(self):
        return (self.points_per_game * points_per_game + self.field_goals_made_per_game * field_goals_made_per_game +
                self.field_goals_att_per_game * field_goals_att_per_game + self.three_points_made_per_game *
                three_points_made_per_game + self.three_points_att_per_game * three_points_att_per_game +
                self.two_points_made_per_game * two_points_made_per_game + self.two_points_att_per_game *
                two_points_att_per_game + self.free_throws_made_per_game * free_throws_made_per_game +
                self.free_throws_att_per_game * free_throws_att_per_game + self.offensive_rebounds_per_game *
                offensive_rebounds_per_game + self.defensive_rebounds_per_game * defensive_rebounds_per_game +
                self.assists_per_game * assists_per_game + self.turnovers_per_game * turnovers_per_game +
                self.steals_per_game * steals_per_game + self.field_goals_percent * field_goals_percent +
                self.free_throws_percent * free_throws_percent + self.opp_points_per_game_allowed *
                opp_points_per_game_allowed + self.opp_field_goals_made_per_game_allowed *
                opp_field_goals_made_per_game_allowed + self.opp_field_goals_att_per_game_allowed *
                opp_field_goals_att_per_game_allowed + self.opp_three_points_made_per_game_allowed *
                opp_three_points_made_per_game_allowed + self.opp_two_points_made_per_game_allowed *
                opp_two_points_made_per_game_allowed + self.opp_two_points_att_per_game_allowed *
                opp_two_points_att_per_game_allowed + self.opp_free_throws_made_per_game_allowed *
                opp_free_throws_made_per_game_allowed + self.opp_free_throws_att_per_game_allowed *
                opp_free_throws_att_per_game_allowed + self.opp_defensive_rebounds_per_game_allowed *
                opp_defensive_rebounds_per_game_allowed + self.opp_assists_per_game_allowed *
                opp_assists_per_game_allowed + self.opp_turnovers_per_game_allowed *
                opp_turnovers_per_game_allowed + self.opp_steals_per_game_allowed *
                opp_steals_per_game_allowed + self.opp_blocks_per_game_allowed *
                opp_blocks_per_game_allowed + self.opp_personal_fouls_per_game_allowed *
                opp_personal_fouls_per_game_allowed + self.opp_field_goals_percent_allowed *
                opp_field_goals_percent_allowed + self.opp_three_points_percent_allowed *
                opp_three_points_percent_allowed + self.opp_free_throws_percent_allowed *
                opp_free_throws_percent_allowed)


def get_team_data():
    allTeams = {}
    teams = Teams(2019)
    for team in teams:
        allTeams[team.name] = team
    return allTeams



def get_todays_games():
    todaysGames = []
    teamData = get_team_data()
    today = datetime.today()
    games_today = Boxscores(today).games[today.strftime('%-m-%-d-%Y')]

    for game in games_today:
        try:
            awayName = team_alt_names[game['away_name']]
            homeName = team_alt_names[game['home_name']]
            awayInfo = teamData[awayName]
            homeInfo = teamData[homeName]
            ag = awayInfo.games_played
            hg = homeInfo.games_played

            away = ballgame(awayName,
                            awayInfo.points / ag,
                            awayInfo.field_goals / ag,
                            awayInfo.field_goal_attempts / ag,
                            awayInfo.three_point_field_goals / ag,
                            awayInfo.three_point_field_goal_attempts / ag,
                            awayInfo.two_point_field_goals / ag,
                            awayInfo.two_point_field_goal_attempts / ag,
                            awayInfo.free_throws / ag,
                            awayInfo.free_throw_attempts / ag,
                            awayInfo.offensive_rebounds / ag,
                            awayInfo.defensive_rebounds / ag,
                            awayInfo.assists / ag,
                            awayInfo.turnovers / ag,
                            awayInfo.steals / ag,
                            awayInfo.field_goal_percentage,
                            awayInfo.free_throw_percentage,

                            homeInfo.opp_points / hg,
                            homeInfo.opp_field_goals / hg,
                            homeInfo.opp_field_goal_attempts / hg,
                            homeInfo.opp_three_point_field_goal_attempts / hg,
                            homeInfo.opp_three_point_field_goals / hg,
                            homeInfo.opp_two_point_field_goal_attempts / hg,
                            homeInfo.opp_free_throws / hg,
                            homeInfo.opp_free_throw_attempts / hg,
                            homeInfo.opp_defensive_rebounds / hg,
                            homeInfo.opp_assists / hg,
                            homeInfo.opp_turnovers / hg,
                            homeInfo.opp_steals / hg,
                            homeInfo.opp_blocks / hg,
                            homeInfo.opp_personal_fouls / hg,
                            homeInfo.opp_field_goal_percentage,
                            homeInfo.opp_three_point_field_goal_percentage,
                            homeInfo.opp_free_throw_percentage,
                            )

            home = ballgame(homeName,
                            homeInfo.points / hg,
                            homeInfo.field_goals / hg,
                            homeInfo.field_goal_attempts / hg,
                            homeInfo.three_point_field_goals / hg,
                            homeInfo.three_point_field_goal_attempts / hg,
                            homeInfo.two_point_field_goals / hg,
                            homeInfo.two_point_field_goal_attempts / hg,
                            homeInfo.free_throws / hg,
                            homeInfo.free_throw_attempts / hg,
                            homeInfo.offensive_rebounds / hg,
                            homeInfo.defensive_rebounds / hg,
                            homeInfo.assists / hg,
                            homeInfo.turnovers / hg,
                            homeInfo.steals / hg,
                            homeInfo.field_goal_percentage,
                            homeInfo.free_throw_percentage,

                            awayInfo.opp_points / ag,
                            awayInfo.opp_field_goals / ag,
                            awayInfo.opp_field_goal_attempts / ag,
                            awayInfo.opp_three_point_field_goal_attempts / ag,
                            awayInfo.opp_three_point_field_goals / ag,
                            awayInfo.opp_two_point_field_goal_attempts / ag,
                            awayInfo.opp_free_throws / ag,
                            awayInfo.opp_free_throw_attempts / ag,
                            awayInfo.opp_defensive_rebounds / ag,
                            awayInfo.opp_assists / ag,
                            awayInfo.opp_turnovers / ag,
                            awayInfo.opp_steals / ag,
                            awayInfo.opp_blocks / ag,
                            awayInfo.opp_personal_fouls / ag,
                            awayInfo.opp_field_goal_percentage,
                            awayInfo.opp_three_point_field_goal_percentage,
                            awayInfo.opp_free_throw_percentage,
                            )

            todaysGames.append([away, home])
        except:
            print(game['away_name'],game['home_name'])

    return todaysGames



def make_predictions():
    todaysGames = get_todays_games()
    games = []
    date = datetime.today().strftime('%Y%m%d')
    for game in todaysGames:
        away_score = game[0].predictScore()
        home_score = game[1].predictScore()
        games.append({'date':date,'away':game[0].name,'home':game[1].name,"away_pred":away_score,"home_pred":home_score})


    outcome = pd.DataFrame(data=games)
    outcome["key"] = outcome["date"] + outcome["home"]
    outcome = outcome[['key','date','away','home',"away_pred","home_pred"]]
    td.append_df_to_excel('Daily_Predictions',outcome)


make_predictions()

def get_yesterdays_scores():
    today = datetime.today() - timedelta(days=1)
    date = datetime.today().strftime('%Y%m%d')
    games_today = Boxscores(today).games[today.strftime('%-m-%-d-%Y')]
    output = []
    for g in games_today:
        if g['away_score'] == 'None':
            print('Not all scores available yet')
            break
        else:
            try:
                output.append({'date':date,'away':team_alt_names[g['away_name']],'home':team_alt_names[g['home_name']],
                               "away_score":g['away_score'],"home_score":g['home_score']})
            except:
                print('Cant find team name in matchup: {} v. {}'.format(g['away_name'],g['home_name']))

    outcome = pd.DataFrame(data=output)
    outcome["key"] = outcome["date"]+outcome["home"]
    outcome = outcome[['key','date', 'away', 'home', "away_score", "home_score"]]
    td.append_df_to_excel('Historic_Scores', outcome)

# get_yesterdays_scores()



