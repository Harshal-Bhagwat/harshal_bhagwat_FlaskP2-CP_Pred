from flask import *
from pickle import *

f = open("model.pkl", "rb")
model = load(f)
f.close()

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
	if request.method == "POST":
		rd = float(request.form["rd"])
		ad = float(request.form["ad"])
		ms = float(request.form["ms"])
		d = [[rd, ad, ms]]
		profit = model.predict(d)
		msg = "Predicted Profit = " + str(round(profit[0], 2))
		return render_template("home.html", msg = msg)
	else:
		return render_template("home.html")

if __name__ == "__main__":
	app.run(use_reloader = True, debug = True)