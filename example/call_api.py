from Osaka.api import GoogleMapAPI

key = "03d7f2d9ccmsha129b9e62cdf9fap153f12jsn0c736f818bc6"
host = "maps-data.p.rapidapi.com"
googleapi = GoogleMapAPI(key, host)
longitude = 112.7521
latitude = -7.2575
hasil = googleapi.search("Mixue", latitude, longitude)
# hasil.to_csv("gmap-search-mixue.csv")
print(hasil.head())
# for review tempat
hasil_review = googleapi.place_reviews(hasil["business_id"])
print(hasil_review.head())
