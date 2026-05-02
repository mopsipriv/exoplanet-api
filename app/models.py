from pydantic import BaseModel

class PlanetCandidate(BaseModel):
    period_days: float
    transit_time_bjd: float
    duration_hours: float

class DetectionResponse(BaseModel):
    kepler_id: str
    candidates_found: int
    candidates: list[PlanetCandidate]