from flask import *
# from wtforms import Form, TextField, HiddenField
from api_key import key
from forms import *
from utils import *

##################################################
# Author: glee-
# https://github.com/glee-/Postulate
##################################################

app = Flask(__name__)
app.secret_key = key

@app.route("/")
def start():
    return redirect(url_for("main"))

@app.route("/osu", methods = ["GET", "POST"])
def main(old=None, newpp=None, uname=None, pp=None):
    if request.method == "GET":
        form = LandingForm(request.form);
        resp = make_response(render_template("home.html", form=form))
        resp.set_cookie("uname", "", expires = 0)
        return resp

    if request.method == "POST":
        uname = ""
        if request.form["uname"] != "":
            uname = request.form["uname"]
        elif "uname" in request.cookies:
            uname = request.cookies.get("uname")

        pp = request.form["pp"]

        if uname != "" and pp.isdigit():
            pp = int(pp)

            total_score, total_acc, pp_raw, pp_rank, plays = get_user(key, uname)
            pp_list, acc_list, score_list = get_user_best(key, uname)
            newpp = get_newpp(pp_list, pp_raw, pp, plays)
            newpp = round(newpp, 2)

            resp = make_response(render_template("estimate.html", old = pp_raw, newpp = newpp, uname= uname, pp=pp))
            resp.set_cookie("uname", uname)
            return resp

        if uname == "":
            flash("No username input")

        if pp == "":
            flash("No pp entered")
        elif not pp.isdigit():
            flash("Invalid pp entered ")

        return render_template("home.html")


@app.errorhandler(400)
def err400(err):
    return redirect(url_for("main"))
