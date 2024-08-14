# Advanced Promo Code Generator

This is an advanced Python application that generates promo codes for various categories. The application uses Flask for the web framework and Gunicorn for serving the application in a production environment.

## Features

- **Generate Promo Codes**: Generates promo codes for specified categories.
- **Flexible Requests**: Allows for customization of the number of codes to be generated.
- **Concurrency**: Uses threading to handle multiple requests efficiently.

## Prerequisites

- **Python**: Version 3.9 or later
- **Gunicorn**: A WSGI HTTP server for running the Flask app
- **Flask**: A lightweight WSGI web application framework

## Installation

### 1. Clone the Repository

First, clone the repository to your local machine:

    git clone <repository-url>
    cd advanced_promo

### 2. Set Up a Virtual Environment

Create and activate a virtual environment:

    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

### 3. Install Dependencies

Install the required packages from `requirements.txt`:

    pip install -r requirements.txt

## Configuration

### Environment Variables

Ensure the following environment variables are set:

- **FLASK_ENV**: Set to `development` for local development or `production` for deployment.

## Running the Application

### Local Development

To run the application locally, use Flask's built-in server:

    flask run --host=0.0.0.0 --port=5000

### Production Deployment with Gunicorn

To run the application in a production environment, use Gunicorn:

    gunicorn --workers=3 --bind 0.0.0.0:5000 --timeout 1200 app:app

## API Endpoints

### Generate Promo Codes

**Endpoint**: `/generate`

**Method**: `GET`

**Parameters**:

- `category` (optional): The category for which to generate promo codes. Can be one of the following: `train`, `chain`, `bike`, `clone`, or `all`.
- `num` (optional): The number of promo codes to generate per category (default: 4, max: 20).

**Example Request**:

    curl "http://localhost:5000/generate?category=train&num=5"

**Response**:

    {
      "codes": {
        "train": ["promo_code_1", "promo_code_2", "promo_code_3", "promo_code_4", "promo_code_5"],
        "chain": ["promo_code_6", "promo_code_7", "promo_code_8", "promo_code_9", "promo_code_10"],
        "bike": ["promo_code_11", "promo_code_12", "promo_code_13", "promo_code_14", "promo_code_15"],
        "clone": ["promo_code_16", "promo_code_17", "promo_code_18", "promo_code_19", "promo_code_20"]
      },
      "Creator": "@mmdceto"
    }

## Troubleshooting

### Common Issues

1. **Port Already in Use**

   If you encounter an error indicating that the port is already in use, you may need to stop the existing process or use a different port.

    sudo lsof -i :5000  # Find the process using the port
    sudo kill -9 <PID>  # Replace <PID> with the process ID

2. **Werkzeug Import Errors**

   If you encounter import errors related to Werkzeug, ensure that you are using compatible versions of Flask and Werkzeug. You can specify the required versions in `requirements.txt`.

    pip install "werkzeug==2.0.0"  # Example version, adjust as needed

### Logs

Check Gunicorn and Flask logs for additional information on errors and application behavior.

## cPanel Hosting

### 1. Setup Python App

- Go to **Setup Python App** on your cPanel.
- Select the latest Python version.
- Set the application root to the project directory.
- Click **Create Application**.

### 2. Upload Files

- Go to **File Manager** and locate the created application directory.
- Open the directory and navigate to the `public` folder.
- Upload `app.py` and other required files to the `public` folder.

### 3. Install Dependencies

- Open the terminal in cPanel.
- Enter the virtual environment with the command provided on the Python App setup page.
- Run the following commands:
```
cd public
pip install -r requirements.txt
```
### 4. Run Gunicorn

- Run the following command to start the application:
```
gunicorn --workers=3 --bind 0.0.0.0:5000 --timeout 1200 app:app
```
## Acknowledgements

- Flask
- Gunicorn
- Werkzeug

