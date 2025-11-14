"""Plate list management service."""
from __future__ import annotations

from collections import OrderedDict

from ..schemas import plate_list as list_schema


class PlateListService:
    def __init__(self) -> None:
        self._lists: "OrderedDict[int, list_schema.PlateList]" = OrderedDict()
        self._counter = 0
        self._item_counter = 0

    def list_lists(self) -> list[list_schema.PlateList]:
        return list(self._lists.values())

    def create_list(self, payload: list_schema.PlateListCreate) -> list_schema.PlateList:
        self._counter += 1
        items = []
        if payload.items:
            for item in payload.items:
                self._item_counter += 1
                items.append(list_schema.PlateListItem(id=self._item_counter, **item.model_dump()))
        plate_list = list_schema.PlateList(id=self._counter, items=items, **payload.model_dump(exclude={"items"}))
        self._lists[self._counter] = plate_list
        return plate_list

    def get_list(self, list_id: int) -> list_schema.PlateList:
        plate_list = self._lists.get(list_id)
        if not plate_list:
            raise KeyError(list_id)
        return plate_list


plate_list_service = PlateListService()
