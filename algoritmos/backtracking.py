from math import ceil
from .package import Package


def backtracking(
    objects: list[float], debug: bool = False, better_than: list[Package] | None = None
) -> list[Package]:
    """
    Encuentra la solución óptima al problema de empaquetamiento con backtracking.
    Parámetros:
        objects: lista de objetos a empaquetar
        debug: si es True, imprime información la cota inferior y las soluciones
            que va encontrando
        better_than: solucion preexistente opcional que se utiliza para podar
            soluciones que no son mejores que esta
    """
    if any(s > 1 for s in objects):
        raise ValueError("No solution: there is an object of size bigger than 1")

    lower_bound = ceil(sum(objects))  # lower bound for the number of packages
    if debug:
        print("Lower bound:", lower_bound)
    return __backtracking_rec(objects, 0, [], better_than, lower_bound, debug)


def __best_solution(
    previous: list[Package] | None, new: list[Package]
) -> list[Package]:
    """
    Compara dos soluciones y devuelve la mejor
    """
    if previous is None or len(new) < len(previous):
        # Necesito clonarlo para que el algoritmo no me la modifique al seguir
        return [x.clone() for x in new]
    return previous


def __backtracking_rec(
    objects: list[float],
    i: int,  # Número de objeto que estoy considerando
    packages: list[Package],
    best: list[Package] | None,
    lower_bound: int,
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
        if not package.fits(objects[i]):
            continue

        package.add_object(objects[i])
        result = __backtracking_rec(
            objects, i + 1, packages, new_best, lower_bound, debug
        )
        new_best = __best_solution(new_best, result)
        package.pop()

        if new_best and (
            len(packages) >= len(new_best) or len(new_best) == lower_bound
        ):
            # Poda
            # Si len(packages) >= len(new_best), no va a mejorar más hasta sacar un envase
            # Si len(new_best) == lower_bound, encontramos una solución óptima
            return new_best

    # 2) Agregarlo a un nuevo envase

    if new_best and len(packages) + 1 >= len(new_best):
        # Poda: si agrego un nuevo envase, ya no va a mejorar
        return new_best

    packages.append(Package(objects[i]))
    result = __backtracking_rec(objects, i + 1, packages, new_best, lower_bound, debug)
    new_best = __best_solution(new_best, result)
    packages.pop()
    return new_best
