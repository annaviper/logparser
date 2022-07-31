from src.funcs import (
    read_file,
    list_hostnames
)
import pytest

FILE_PATH = r'tests\assets\input-file.txt'


class TestReadFile:
    def test_exception(self):
        with pytest.raises(TypeError):
            read_file(0)

    def test_success(self):
        doc = read_file(FILE_PATH)
        assert len(doc) > 0


@pytest.mark.parametrize('init, end, hostname, expected', [
    (1565647204351, 1565647247170, 'Matina', ['Aadvik', 'Jeremyah']),
    (1565647204351, 1565647247170, 'Eron', ['Heera']),
    (1565647205599, 1565647246869, 'NonExistentHostName', []),
])
def test_list_hostnames(init, end, hostname, expected):
    output = list_hostnames(FILE_PATH, init, end, hostname)
    assert output == expected
