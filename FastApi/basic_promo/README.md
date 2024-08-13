# FastAPI Advanced Promo

Welcome to the **FastAPI Advanced Promo** repository! This project provides an advanced implementation of a promotional code generator using the FastAPI web framework. It includes enhanced features for generating promotional codes with flexible query parameters and improved configuration options.

## Overview

The FastAPI Advanced Promo application allows users to generate promotional codes for specified categories with the ability to customize the number of codes. It provides a robust and flexible API for generating promo codes, making it suitable for more complex use cases.

## Features

- Generate promo codes for specified categories with customizable quantity.
- Flexible query parameters to filter categories and control the number of codes.
- Includes enhanced error handling and detailed API responses.

## Directory Structure

```
/FastApi/advanced_promo
    /app.py
    /README.md
```
## Getting Started

1. **Clone the Repository:**
```
   git clone https://github.com/mamadceto/H-P-G-Api
```
2. **Navigate to the Project Directory:**
   `cd fastapi/advanced_promo`

3. **Install Dependencies:**
```
   pip install -r requirements.txt
```
4. **Run the Application:**
```
   uvicorn app:app --reload
```
5. **Access the API:**
   Open your web browser or API client and go to `http://localhost:8000/generate` with appropriate query parameters to generate promo codes.

## Usage

### Endpoint

- **GET** `/generate`

  This endpoint generates promo codes based on specified query parameters.

### Query Parameters

- **category**: (Optional) The category for which to generate promo codes. Options include `"train"`, `"chain"`, `"bike"`, `"clone"`, or `"all"` for all categories.
- **num**: (Optional) The number of promo codes to generate per category. Maximum is 20.

### Example Request

To generate promo codes for the `train` category with a request for 5 codes, make a GET request to:

```
http://localhost:8000/generate?category=train&num=5
```
### Example Response

The response will be a JSON object containing the generated promo codes for the requested category and the creator information:
```json
{
  "train": [
    "promoCode1",
    "promoCode2",
    "promoCode3",
    "promoCode4",
    "promoCode5"
  ],
  "Creator": "@mmdceto"
}
```
If the `category` parameter is set to `"all"`, the response will include promo codes for all categories:
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

- **Maximum Number of Codes:**
  The maximum number of codes that can be requested per category is defined by the `MAX_CODES` variable in `app.py`.

- **Category Options:**
  The available categories are predefined in the `get_app_data()` function in `app.py`.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please submit a pull request or open an issue.

## Contact

For any inquiries or feedback, please contact [@mmdceto](https://t.me/mmdceto).

