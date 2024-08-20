from fastapi import APIRouter
from strotd.categories.schemas import SNewCategory, SCategory
from strotd.categories.dao import CategoryDAO
from fastapi_versioning import version
from strotd.exceptions import ObjectAlreadyExistsException, ObjectNotFoundException
router = APIRouter(
    tags=['Categories'],
    prefix=''
)


@router.post("/category")
@version(1)
async def post_cat(category: SNewCategory):
    cat = await CategoryDAO.find_one_or_none(name=category.name)
    if cat:
        raise ObjectAlreadyExistsException

    cat = await CategoryDAO.add(name=category.name)
    cat = SCategory.model_validate(cat).model_dump()
    return cat


@router.get("/categories")
@version(1)
async def get_cats(page: int = 1, per_page: int = 10) -> list[SCategory]:
    cats = await CategoryDAO.find_all(page=page, per_page=per_page)
    return cats


@router.delete("/category/{id}")
@version(1)
async def del_cat(id: int) -> SCategory:
    cat = await CategoryDAO.delete(id=id)
    return cat


@router.put("/category/{id}")
@version(1)
async def update_cat(cat_id: int, update_data: SNewCategory):
    cat = await CategoryDAO.find_one_or_none(id=cat_id)
    if not cat:
        raise ObjectNotFoundException

    cat = await CategoryDAO.update(cat_id, **update_data.model_dump())
    cat = SCategory.model_validate(cat).model_dump()
    return cat
