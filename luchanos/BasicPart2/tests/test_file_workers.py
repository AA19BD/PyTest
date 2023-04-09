import pytest

from luchanos.BasicPart2.my_functions.file_workers import read_from_file


def create_test_data(test_data):
    with open("test_file.txt", "a") as f:
        f.writelines(test_data)


@pytest.mark.parametrize('test_data',[(['one\n', 'two\n', 'three\n', 'four\n', 'five\n', 'six\n', 'seven\n']),
                                  (['one\n', 'two\n', 'three\n'])])
def test_read_from_file3(test_data) -> None:
    create_test_data(test_data)
    assert read_from_file("test_file.txt") == test_data


def test_read_from_file() -> None:
    test_data = ['one\n', 'two\n', 'three\n']
    create_test_data(test_data)
    assert read_from_file("test_file.txt") == test_data


def test_read_from_file2() -> None:
    test_data = ['one\n', 'two\n', 'three\n', 'four\n', 'five\n', 'six\n']
    create_test_data(test_data)
    assert read_from_file("test_file.txt") == test_data
