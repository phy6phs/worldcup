'''
Created on May 27, 2014

@author: philip
'''

import csv

class Team(object):
    def __init__(self, initial_name = "Brazil"):
        self.name = initial_name
        self.games = 0
        self.goals_scored = 0
        self.goals_conceded = 0
        self.goals_scored_per_game = 0.
        self.goals_conceded_per_game = 0.
        self.get_goals()
        #group parameters
        self.group_pts = 0
        self.group_goals_scored = 0
        self.group_goals_conceded = 0
        #for what stage of competition exit
        self.n_ko_group = 0
        self.n_ko_16 = 0
        self.n_ko_quarter = 0
        self.n_ko_semi = 0
        self.n_ru_final = 0
        self.n_win_final = 0   
        
    def print_results(self):
        input_file = csv.DictReader(open("/home/philip/workspace/wordcup/results.csv"))
        for row in input_file:
            date = row["date"]
            home_team = row["home_team"]
            away_team = row["away_team"]
            home_goals = int(row["home_goals"])
            away_goals = int(row["away_goals"])

            if home_team == self.name or away_team == self.name:
                print date+", "+home_team+" ",home_goals,"-",away_goals," "+away_team

    def get_goals(self): #scored and conceded
        input_file = csv.DictReader(open("/home/philip/workspace/wordcup/results.csv"))
        goals_scored = 0;
        goals_conceded = 0;
        games = 0
        for row in input_file:
            home_team = row["home_team"]
            away_team = row["away_team"]
            home_goals = int(row["home_goals"])
            away_goals = int(row["away_goals"])
            
            if home_team == self.name:
                goals_scored += home_goals
                goals_conceded += away_goals
                games += 1
            if away_team == self.name:
                goals_scored += away_goals
                goals_conceded += home_goals
                games += 1
                
        self.goals_scored = goals_scored
        self.goals_conceded = goals_conceded
        self.games = games
        self.goals_scored_per_game = float(self.goals_scored)/self.games
        self.goals_conceded_per_game = float(self.goals_conceded)/self.games
        
    def print_games_and_goals(self):
        print "games: ", self.games
        print "goals scored per game: ", float(self.goals_scored)/self.games
        print "goals conceded per game: ", float(self.goals_conceded)/self.games
        
##test to see if can knock out
#Brazil = Team("Brazil")
#
#A1 = Brazil
#A1.n_ko_group += 1
#
#print "brazil ko: ", Brazil.n_ko_group


##Brazil.print_results()        
#Brazil.print_games_and_goals()
#
#Argentina = Team("Argentina")
##Argentina.print_results()        
#Argentina.print_games_and_goals()
