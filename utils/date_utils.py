from datetime import date

MOIS = [
    "janvier", "février", "mars", "avril", "mai", "juin",
    "juillet", "août", "septembre", "octobre", "novembre", "décembre"
]


def date_fr(d: date) -> str:
    return f"{d.day} {MOIS[d.month - 1]} {d.year}"
