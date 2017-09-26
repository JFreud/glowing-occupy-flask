import occupation
from flask import Flask,render_template

my_app = Flask(__name__)

occDict = occupation.make_dict("occupations.csv")
listOcc = list(occDict.keys())
listPerc = list(occDict.values())



@my_app.route("/occupations")
def occupations():
    return render_template("base.html", listOcc=listOcc, listPerc=listPerc, randOcc = occupation.pick_random(occDict, 99.8))


if __name__ == "__main__":
    my_app.debug = True
    my_app.run()
