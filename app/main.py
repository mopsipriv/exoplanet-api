from fastapi import FastAPI

app = FastAPI(title="Exoplanet Detection API",description="Detects exoplanet transit candidates in Kepler light curves", version="1.0.0")

@app.get("/")
def hello():
    return {"message": "Exoplanet Detection API", "docs_url": "/docs"}

@app.get("/health")
def health():
    return {"status": "ok", "version": "0.1.0"}