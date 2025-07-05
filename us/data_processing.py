def process_routes(df, source=None, dest=None):
    if source:
        df = df[df["SourceAirport"] == source]
    if dest:
        df = df[df["DestAirport"] == dest]
    popular_routes = (
        df.groupby(["SourceAirport", "DestAirport"])
        .size()
        .reset_index(name="Count")
        .sort_values("Count", ascending=False)
        .head(10)
    )
    return popular_routes 