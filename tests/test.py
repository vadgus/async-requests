def test_defaults():
    from src.request import Request
    r = Request(10)
    assert r._read == r._amount
