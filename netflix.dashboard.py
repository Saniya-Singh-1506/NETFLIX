import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Page config
st.set_page_config(page_title="Netflix Dashboard", layout="wide")
st.markdown("<h1 style='text-align:center;color:#FF0000;'>🎬 Netflix Dashboard</h1>", unsafe_allow_html=True)

# Load data (your original code)
df=pd.read_csv("C:\\Users\\hp\\AppData\\Local\\Temp\\2a495318-d246-49b0-9ec4-6377c7752c85_archive (2).zip.c85\\netflix_titles.csv")
df=df.dropna(subset=["type","release_year","rating","country","duration"])

# Set dark style
plt.style.use("dark_background")

# --- Movies vs TV Shows ---
st.subheader("📊 Number of Movies vs TV Shows")
type_counts=df["type"].value_counts()
fig, ax = plt.subplots(figsize=(6,4))
ax.bar(type_counts.index, type_counts.values, color=["skyblue","orange"])
ax.set_title("NUMBER OF MOVIES VS T.V SHOWS ON NETFLIX", color="white")
ax.set_xlabel('TYPE', color="white")
ax.set_ylabel("COUNT", color="white")
ax.tick_params(colors="white")
st.pyplot(fig)

# --- Content Rating ---
st.subheader("🍿 Content Rating Distribution")
rating_counts=df["rating"].value_counts()
fig, ax = plt.subplots(figsize=(8,6))
colors = plt.cm.Set3(range(len(rating_counts)))
ax.pie(rating_counts.values, labels=rating_counts.index, autopct="%1.1f%%",
       startangle=140, shadow=True, wedgeprops={'edgecolor':'black'}, colors=colors)
ax.set_title("PERCENTAGE OF CONTENT RATING", color="white")
st.pyplot(fig)

# --- Movie Duration ---
st.subheader("⏱ Distribution of Movie Duration")
movie_df=df[df["type"]== "Movie"].copy()
movie_df["duration_int"]=movie_df['duration'].str.replace(" min"," ").astype(int)
fig, ax = plt.subplots(figsize=(8,6))
ax.hist(movie_df["duration_int"], bins=30, color="purple", edgecolor="white")
ax.set_title("DISTRIBUTION OF MOVIE DURATION", color="white")
ax.set_xlabel('DURATION(MINS)', color="white")
ax.set_ylabel("NUMBER OF MOVIES", color="white")
ax.tick_params(colors="white")
st.pyplot(fig)

# --- Release Year vs Shows ---
st.subheader("📅 Release Year vs Number of Shows")
release_counts=df["release_year"].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(release_counts.index, release_counts.values, color="red")
ax.set_title("RELEASE YEAR VS NO. OF SHOWS", color="white")
ax.set_xlabel('RELEASE YEAR', color="white")
ax.set_ylabel("NUMBER OF SHOWS", color="white")
ax.tick_params(colors="white")
st.pyplot(fig)

# --- Top Countries ---
st.subheader("🌍 Top 10 Countries by Number of Shows")
country_counts = df["country"].value_counts().head(10)
fig, ax = plt.subplots(figsize=(8,6))
ax.barh(country_counts.index, country_counts.values, color="teal")
ax.set_title("TOP 10 COUNTRIES BY NO. OF SHOWS", color="white")
ax.set_xlabel('NUMBER OF SHOWS', color="white")
ax.tick_params(colors="white")
st.pyplot(fig)

# --- Movies vs TV Shows per Year ---
st.subheader("📈 Comparison: Movies vs TV Shows per Year")
content_by_year = df.groupby(["release_year","type"]).size().unstack().fillna(0)
fig, ax = plt.subplots(figsize=(10,6))
ax.plot(content_by_year.index, content_by_year["Movie"], color="blue", label="Movies")
ax.plot(content_by_year.index, content_by_year["TV Show"], color="orange", label="TV Shows")
ax.set_title("COMPARISON B/W MOVIES AND TV SHOWS PER YEAR", color="white")
ax.set_xlabel("YEAR", color="white")
ax.set_ylabel("COUNT", color="white")
ax.legend()
ax.tick_params(colors="white")
st.pyplot(fig)
