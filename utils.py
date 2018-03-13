import requests
import numpy as np
import math
from scipy.integrate import quad

def get_weights(length):
    weights = []
    for i in range(length):
        weights.append(0.95**i)
    return weights

def get_user(key, uname):
    payload = {"k": key, "u": uname, "type": "string"}
    r = requests.get("https://osu.ppy.sh/api/get_user", params = payload)
    json = r.json()
    user = json[0]
    return int(user["total_score"]), float(user["accuracy"]), int(user["pp_raw"]), int(user["pp_rank"])

def get_user_best(key, uname):
    payload = {"k": key, "u": uname, "limit": 100, "type": "string"}
    r = requests.get("https://osu.ppy.sh/api/get_user_best", params = payload)
    json = r.json()

    pp_list = []
    acc_list = []
    score_list = []
    # print(json[0])
    for result in json:
        pp_list.append(float(result["pp"]))

        weightedhits = int(result["count300"]) * 300 + int(result["count100"]) * 100 + int(result["count50"]) * 50
        totalhits = 300 * sum([int(result["count300"]), int(result["count100"]), int(result["count50"]), int(result["countmiss"])])
        acc_list.append(weightedhits/totalhits)

        score_list.append(int(result["score"]))

    return pp_list, acc_list, score_list

def weighted_avg(lst, weights):
    return [lst[i] * weights[i] for i in range(len(lst))]

def calculate_exp_regression(lst):
    #Fitting: y = ab^x
    x = np.arange(len(lst))
    y = np.array(lst)
    b, a = np.exp(np.polyfit(x, np.log(y), 1))
    return a,b

def calculate_estimation(a, b):
    return quad(lambda x,a,b: a * b ** x, 99, np.inf, args = (a,b))[0]

def calculate_unique(bonuspp):
    return math.log(1 - bonuspp / 416.6667, 0.9994)

def calculate_new_pp(pp_list, pp):
    
