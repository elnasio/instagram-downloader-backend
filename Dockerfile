# Gunakan base image python
FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Salin file
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file lain
COPY . .

# Expose port Flask
EXPOSE 5000

# Jalankan app via gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
