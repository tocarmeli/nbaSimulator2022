from offense import Offense
from defense import Defense
import pandas as pd

off_2022 = Offense('C:/Users/tocar/Documents/Code/NBA_Season_Simulation/offensePerGame2022.csv')
off_2021 = Offense('C:/Users/tocar/Documents/Code/NBA_Season_Simulation/offensePerGame2021.csv')
defe_2022 = Defense('C:/Users/tocar/Documents/Code/NBA_Season_Simulation/defensePerGame2022.csv')
defe_2021 = Defense('C:/Users/tocar/Documents/Code/NBA_Season_Simulation/defensePerGame2021.csv')

offense_scores_2022 = off_2022.calc_total_score()
defense_scores_2022 = defe_2022.calc_total_score()
offense_scores_2021 = off_2021.calc_total_score()
defense_scores_2021 = defe_2022.calc_total_score()
total_team_score_2022 = [0] * 30
total_team_score_2021 = [0] * 30
total_team_score = [0] * 30

for k in range(len(offense_scores_2022)):
    total_team_score_2022[k] = offense_scores_2022[k] + defense_scores_2022[k]
    total_team_score_2021[k] = offense_scores_2021[k] + defense_scores_2021[k]
    total_team_score[k] = total_team_score_2022[k] + (total_team_score_2022[k] - total_team_score_2021[k])

index_winning_team = total_team_score.index(max(total_team_score))
print(off_2022.return_team(index_winning_team))
print(total_team_score[index_winning_team])