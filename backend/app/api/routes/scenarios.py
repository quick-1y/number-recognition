"""Scenario endpoints."""
from __future__ import annotations

from fastapi import APIRouter

from ...schemas import scenario as scenario_schema
from ...services.scenario_service import scenario_service

router = APIRouter(prefix="/scenarios", tags=["scenarios"])


@router.get("", response_model=list[scenario_schema.ScenarioRule])
async def list_scenarios() -> list[scenario_schema.ScenarioRule]:
    return scenario_service.list_scenarios()


@router.put("/{name}", response_model=scenario_schema.ScenarioRule)
async def upsert_scenario(name: str, payload: scenario_schema.ScenarioRule) -> scenario_schema.ScenarioRule:
    scenario = payload.model_copy(update={"name": name})
    return scenario_service.put_scenario(scenario)
