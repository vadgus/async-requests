from src.request import Request


def test_ok():
    return Request().run(10)
