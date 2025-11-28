from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db, get_current_user
from app.models.channel import Channel
from app.schemas.channel import ChannelCreate, ChannelOut, ChannelUpdate

router = APIRouter(prefix="/channels", tags=["channels"])


@router.get("/", response_model=list[ChannelOut])
async def list_channels(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Channel))
    return result.scalars().all()


@router.post("/", response_model=ChannelOut, status_code=status.HTTP_201_CREATED)
async def create_channel(channel_in: ChannelCreate, db: AsyncSession = Depends(get_db)):
    channel = Channel(**channel_in.model_dump())
    db.add(channel)
    await db.commit()
    await db.refresh(channel)
    return channel


@router.patch("/{channel_id}", response_model=ChannelOut)
async def update_channel(
    channel_id: int,
    channel_in: ChannelUpdate,
    db: AsyncSession = Depends(get_db),
    token=Depends(get_current_user),
):
    channel = await db.get(Channel, channel_id)
    if channel is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Channel not found")
    for field, value in channel_in.model_dump(exclude_none=True).items():
        setattr(channel, field, value)
    await db.commit()
    await db.refresh(channel)
    return channel


@router.delete("/{channel_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_channel(channel_id: int, db: AsyncSession = Depends(get_db)):
    channel = await db.get(Channel, channel_id)
    if channel is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Channel not found")
    await db.delete(channel)
    await db.commit()
    return None
