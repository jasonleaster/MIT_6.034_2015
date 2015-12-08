from copy import deepcopy

class Point(object):
    """A Point has a name and a list or tuple of coordinates, and optionally a
    classification, and/or alpha value."""
    def __init__(self, name, coords, classification=None, alpha=None):
        self.name = name
        self.coords = coords
        self.classification = classification
        self.alpha = alpha

    def copy(self):
        return deepcopy(self)

    def __eq__(self, other):
        try:
            return (self.coords == other.coords
                    and self.classification == other.classification
                    and self.alpha == other.alpha)
        except:
            return False

    def __str__(self):
        if self.classification is None and self.alpha is None:
            return "Point(%s)" % (str(self.name), str(self.coords))
        return "Point(%s, %s, class=%s, alpha=%s)" % (str(self.name), \
            str(self.coords), str(self.classification), str(self.alpha))

    __repr__ = __str__


class DecisionBoundary(object):
    """A DecisionBoundary is defined by two parameters: a normal vector w, and
    an offset b.  w is represented as a list or tuple of coordinates."""
    def __init__(self, w, b):
        self.w = w
        self.b = b

    def copy(self):
        return deepcopy(self)

    def __eq__(self, other):
        try:
            return self.w == other.w and self.b == other.b
        except:
            return False

    def __str__(self):
        return "DecisionBoundary(w=%s, b=%s)" % (str(self.w), str(self.b))

    __repr__ = __str__


class SupportVectorMachine(object):
    """A SupportVectorMachine is a classifier that uses a DecisionBoundary to
    classify points.  It has a list of training points and optionally a list of
    support vectors."""
    def __init__(self, boundary, training_points=[], support_vectors=[]):
        self.boundary = boundary
        self.training_points = training_points[:]
        self.support_vectors = support_vectors[:]

    def set_boundary(self, new_boundary):
        self.boundary = new_boundary
        return self

    def copy(self):
        return deepcopy(self)

    def __eq__(self, other):
        try:
            assert self.boundary == other.boundary
            assert equality_by_string(self.training_points,
                                      other.training_points)
            assert equality_by_string(self.support_vectors,
                                      other.support_vectors)
            return True
        except:
            return False

    def __str__(self):
        len_and_str = lambda x: tuple([fn(x) for fn in (len, str)])
        return ('SupportVectorMachine with:'
            + '\n * boundary: %s' % str(self.boundary)
            + '\n * %i training points: %s' % len_and_str(self.training_points)
            + '\n * %i support vectors: %s' % len_and_str(self.support_vectors))

    __repr__ = __str__


def convert_point_to_coords(v):
    """Given either a Point object or a tuple of coordinates, returns a tuple of
    coordinates."""
    return v.coords if is_class_instance(v, 'Point') else v

def vector_add(v1, v2):
    """Given two vectors represented as lists or tuples of coordinates, returns
    their sum as a list of coordinates."""
    if len(v1) != len(v2):
        raise IndexError("vector_add: Input vectors must be same length")
    return [x1 + x2 for (x1,x2) in zip(v1,v2)]

def scalar_mult(scalar, vector):
    """Given a constant scalar and a vector (as a tuple or list of coordinates),
    returns a scaled list of coordinates"""
    return [scalar*coord for coord in convert_point_to_coords(vector)]

def equality_by_string(set1, set2):
    """This is a hack to get around reference equality.
    Returns True if two sets (or lists) contain equivalent elements"""
    return sorted(map(str, set1)) == sorted(map(str, set2))

def is_class_instance(obj, class_name):
    return hasattr(obj, '__class__') and obj.__class__.__name__ == class_name

__all__ = ['Point', 'DecisionBoundary', 'SupportVectorMachine', 'vector_add',
           'scalar_mult', 'equality_by_string', 'is_class_instance']