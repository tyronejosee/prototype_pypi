from utils_funcs.functions import is_valid_email, slugify


def test_is_valid_email():
    assert is_valid_email("test@example.com")
    assert is_valid_email("user.name+tag@sub.domain.co.uk")
    assert not is_valid_email("invalid-email")
    assert not is_valid_email("missing@domain")
    assert not is_valid_email("missing@.com")
    assert not is_valid_email("@missingusername.com")


def test_slugify():
    assert slugify("Hello World!") == "hello-world"
    assert slugify("Python & Django") == "python-django"
    assert slugify("Café del Mar") == "cafe-del-mar"
    assert slugify("multiple    spaces") == "multiple-spaces"
    assert slugify("under_scores", "_") == "under_scores"
    assert slugify("mix-of-separators", "_") == "mix_of_separators"
