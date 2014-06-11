'''
Created on May 27, 2014

@author: philip
'''

import csv
import datetime
##import matplotlib.mlab as mlab
from scipy import optimize
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import math 
from scipy.misc import factorial
import pylab 

class Team(object):
    def __init__(self, initial_name = "Brazil", initial_continent = "SA"):
        self.name = initial_name
        self.continent = initial_continent
        #team info to get from csv file
        self.games = 0
        self.home_games = 0
        self.away_games = 0
        self.neutral_games = 0
        self.wins = 0
        self.win_percentage = 0
        self.home_wins = 0
        self.home_win_percentage = 0
        self.away_wins = 0
        self.away_win_percentage = 0
        self.neutral_wins = 0
        self.neutral_win_percentage = 0
        self.loses = 0
        self.home_loses = 0
        self.away_loses = 0
        self.neutral_loses = 0
        self.draws = 0
        self.home_draws = 0
        self.away_draws = 0
        self.neutral_draws = 0
        #for plotting
        self.goals_list = []
        #goal info
        self.goals_scored = 0
        self.home_goals_scored = 0
        self.away_goals_scored = 0
        self.neutral_goals_scored = 0
        self.goals_conceded = 0
        self.home_goals_conceded = 0
        self.away_goals_conceded = 0
        self.neutral_goals_conceded = 0
        self.goals_scored_per_game = 0.
        self.goals_conceded_per_game = 0.
        #clean sheets
        self.clean_sheets = 0
        self.home_clean_sheets = 0
        self.away_clean_sheets = 0
        self.neutral_clean_sheets = 0       
        #get info
        self.get_info()
        #group parameters
        self.group_pts = 0
        self.group_goals_scored = 0
        self.group_goals_conceded = 0
        #for what stage of competition exit
        self.n_ko_group = 0.
        self.n_ko_16 = 0.
        self.n_ko_qf = 0.
        self.n_ko_sf = 0.
        self.n_ru_final = 0.
        self.n_win_final = 0.  

    def get_rank(self):   
        ranks = []
        
        with open('../rankings.csv','r') as f:
            next(f)
            reader=csv.reader(f,delimiter='\t')
            for rank in reader:
                ranks.append(rank)
                
        return ranks                          

    def get_info(self): #scored and conceded
        input_file = csv.DictReader(open("../results.csv"))
        
        rankings = self.get_rank()
                            
        for row in input_file:
            date = row["date"]
            home_team = row["home_team"]
            away_team = row["away_team"]
            home_goals = int(row["home_goals"])
            away_goals = int(row["away_goals"])
            neutral = int(row["neutral"])
            
            #only include top 100 teams
            if any(home_team in s for s in rankings) and any(away_team in s for s in rankings) and home_team != "Oman" and away_team != "Oman":
                pass
            else:
                continue        
            
            #histogram example
            if (home_team == self.name):
                self.goals_list.append(home_goals)
            elif (away_team == self.name):
                self.goals_list.append(away_goals)  
            
            #assign the date from a string 
            dt = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            
            #home matches get info
            if (home_team == self.name and neutral == 0):
                self.set_home_info(home_goals, away_goals)          
            #away matches get info    
            elif (away_team == self.name and neutral == 0):
                self.set_away_info(away_goals, home_goals)
            #neutral match home team 1st
            elif (home_team == self.name and neutral == 1):
                self.set_neutral_info(home_goals, away_goals)
            #neutral match away team 1st
            elif (away_team == self.name and neutral == 1):       
                self.set_neutral_info(away_goals, home_goals)
        
        if self.games > 0:  
            self.win_percentage =   100*float(self.wins)/self.games
            self.goals_scored_per_game = float(self.goals_scored)/self.games
            self.goals_conceded_per_game = float(self.goals_conceded)/self.games 
        if self.home_games > 0:  
            self.home_win_percentage = 100*float(self.home_wins)/self.home_games
        if self.away_games > 0:
            self.away_win_percentage = 100*float(self.away_wins)/self.away_games
        if self.neutral_games > 0:
            self.neutral_win_percentage = 100*float(self.neutral_wins)/self.neutral_games   
    
    def make_goals_plot(self):
        # the histogram of the data
        goals = self.goals_list
        mean_g = np.mean(goals)
        std_g = np.std(goals)
        data = Counter(goals)
#        print data.most_common()
        
        gls = zip(*data.most_common())
        n_gls = gls[0]  # Returns all unique items and their counts
        mult_gls = gls[1]
        gls_sorted = list(n_gls)
        gls_sorted = sorted(gls_sorted)
        mult_gls_errs = np.sqrt(mult_gls)
        
        fitfunc = lambda p, x: (self.games*(p[0]**x)*math.exp(-p[0]))/factorial(x) # Target function
        errfunc = lambda p, x, y: fitfunc(p, x) - y # Distance to the target function
        p0 = [1.] # Initial guess for the parameters
        p1, success = optimize.leastsq(errfunc, p0[:], args=(n_gls, mult_gls))
        
        fig = pylab.figure()
#        fig, ax = plt.subplots()
#        ax.plot(mult_gls, 'k.', label='data')
#        ax.plot(fitfunc(p1, gls_sorted), 'r-', label='$\mathrm{Poissonian\ fit}, \mu= %3.3f$' % (p1[0]))
        
        plt.plot(fitfunc(p1, gls_sorted), "r-", label = '$\mathrm{Poissonian\ fit}, \mu= %3.3f$' % (p1[0]))
        
        max_y = data.most_common(1)  # Returns the highest occurring item
        max_x = max(goals)+1
#       plt.hist(goals, 20, facecolor='green'), #normed=np.sum(mult_gls)
        
        #if you want error bars
        plt.errorbar(n_gls, mult_gls, yerr=mult_gls_errs, fmt='k.', label = 'data')
        #plt.text(4, 25, '$\mathrm{Poissonian\ fit}, \mu= %3.3f$' % (p1[0]))
#        plt.legend([n_gls, fitfunc(p1, gls_sorted)], ['fit', 'hist'])
#        plt.text(5, 5.5, 'Index = %5.2f +/- %5.2f' % (index, indexErr))
        legend = plt.legend(loc='upper right', shadow=True)
        plt.xlabel('Number of Goals Scored')
        plt.ylabel('Games')
        string = '$\mathrm{Histogram\ of\ Goals:}\ \mu=%3.3f,\ \sigma=%3.3f$'%(mean_g, std_g)
        plt.title(string)
        plt.axis([-0.5, max_x, 0, max_y[0][1]+10]) #unnormalised
#       plt.axis([-0.5, max_x, 0, 1.5]) #normalised
        plt.grid(True)

#       plt.show()
        fig.savefig('../plots/'+self.name+'_Gls_Scored.png')
        fig.savefig('../plots/'+self.name+'_Gls_Scored.pdf')
        
    def print_info(self):
        print "************************************************************"
        print "Team: ", self.name 
        print "************************************************************"
        print "Games: ", self.games
        print "Wins: ", self.wins
        print "Draws: ", self.draws
        print "Loses: ", self.loses
        print "Win %: ", self.win_percentage
        print "Goals scored: ",  self.goals_scored
        print "Goals conceded: ",  self.goals_conceded
        print "Clean sheets: ", self.clean_sheets
        print "goals scored per game: ", float(self.goals_scored)/self.games
        print "goals conceded per game: ", float(self.goals_conceded)/self.games
        print "************************************************************" 
        print "Home Games: ", self.home_games
        print "Wins: ", self.home_wins
        print "Draws: ", self.home_draws
        print "Loses: ", self.home_loses
        print "Win %: ", self.home_win_percentage
        print "goals scored: ", self.home_goals_scored
        print "goals conceded: ", self.home_goals_conceded
        print "Clean sheets: ", self.home_clean_sheets
        print "goals scored per game: ", float(self.home_goals_scored)/self.home_games
        print "goals conceded per game: ", float(self.home_goals_conceded)/self.home_games
        print "************************************************************"
        print "Away Games: ", self.away_games
        print "Wins: ", self.away_wins
        print "Draws: ", self.away_draws
        print "Loses: ", self.away_loses
        print "Win %: ", self.away_win_percentage
        print "goals scored: ", self.away_goals_scored
        print "goals conceded: ", self.away_goals_conceded
        print "Clean sheets: ", self.away_clean_sheets
        print "goals scored per game: ", float(self.away_goals_scored)/self.away_games
        print "goals conceded per game: ", float(self.away_goals_conceded)/self.away_games
        print "************************************************************"
        print "Neutral Games: ", self.neutral_games
        print "Wins: ", self.neutral_wins
        print "Draws: ", self.neutral_draws
        print "Loses: ", self.neutral_loses
        print "Win %: ", self.neutral_win_percentage
        print "goals scored: ", self.neutral_goals_scored
        print "goals conceded: ", self.neutral_goals_conceded
        print "Clean sheets: ", self.neutral_clean_sheets
        print "goals scored per game: ", float(self.neutral_goals_scored)/self.neutral_games
        print "goals conceded per game: ", float(self.neutral_goals_conceded)/self.neutral_games
        print "************************************************************"        
        
             
    def print_results(self):
        input_file = csv.DictReader(open("/home/philip/workspace/wordcup/results.csv"))
        for row in input_file:
            date = row["date"]
            home_team = row["home_team"]
            away_team = row["away_team"]
            home_goals = int(row["home_goals"])
            away_goals = int(row["away_goals"])
            neutral = int(row["neutral"])
                       
            if home_team == self.name or away_team == self.name:
                print date+", "+home_team+", ",away_team,", ",home_goals,", ",away_goals,", ",neutral

    def set_home_info(self, for_goals, against_goals):
        self.goals_scored += for_goals
        self.goals_conceded += against_goals
        self.home_goals_scored += for_goals
        self.home_goals_conceded += against_goals         
        self.games += 1
        self.home_games += 1
        
        if(against_goals == 0):
            self.clean_sheets += 1
            self.home_clean_sheets += 1
                
        if(for_goals > against_goals):
            self.wins += 1
            self.home_wins += 1
        elif(for_goals < against_goals):
            self.loses += 1
            self.home_loses += 1
        else:
            self.draws += 1
            self.home_draws += 1
    
    def set_away_info(self, for_goals, against_goals):
        self.goals_scored += for_goals
        self.goals_conceded += against_goals
        self.away_goals_scored += for_goals
        self.away_goals_conceded += against_goals         
        self.games += 1
        self.away_games += 1
        
        if(against_goals == 0):
            self.clean_sheets += 1
            self.away_clean_sheets += 1
                
        if(for_goals > against_goals):
            self.wins += 1
            self.away_wins += 1
        elif(for_goals < against_goals):
            self.loses += 1
            self.away_loses += 1
        else:
            self.draws += 1
            self.away_draws += 1
    def set_neutral_info(self, for_goals, against_goals):
        self.goals_scored += for_goals
        self.goals_conceded += against_goals
        self.neutral_goals_scored += for_goals
        self.neutral_goals_conceded += against_goals         
        self.games += 1
        self.neutral_games += 1
        
        if(against_goals == 0):
            self.clean_sheets += 1
            self.neutral_clean_sheets += 1
                
        if(for_goals > against_goals):
            self.wins += 1
            self.neutral_wins += 1
        elif(for_goals < against_goals):
            self.loses += 1
            self.neutral_loses += 1
        else:
            self.draws += 1
            self.neutral_draws += 1
            