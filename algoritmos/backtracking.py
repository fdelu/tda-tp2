from .package import Package


# Uses better_than to prune the search space
def backtracking(
    objects: list[float], debug: bool = False, better_than: list[Package] | None = None
) -> list[Package]:
    if any(s > 1 for s in objects):
        raise ValueError("No solution: there is an object of size bigger than 1")
    return __backtracking_rec(objects, 0, [], better_than, debug)


def __best_solution(
    previous: list[Package] | None, new: list[Package]
) -> list[Package]:
    if previous is None or len(new) < len(previous):
        # Necesito clonarlo para que el algoritmo no me la modifique al seguir
        return [x.clone() for x in new]
    return previous


def __backtracking_rec(
    objects: list[float],
    i: int,
    packages: list[Package],
    best: list[Package] | None,
    debug: bool,
) -> list[Package]:
    if i == len(objects):
        # Por las podas de abajo, esta solución es siempre mejor que best
        if debug:
            l = len(best) if best else len(objects)
            print(f"Previous best: {l}, new best: {len(packages)}\n{packages}")
        return packages

    new_best = best

    # Para cada objeto, probamos todas las posibilidades:
    # 1) Agregarlo a cualquiera de los envases existentes (siempre que entre)

    # En el peor caso, hay i envases
    for package in packages:
        if new_best and len(packages) >= len(new_best):
            # Poda: por esta rama ya no mejora más
            return new_best

        if package.fits(objects[i]):
            package.add_object(objects[i])
            result = __backtracking_rec(objects, i + 1, packages, new_best, debug)
            new_best = __best_solution(new_best, result)
            package.pop()

    # 2) Agregarlo a un nuevo envase

    if new_best and len(packages) + 1 >= len(new_best):
        # Poda: si agrego un nuevo envase, ya no va a mejorar
        return new_best

    packages.append(Package(objects[i]))
    result = __backtracking_rec(objects, i + 1, packages, new_best, debug)
    new_best = __best_solution(new_best, result)
    packages.pop()
    return new_best
