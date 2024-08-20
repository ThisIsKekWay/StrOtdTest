import pytest

from strotd.products.dao import ProductsDAO


@pytest.mark.parametrize("name, is_exists", [
    ("Product 1", True),
    ("Product 2", True),
    ("Product 11", False)
])
async def test_get_product_by_name(name, is_exists):
    prod = await ProductsDAO.find_one_or_none(name=name)

    if is_exists:
        assert prod
        print(prod)
        assert prod["name"] == name
    else:
        assert not prod


@pytest.mark.parametrize("category_id, count", [
    (1, 2),
    (2, 2),
    (5, 1)
])
async def test_get_prods_with_filter(category_id, count):
    prods = await ProductsDAO.find_all(filter={"category_id": category_id})

    assert len(prods) == count


async def test_del_upd_add_prod():
    await ProductsDAO.delete(id=1)

    prods = await ProductsDAO.find_all(filter={"category_id": 1})
    assert len(prods) == 1

    new_product = {
        'name': 'Новый продукт',
        'description': 'Новое описание',
        'price': 123.123,
        'category_id': 1
    }

    prods = await ProductsDAO.add(**new_product)
    assert prods["name"] == "Новый продукт"

    updated_product = {
        'name': 'Измененный продукт',
        'description': 'Измененное описание',
        'price': 123.321,
        'category_id': 1
    }
    prods = await ProductsDAO.update(prods["id"], **updated_product)
    assert prods["name"] == "Измененный продукт"
