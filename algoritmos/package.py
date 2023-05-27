class Package:
    inner: list[float]
    sum: float  # para no tener que recorrer todos los objetos

    def __init__(self, *args: float):
        self.inner = list(args)
        self.sum = sum(args)

    def add_object(self, object: float):
        self.inner.append(object)
        self.sum += object

    def fits(self, object: float):
        return self.sum + object <= 1

    def pop(self):
        last = self.inner.pop()
        self.sum -= last

    def size(self):
        return self.sum

    def clone(self):
        return Package(*self.inner)

    def __str__(self):
        return str(self.inner)

    def __repr__(self) -> str:
        return str(self)

    def __len__(self):
        return len(self.inner)
