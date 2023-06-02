from .package import Package
from heapq import heapreplace, heappush


def greedy_alternativo(objects: list[float]) -> list[Package]:
    packages: list[Package] = [Package()]
    for obj in sorted(objects, reverse=True):
        smallest_package = packages[0]
        if smallest_package.fits(obj):
            smallest_package.add_object(obj)
            heapreplace(packages, smallest_package) # update position
        else:
            new_package = Package(obj)
            heappush(packages, new_package)
    return packages
