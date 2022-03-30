from flask import Flask, render_template
import tracker

app= Flask(__name__)

@app.route("/")
def index():
	'''calls the TFL API, requests times for inbound and outbound trains,
	and then sends the times to render_template'''
	
	inbound = tracker.train_finder('910GWDST', #Wood Street
		                           '910GLIVST' #Liverpool Street
		                           )

	homebound = tracker.train_finder('910GLIVST', #Liverpool Street
	                                 '910GCHINGFD' #Chingford
	                                 )

	return render_template("index.html", inbound=inbound, homebound=homebound)

if __name__ == "__main__":
	app.run()