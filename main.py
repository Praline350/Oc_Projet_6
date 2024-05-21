import csv
import time

from display import Display
from optimized import Optimized


def read_data(file):
    """Lit les données d'un fichier csv"""

    data = []
    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(tuple(row))
        return data


def run():
    """Lance le programme"""

    display = Display()
    algo = Optimized()
    data_file = display.path_choice()
    max_budget = display.max_budget_choice() 
    score_user = display.score_choice()
    start = time.time()
    data = read_data(data_file)
    action = algo.calculate_benef_data(data)
    scored_action = algo.calculate_score(action, max_budget, score_user)
    selected_actions, infos = algo.best_action(scored_action, max_budget)
    end = time.time()
    timer = end - start
    display.display_result(selected_actions, infos, timer)


run()