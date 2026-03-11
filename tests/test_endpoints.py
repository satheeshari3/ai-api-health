def test_url_validation():
    from backend.utils.validator import is_valid_url

    assert is_valid_url("https://google.com")
    assert not is_valid_url("invalid-url")