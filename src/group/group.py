'''
Created on Jun 1, 2014

@author: philip
'''

from match.match import Match, GroupMatch, KOMatch
from team.team import Team 
from operator import itemgetter, attrgetter

class Group(object):
    '''
    Group matches: simulate 
    '''
    def __init__(self, init_team_a, init_team_b, init_team_c, init_team_d):
        '''
        Constructor
        '''
        self.team_a = init_team_a
        self.team_b = init_team_b
        self.team_c = init_team_c
        self.team_d = init_team_d
        self.play_matches()
        self.team_1 = init_team_a
        self.team_2 = init_team_a
        self.sort_group()
        
    def play_matches(self):
        TeamA = self.team_a
        TeamB = self.team_b
        TeamC = self.team_c
        TeamD = self.team_d
        
        GroupMatch1 = GroupMatch(TeamA, TeamB)
        GroupMatch2 = GroupMatch(TeamC, TeamD)
        '''few days'''
        GroupMatch3 = GroupMatch(TeamA, TeamC)
        GroupMatch4 = GroupMatch(TeamD, TeamB)
        '''few days'''
        GroupMatch5 = GroupMatch(TeamD, TeamA)
        GroupMatch6 = GroupMatch(TeamB, TeamC)
#        print TeamA.name, ": ", TeamA.group_pts
#        print TeamB.name, ": ", TeamB.group_pts
#        print TeamC.name, ": ", TeamC.group_pts
#        print TeamD.name, ": ", TeamD.group_pts
    
    def sort_group(self):
        TeamA = self.team_a
        TeamB = self.team_b
        TeamC = self.team_c
        TeamD = self.team_d
        
        teams = [
        (TeamA, TeamA.name, TeamA.group_pts, TeamA.group_goals_scored-TeamA.group_goals_conceded, TeamA.group_goals_scored),
        (TeamB, TeamB.name, TeamB.group_pts, TeamB.group_goals_scored-TeamB.group_goals_conceded, TeamB.group_goals_scored),
        (TeamC, TeamC.name, TeamC.group_pts, TeamC.group_goals_scored-TeamC.group_goals_conceded, TeamC.group_goals_scored),
        (TeamD, TeamD.name, TeamD.group_pts, TeamD.group_goals_scored-TeamD.group_goals_conceded, TeamD.group_goals_scored)
        ]      
        
        s1 = sorted(teams, key=lambda teams: teams[4], reverse=True)
        s2 = sorted(s1, key=lambda teams: teams[3], reverse=True)
        s3 = sorted(s2, key=lambda teams: teams[2], reverse=True)
        
        #print s3
        self.team_1 = s3[0][0]
        self.team_2 = s3[1][0]
        Team3 = s3[2][0]
        Team4 = s3[3][0]
        Team3.n_ko_group += 1
        Team4.n_ko_group += 1
        
        #for now do for all teams
        self.reset_group_info(TeamA)
        self.reset_group_info(TeamB)
        self.reset_group_info(TeamC)
        self.reset_group_info(TeamD)
        
    def reset_group_info(self, team_input):
            team_input.group_pts = 0
            team_input.group_goals_scored = 0
            team_input.group_goals_conceded = 0
            
