class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')
            
    # Vector addition
    def plus(self, v):
        new_coords = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coords)
    
    # Vector subtraction
    def minus(self, v):
        new_coords = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coords)
    
    # Scalar multiplication
    def times_scalar(self, c):
        new_coords = [c * x for x in self.coordinates]
        return Vector(new_coords)
    
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

vec = Vector([1, 2, 3])
print(vec) # Vector: (1, 2, 3)
vec2 = Vector([2, 3, 4])
print(vec.plus(vec2)) # Vector: (3, 5, 7)
print(vec.times_scalar(2)) # Vector: (2, 4, 8)

# https://repl.it/repls/BiodegradableOutlandishStruct#main.py
