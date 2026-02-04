from flask import Flask, render_template, request
from services.geoapify_service import get_nearby_places
import math

app = Flask(__name__)

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * \
        math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    return round(R * (2 * math.atan2(math.sqrt(a), math.sqrt(1-a))), 2)

@app.route("/")
def index():
    lat = request.args.get("lat", type=float)
    lon = request.args.get("lon", type=float)
    radius = request.args.get("radius", 3000, type=int)

    CATEGORY_GROUPS = {
        "Healthcare": ["healthcare.hospital", "healthcare.clinic"],
        "Education": ["education.school", "education.college"],
        "Food & Dining": ["catering.restaurant", "catering.cafe"],
        "Business": ["commercial.office"]
    }

    if not lat or not lon:
        return render_template(
            "index.html",
            results=[],
            categories=CATEGORY_GROUPS.keys(),
            radius=radius
        )

    results = []

    for group, cats in CATEGORY_GROUPS.items():
        places = get_nearby_places(lat, lon, radius, cats)
        for p in places:
            results.append({
                "name": p["name"],
                "group": group,
                "phone": p.get("phone"),
                "lat": p["lat"],
                "lon": p["lon"],
                "distance": calculate_distance(lat, lon, p["lat"], p["lon"])
            })

    return render_template(
        "index.html",
        results=results,
        categories=CATEGORY_GROUPS.keys(),
        radius=radius
    )

if __name__ == "__main__":
    app.run(debug=True)
