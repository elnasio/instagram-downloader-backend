# 📥 Instagram Video Downloader API

A lightweight and private backend built with **Flask + yt-dlp** to fetch direct video URLs from public Instagram posts and reels.  
Perfect for integrating into your own apps without relying on public third-party services.

---

## 🚀 Features

✅ Extract direct video URL from Instagram link  
✅ Built using [yt-dlp](https://github.com/yt-dlp/yt-dlp)  
✅ Simple Flask API  
✅ No need for login or Instagram API  
✅ Ready for integration with mobile apps (Flutter, React Native, etc.)

---

## 📦 Requirements

- Python 3.8+
- pip
- `yt-dlp` (auto-installed via `requirements.txt`)

---

## 🛠️ Setup (MacOS/Linux)

```bash
# Clone this repo
git clone https://github.com/yourusername/instagram-downloader-backend.git
cd instagram-downloader-backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
