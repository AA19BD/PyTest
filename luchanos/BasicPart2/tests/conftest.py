import pytest


@pytest.fixture(autouse=True)
def clean_txt_file() -> None:
    with open("test_file.txt", "w"):
        pass
