from fastapi import FastAPI, HTTPException
from app.detector import find_planets
from app.models import DetectionResponse,PlanetCandidate
import logging

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

app = FastAPI(title="Exoplanet Detection API",description="Detects exoplanet transit candidates in Kepler light curves", version="1.0.0")

@app.get("/")
def hello():
    return {"message": "Exoplanet Detection API", "docs_url": "/docs"}

@app.get("/health")
def health():
    return {"status": "ok", "version": "0.1.0"}

@app.get("/exoplanets/{kepler_id}")
def detect_exoplanets(kepler_id: str):
    logger.info(f"Searching for planets for star: {kepler_id}")
    candidates= find_planets(kepler_id)

    if len(candidates) == 0:
        logger.warning(f"No candidates found for star: {kepler_id}")
        raise HTTPException(
            status_code=404,detail=f"No data found for star '{kepler_id}' in Kepler archive"
            )
    
    logger.info(f"Found {len(candidates)} candidates for {kepler_id}")
    
    return DetectionResponse(
        kepler_id=kepler_id,
        candidates_found=len(candidates),
        candidates=candidates,
    )