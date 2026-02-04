import requests

GEOAPIFY_API_KEY = "256f061ce0084a45b5cf289e6b9ffc08"

def get_nearby_places(lat, lon, radius, categories):
    results = []

    for category in categories:
        url = "https://api.geoapify.com/v2/places"

        params = {
            "categories": category,
            "filter": f"circle:{lon},{lat},{radius}",
            "limit": 50,
            "apiKey": GEOAPIFY_API_KEY
        }

        response = requests.get(url, params=params,timeout=10)
        data = response.json()

        for place in data.get("features", []):
            props = place.get("properties", {})

            results.append({
                "name": props.get("name"),
                "category": category,
                "phone": props.get("phone"),
                "website": props.get("website"),
                "address": props.get("formatted"),
                "lat": props.get("lat"),
                "lon": props.get("lon")
            })

    return results
