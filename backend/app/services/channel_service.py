"""In-memory channel service used for prototyping and tests."""
from __future__ import annotations

from collections import OrderedDict
from typing import Dict

from ..schemas import channel as channel_schema


class ChannelService:
    """Simple channel service storing data in memory."""

    def __init__(self) -> None:
        self._channels: "OrderedDict[int, channel_schema.Channel]" = OrderedDict()
        self._counter: int = 0

    def list_channels(self) -> list[channel_schema.Channel]:
        return list(self._channels.values())

    def create_channel(self, payload: channel_schema.ChannelCreate) -> channel_schema.Channel:
        self._counter += 1
        channel = channel_schema.Channel(id=self._counter, **payload.model_dump())
        self._channels[channel.id] = channel
        return channel

    def get_channel(self, channel_id: int) -> channel_schema.Channel:
        channel = self._channels.get(channel_id)
        if not channel:
            raise KeyError(channel_id)
        return channel

    def update_channel(
        self, channel_id: int, payload: channel_schema.ChannelUpdate
    ) -> channel_schema.Channel:
        channel = self.get_channel(channel_id)
        update_data = payload.model_dump(exclude_unset=True)
        updated = channel.model_copy(update=update_data)
        self._channels[channel_id] = updated
        return updated

    def delete_channel(self, channel_id: int) -> None:
        if channel_id in self._channels:
            del self._channels[channel_id]
        else:
            raise KeyError(channel_id)


channel_service = ChannelService()
