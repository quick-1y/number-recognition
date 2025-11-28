"""Minimal rules engine stub with list checks and webhook scheduling hooks."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable

from app.models.plate_list import PlateList
from app.worker.pipeline import RecognitionEvent


@dataclass
class RuleDecision:
    matched_lists: list[str]
    action: str


class RulesEngine:
    def __init__(self, lists: Iterable[PlateList]):
        self.lists = {lst.name: lst for lst in lists}

    def evaluate(self, recognition: RecognitionEvent) -> RuleDecision | None:
        matched = [name for name, lst in self.lists.items() if self._matches(lst, recognition)]
        if not matched:
            return None
        action = "notify" if any(self.lists[name].type == "black" for name in matched) else "store"
        return RuleDecision(matched_lists=matched, action=action)

    @staticmethod
    def _matches(lst: PlateList, recognition: RecognitionEvent) -> bool:
        if not lst.active:
            return False
        # Simplified mask match to demonstrate extensibility
        return any(
            recognition.ocr.text.startswith(item.plate_value.replace("*", "")) for item in lst.items
        )
