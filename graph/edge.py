def log_class_calls(cls):
    """
    A class decorator to log each time a method of the decorated class is called.
    """
    def log_method_call(func):
        def wrapper(*args, **kwargs):
            print(f"Method {func.__name__} of class {cls.__name__} was called.")
            return func(*args, **kwargs)
        return wrapper

    # Apply the log_method_call decorator to each method in the class.
    for attr in cls.__dict__:
        if callable(getattr(cls, attr)):
            setattr(cls, attr, log_method_call(getattr(cls, attr)))

    return cls

@log_class_calls
class Edge:
    def __init__(self, start_vertex, end_vertex, weight=1, directed=True):
        self.__start_vertex = start_vertex
        self.__end_vertex = end_vertex
        self.__weight = weight
        self.__directed = directed

    def __str__(self):
        if self.__directed:
            print_pattern = "{0} -{1}-> {2}"
        else:
            print_pattern = "{0} <-{1}-> {2}"
        return print_pattern.format(self.__start_vertex.get_label(), self.__weight, self.__end_vertex.get_label())

    def get_start_vertex(self):
        return self.__start_vertex

    def get_end_vertex(self):
        return self.__end_vertex

    def get_weight(self):
        return self.__weight

    def __lt__(self, other):
        return self.__weight < other.get_weight()

    def __eq__(self, other):
        weight_equal = self.__weight == other.get_weight()
        start_vertex_equal = self.__start_vertex == other.get_start_vertex()
        end_vertex_equal = self.__end_vertex == other.get_end_vertex()

        return weight_equal == start_vertex_equal == end_vertex_equal == True

    def __hash__(self):
        return hash(self.__start_vertex.get_label() +
                    self.__end_vertex.get_label() + str(self.__weight))