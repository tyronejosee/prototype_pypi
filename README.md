# **Utils Funcs**

A collection of reusable functions that simplify common tasks and frequent operations within the project. These functions are designed to improve
development efficiency by providing simple and effective solutions for tasks like data manipulation, validations, and transformations.

## ✨ **Features**

- **`is_valid_email(email: str) -> bool`**: Validates if the provided email is in a correct format.
- **`slugify(text: str, separator: str = "-") -> str`**: Converts a string into a slugified format, suitable for URLs.

## 📦 **Installation**

You can install this package via pip:

```bash
pip install utils_funcs
```

## 🚀 **Usage**

### `is_valid_email`

This function checks if an email is valid according to a standard regex pattern.

```python
from your_package import is_valid_email

email = "example@example.com"
is_valid = is_valid_email(email)

print(is_valid)  # True if the email is valid, False otherwise
```

### `slugify`

This function converts a given string into a slugified format, which is useful for generating clean URLs. You can also specify a custom separator (default is `-`).

```python
from utils_funcs import slugify

text = "This is an Example Title!"
slug = slugify(text)

print(slug)  # Output: "this-is-an-example-title"
```

## 🤝 **Contributing**

Contributions are welcome! If you find any issues or would like to add new features, feel free to fork the repository and submit a pull request.

## ⚖️ **License**

This project is licensed under the MIT License - see the `LICENSE` file for details.
