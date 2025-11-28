from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.models.recognition import Recognition
from app.schemas.recognition import RecognitionCreate, RecognitionOut

router = APIRouter(prefix="/recognitions", tags=["recognitions"])


@router.get("/", response_model=list[RecognitionOut])
async def list_recognitions(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Recognition).order_by(Recognition.timestamp.desc()).limit(100))
    return result.scalars().all()


@router.post("/", response_model=RecognitionOut, status_code=status.HTTP_201_CREATED)
async def register_recognition(payload: RecognitionCreate, db: AsyncSession = Depends(get_db)):
    event = Recognition(**payload.model_dump())
    db.add(event)
    await db.commit()
    await db.refresh(event)
    return event
