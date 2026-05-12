from config import MAX_STRESS_SCORE


def calculate_stress_score(
    crowd_density: int,
    noise_sensitivity: int,
    crowd_sensitivity: int,
    uncertainty_tolerance: int,
    incident: str,
) -> int:
    """
    Calcula carga sensorial total.

    Outputs:
        Valor entre 0 y 100.
    """
    score = crowd_density

    score += noise_sensitivity * 2
    score += crowd_sensitivity * 3
    score += (10 - uncertainty_tolerance) * 2

    if incident != "Sin incidencias":
        score += 15

    return min(score, MAX_STRESS_SCORE)
