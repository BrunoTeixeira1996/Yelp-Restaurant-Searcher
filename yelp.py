import requests, sys, json

if len(sys.argv) < 2:
    print("Usage: yelp.py City name")
    sys.exit()

city = ' '.join(sys.argv[1:])
key = "YOURKEY"
url = "https://api.yelp.com/v3/businesses/search?location=%s" % (city)
header = {"Authorization":"Bearer %s" %key}
data = requests.get(url, headers=header).json()

for i in data['businesses']:
    rating = i['rating']
    phone = i['phone']
    name = i['name']
    city = i['location']['city']
    country = i ['location']['country']
    address = i ['location']['address1']
    food = i['categories'][0]['title']
    count = i['review_count']
    print("\nName:",name)
    print("Food:",food)
    print("Rating:",rating)
    print("City:",city,country)
    print("Phone:",phone)
    print("Address:",address)
    print("This business has:",count, "reviews")
