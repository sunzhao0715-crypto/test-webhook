from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "ok", "message": "Backend is running"}


@router.get("/ping")
async def ping():
    return {"ping": "pong"}