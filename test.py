from lib import Requests


def test_defaults():
    r = Requests(10)
    assert r._read == r._amount
