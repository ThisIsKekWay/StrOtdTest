import pytest

from strotd.categories.dao import CategoryDAO


@pytest.mark.parametrize("name, is_exists", [
    ("Зачем", True),
    ("Попил", True),
    ("Кто не даст нормальную обратную связь тот лох", False)
])
async def test_get_category(name, is_exists):
    cat = await CategoryDAO.find_one_or_none(name=name)

    if is_exists:
        assert cat
        assert cat["name"] == name
    else:
        assert not cat


async def test_get_categories():
    cat = await CategoryDAO.find_all()
    assert len(cat) == 7


async def test_add_and_delete_category():
    cat = await CategoryDAO.add(name="Новая категория")
    assert cat
    print(cat)
    assert cat["name"] == "Новая категория"

    cat = await CategoryDAO.delete(name="Новая категория")

    cats = await CategoryDAO.find_all()
    assert len(cats) == 7


