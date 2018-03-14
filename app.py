from flask import *
from api_key import key
from utils import *

##################################################
# Author: glee-
# https://github.com/glee-/Postulate
##################################################

app = Flask(__name__)

@app.route("/")
def start():
    return redirect(url_for("main"))

@app.route("/osu", methods = ["GET", "POST"])
def main(old=None, newpp=None, uname=None, pp=None):
    if request.method == "GET":
        resp = make_response(render_template("home.html"))
        resp.set_cookie("uname", "", expires = 0)
        return resp

    if request.method == "POST":
        uname = ""
        if "uname" in request.cookies:
            uname = request.cookies.get("uname")
        else:
            uname = request.form["uname"]

        pp = int(request.form["pp"])

        total_score, total_acc, pp_raw, pp_rank = get_user(key, uname)
        pp_list, acc_list, score_list = get_user_best(key, uname)
        newpp = get_newpp(pp_list, pp_raw, pp)
        newpp = round(newpp, 2)

        resp = make_response(render_template("estimate.html", old = pp_raw, newpp = newpp, uname= uname, pp=pp))
        resp.set_cookie("uname", uname)
        return resp

@app.errorhandler(400)
def err400(err):
    return redirect(url_for("main"))
