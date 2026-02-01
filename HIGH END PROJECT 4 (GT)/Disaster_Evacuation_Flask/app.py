from flask import Flask, render_template, request
from graph_logic import find_evacuation_route

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/evacuate", methods=["POST"])
def evacuate():
    location = request.form["location"]
    destination = request.form["destination"]
    disaster = request.form["disaster"]

    route, distance = find_evacuation_route(location, destination, disaster)
    
    # Check if no path was found (distance will be float('inf'))
    if distance == float('inf'):
        return render_template(
            "result.html",
            route=route[0],
            distance="No safe route available",
            disaster=disaster.capitalize(),
            no_route=True
        )
    
    return render_template(
        "result.html",
        route=" → ".join(route),
        distance=distance,
        disaster=disaster.capitalize(),
        no_route=False
    )

if __name__ == "__main__":
    app.run(debug=True)