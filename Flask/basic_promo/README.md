# Flask Basic Promo

Welcome to the **Flask Basic Promo** repository! This project provides a simple implementation of a promotional code generator using the Flask web framework. It generates a fixed number of promo codes for each category.

## Overview

The Flask Basic Promo application is designed to create promotional codes for various categories of games. It provides a straightforward API endpoint to generate a set number of codes for each category.

## Features

- Generates a fixed number of promo codes for each category (default: 4).
- Simple and easy-to-use implementation.
- Ideal for basic use cases where no additional customization is needed.

## Directory Structure
```
/Flask/basic_promo
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
   cd flask/basic_promo
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

  This endpoint generates promo codes for all predefined categories.

### Example Request

To generate promo codes for all categories, you can make a GET request to:

`http://localhost:5000/generate`

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
  You can modify the number of codes generated per category by changing the `num_codes_per_category` variable in `app.py`.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please submit a pull request or open an issue.

## Contact

For any inquiries or feedback, please contact [@mmdceto](https://t.me/mmdceto).

