# FastAPI Basic Promo

Welcome to the **FastAPI Basic Promo** repository! This project provides a basic implementation of a promotional code generator using the FastAPI web framework. It is designed to generate promotional codes for various categories with a simple setup and minimal configuration.

## Overview

The FastAPI Basic Promo application allows users to generate promotional codes for all predefined categories of games. This basic setup is straightforward and provides an easy way to generate promo codes with minimal configuration.

## Features

- Generate promo codes for all predefined categories.
- Simple and easy to set up and use.
- Provides basic error handling and responses.

## Directory Structure

```
/FastApi/basic_promo
    /app.py
    /README.md
```
## Getting Started

1. **Clone the Repository:**
```
   git clone https://github.com/mamadceto/H-P-G-Api
```
2. **Navigate to the Project Directory:**
```
   cd fastapi/basic_promo
```
3. **Install Dependencies:**
```
   pip install -r requirements.txt
```
4. **Run the Application:**
```
   uvicorn app:app --reload
```
5. **Access the API:**
   Open your web browser or API client and go to `http://localhost:8000/generate` to generate promo codes.

## Usage

### Endpoint

- **GET** `/generate`

  This endpoint generates promo codes for all predefined categories.

### Example Request

To generate promo codes, make a GET request to:
```
http://localhost:8000/generate
```
### Example Response

The response will be a JSON object containing the generated promo codes for each category, as well as the creator information:
```json
{
  "train": [
    "promoCode1",
    "promoCode2",
    "promoCode3",
    "promoCode4"
  ],
  "chain": [
    "promoCode5",
    "promoCode6",
    "promoCode7",
    "promoCode8"
  ],
  "bike": [
    "promoCode9",
    "promoCode10",
    "promoCode11",
    "promoCode12"
  ],
  "clone": [
    "promoCode13",
    "promoCode14",
    "promoCode15",
    "promoCode16"
  ],
  "Creator": "@mmdceto"
}
```
## Configuration

- **Number of Codes per Category:**
  The number of codes generated per category is defined by the `num_codes_per_category` variable in `app.py`. You can modify this value if needed.

- **Category Options:**
  The available categories are predefined in the `get_app_data()` function in `app.py`.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please submit a pull request or open an issue.

## Contact

For any inquiries or feedback, please contact [@mmdceto](https://t.me/mmdceto).

