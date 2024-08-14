# Flask Promo Code Generator

## Overview

This is a Flask API for generating promotional codes using an external service. The application is deployed with Gunicorn for production.

## Prerequisites

- Python 3.9 or later
- Access to a Linux server or cPanel with SSH access

## Installation and Setup

### On a Linux Server

1. **Clone the Repository**

   Run:
```
git clone https://github.com/username/repository.git
cd repository/Flask/basic_promo/Server
```
2. **Create and Activate a Virtual Environment**

   Run:
```
python3 -m venv venv
source venv/bin/activate
```
3. **Install Dependencies**

   Run:
```
pip install -r requirements.txt
```
4. **Run the Application with Gunicorn**

   Run:

```
gunicorn --workers=3 --bind 0.0.0.0:5000 --timeout 1200 app:app
```
   - `--workers=3`: Number of worker processes
   - `--bind 0.0.0.0:5000`: Address and port
   - `--timeout 1200`: Request timeout in seconds

### On cPanel Hosting

1. **Access SSH**

   Use SSH to connect to your cPanel account.

2. **Clone the Repository**

   Run:
```
git clone https://github.com/username/repository.git
cd repository/Flask/basic_promo/Server
```
3. **Create and Activate a Virtual Environment**

   Run:
```
python3 -m venv venv
source venv/bin/activate
```
4. **Install Dependencies**

   Run:
```
pip install -r requirements.txt
```
5. **Configure Python App in cPanel**

   - Go to "Setup Python App" in cPanel.
   - Set Python version to 3.9 or later.
   - Set the application root to the project directory.
   - Set "Startup File" to `app:app`.
   - Click "Setup".

## `requirements.txt`

Create this file with the following content:
```
Flask==2.2.0
requests==2.28.1
gunicorn==23.0.0
```
## Usage

Access the API endpoint to generate promotional codes:

`http://your-domain:5000/generate`

This endpoint will return generated codes in JSON format.

## Troubleshooting

If you encounter issues, ensure all dependencies are installed correctly and check the server logs for errors.

