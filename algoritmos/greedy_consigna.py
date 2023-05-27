from .package import Package


def greedy_consigna(objects: list[float]) -> list[Package]:
    if any(s > 1 for s in objects):
        raise ValueError("No solution: there is an object of size bigger than 1")

    packages: list[Package] = [Package()]

    for obj in objects:
        if not packages[-1].fits(obj):
            # cierro paquete y abro uno nuevo
            packages.append(Package())
        packages[-1].add_object(obj)

    return packages
