from .package import Package
from heapq import heapreplace, heappush


def greedy_alternativo(objects: list[float]) -> list[Package]:
    packages: list[tuple[float, Package]] = [(0, Package())]
    for obj in sorted(objects, reverse=True):
        _, smallest_package = packages[0]
        if smallest_package.fits(obj):
            smallest_package.add_object(obj)
            heapreplace(packages, (smallest_package.size(), smallest_package))
        else:
            new_package = Package(obj)
            heappush(packages, (new_package.size(), new_package))
    return [x[1] for x in packages]
