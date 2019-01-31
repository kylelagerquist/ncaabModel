from datetime import datetime
from sportsreference.ncaab.teams import Teams
from sportsreference.ncaab.boxscore import Boxscores

Intercept = -1.33125707
ppg = 0.21645325
opp_blk_pg = -0.10867703
fg_att_pg = 0.38867914
ft_pg = 0.17204567
fls_pg = 0.19766658
thr_pg = 0.67232796
ft_per = 5.40742363
fg_per = 44.00687748
thr_per = -13.59364137
opp_ppg = 0.04600383
opp_fg_att_pg = 0.02761445
opp_ft_pg = -0.11051277
opp_fls_pg = 0.27910239
opp_stls_pg = -0.15078265
opp_fg_per = 0.72859726
opp_thr_per = -5.30024252
opp_two_per = -2.78271362

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
                  'Brigham Young': 'Brigham Young', 'Brown': 'Brown', 'Bryant': 'Bryant', 'Bucknell': 'Bucknell',
                  'Buffalo': 'Buffalo', 'Butler': 'Butler', 'Cal Poly': 'Cal Poly',
                  'Cal State Bakersfield': 'Cal State Bakersfield',
                  'Cal State Fullerton': 'Cal State Fullerton', 'Cal State Northridge': 'Cal State Northridge',
                  'California Baptist': 'California Baptist', 'UC-Davis': 'UC-Davis', 'UC-Irvine': 'UC-Irvine',
                  'UC-Riverside': 'UC-Riverside', 'UC-Santa Barbara': 'UC-Santa Barbara',
                  'University of California': 'University of California', 'Campbell': 'Campbell',
                  'Canisius': 'Canisius',
                  'Central Arkansas': 'Central Arkansas', 'Central Connecticut State': 'Central Connecticut State',
                  'Central Florida': 'Central Florida', 'Central Michigan': 'Central Michigan',
                  'Charleston Southern': 'Charleston Southern', 'Charlotte': 'Charlotte', 'Chattanooga': 'Chattanooga',
                  'Chicago State': 'Chicago State', 'Cincinnati': 'Cincinnati', 'Citadel': 'Citadel',
                  'Clemson': 'Clemson',
                  'Cleveland State': 'Cleveland State', 'Coastal Carolina': 'Coastal Carolina', 'Colgate': 'Colgate',
                  'College of Charleston': 'College of Charleston', 'Colorado State': 'Colorado State',
                  'Colorado': 'Colorado',
                  'Columbia': 'Columbia', 'Connecticut': 'Connecticut', 'Coppin State': 'Coppin State',
                  'Cornell': 'Cornell',
                  'Creighton': 'Creighton', 'Dartmouth': 'Dartmouth', 'Davidson': 'Davidson', 'Dayton': 'Dayton',
                  'Delaware State': 'Delaware State', 'Delaware': 'Delaware', 'Denver': 'Denver', 'DePaul': 'DePaul',
                  'Detroit Mercy': 'Detroit Mercy', 'Drake': 'Drake', 'Drexel': 'Drexel', 'Duke': 'Duke',
                  'Duquesne': 'Duquesne',
                  'East Carolina': 'East Carolina', 'East Tennessee State': 'East Tennessee State',
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
                  'Illinois-Chicago': 'Illinois-Chicago', 'Illinois State': 'Illinois State', 'Illinois': 'Illinois',
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
                  'Long Beach State': 'Long Beach State', 'Long Island University': 'Long Island University',
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
                  'Ole Miss': 'Mississippi', 'Missouri-Kansas City': 'Missouri-Kansas City',
                  'Missouri State': 'Missouri State',
                  'Missouri': 'Missouri', 'Monmouth': 'Monmouth', 'Montana State': 'Montana State',
                  'Montana': 'Montana',
                  'Morehead State': 'Morehead State', 'Morgan State': 'Morgan State',
                  "Mount St. Mary's": "Mount St. Mary's",
                  'Murray State': 'Murray State', 'Navy': 'Navy', 'Omaha': 'Omaha', 'Nebraska': 'Nebraska',
                  'Nevada-Las Vegas': 'Nevada-Las Vegas', 'Nevada': 'Nevada', 'New Hampshire': 'New Hampshire',
                  'New Mexico State': 'New Mexico State', 'New Mexico': 'New Mexico', 'New Orleans': 'New Orleans',
                  'Niagara': 'Niagara', 'Nicholls State': 'Nicholls State', 'NJIT': 'NJIT',
                  'Norfolk State': 'Norfolk State',
                  'North Alabama': 'North Alabama', 'UNC Asheville': 'North Carolina-Asheville',
                  'North Carolina A&T': 'North Carolina A&T', 'North Carolina Central': 'North Carolina Central',
                  'North Carolina-Greensboro': 'North Carolina-Greensboro',
                  'North Carolina State': 'North Carolina State',
                  'North Carolina-Wilmington': 'North Carolina-Wilmington', 'North Carolina': 'North Carolina',
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
                  'Pennsylvania': 'Pennsylvania', 'Pepperdine': 'Pepperdine', 'Pittsburgh': 'Pittsburgh',
                  'Portland State': 'Portland State', 'Portland': 'Portland', 'Prairie View': 'Prairie View',
                  'Presbyterian': 'Presbyterian', 'Princeton': 'Princeton', 'Providence': 'Providence',
                  'Purdue': 'Purdue',
                  'Quinnipiac': 'Quinnipiac', 'Radford': 'Radford', 'Rhode Island': 'Rhode Island', 'Rice': 'Rice',
                  'Richmond': 'Richmond', 'Rider': 'Rider', 'Robert Morris': 'Robert Morris', 'Rutgers': 'Rutgers',
                  'Sacramento State': 'Sacramento State', 'Sacred Heart': 'Sacred Heart',
                  'Saint Francis (PA)': 'Saint Francis (PA)',
                  "Saint Joseph's": "Saint Joseph's", 'Saint Louis': 'Saint Louis',
                  "Saint Mary's (CA)": "Saint Mary's (CA)",
                  "Saint Peter's": "Saint Peter's", 'Sam Houston State': 'Sam Houston State', 'Samford': 'Samford',
                  'San Diego State': 'San Diego State', 'San Diego': 'San Diego', 'San Francisco': 'San Francisco',
                  'San Jose State': 'San Jose State', 'Santa Clara': 'Santa Clara', 'Savannah State': 'Savannah State',
                  'Seattle': 'Seattle', 'Seton Hall': 'Seton Hall', 'Siena': 'Siena', 'South Alabama': 'South Alabama',
                  'South Carolina State': 'South Carolina State', 'USC Upstate': 'South Carolina Upstate',
                  'South Carolina': 'South Carolina', 'South Dakota State': 'South Dakota State',
                  'South Dakota': 'South Dakota',
                  'South Florida': 'South Florida', 'Southeast Missouri State': 'Southeast Missouri State',
                  'Southeastern Louisiana': 'Southeastern Louisiana', 'USC': 'Southern California',
                  'SIU Edwardsville': 'SIU Edwardsville', 'Southern Illinois': 'Southern Illinois',
                  'SMU': 'Southern Methodist', 'Southern Mississippi': 'Southern Mississippi',
                  'Southern Utah': 'Southern Utah', 'Southern': 'Southern', 'St. Bonaventure': 'St. Bonaventure',
                  'St. Francis (NY)': 'St. Francis (NY)', "St. John's (NY)": "St. John's (NY)", 'Stanford': 'Stanford',
                  'Stephen F. Austin': 'Stephen F. Austin', 'Stetson': 'Stetson', 'Stony Brook': 'Stony Brook',
                  'Syracuse': 'Syracuse', 'Temple': 'Temple', 'Tennessee-Martin': 'Tennessee-Martin',
                  'Tennessee State': 'Tennessee State', 'Tennessee Tech': 'Tennessee Tech', 'Tennessee': 'Tennessee',
                  'Texas A&M-Corpus Christi': 'Texas A&M-Corpus Christi', 'Texas A&M': 'Texas A&M',
                  'Texas-Arlington': 'Texas-Arlington', 'Texas Christian': 'Texas Christian',
                  'Texas-El Paso': 'Texas-El Paso',
                  'Texas-Rio Grande Valley': 'Texas-Rio Grande Valley', 'Texas-San Antonio': 'Texas-San Antonio',
                  'Texas Southern': 'Texas Southern', 'Texas State': 'Texas State', 'Texas Tech': 'Texas Tech',
                  'Texas': 'Texas',
                  'Toledo': 'Toledo', 'Towson': 'Towson', 'Troy': 'Troy', 'Tulane': 'Tulane', 'Tulsa': 'Tulsa',
                  'UCLA': 'UCLA',
                  'Utah State': 'Utah State', 'Utah Valley': 'Utah Valley', 'Utah': 'Utah', 'Valparaiso': 'Valparaiso',
                  'Vanderbilt': 'Vanderbilt', 'Vermont': 'Vermont', 'Villanova': 'Villanova',
                  'Virginia Commonwealth': 'Virginia Commonwealth', 'VMI': 'VMI', 'Virginia Tech': 'Virginia Tech',
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
    def __init__(self, name, ppg, blocks, fg_att, ft, fouls, threes, ft_per, fg_per, three_per, steals, two_per,
                 h_ppg, h_blocks, h_fg_att, h_ft, h_fouls, h_threes, h_ft_per, h_three_per, h_steals, h_two_per):
        self.name = name
        self.ppg = ppg
        self.blocks = blocks
        self.fg_att = fg_att
        self.ft = ft
        self.fouls = fouls
        self.threes = threes
        self.ft_per = ft_per
        self.fg_per = fg_per
        self.three_per = three_per
        self.steals = steals
        self.two_per = two_per
        self.h_ppg = h_ppg
        self.h_blocks = h_blocks
        self.h_fg_att = h_fg_att
        self.h_ft = h_ft
        self.h_fouls = h_fouls
        self.h_threes = h_threes
        self.h_ft_per = h_ft_per
        self.h_three_per = h_three_per
        self.h_steals = h_steals
        self.h_two_per = h_two_per

    def info(self):
        print(self.away + ' at ' + self.home)

    def predictScore(self):
        return Intercept + ppg * self.ppg + opp_blk_pg * self.h_blocks + fg_att_pg * self.fg_att + ft_pg * self.ft + \
               fls_pg * self.fouls + thr_pg * self.threes + ft_per * self.ft_per + fg_per * self.fg_per + thr_per * self.three_per + \
               opp_ppg * self.h_ppg + opp_fg_att_pg * self.h_fg_att + opp_ft_pg * self.h_ft + opp_fls_pg * self.h_fouls + \
               opp_stls_pg * self.h_fouls + opp_fg_per * self.h_fg_att + opp_thr_per * self.h_three_per + opp_two_per * self.h_two_per


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

    games_today = [games_today[0]]

    for game in games_today:
        awayName = team_alt_names[game['away_name']]
        homeName = team_alt_names[game['home_name']]
        awayInfo = teamData[awayName]
        homeInfo = teamData[homeName]
        ag = awayInfo.games_played
        hg = homeInfo.games_played

        away = ballgame(awayName, awayInfo.points / ag, awayInfo.blocks / ag, awayInfo.field_goal_attempts / ag,
                        awayInfo.free_throws / ag,
                        awayInfo.personal_fouls / ag, awayInfo.three_point_field_goals / ag,
                        awayInfo.free_throw_percentage, awayInfo.field_goal_percentage,
                        awayInfo.three_point_field_goal_percentage,
                        awayInfo.steals / ag, awayInfo.two_point_field_goal_percentage,
                        homeInfo.points / hg, homeInfo.blocks / hg, homeInfo.field_goal_attempts / hg,
                        homeInfo.free_throws / hg,
                        homeInfo.personal_fouls / hg, homeInfo.three_point_field_goals / hg,
                        homeInfo.free_throw_percentage, homeInfo.three_point_field_goal_percentage,
                        homeInfo.steals / hg, homeInfo.two_point_field_goal_percentage,
                        )

        home = ballgame(homeName, homeInfo.points / ag, homeInfo.blocks / ag, homeInfo.field_goal_attempts / ag,
                        homeInfo.free_throws / ag,
                        homeInfo.personal_fouls / ag, homeInfo.three_point_field_goals / ag,
                        homeInfo.free_throw_percentage, homeInfo.field_goal_percentage,
                        homeInfo.three_point_field_goal_percentage,
                        homeInfo.steals / ag, homeInfo.two_point_field_goal_percentage,
                        awayInfo.points / hg, awayInfo.blocks / hg, awayInfo.field_goal_attempts / hg,
                        awayInfo.free_throws / hg,
                        awayInfo.personal_fouls / hg, awayInfo.three_point_field_goals / hg,
                        awayInfo.free_throw_percentage, awayInfo.three_point_field_goal_percentage,
                        awayInfo.steals / hg, awayInfo.two_point_field_goal_percentage,
                        )
        todaysGames.append([away, home])

    return todaysGames


def make_predictions():
    todaysGames = get_todays_games()

    for game in todaysGames:
        away_score = game[0].predictScore()
        home_score = game[1].predictScore()
        print(game[0].name + ': ' + str(away_score))
        print(game[1].name + ': ' + str(home_score))
        print('Total: ' + str(away_score + home_score))
        print('')


make_predictions()
