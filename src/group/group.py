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
            
#wc_team_names = ["Brazil", "Croatia", "Mexico", "Cameroon", "Spain", "Netherlands", "Chile", "Australia", "Colombia", "Greece", 
#                 "Cote dIvoire", "Japan", "Uruguay", "Costa Rica", "England", "Italy", "Switzerland", "Ecuador", "France", 
#                 "Honduras", "Argentina", "Bosnia-Herzegovina", "Iran", "Nigeria", "Germany", "Portugal", "Ghana", "United States",
#                 "Belgium", "Algeria", "Russia", "Korea Republic"
#                 ]
#win_rate = []
#
#for wc_team in wc_team_names:
#    Temp = Team(wc_team)
#    rate = [wc_team, Temp.win_percentage]    
#    win_rate.append(rate)
#    
#sort = sorted(win_rate, key=itemgetter(1), reverse=True)
#
#for i in range(0,32):
#    print sort[i][0], ": ", sort[i][1]
  
Brazil = Team("Brazil", "SA")
#Brazil.print_info()
#Brazil.print_results()
#Brazil.make_goals_plot()
#
Croatia = Team("Croatia", "EU")
#Mexico = Team("Mexico", "NA")
#Cameroon = Team("Cameroon", "AF")
Croatia.make_goals_plot()


#
#Spain = Team("Spain", "EU")
#Netherlands = Team("Netherlands", "EU")
#Chile = Team("Chile", "SA")
#Australia = Team("Australia", "AS")        
#       
#Colombia = Team("Colombia", "SA")
#Greece = Team("Greece", "EU")
#Ivory_Coast = Team("Cote dIvoire", "AF")
#Japan  = Team("Japan", "AS")
#        
#Uruguay = Team("Uruguay", "SA")
#Costa_Rica = Team("Costa Rica", "NA")
#England = Team("England", "EU")
#Italy = Team("Italy", "EU")
#
#Switzerland = Team("Switzerland", "EU")
#Ecuador = Team("Ecuador", "SA")
#France = Team("France", "EU")
#Honduras = Team("Honduras", "NA")
#
#Argentina = Team("Argentina", "SA")
#Bosnia_Herzegovina = Team("Bosnia-Herzegovina")
#Iran = Team("Iran", "AS")
#Nigeria = Team("Nigeria", "AF")
#
#Germany = Team("Germany", "EU")
#Portugal = Team("Portugal", "EU")
#Ghana = Team("Ghana", "AF")
#United_States = Team("United States", "NA")
#
#Belgium = Team("Belgium", "EU")
#Algeria = Team("Algeria", "AF")
#Russia = Team("Russia", "EU")
#South_Korea = Team("Korea Republic", "AS")
#
#for i in range(0, 10000):
#    print '''Tournament ''', i
#    print '''group A'''  
#    GroupA = Group(Brazil, Croatia, Mexico, Cameroon)        
#    print '''group B'''      
#    GroupB = Group(Spain, Netherlands, Chile, Australia)
#    print '''Group C'''
#    GroupC = Group(Colombia, Greece, Ivory_Coast, Japan)  
#    print '''Group D'''
#    GroupD = Group(Uruguay, Costa_Rica, England, Italy)
#    print '''Group E'''
#    GroupE = Group(Switzerland, Ecuador, France, Honduras)
#    print '''Group F'''
#    GroupF = Group(Argentina, Bosnia_Herzegovina, Iran, Nigeria)
#    print '''Group G'''
#    GroupG = Group(Germany, Portugal, Ghana, United_States)
#    print '''Group H'''
#    GroupH = Group(Belgium, Algeria, Russia, South_Korea)
#    
#    print '''Round of 16'''
#    Match16_1 = KOMatch(GroupA.team_1, GroupB.team_2, "16")
#    Match16_2 = KOMatch(GroupA.team_2, GroupB.team_1, "16")
#    Match16_3 = KOMatch(GroupC.team_1, GroupD.team_2, "16")
#    Match16_4 = KOMatch(GroupC.team_2, GroupD.team_1, "16")
#    Match16_5 = KOMatch(GroupE.team_1, GroupF.team_2, "16")
#    Match16_6 = KOMatch(GroupE.team_2, GroupF.team_1, "16")
#    Match16_7 = KOMatch(GroupG.team_1, GroupH.team_2, "16")
#    Match16_8 = KOMatch(GroupG.team_2, GroupH.team_1, "16")
#    
#    print '''Quarter Final'''
#    MatchQ_1 = KOMatch(Match16_1.win, Match16_3.win, "QF")
#    MatchQ_2 = KOMatch(Match16_2.win, Match16_4.win, "QF")
#    MatchQ_3 = KOMatch(Match16_5.win, Match16_7.win, "QF")
#    MatchQ_4 = KOMatch(Match16_6.win, Match16_8.win, "QF")
#    
#    print '''Semi Final'''
#    MatchS_1 = KOMatch(MatchQ_1.win, MatchQ_3.win, "SF")
#    MatchS_2 = KOMatch(MatchQ_2.win, MatchQ_4.win, "SF")
#    
#    print '''Final'''
#    MatchF = KOMatch(MatchS_1.win, MatchS_2.win, "Final")
#    
#    Winner = MatchF.win
#    print "Winner is: ", Winner.name, "!"
#
#wc_teams = [Brazil, Croatia, Mexico, Cameroon, Spain, Netherlands, Chile, Australia, Colombia, Greece, 
#                 Ivory_Coast, Japan, Uruguay, Costa_Rica, England, Italy, Switzerland, Ecuador, France, 
#                 Honduras, Argentina, Bosnia_Herzegovina, Iran, Nigeria, Germany, Portugal, Ghana, United_States,
#                 Belgium, Algeria, Russia, South_Korea
#                 ]
#
##will have to put teams in to a list and then loop ove the list!
#for wc_team in wc_teams:
#    print wc_team.name,"\t %.4f \t %.4f \t %.4f \t %.4f \t %.4f \t %.4f" % (float(wc_team.n_ko_group)/10000, 
#                                                                            float(wc_team.n_ko_16)/10000, float(wc_team.n_ko_qf)/10000,
#                                                                            float(wc_team.n_ko_sf)/10000, float(wc_team.n_ru_final)/10000,
#                                                                            float(wc_team.n_win_final)/10000)
# 
#win_rate = []
#
#for wc_team in wc_teams:
#    rate = [wc_team.name, float(wc_team.n_win_final)/10000]    
#    win_rate.append(rate)
#    
#sort = sorted(win_rate, key=itemgetter(1), reverse=True)
#print "********************************************************************"
#print "in winning order:"
#for i in range(0,32):
#    print sort[i][0], ": ", sort[i][1]
#        
