from open_file import read_from_file
import pytest
import io


DATA = """\
line 1
line 2
line 3
"""


def test_read_from_file(mocker):
    mocker.patch(
        "builtins.open",
        return_value=io.StringIO(DATA)
    )  
    lines = read_from_file("file.txt")
    print(F"Type is {type(lines)}")
    assert lines[0] == "line 1\n"
    assert lines[1] == "line 2\n"
    assert lines[2] == "line 3\n"