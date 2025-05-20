from flask import Flask, request, jsonify
import yt_dlp
import os
import re

app = Flask(__name__)

# Validasi sederhana link Instagram
def is_valid_instagram_url(url):
    return isinstance(url, str) and re.match(r"^https:\/\/(www\.)?instagram\.com\/(p|reel|tv)\/[a-zA-Z0-9_\-]+\/?", url)

@app.route("/fetch", methods=["POST"])
def fetch_video():
    data = request.get_json()
    url = data.get("url")

    if not is_valid_instagram_url(url):
        return jsonify({
            "status": "error",
            "message": "URL Instagram tidak valid atau kosong"
        }), 400

    # Periksa apakah cookies.txt tersedia
    cookie_path = "cookies.txt"
    use_cookies = os.path.isfile(cookie_path)

    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }

    if use_cookies:
        ydl_opts['cookiefile'] = cookie_path

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

            return jsonify({
                "status": "success",
                "title": info.get("title"),
                "video_url": info.get("url"),
                "thumbnail": info.get("thumbnail"),
                "duration": info.get("duration"),
                "uploader": info.get("uploader"),
            })

    except yt_dlp.utils.DownloadError as de:
        return jsonify({
            "status": "error",
            "message": "Gagal mengambil video. Instagram mungkin butuh login atau cookie sudah expired.",
            "detail": str(de)
        }), 500

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Terjadi kesalahan server",
            "detail": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
