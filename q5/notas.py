def media(notas: list) -> float:
    if len(notas) == 0:
        return 0.0
    return sum(notas) / len(notas)

def maior(notas: list) -> float:
    if len(notas) == 0:
        return 0.0
    return max(notas)


def menor(notas: list) -> float:
    if len(notas) == 0:
        return 0.0
    return min(notas)
