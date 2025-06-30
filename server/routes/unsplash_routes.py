# server/routes/unsplash_routes.py
import os
import requests
from flask import Blueprint, jsonify

unsplash_bp = Blueprint('unsplash', __name__)

@unsplash_bp.route('/fashion-images', methods=['GET'])
def get_fashion_images():
    access_key = os.getenv('UNSPLASH_ACCESS_KEY')

    if not access_key:
        return jsonify({'error': 'Missing Unsplash access key'}), 500

    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": "fashion",
        "client_id": access_key,
        "per_page": 12
    }

    res = requests.get(url, params=params)
    if res.status_code != 200:
        return jsonify({'error': 'Failed to fetch from Unsplash'}), res.status_code

    results = [
        {
            "id": photo["id"],
            "url": photo["urls"]["regular"],
            "photographer": photo["user"]["name"],
            "photographer_url": photo["user"]["links"]["html"],
            "description": photo.get("description") or photo.get("alt_description") or "Fashion Item"
        }
        for photo in res.json().get("results", [])
    ]

    return jsonify(results)
