# Flask Promo Code Generator

## Overview

This is a Flask API for generating promotional codes using an external service. The application is deployed with Gunicorn for production.

## Prerequisites

- Python 3.9 or later
- Access to a Linux server or cPanel with SSH access

## Installation

### On a Linux Server

1. **Connect to Your Server**

   Use SSH to connect to your server.

2. **Install Python and Dependencies**

   Make sure Python 3.9 is installed. If not, install it using your package manager. For example, on Debian-based systems:
```   
sudo apt update   
sudo apt install python3.9
```
3. **Clone the Repository**

   Clone the repository to your desired directory:
```
git clone https://github.com/yourusername/yourrepository.git  
cd Flask/basic_promo/Server
```
4. **Set Up a Virtual Environment**

   Create and activate a virtual environment:
```
python3.9 -m venv venv
source venv/bin/activate
```
5. **Install Required Packages**

   Install the necessary Python packages:
```
pip install -r requirements.txt
```
6. **Run the Application**

   Use `gunicorn` to start the application:
```
gunicorn --workers=3 --bind 0.0.0.0:5000 --timeout 1200 app:app
```
## On cPanel Hosting

1. **Setup Python App**

   - Log in to your cPanel account.
   - Navigate to **Setup Python App**.
   - Select the latest Python version available.
   - Set the **Application root** to the project directory (e.g., `Api-Promo`).
   - Click **Create Application**.

2. **Upload the Application Code**

   - Open **File Manager** in cPanel.
   - Locate the directory with the same name as the application you just created (e.g., `Api-Promo`).
   - Enter the `public` folder inside this directory.
   - Upload the `app.py` file into the `public` folder.

3. **Install Dependencies**

   - Open **Terminal** in cPanel.
   - Enter the virtual environment with the command provided in the **Python App** setup page.
   - Navigate to the `public` folder:
```
cd public
```
   - Install the required Python packages:
```
pip install -r requirements.txt
```
4. **Run the Application**

   - In the Terminal, start the application with:
```
   gunicorn --workers=3 --bind 0.0.0.0:5000 --timeout 1200 app:app
```
## Usage

Access the API endpoint to generate promotional codes:
```
http://your-domain:5000/generate
```
This endpoint will return generated codes in JSON format.

