import numpy as np
import itertools

class Simulator:
    def __init__(self, groups: list, data):
        self.groups = groups
        self.data = data
    
    def simulate_game(self, team_a, team_b):
        goals_team_a, goals_team_b = self.get_goals(team_a, team_b, 2010)
        predicted_a_goal = stats.mode(np.random.poisson(goals_team_a.mean(), 100000))
        predicted_b_goal = stats.mode(np.random.poisson(goals_team_b.mean(), 100000))

        return (int(predicted_a_goal[0]), (predicted_b_goal[0]))
    
    def simulate_group_stage(self):
        for group in self.groups:
            games = list(itertools.combinations(group, 2))
            for game in games:
                team_a, team_b = game
                team_a_goal, team_b_goal = self.simulate_game(team_a, team_b)

                print(f"{team_a} {team_a_goal} : {team_b_goal} {team_b}")

    
    def get_goals(self, team_a, team_b, since=2010):
        home = self.data.loc[(self.data['home_team'] == team_a) & (self.data['away_team'] == team_b) & (self.data['year'] >= since)]
        away = self.data.loc[(self.data['home_team'] == team_b) & (self.data['away_team'] == team_a) & (self.data['year'] >= since)]

        goals_team_a = np.array(list(home.home_score) + list(away.away_score))
        goals_team_b = np.array(list(home.away_score) + list(away.home_score))

        return (goals_team_a, goals_team_b)

    
