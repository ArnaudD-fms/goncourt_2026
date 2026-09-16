from datetime import date

MOIS = [
    "janvier", "février", "mars", "avril", "mai", "juin",
    "juillet", "août", "septembre", "octobre", "novembre", "décembre"
]


def date_fr(d: date) -> str:
    """
    Méthode permettant de convertir la date passée en paramètre en format adapté à l'affichage
    exemple > 2026-09-16 en entrée = 16 septembre 2026 en sortie

    :param d: la date à convertir
    :return: string contenant la date formatée
    """
    return f"{d.day} {MOIS[d.month - 1]} {d.year}"
