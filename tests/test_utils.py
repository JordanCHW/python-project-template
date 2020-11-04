from python_project_template.utils import add


def test_add():
    x = 8
    y = 9
    expected = 17
    assert add(x, y) == expected
