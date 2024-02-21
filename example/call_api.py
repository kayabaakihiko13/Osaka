from Osaka.api import GoogleMapAPI

key = "YOUR X-RapidAPI-Key"
host = "X-RapidAPI-Host"
googleapi = GoogleMapAPI(key, host)
longitude = 112.7521
latitude = -7.2575
hasil = googleapi.search("Mixue", latitude, longitude)
# hasil.to_csv("gmap-search-mixue.csv")
print(hasil.head())
# for review tempat
hasil_review = googleapi.place_reviews(hasil["business_id"])
print(hasil_review)
