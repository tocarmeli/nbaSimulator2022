import pandas as pd
import random

class Defense:
    def __init__(self, spreadsheet_path:str) -> None:
        self.excel_path = spreadsheet_path
        self.excel = pd.read_csv(self.excel_path, sep=',')
        self.excel = self.excel[['Team', 'FG%', '3P%', 'TRB','TOV', 'PTS']]

    def fg_score(self):
        fg_arr = [0] * 30

        for k in range(len(self.excel['FG%']) - 1):
            if self.excel['FG%'][k] < 0.455:
                fg_arr[k] = random.randint(8,10) / 2
            elif self.excel['FG%'][k] >= 0.455 and self.excel['FG%'][k] < 0.465:
                fg_arr[k] = random.randint(5,7) / 2
            else:
                fg_arr[k] = random.randint(1,4) / 2
        return fg_arr


    def fg_three_score(self):
        arr_3p = [0] * 30
        for k in range(len(self.excel['3P%']) - 1):
            if self.excel['3P%'][k] < 0.35:
                arr_3p[k] = random.randint(8,10)
            elif self.excel['3P%'][k] >= 0.35 and self.excel['3P%'][k] < 0.36:
                arr_3p[k] = random.randint(5,7)
            else:
                arr_3p[k] = random.randint(1,4)
        return arr_3p



    def rebound_score(self):
        arr_rebound = [0] * 30
        for k in range(len(self.excel) - 1):
            if self.excel['TRB'][k] < 43.5:
                arr_rebound[k] = random.randint(12,15)
            elif self.excel['TRB'][k] >= 43.5 and self.excel['TRB'][k] < 46:
                arr_rebound[k] = random.randint(6,11)
            else:
                arr_rebound[k] = random.randint(1,5)
        return arr_rebound

    def tov_score(self):
        arr_tov = [0] * 30
        for k in range(len(self.excel['TOV']) - 1):
            if self.excel['TOV'][k] > 13.7:
                arr_tov[k] = random.randint(12,15)
            elif self.excel['TOV'][k] <= 13.7 and self.excel['TOV'][k] >= 13.4:
                arr_tov[k] = random.randint(6,11)
            else:
                arr_tov[k] = random.randint(1,5)
        return arr_tov

    def pts_score(self):
        arr_pts = [0] * 30
        for k in range(len(self.excel['PTS']) - 1):
            if self.excel['PTS'][k] < 107:
                arr_pts[k] = random.randint(16,20)
            elif self.excel['PTS'][k] >= 107 and self.excel['PTS'][k] < 111.5:
                arr_pts[k] = random.randint(8,15)
            else:
                arr_pts[k] = random.randint(1,7)
        return arr_pts


    def calc_total_score(self):
        total_score = [0] * 30
        fg = self.fg_score()
        fg_3 = self.fg_three_score()
        tov = self.tov_score()
        reb = self.rebound_score()
        pts = self.pts_score()
        for k in range(30):
            total_score[k] = fg[k] + fg_3[k] + tov[k] + reb[k] + pts[k]

        return total_score

    if __name__ == '__main__':
        program = Defense()