import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# ================== Load Data ==================
df = pd.read_csv(
    "C:\\Users\\hp\\AppData\\Local\\Temp\\2a495318-d246-49b0-9ec4-6377c7752c85_archive (2).zip.c85\\netflix_titles.csv"
)

# Clean data
df = df.dropna(subset=["type", "release_year", "rating", "country", "duration"])

# ================== Streamlit Setup ==================
st.set_page_config(page_title="Netflix Dashboard (Matplotlib)", layout="wide")
st.title("🎬 Netflix Dashboard (Matplotlib Edition)")

# ================== Movies vs TV Shows ==================
st.subheader("Number of Movies vs TV Shows")
type_counts = df["type"].value_counts()
fig1, ax1 = plt.subplots(figsize=(6,4))
ax1.bar(type_counts.index, type_counts.values, color=["skyblue","orange"])
ax1.set_title("NUMBER OF MOVIES VS T.V SHOWS ON NETFLIX")
ax1.set_xlabel("TYPE")
ax1.set_ylabel("COUNT")
st.pyplot(fig1)

# ================== Ratings ==================
st.subheader("Percentage of Content Ratings")
rating_counts = df["rating"].value_counts()
fig2, ax2 = plt.subplots(figsize=(8,6))
ax2.pie(rating_counts.values, labels=rating_counts.index, autopct="%1.1f%%", startangle=90)
ax2.set_title("PERCENTAGE OF CONTENT RATING")
st.pyplot(fig2)

# ================== Movie Duration ==================
st.subheader("Distribution of Movie Duration")
movie_df = df[df["type"]== "Movie"].copy()
movie_df["duration_int"] = movie_df["duration"].str.replace(" min","", regex=False).astype(int)
fig3, ax3 = plt.subplots(figsize=(8,6))
ax3.hist(movie_df["duration_int"], bins=30, color="purple", edgecolor="black")
ax3.set_title("DISTRIBUTION OF MOVIE DURATION")
ax3.set_xlabel("DURATION (MINS)")
ax3.set_ylabel("NUMBER OF MOVIES")
st.pyplot(fig3)

# ================== Release Year ==================
st.subheader("Release Year vs Number of Shows")
release_counts = df["release_year"].value_counts().sort_index()
fig4, ax4 = plt.subplots(figsize=(10,6))
ax4.scatter(release_counts.index, release_counts.values, color="red")
ax4.set_title("RELEASE YEAR VS NO. OF SHOWS")
ax4.set_xlabel("RELEASE YEAR")
ax4.set_ylabel("NUMBER OF SHOWS")
st.pyplot(fig4)

# ================== Top 10 Countries ==================
st.subheader("Top 10 Countries by Number of Shows")
country_counts = df["country"].value_counts().head(10)
fig5, ax5 = plt.subplots(figsize=(8,6))
ax5.barh(country_counts.index, country_counts.values, color="teal")
ax5.set_title("TOP 10 COUNTRIES BY NO. OF SHOWS")
ax5.set_xlabel("NUMBER OF SHOWS")
ax5.set_ylabel("COUNTRY")
st.pyplot(fig5)

# ================== Movies vs TV Shows per Year ==================
st.subheader("Comparison: Movies vs TV Shows by Year")
content_by_year = df.groupby(["release_year","type"]).size().unstack().fillna(0)
fig6, ax6 = plt.subplots(figsize=(10,6))
ax6.plot(content_by_year.index, content_by_year["Movie"], color="blue", label="Movies")
ax6.plot(content_by_year.index, content_by_year["TV Show"], color="orange", label="TV Shows")
ax6.set_title("COMPARISON: MOVIES VS TV SHOWS PER YEAR")
ax6.set_xlabel("YEAR")
ax6.set_ylabel("COUNT")
ax6.legend()
st.pyplot(fig6)
