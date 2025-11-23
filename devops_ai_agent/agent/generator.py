def generate_file(type):
    if type == "docker":
        return """
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
        """
    if type == "nginx":
        return """
server {
    listen 80;
    location / {
        proxy_pass http://flask_app:5000;
    }
}
        """
    if type == "github-actions":
        return """
name: CI

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: echo "Running tests..."
        """
    return "Unknown file type."
