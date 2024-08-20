from fastapi import APIRouter, HTTPException, Depends
from fastapi_versioning import version
from strotd.products.dao import ProductsDAO
from strotd.products.schemas import SNewProduct, SProduct, SProductFilter
from strotd.exceptions import ObjectNotFoundException

router = APIRouter(
    tags=['Products'],
    prefix=''
)


@router.get("/products")
@version(1)
async def get_prods(
        filter: SProductFilter = Depends(),
        page: int = 1,
        per_page: int = 10
) -> list[SProduct]:
    prod = await ProductsDAO.find_all(page=page, per_page=per_page, filter=filter.model_dump())
    return prod


@router.get("/product/{id}")
@version(1)
async def get_prod_by_id(prod_id: int):
    prod = await ProductsDAO.find_one_or_none(id=prod_id)
    if not prod:
        raise ObjectNotFoundException

    prod = SProduct.model_validate(prod).model_dump()
    return prod


@router.post("/product")
@version(1)
async def post_prod(product: SNewProduct):
    prod = await ProductsDAO.add(
        name=product.name,
        description=product.description,
        price=product.price,
        category_id=product.category_id,
    )
    prod = SProduct.model_validate(prod).model_dump()
    return prod


@router.put("/product/{id}")
@version(1)
async def update_product(product_id: int, update_data: SNewProduct):
    existing_product = await ProductsDAO.find_one_or_none(id=product_id)

    if existing_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    updated_prod = await ProductsDAO.update(product_id, **update_data.model_dump())
    updated_prod = SProduct.model_validate(updated_prod).model_dump()
    return updated_prod


@router.delete('/product/{id}')
@version(1)
async def delete_product(prod_id: int):
    prod = await ProductsDAO.find_one_or_none(id=prod_id)
    if not prod:
        raise ObjectNotFoundException

    prod = await ProductsDAO.delete(id=prod_id)
    return prod
