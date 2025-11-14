"""Plate lists endpoints."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException, status

from ...schemas import plate_list as list_schema
from ...services.list_service import plate_list_service

router = APIRouter(prefix="/lists", tags=["lists"])


@router.get("", response_model=list[list_schema.PlateList])
async def list_plate_lists() -> list[list_schema.PlateList]:
    return plate_list_service.list_lists()


@router.post("", response_model=list_schema.PlateList, status_code=status.HTTP_201_CREATED)
async def create_plate_list(payload: list_schema.PlateListCreate) -> list_schema.PlateList:
    return plate_list_service.create_list(payload)


@router.get("/{list_id}", response_model=list_schema.PlateList)
async def get_plate_list(list_id: int) -> list_schema.PlateList:
    try:
        return plate_list_service.get_list(list_id)
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="List not found")
