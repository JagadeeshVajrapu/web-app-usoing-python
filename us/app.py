from flask import Flask, render_template, request
import data_fetching
import data_processing

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    airports = sorted(set(data_fetching.get_routes_data()["SourceAirport"]))
    if request.method == 'POST':
        source = request.form.get("source")
        dest = request.form.get("dest")
        df = data_fetching.get_routes_data()
        popular_routes = data_processing.process_routes(df, source, dest)
        return render_template(
            "results.html",
            popular_routes=popular_routes.to_dict(orient="records"),
            source=source,
            dest=dest,
            airports=airports
        )
    return render_template("index.html", airports=airports)

if __name__ == '__main__':
    app.run(debug=True) 