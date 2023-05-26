from .package import Package


def backtracking(objects: list[float], debug: bool = False):
    if any(s > 1 for s in objects):
        raise ValueError("No solution: there is an object of size bigger than 1")
    return backtracking_rec(objects, 0, [], len(objects), debug)


def backtracking_rec(
    objects: list[float], i: int, packages: list[Package], best: int, debug: bool
):
    if i == len(objects):
        # Por las podas de abajo, esta solución es siempre mejor que best
        if debug:
            print(f"Previous best: {best}, new best: {len(packages)}\n{packages}")
        return len(packages)

    new_best = best

    # Para cada objeto, probamos todas las posibilidades:
    # 1) Agregarlo a cualquiera de los paquetes existentes que entre
    # 2) Agregarlo a un nuevo paquete
    for package in packages:
        if len(packages) == new_best:  # Poda: por esta rama ya no mejora más
            break

        if package.fits(objects[i]):
            package.add_object(objects[i])
            result = backtracking_rec(objects, i + 1, packages, new_best, debug)
            new_best = min(new_best, result)
            package.remove_object(objects[i])

    if len(packages) + 1 < new_best:  # Poda
        packages.append(Package())
        packages[-1].add_object(objects[i])
        result = backtracking_rec(objects, i + 1, packages, new_best, debug)
        new_best = min(new_best, result)
        packages.pop()

    return new_best
