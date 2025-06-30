from flask import jsonify
import requests
import os

def register_image_routes(app):
    UNSPLASH_ACCESS_KEY = os.getenv("unGYk1Aq4QPCkCTpNpz6uVkkazG1xKc3b_o4uUBPNKU")

    @app.route("/api/fashion-images", methods=["GET"])
    def get_fashion_images():
        if not UNSPLASH_ACCESS_KEY:
            return jsonify({"error": "Missing Unsplash access key"}), 500

        try:
            url = "https://api.unsplash.com/search/photos"
            params = {
                "query": "fashion",
                "per_page": 12,
                "client_id": 'unGYk1Aq4QPCkCTpNpz6uVkkazG1xKc3b_o4uUBPNKU'
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            images = [
                {
                    "id": img["id"],
                    "url": img["urls"]["regular"],
                    "description": img["alt_description"],
                    "photographer": img["user"]["name"],
                    "photographer_url": img["user"]["links"]["html"]
                }
                for img in data.get("results", [])
            ]

            return jsonify(images)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
