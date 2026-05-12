def estimate_stress(
    crowd_level: int,
    noise_sensitivity: int,
    crowd_sensitivity: int,
    uncertainty_tolerance: int,
    incident: str,
):
    score = crowd_level

    score += noise_sensitivity * 2
    score += crowd_sensitivity * 3
    score += (10 - uncertainty_tolerance) * 2

    if incident != "Sin incidencias":
        score += 15

    return min(score, 100)
