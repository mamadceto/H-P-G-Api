# Promo Code Generator

Welcome to the **Promo Code Generator** repository! This project features implementations of promotional code generators using two popular Python frameworks: **Flask** and **FastAPI**. It includes both basic and advanced versions of the generator to accommodate different use cases.

## Overview

The Promo Code Generator enables you to create promotional codes for various categories of games. The project is divided into two main frameworks, each with two versions:

- **Flask**: A micro web framework for Python.
  - **Basic Promo**: Generates a fixed number of promo codes for each category.
  - **Advanced Promo**: Provides customizable parameters for generating promo codes.

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
  - **Basic Promo**: Generates a fixed number of promo codes for each category.
  - **Advanced Promo**: Allows for flexible API queries to customize the number of promo codes.

## Features

- **Basic Promo**:
  - Generates a predetermined number of promo codes for each category.
  - Simple and easy-to-use implementation.

- **Advanced Promo**:
  - Allows for the customization of the number of promo codes generated.
  - Supports query parameters for filtering and adjusting the output.
  - Includes enhanced error handling and validation.

## Directory Structure

/project-root
    /flask
        /basic_promo
            /app.py
            /README.md
        /advanced_promo
            /app.py
            /README.md
    /fastapi
        /basic_promo
            /app.py
            /README.md
        /advanced_promo
            /app.py
            /README.md
    README.md

## Getting Started

1. **Clone the Repository:**
   git clone https://github.com/your-username/promo-code-generator.git

2. **Navigate to the Desired Framework and Version:**
   cd flask/basic_promo   # or flask/advanced_promo
   # or
   cd fastapi/basic_promo  # or fastapi/advanced_promo

3. **Install Dependencies:**
   pip install -r requirements.txt

4. **Run the Application:**
   - **Flask:**
     python app.py
   - **FastAPI:**
     uvicorn app:app --reload

5. **Access the API:**
   - **Flask:** http://localhost:5000/generate
   - **FastAPI:** http://localhost:8000/generate

## API Usage

- **Basic Promo**: Generates a fixed number of promo codes (default: 4) for each category.
- **Advanced Promo**: Customize the number of promo codes and category using query parameters:
  - `category` (optional): Specify a category such as `train`, `chain`, `bike`, or `clone`. To generate codes for all categories, use `all`.
  - `num` (optional): Specify the number of promo codes to generate. Maximum allowed is 20.

## Links

- [Flask Basic Promo README](flask/basic_promo/README.md)
- [Flask Advanced Promo README](flask/advanced_promo/README.md)
- [FastAPI Basic Promo README](fastapi/basic_promo/README.md)
- [FastAPI Advanced Promo README](fastapi/advanced_promo/README.md)

## Contributing

Feel free to fork the repository, make changes, and submit pull requests. We welcome contributions that enhance the functionality and usability of the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please open an issue on the repository or contact us at [your-email@example.com].
