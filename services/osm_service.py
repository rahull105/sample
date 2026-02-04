import requests

OVERPASS_URL = "http://overpass-api.de/api/interpreter"

def get_places(lat, lng, radius, tags):
    results = []

    for tag in tags:
        query = f"""
        [out:json];
        node
          ["amenity"="{tag}"]
          (around:{radius},{lat},{lng});
        out;
        """
        response = requests.post(OVERPASS_URL, data=query)
        data = response.json()

        for el in data["elements"]:
            tags_data = el.get("tags", {})

            results.append({
                "name": tags_data.get("name"),
                "category": tag,
                "email": tags_data.get("email"),
                "phone": tags_data.get("phone"),
                "website": tags_data.get("website") or tags_data.get("contact:website"),
                "address": tags_data.get("addr:full"),
                "lat": el["lat"],
                "lon": el["lon"]
            })


    return results
