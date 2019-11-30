def test_defaults():
    from src.lib import Requests
    r = Requests(10)
    assert r._read == r._amount
