from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.models.plate_list import PlateList
from app.models.plate_list_item import PlateListItem
from app.schemas.plate_list import PlateListCreate, PlateListOut

router = APIRouter(prefix="/plate-lists", tags=["lists"])


@router.get("/", response_model=list[PlateListOut])
async def list_plate_lists(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PlateList))
    return result.scalars().unique().all()


@router.post("/", response_model=PlateListOut, status_code=status.HTTP_201_CREATED)
async def create_plate_list(list_in: PlateListCreate, db: AsyncSession = Depends(get_db)):
    plate_list = PlateList(**list_in.model_dump(exclude={"items"}))
    db.add(plate_list)
    await db.flush()
    for item in list_in.items:
        db_item = PlateListItem(**item.model_dump(), plate_list=plate_list)
        db.add(db_item)
    await db.commit()
    await db.refresh(plate_list)
    return plate_list


@router.get("/{list_id}", response_model=PlateListOut)
async def get_plate_list(list_id: int, db: AsyncSession = Depends(get_db)):
    plate_list = await db.get(PlateList, list_id)
    if plate_list is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="List not found")
    return plate_list
