import re
import unicodedata


def is_valid_email(email: str) -> bool:
    """
    Returns True if the email is valid, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))


def slugify(text: str, separator: str = "-") -> str:
    """
    Accepts a string and returns a slugified version of the string.
    """
    text = (
        unicodedata.normalize(
            "NFKD",
            text,
        )
        .encode("ascii", "ignore")
        .decode("utf-8")
    )
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s_-]+", separator, text)
