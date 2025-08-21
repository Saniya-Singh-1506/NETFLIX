import pandas as pd
import matplotlib.pyplot as plt

#load the data
df=pd.read_csv("C:\\Users\\hp\\AppData\\Local\\Temp\\2a495318-d246-49b0-9ec4-6377c7752c85_archive (2).zip.c85\\netflix_titles.csv")

#clean data
df=df.dropna(subset=["type","release_year","rating","country","duration"])

#get the movie vs tv show(type coloumn name)
type_counts=df["type"].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values, color=["skyblue","orange"])
plt.title("NUMBER OF MOVIES VS T.V SHOWS ON NETFLIX")
plt.xlabel('TYPE')
plt.ylabel("COUNT")
plt.tight_layout()
plt.savefig("movie_vs_tvshow.png")
plt.show()

#ratingcount using pie chart

rating_counts=df["rating"].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts.values, labels=rating_counts.index,autopct="%1.1f%%",startangle=90)
plt.title("PERCENTAGE OF CONTENT RATING")
plt.tight_layout()
plt.savefig("content_rating.png")
plt.show()

#DURATION OF MOVIE
movie_df=df[df["type"]== "Movie"].copy()
movie_df["duration_int"]=movie_df['duration'].str.replace(" min"," ").astype(int)

plt.figure(figsize=(8,6))
plt.hist(movie_df["duration_int"],bins=30,color="purple",edgecolor="black")
plt.title("DISTRIBUTION OF MOVIE DURATION")
plt.xlabel('DURATION(MINS)')
plt.ylabel("NUMBER OF MOVIES")
plt.tight_layout()
plt.savefig("movie.duration.png")
plt.show()

#RElEASE COUNT
release_counts=df["release_year"].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index, release_counts.values, color="red")
plt.title("RELEASE YEAR VS NO. OF SHOWS")
plt.xlabel('RELEASE YEAR')
plt.ylabel("NUMBER OF SHOWS")
plt.tight_layout()
plt.savefig("release.vs.show.png")
plt.show()

country_counts = df["country"].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index,country_counts.values,color="teal")
plt.title("TOP 10 COUNTRIES BY NO. OF SHOWS")
plt.xlabel('NUMBER OF SHOWS')
plt.ylabel("COUNTRY")
plt.tight_layout()
plt.savefig("shows.country.png")
plt.show()

#content by year
content_by_year = df.groupby(["release_year","type"]).size().unstack().fillna(0)
fig, ax = plt.subplots(1,2, figsize=(12,5))

#first subplot.movies
ax[0].plot(content_by_year.index,content_by_year["Movie"], color="blue")
ax[0].set_title("MOVIE RELEASED PER YEAR")
ax[0].set_xlabel("YEAR")
ax[0].set_ylabel("NUMBER OF MOVIES")

#second subplot : tv showa
ax[0].plot(content_by_year.index,content_by_year["TV Show"], color="orange")
ax[0].set_title("TV SHOW RELEASED PER YEAR")
ax[0].set_xlabel("YEAR")
ax[0].set_ylabel("NUMBER OF SHOWS")

fig.suptitle("COMPARISION B/W MOVIE AND TV SHOWS")

plt.tight_layout
plt.savefig("compare.png")
plt.show()