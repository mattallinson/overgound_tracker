from flask import Flask, render_template
import tracker

app= Flask(__name__)

@app.route("/")
def index():
	
	inbound = tracker.train_finder('Wood Street','Liverpool Street')
	homebound = tracker.train_finder('Liverpool Street', 'Chingford')

	return render_template("index.html", inbound=inbound, homebound=homebound)

if __name__ == "__main__":
	app.run()