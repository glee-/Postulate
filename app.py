from flask import *
from api_key import key
from utils import *


app = Flask(__name__)

@app.route("/")
def start():
    return redirect(url_for("main"))

@app.route("/osu", methods = ["GET", "POST"])
def main():
    if request.method == "GET":
        resp = make_response(render_template("home.html"))
        resp.set_cookie("uname", "", expires = 0)
        return resp


    if request.method == "POST":
        uname = request.form["uname"]
        pp = int(request.form["pp"])

        total_score, total_acc, pp_raw, pp_rank = get_user(key, uname)

        pp_list, acc_list, score_list = get_user_best(key, uname)
        weights = get_weights(len(pp_list));

        unweighted_pp_sum = sum(pp_list)

        weighted_pp_avg = weighted_avg(pp_list, weights)
        weighted_pp_sum = sum(weighted_pp_avg)

        top_acc = sum(weighted_avg(acc_list, weights)) / sum(weights)

        a,b = calculate_exp_regression(weighted_pp_avg)
        tail = calculate_estimation(a, b)

        bonuspp = pp_raw - (weighted_pp_sum + tail)
        unique_scores = calculate_unique(bonuspp)

        newpp = calculate_new_pp(pp_list, pp)

        return str(top_acc)