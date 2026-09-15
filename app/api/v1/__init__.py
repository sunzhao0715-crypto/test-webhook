from app.api.v1.endpoints import health, items
from fastapi import APIRouter

router = APIRouter()
router.include_router(health.router, tags=["健康检查"])
router.include_router(items.router, tags=["商品管理"])