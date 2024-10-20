import tweepy

# Replace with your Bearer Token
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAACr%2BwQEAAAAAvgb1hvtpKeOHZ6ZUNRu5%2FPtLAxs%3DmdpnQBLrfakoTtZfKJPSefuHsLOsUmg5Ufy63Fnoaoj5AzmNv2'

# Authenticate with the Twitter API v2
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Define your search query and geocode parameters
search_query = 'your search query has:geo'
# Since Twitter API v2 does not support direct geocode, 
# you can search for tweets with geo-tagged data using 'has:geo'

# Define other query parameters
query_params = {
    'query': search_query,
    'max_results': 10,  # Retrieve up to 10 tweets
    'tweet.fields': 'geo',  # Get geographical info if available
    'expansions': 'geo.place_id',
    'place.fields': 'full_name'
}

# Search for tweets
response = client.search_recent_tweets(**query_params)

# Process and print the results
if response.data:
    for tweet in response.data:
        print(f'Tweet: {tweet.text}')
        if 'geo' in tweet:
            print(f'Geo data available: {tweet.geo}')
else:
    print("No tweets found with the specified query.")
