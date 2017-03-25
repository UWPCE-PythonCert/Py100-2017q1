import pytest

from SparseArray import SparseArray


@pytest.fixture(scope='function')
def my_array():
    return SparseArray([1, 2, 0, 0, 0, 0, 3, 0, 0, 4, 0, 0])


def test_array_repo(my_array):
    assert repr(my_array) == 'SparseArray([1, 2, 0, 0, 0, 0, 3, 0, 0, 4, 0, 0])'


def test_get(my_array):
    assert my_array[1] == 2
    assert my_array[3] == 0
    assert my_array[11] == 0
    with pytest.raises(IndexError):
        my_array[12]


def test_set(my_array):
    my_array[2] = 5
    assert my_array[2] == 5
    my_array[6] = 0
    assert my_array[6] == 0


def test_length(my_array):
    assert len(my_array) == 12


def test_append(my_array):
    my_array.append(5)
    assert my_array[12] == 5


def test_get_slice(my_array):
    assert my_array[0:] == [1, 2, 0, 0, 0, 0, 3, 0, 0, 4, 0, 0]
    assert my_array[:12] == [1, 2, 0, 0, 0, 0, 3, 0, 0, 4, 0, 0]
    assert my_array[:12:2] == [1, 0, 0, 3, 0, 0]
    assert my_array[0:12] == [1, 2, 0, 0, 0, 0, 3, 0, 0, 4, 0, 0]
    assert my_array[1:3] == [2, 0]


def test_set_slice(my_array):
    my_array[0:] = [1, 2, 0, 0, 0, 0, 3, 0, 0, 4, 0, 5]
    assert my_array[0:] == [1, 2, 0, 0, 0, 0, 3, 0, 0, 4, 0, 5]
    my_array[:12] = [1, 2, 0, 0, 0, 0, 3, 0, 0, 4, 0, 5]
    assert my_array[:12] == [1, 2, 0, 0, 0, 0, 3, 0, 0, 4, 0, 5]
    my_array[0:11] = [1, 2, 0, 0, 0, 0, 3, 0, 0, 4, 5]
    assert my_array[0:11] == [1, 2, 0, 0, 0, 0, 3, 0, 0, 4, 5]
    my_array[1:4] = [2, 0, 3]
    assert my_array[1:4] == [2, 0, 3]

# print(sa)
# print(len(sa))
# print(sa[9])
# sa[2] = 5
# print(sa[2])
# print(sa[1])
# sa[1] = 0
# print(sa[1])
# sa[3] = 0
# print(sa[1])
# print(sa)
# sa.append(5)
# print(sa)
# print(sa[3:])
