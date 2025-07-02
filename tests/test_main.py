import pytest
from square import solution
from vote import vote
from shelves import Shelves


@pytest.mark.parametrize(
    'a, b, c, expected',
    [
        (1, 8, 15, (-3.0, -5.0)),
        (1, -13, 12, (12.0, 1.0)),
        (-4, 28, -49, 3.5),
        (1, 1, 1, 'There are no roots')
    ]
)
def test_solution(a, b, c, expected):
    assert solution(a, b, c) == expected


@pytest.mark.parametrize(
    'a, b, c, d, e, expected',
    [
        (1, 1, 1, 2, 3, 1),
        (1, 2, 3, 2, 2, 2),
        (4, 4, 5, 4, 1, 4)
    ]
)
def test_vote(a, b, c, d, e, expected):
    assert vote([a, b, c, d, e]) == expected


@pytest.fixture
def create_shelves():
    shelves = Shelves()
    shelves.make_dir('1', '')
    shelves.make_dir('2', '')
    shelves.make_dir('3', '')
    shelves.add('passport', '2207 876234', 'Василий Гупкин', 1)
    shelves.add('invoice', '11-2', 'Геннадий Покемонов', 1)
    shelves.add('insurance', '10006', 'Аристарх Павлов', 2)
    shelves.add('driver license', '5455 028765', 'Василий Иванов', 1)
    return shelves


def test_create_empty_shelves():
    shelves = Shelves()
    assert len(shelves.get_all_notes()) == 0


def test_create_docs(create_shelves):
    shelves = create_shelves
    assert len(shelves.get_all_notes()) == 4


def test_add_document(create_shelves):
    shelves = create_shelves
    shelves.add('international passport', '311 020203', 'Александр Пушкин', 3)
    assert len(shelves.get_all_notes()) == 5


def test_exist_note(create_shelves):
    shelves = create_shelves
    assert shelves.get_name("10006") == 'Аристарх Павлов'


def test_find_non_exist_note(create_shelves):
    shelves = create_shelves
    assert shelves.get_name('123456') == 'Документ не найден'
