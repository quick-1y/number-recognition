"""Scenario engine placeholder implementation."""
from __future__ import annotations

from collections import OrderedDict

from ..schemas import scenario as scenario_schema


class ScenarioService:
    def __init__(self) -> None:
        self._scenarios: "OrderedDict[str, scenario_schema.ScenarioRule]" = OrderedDict()

    def list_scenarios(self) -> list[scenario_schema.ScenarioRule]:
        return list(self._scenarios.values())

    def put_scenario(self, scenario: scenario_schema.ScenarioRule) -> scenario_schema.ScenarioRule:
        self._scenarios[scenario.name] = scenario
        return scenario


scenario_service = ScenarioService()
