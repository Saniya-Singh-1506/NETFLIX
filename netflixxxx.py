import pandas as pd
import plotly.express as px

# Load the data
df=pd.read_csv("C:\\Users\\hp\\AppData\\Local\\Temp\\2a495318-d246-49b0-9ec4-6377c7752c85_archive (2).zip.c85\\netflix_titles.csv")

# Clean data
df = df.dropna(subset=["type", "release_year", "rating", "country", "duration"])

# --- Movie vs TV Show ---
type_counts = df["type"].value_counts().reset_index()
type_counts.columns = ["Type", "Count"]   # rename columns
fig1 = px.pie(type_counts, names="Type", values="Count",
              title="Movies vs TV Shows",
              color_discrete_sequence=px.colors.sequential.RdBu)
fig1.show()

# --- Top 10 Countries ---
top_countries = df["country"].value_counts().head(10).reset_index()
top_countries.columns = ["Country", "Count"]
fig2 = px.bar(top_countries, x="Country", y="Count",
              title="Top 10 Countries on Netflix",
              color="Count", text="Count")
fig2.show()

# --- Content Release Trend ---
year_trend = df["release_year"].value_counts().sort_index().reset_index()
year_trend.columns = ["Year", "Count"]
fig3 = px.line(year_trend, x="Year", y="Count",
               markers=True, title="Content Release Trend over Years")
fig3.show()

# --- Top 10 Genres ---
df["listed_in"] = df["listed_in"].apply(lambda x: x.split(",")[0])
top_genres = df["listed_in"].value_counts().head(10).reset_index()
top_genres.columns = ["Genre", "Count"]
fig4 = px.bar(top_genres, x="Genre", y="Count", orientation="v",
              title="Top 10 Genres", color="Count", text="Count")
fig4.show()

# --- Rating Distribution ---
rating_dist = df["rating"].value_counts().reset_index()
rating_dist.columns = ["Rating", "Count"]
fig5 = px.bar(rating_dist, x="Rating", y="Count",
              title="Rating Distribution", color="Count", text="Count")
fig5.show()
