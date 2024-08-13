# Flask Advanced Promo

Welcome to the **Flask Advanced Promo** repository! This project provides a more advanced implementation of a promotional code generator using the Flask web framework. It includes enhanced features such as the ability to specify categories and the number of codes to generate.

## Overview

The Flask Advanced Promo application allows users to generate promotional codes for specific categories of games and customize the number of codes generated. This more advanced setup provides flexibility and control over the promo code generation process.

## Features

- Generate promo codes for a specific category or all categories.
- Specify the number of promo codes to generate (up to a maximum limit).
- Provides detailed error handling and responses.
- Ideal for use cases requiring more control and customization.

## Directory Structure

```
/Flask/advanced_promo
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
   cd flask/advanced_promo
```
3. **Install Dependencies:**
```
   pip install -r requirements.txt
```
4. **Run the Application:**
```
   python app.py
```
5. **Access the API:**
   Open your web browser or API client and go to `http://localhost:5000/generate` to generate promo codes.

## Usage

### Endpoint

- **GET** `/generate`

  This endpoint generates promo codes based on the specified category and number of codes.

### Query Parameters

- **`category`** (optional): The category for which to generate promo codes (e.g., `train`, `chain`, `bike`, `clone`). If not specified, generates codes for all categories.
- **`num`** (optional): The number of promo codes to generate per category (default is 4, with a maximum of 20).

### Example Request

To generate 5 promo codes for the `train` category, make a GET request to:
```
http://localhost:5000/generate?category=train&num=5
```
### Example Response

The response will be a JSON object containing the generated promo codes for the specified category or all categories, as well as the creator information:
```json
{
  "train": [
    "promoCode1",
    "promoCode2",
    "promoCode3",
    "promoCode4",
    "promoCode5"
  ],
  "chain": [
    "promoCode6",
    "promoCode7",
    "promoCode8",
    "promoCode9",
    "promoCode10"
  ],
  "bike": [
    "promoCode11",
    "promoCode12",
    "promoCode13",
    "promoCode14",
    "promoCode15"
  ],
  "clone": [
    "promoCode16",
    "promoCode17",
    "promoCode18",
    "promoCode19",
    "promoCode20"
  ],
  "Creator": "@mmdceto"
}
```
## Configuration

- **Number of Codes per Category:**
  You can modify the maximum number of codes that can be generated per category by changing the `MAX_CODES` variable in `app.py`.

- **Category Options:**
  The available categories are predefined in the `get_app_data()` function in `app.py`.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please submit a pull request or open an issue.

## Contact

For any inquiries or feedback, please contact [@mmdceto](https://t.me/mmdceto).

