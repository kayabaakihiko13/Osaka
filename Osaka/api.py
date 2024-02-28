import requests
import pandas as pd
from typing import Union
from datetime import datetime


class GoogleMapAPI(object):
    def __init__(self, api_key: str, api_host: str):
        self.key = api_key
        self.host = api_host
        self.url_search = "https://maps-data.p.rapidapi.com/searchmaps.php"
        self.url_place_reviews = "https://maps-data.p.rapidapi.com/reviews.php"

    def search(
        self, query: str, lat: float, long: float, limit: int = 10
    ) -> pd.DataFrame:
        headers = {"X-RapidAPI-Key": self.key, "X-RapidAPI-Host": self.host}
        query_header = {
            "query": query,
            "limit": str(limit),
            "country": "us",
            "lang": "en",
            "lat": str(lat),
            "lng": str(long),
            "offset": "0",
            "zoom": "13",
        }

        response = requests.get(self.url_search, headers=headers, params=query_header)
        df = pd.json_normalize(response.json().get("data", []))

        return df

    def place_reviews(
        self, business_id: Union[pd.Series, str], limit=20
    ) -> pd.DataFrame:
        headers = {"X-RapidAPI-Key": self.key, "X-RapidAPI-Host": self.host}

        if isinstance(business_id, str):
            querystring = {
                "business_id": business_id,
                "country": "us",
                "lang": "en",
                "limit": str(limit),
            }
            response = requests.get(
                self.url_place_reviews, headers=headers, params=querystring
            )
            data = response.json()
            if isinstance(data, list):
                reviews = data[0].get("reviews", [])
            else:
                reviews = data.get("data", {}).get("reviews", [])
            return pd.json_normalize(reviews) if reviews else pd.DataFrame()

        elif isinstance(business_id, pd.Series):
            all_results = []

            for id in business_id:
                querystring = {
                    "business_id": id,
                    "country": "us",
                    "lang": "en",
                    "limit": str(limit),
                }
                response = requests.get(
                    self.url_place_reviews, headers=headers, params=querystring
                )
                data = response.json()
                if isinstance(data, list):
                    reviews = data[0].get("reviews", [])
                else:
                    reviews = data.get("data", {}).get("reviews", [])

                result_data = pd.json_normalize(reviews) if reviews else pd.DataFrame()
                result_data["business_id"] = id
                all_results.append(result_data)

            return pd.concat(all_results, ignore_index=True)


class Twitter_API(object):
    def __init__(self, api_key: str, api_host: str):
        self.key = api_key
        self.host = api_host
        self.hastag = "twitter154.p.rapidapi.com"
        self.url_hastag = "https://twitter154.p.rapidapi.com/hashtag/hashtag"

    def hashtag(
        self, hashtag: str, limit: int = 20, section: str = "top"
    ) -> pd.DataFrame:
        header = {"X-RapidAPI-Key": self.key, "X-RapidAPI-Host": self.host}
        querystring = {"hashtag": hashtag, "limit": str(limit), "section": section}
        response = requests.get(self.url_hastag, headers=header, params=querystring)
        selected_columns = [
            "tweet_id",
            "creation_date",
            "text",
            "media_url",
            "video_url",
            "user.username",
            "favorite_count",
            "retweet_count",
            "reply_count",
            "quote_count",
            "retweet",
            "views",
            "timestamp",
            "source",
        ]
        df = pd.json_normalize(response.json().get("results", []))[selected_columns]
        # convert time stamps be normal
        df["timestamp"] = df["timestamp"].apply(
            lambda x: datetime.utcfromtimestamp(x).strftime("%Y-%m-%d %H:%M:%S UTC")
        )
        return df
