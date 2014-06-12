from match.match import Match, GroupMatch, KOMatch
from team.team import Team 
from group.group import Group

'''set the number of tournaments you want to simulate'''
num_tournaments = 10000

'''initialise all the team info'''
Brazil = Team("Brazil", "SA")
'''If you want to print some info or save a graph uncomment'''
#Brazil.print_info()
#Brazil.print_results()
Brazil.make_goals_plot()
Croatia = Team("Croatia", "EU")
Mexico = Team("Mexico", "NA")
Cameroon = Team("Cameroon", "AF")

Spain = Team("Spain", "EU")
Netherlands = Team("Netherlands", "EU")
Chile = Team("Chile", "SA")
Australia = Team("Australia", "AS")        
       
Colombia = Team("Colombia", "SA")
Greece = Team("Greece", "EU")
Ivory_Coast = Team("Cote dIvoire", "AF")
Japan  = Team("Japan", "AS")
        
Uruguay = Team("Uruguay", "SA")
Costa_Rica = Team("Costa Rica", "NA")
England = Team("England", "EU")
Italy = Team("Italy", "EU")

Switzerland = Team("Switzerland", "EU")
Ecuador = Team("Ecuador", "SA")
France = Team("France", "EU")
Honduras = Team("Honduras", "NA")

Argentina = Team("Argentina", "SA")
Bosnia_Herzegovina = Team("Bosnia-Herzegovina")
Iran = Team("Iran", "AS")
Nigeria = Team("Nigeria", "AF")

Germany = Team("Germany", "EU")
Portugal = Team("Portugal", "EU")
Ghana = Team("Ghana", "AF")
United_States = Team("United States", "NA")

Belgium = Team("Belgium", "EU")
Algeria = Team("Algeria", "AF")
Russia = Team("Russia", "EU")
South_Korea = Team("Korea Republic", "AS")

'''Run the tournaments'''
for i in range(0, num_tournaments):
    '''group A'''  
    GroupA = Group(Brazil, Croatia, Mexico, Cameroon)        
    '''group B'''      
    GroupB = Group(Spain, Netherlands, Chile, Australia)
    '''Group C'''
    GroupC = Group(Colombia, Greece, Ivory_Coast, Japan)  
    '''Group D'''
    GroupD = Group(Uruguay, Costa_Rica, England, Italy)
    '''Group E'''
    GroupE = Group(Switzerland, Ecuador, France, Honduras)
    '''Group F'''
    GroupF = Group(Argentina, Bosnia_Herzegovina, Iran, Nigeria)
    '''Group G'''
    GroupG = Group(Germany, Portugal, Ghana, United_States)
    '''Group H'''
    GroupH = Group(Belgium, Algeria, Russia, South_Korea)
    
    '''Round of 16'''
    Match16_1 = KOMatch(GroupA.team_1, GroupB.team_2, "16")
    Match16_2 = KOMatch(GroupA.team_2, GroupB.team_1, "16")
    Match16_3 = KOMatch(GroupC.team_1, GroupD.team_2, "16")
    Match16_4 = KOMatch(GroupC.team_2, GroupD.team_1, "16")
    Match16_5 = KOMatch(GroupE.team_1, GroupF.team_2, "16")
    Match16_6 = KOMatch(GroupE.team_2, GroupF.team_1, "16")
    Match16_7 = KOMatch(GroupG.team_1, GroupH.team_2, "16")
    Match16_8 = KOMatch(GroupG.team_2, GroupH.team_1, "16")
    
    '''Quarter Final'''
    MatchQ_1 = KOMatch(Match16_1.win, Match16_3.win, "QF")
    MatchQ_2 = KOMatch(Match16_2.win, Match16_4.win, "QF")
    MatchQ_3 = KOMatch(Match16_5.win, Match16_7.win, "QF")
    MatchQ_4 = KOMatch(Match16_6.win, Match16_8.win, "QF")
    
    '''Semi Final'''
    MatchS_1 = KOMatch(MatchQ_1.win, MatchQ_3.win, "SF")
    MatchS_2 = KOMatch(MatchQ_2.win, MatchQ_4.win, "SF")
    
    '''Final'''
    MatchF = KOMatch(MatchS_1.win, MatchS_2.win, "Final")
    
    Winner = MatchF.win

wc_teams = [Brazil, Croatia, Mexico, Cameroon, Spain, Netherlands, Chile, Australia, Colombia, Greece, 
                 Ivory_Coast, Japan, Uruguay, Costa_Rica, England, Italy, Switzerland, Ecuador, France, 
                 Honduras, Argentina, Bosnia_Herzegovina, Iran, Nigeria, Germany, Portugal, Ghana, United_States,
                 Belgium, Algeria, Russia, South_Korea
                 ]

#will have to put teams in to a list and then loop ove the list!
for wc_team in wc_teams:
    print wc_team.name,"\t %.4f \t %.4f \t %.4f \t %.4f \t %.4f \t %.4f" % (float(wc_team.n_ko_group)/num_tournaments, 
                                                                            float(wc_team.n_ko_16)/num_tournaments, float(wc_team.n_ko_qf)/num_tournaments,
                                                                            float(wc_team.n_ko_sf)/num_tournaments, float(wc_team.n_ru_final)/num_tournaments,
                                                                            float(wc_team.n_win_final)/num_tournaments)

'''uncomment this for win rate in order''' 
#win_rate = []
#
#for wc_team in wc_teams:
#    rate = [wc_team.name, float(wc_team.n_win_final)/num_tournaments]    
#    win_rate.append(rate)
#    
#sort = sorted(win_rate, key=itemgetter(1), reverse=True)
#print "********************************************************************"
#print "in winning order:"
#for i in range(0,32):
#    print sort[i][0], ": ", sort[i][1]