from flask import Flask, render_template

# Create a website object:
app = Flask(__name__)


# Refer to the app variable. Use route() that belongs to the app object:
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # df = pandas.read_scv("")
    temperature = 23  # df.station(data)
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }


if __name__ == "__main__":
    app.run(debug=True)
