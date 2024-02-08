import pandas as pd

df = pd.read_json("http://swiftapi.rubypaper.co.kr:2029/hoppin/movies?version=1&page=1&count=30&genreId=&order=releasedateasc")
# print(type(df))

hoppin = df["hoppin"]
# print(hoppin)
movies = hoppin['movies']
movie = movies["movie"]
for item in movie:
    print(item["title"] + ":" + item["genreNames"])