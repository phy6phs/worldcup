'''
Created on Jun 1, 2014

@author: philip
'''

from match.match import Match, GroupMatch, KOMatch
from team.team import Team 

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
        print TeamA.name, ": ", TeamA.group_pts
        print TeamB.name, ": ", TeamB.group_pts
        print TeamC.name, ": ", TeamC.group_pts
        print TeamD.name, ": ", TeamD.group_pts
    
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

print '''Tournament'''
print '''group A'''        
Brazil = Team("Brazil")
Croatia = Team("Croatia")
Mexico = Team("Mexico")
Cameroon = Team("Cameroon")
        
GroupA = Group(Brazil, Croatia, Mexico, Cameroon)        
GroupA.sort_group()

print '''group B'''      
Spain = Team("Spain")
Netherlands = Team("Netherlands")
Chile = Team("Chile")
Australia = Team("Australia")        

GroupB = Group(Spain, Netherlands, Chile, Australia)
        
print '''Group C'''
Colombia = Team("Colombia")
Greece = Team("Greece")
Ivory_Coast = Team("Cote dIvoire")
Japan  = Team("Japan")

GroupC = Group(Colombia, Greece, Ivory_Coast, Japan)      
        
print '''Group D'''
Uruguay = Team("Uruguay")
Costa_Rica = Team("Costa Rica")
England = Team("England")
Italy = Team("Italy")

GroupD = Group(Uruguay, Costa_Rica, England, Italy)

print '''Group E'''
Switzerland = Team("Switzerland")
Ecuador = Team("Ecuador")
France = Team("France")
Honduras = Team("Honduras")

GroupE = Group(Switzerland, Ecuador, France, Honduras)

print '''Group F'''
Argentina = Team("Argentina")
Bosnia_Herzegovina = Team("Bosnia-Herzegovina")
Iran = Team("Iran")
Nigeria = Team("Nigeria")

GroupF = Group(Argentina, Bosnia_Herzegovina, Iran, Nigeria)

print '''Group G'''
Germany = Team("Germany")
Portugal = Team("Portugal")
Ghana = Team("Ghana")
United_States = Team("United States")

GroupG = Group(Germany, Portugal, Ghana, United_States)

print '''Group H'''
Belgium = Team("Belgium")
Algeria = Team("Algeria")
Russia = Team("Russia")
South_Korea = Team("Korea Republic")

GroupH = Group(Belgium, Algeria, Russia, South_Korea)

print '''Round of 16'''
Match16_1 = KOMatch(GroupA.team_1, GroupB.team_2)
Match16_2 = KOMatch(GroupA.team_2, GroupB.team_1)
Match16_3 = KOMatch(GroupC.team_1, GroupD.team_2)
Match16_4 = KOMatch(GroupC.team_2, GroupD.team_1)
Match16_5 = KOMatch(GroupE.team_1, GroupF.team_2)
Match16_6 = KOMatch(GroupE.team_2, GroupF.team_1)
Match16_7 = KOMatch(GroupG.team_1, GroupH.team_2)
Match16_8 = KOMatch(GroupG.team_2, GroupH.team_1)

print '''Quarter Final'''
MatchQ_1 = KOMatch(Match16_1.win, Match16_3.win)
MatchQ_2 = KOMatch(Match16_2.win, Match16_4.win)
MatchQ_3 = KOMatch(Match16_5.win, Match16_7.win)
MatchQ_4 = KOMatch(Match16_6.win, Match16_8.win)

print '''Semi Final'''
MatchS_1 = KOMatch(MatchQ_1.win, MatchQ_3.win)
MatchS_2 = KOMatch(MatchQ_2.win, MatchQ_4.win)

print '''Final'''
MatchF = KOMatch(MatchS_1.win, MatchS_2.win)

Winner = MatchF.win
print "Winner is: ", Winner.name, "!"




        