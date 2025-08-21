import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Load data
df=pd.read_csv("C:\\Users\\hp\\AppData\\Local\\Temp\\2a495318-d246-49b0-9ec4-6377c7752c85_archive (2).zip.c85\\netflix_titles.csv")
df=df.dropna(subset=["type","release_year","rating","country","duration"])

# Prepare data
type_counts=df["type"].value_counts()
rating_counts=df["rating"].value_counts()
movie_df=df[df["type"]=="Movie"].copy()
movie_df["duration_int"]=movie_df['duration'].str.replace(" min"," ").astype(int)
release_counts=df["release_year"].value_counts().sort_index()
country_counts=df["country"].value_counts().head(10)
content_by_year = df.groupby(["release_year","type"]).size().unstack().fillna(0)

# Set style & figure
plt.style.use("ggplot")
fig = plt.figure(constrained_layout=True, figsize=(16,12))
fig.patch.set_facecolor("#1e1e2f")  # Dark background
gs = GridSpec(3, 2, figure=fig)

# Movies vs TV Shows
ax1 = fig.add_subplot(gs[0,0])
ax1.bar(type_counts.index, type_counts.values, color=["skyblue","orange"])
ax1.set_title("Movies vs TV Shows", color="white")
ax1.tick_params(colors="white")
ax1.yaxis.label.set_color("white")
ax1.xaxis.label.set_color("white")

# Pie chart
ax2 = fig.add_subplot(gs[0,1])
colors = plt.cm.Paired(range(len(rating_counts)))
ax2.pie(rating_counts.values, labels=rating_counts.index, autopct="%1.1f%%", startangle=140, shadow=True, colors=colors, wedgeprops={'edgecolor':'black'})
ax2.set_title("Content Rating %", color="white")

# Movie Duration
ax3 = fig.add_subplot(gs[1,0])
ax3.hist(movie_df["duration_int"], bins=30, color="purple", edgecolor="black")
ax3.set_title("Movie Duration Distribution", color="white")
ax3.set_xlabel("Minutes", color="white")
ax3.set_ylabel("Number of Movies", color="white")
ax3.tick_params(colors="white")

# Release Year vs Shows
ax4 = fig.add_subplot(gs[1,1])
ax4.scatter(release_counts.index, release_counts.values, color="red", s=15)
ax4.set_title("Release Year vs No. of Shows", color="white")
ax4.set_xlabel("Year", color="white")
ax4.set_ylabel("Count", color="white")
ax4.tick_params(colors="white")

# Top Countries
ax5 = fig.add_subplot(gs[2,0])
ax5.barh(country_counts.index, country_counts.values, color="teal")
ax5.set_title("Top 10 Countries", color="white")
ax5.set_xlabel("Number of Shows", color="white")
ax5.tick_params(colors="white")

# Movies vs TV Shows over time
ax6 = fig.add_subplot(gs[2,1])
ax6.plot(content_by_year.index, content_by_year["Movie"], color="blue", label="Movies")
ax6.plot(content_by_year.index, content_by_year["TV Show"], color="orange", label="TV Shows")
ax6.set_title("Movies vs TV Shows Over Time", color="white")
ax6.legend()
ax6.tick_params(colors="white")
ax6.xaxis.label.set_color("white")
ax6.yaxis.label.set_color("white")

plt.suptitle("Netflix Dashboard", fontsize=22, color="white", fontweight="bold")
plt.show()
