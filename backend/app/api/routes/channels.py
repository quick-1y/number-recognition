"""Channel CRUD routes."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException, status

from ...schemas import channel as channel_schema
from ...services.channel_service import channel_service

router = APIRouter(prefix="/channels", tags=["channels"])


@router.get("", response_model=list[channel_schema.Channel])
async def list_channels() -> list[channel_schema.Channel]:
    return channel_service.list_channels()


@router.post("", response_model=channel_schema.Channel, status_code=status.HTTP_201_CREATED)
async def create_channel(payload: channel_schema.ChannelCreate) -> channel_schema.Channel:
    return channel_service.create_channel(payload)


@router.put("/{channel_id}", response_model=channel_schema.Channel)
async def update_channel(
    channel_id: int, payload: channel_schema.ChannelUpdate
) -> channel_schema.Channel:
    try:
        return channel_service.update_channel(channel_id, payload)
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Channel not found")


@router.delete("/{channel_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_channel(channel_id: int) -> None:
    try:
        channel_service.delete_channel(channel_id)
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Channel not found")
