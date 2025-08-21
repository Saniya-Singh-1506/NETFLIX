import pandas as pd
import streamlit as st
import plotly.express as px

# Load data
df = pd.read_csv("C:\\Users\\hp\\AppData\\Local\\Temp\\2a495318-d246-49b0-9ec4-6377c7752c85_archive (2).zip.c85\\netflix_titles.csv")

# Clean data
df = df.dropna(subset=["type", "release_year", "rating", "country", "duration"])

# Dashboard Title
st.markdown("<h1 style='text-align: center; color: #E50914;'>🎬 Netflix Insights Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

# --- Movies vs TV Shows ---
st.markdown("### 🍿 **Movies vs TV Shows**")
type_counts = df["type"].value_counts()
fig1 = px.bar(type_counts, x=type_counts.index, y=type_counts.values, 
              color=type_counts.index, labels={"x": "Type", "y": "Count"})
st.plotly_chart(fig1)
st.markdown("---")

# --- Rating Distribution ---
st.markdown("### ⭐ **Content Ratings Breakdown**")
rating_counts = df["rating"].value_counts()
fig2 = px.pie(values=rating_counts.values, names=rating_counts.index, 
              title="Content Ratings")
st.plotly_chart(fig2)
st.markdown("---")

# --- Movie Duration Distribution ---
st.markdown("### ⏱️ **Movie Duration Distribution**")
movie_df = df[df["type"] == "Movie"].copy()
movie_df["duration_int"] = movie_df['duration'].str.replace(" min","").astype(int)
fig3 = px.histogram(movie_df, x="duration_int", nbins=30, color_discrete_sequence=["purple"])
st.plotly_chart(fig3)
st.markdown("---")

# --- Release Year vs No. of Shows ---
st.markdown("### 📅 **Release Trends Over Years**")
release_counts = df["release_year"].value_counts().sort_index()
fig4 = px.scatter(x=release_counts.index, y=release_counts.values, 
                  labels={"x": "Release Year", "y": "Number of Shows"}, color_discrete_sequence=["red"])
st.plotly_chart(fig4)
st.markdown("---")

# --- Top 10 Countries ---
st.markdown("### 🌍 **Top 10 Countries with Most Content**")
country_counts = df["country"].value_counts().head(10)
fig5 = px.bar(country_counts, x=country_counts.values, y=country_counts.index, 
              orientation="h", color=country_counts.values, labels={"x":"No. of Shows", "y":"Country"})
st.plotly_chart(fig5)
st.markdown("---")

# --- Content by Year (Movies vs TV Shows) ---
st.markdown("### 🎭 **Movies vs TV Shows by Year**")
content_by_year = df.groupby(["release_year","type"]).size().unstack().fillna(0)
fig6 = px.line(content_by_year, x=content_by_year.index, y=["Movie","TV Show"],
               labels={"value":"Count","release_year":"Year"}, markers=True)
st.plotly_chart(fig6)
