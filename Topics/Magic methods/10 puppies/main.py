class Puppy:
    n_puppies = 0  # number of created puppies

    def __new__(cls):
        if cls.n_puppies < 10:
            cls.n_puppies += 1
            return object.__new__(Puppy)
