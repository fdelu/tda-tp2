class Package:
    objects: dict[
        float, int
    ]  # en caso de que haya objetos repetidos, cuento cuantos hay
    sum: float  # para no tener que recorrer todos los objetos

    def __init__(self):
        self.objects = {}
        self.sum = 0

    def add_object(self, object: float):
        self.objects[object] = self.objects.get(object, 0) + 1
        self.sum += object

    def fits(self, object: float):
        return self.sum + object <= 1

    def remove_object(self, object: float):
        self.objects[object] -= 1
        if self.objects[object] == 0:
            del self.objects[object]
        self.sum -= object

    def as_list(self):
        return [x for y in [[k] * v for k, v in self.objects.items()] for x in y]

    def __str__(self):
        return str(self.as_list())

    def __repr__(self) -> str:
        return str(self)

    def __len__(self):
        return len(self.as_list())
