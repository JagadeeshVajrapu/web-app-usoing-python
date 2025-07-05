import pandas as pd

def get_routes_data():
    cols = [
        "Airline", "AirlineID", "SourceAirport", "SourceAirportID",
        "DestAirport", "DestAirportID", "Codeshare", "Stops", "Equipment"
    ]
    df = pd.read_csv("data/routes.dat", names=cols)
    return df 