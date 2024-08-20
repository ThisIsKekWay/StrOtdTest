from fastapi import FastAPI
from strotd.categories.routers import router as categories_router
from strotd.products.routers import router as products_router
from fastapi_versioning import VersionedFastAPI

app = FastAPI(
    title="Управление продуктами",
    root_path="/api"
)


app.include_router(categories_router)
app.include_router(products_router)
app = VersionedFastAPI(
    app=app,
    version_format='{major}',
    prefix_format='/api/v{major}',
)
