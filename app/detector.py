import lightkurve as lk
import numpy as np

def find_planets(kepler_id: str) -> list[dict]:
    search_result=lk.search_lightcurve(kepler_id,mission="Kepler",cadence="long")
    if len(search_result)==0:
        return []
    lc=search_result[0].download()
    lc_clean=lc.remove_nans().remove_outliers().flatten()
    bls = lc_clean.to_periodogram(method="bls", period=np.linspace(0.5, 10, 10000))

    max_period=bls.period_at_max_power.value
    max_transit=bls.transit_time_at_max_power.value
    max_duration=bls.duration_at_max_power.value * 24

    return [
        {
            "period_days": max_period,
            "transit_time_bjd": max_transit,
            "duration_hours": max_duration,
        }
    ]