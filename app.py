from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route("/fetch", methods=["POST"])
def fetch_video():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL tidak ditemukan"}), 400

    try:
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return jsonify({
                "video_url": info.get("url"),
                "title": info.get("title"),
                "thumbnail": info.get("thumbnail"),
            })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
