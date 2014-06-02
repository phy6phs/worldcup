'''
Created on May 27, 2014

@author: philip
'''
#import sys
#print sys.path
#sys.path.append('../src')
from team.team import Team #works for eclipse
import numpy as np

class Match(object):
    '''
    match between two teams
    '''
    '''constructor'''
    def __init__(self, init_team_a, init_team_b):
        self.team_a = init_team_a
        self.team_b = init_team_b
        self.goals_a = 0
        self.goals_b = 0
        self.play_match()
    
    def play_match(self):
        team_a = self.team_a
        team_b = self.team_b
        goals_a = (team_a.goals_scored_per_game+team_b.goals_conceded_per_game)/2
        goals_b = (team_a.goals_conceded_per_game+team_b.goals_scored_per_game)/2
        r1 = np.random.poisson(goals_a)
        r2 = np.random.poisson(goals_b)
        self.goals_a = r1
        self.goals_b = r2

        print team_a.name," ", r1, " - ", r2, " ", team_b.name


class GroupMatch(Match):
    def play_match(self):
        team_a = self.team_a
        team_b = self.team_b
        goals_a = (team_a.goals_scored_per_game+team_b.goals_conceded_per_game)/2
        goals_b = (team_a.goals_conceded_per_game+team_b.goals_scored_per_game)/2
        r1 = np.random.poisson(goals_a)
        r2 = np.random.poisson(goals_b)
        self.goals_a = r1
        self.goals_b = r2
        
        #assign points if it's a group match
        if(r1 > r2):
            team_a.group_pts += 3
        if(r1 == r2):
            team_a.group_pts += 1
            team_b.group_pts += 1
        if(r2 > r1):
            team_b.group_pts += 3
        #goals for group mathces
        team_a.group_goals_scored += r1
        team_b.group_goals_scored += r2
        team_a.group_goals_conceded += r2
        team_b.group_goals_conceded += r1
          
        print team_a.name," ", r1, " - ", r2, " ", team_b.name

class KOMatch(Match):
    
    
    def play_match(self):
        team_a = self.team_a
        team_b = self.team_b
        goals_a = (team_a.goals_scored_per_game+team_b.goals_conceded_per_game)/2
        goals_b = (team_a.goals_conceded_per_game+team_b.goals_scored_per_game)/2
        r1 = np.random.poisson(goals_a)
        r2 = np.random.poisson(goals_b)
        self.goals_a = r1
        self.goals_b = r2

        #initialise winner
        self.win = team_a
        #if scores are level will need to add extra time and penalties (better model). For now just assign random num
        if r1 > r2:
            self.win = team_a
        elif r2 > r1:
            self.win = team_b
        else:
            rand_u = np.random.uniform(0,1,1)
            if rand_u <= 0.5:
                self.win = team_a
            else:
                self.win = team_b 
           
        print team_a.name," ", r1, " - ", r2, " ", team_b.name

#Brazil = Team("Brazil")
##Brazil.print_games_and_goals()
#Argentina = Team("Argentina")
#Match1 = Match(Brazil, Argentina, True)
#
##test for random matches
#home_wins = 0
#away_wins = 0
#tot_goals = 0
#for x in range(0,10000):
#    Match1.play_match()
#    tot_goals += Match1.goals_a + Match1.goals_b
#    if Match1.goals_a > Match1.goals_b:
#        home_wins+=1
#    if Match1.goals_a < Match1.goals_b:
#        away_wins+=1
#
#print "home wins: ",     home_wins
#print "away wins: ",     away_wins
#print "ave goals: ",     float(tot_goals)/10000
#print "home pts: ",      Brazil.group_pts