def iter_exam():
    class Test:
        def __init__(self, limit):
            self.limit = limit

        """ Called When Iterator is Initialized  """

        def __iter__(self):
            self.x = 10
            return self

        """ To Move Next Element """

        def __next__(self):
            # Store Current Value of X
            x = self.x

            # Stop Iteration if limit is reached
            if x > self.limit:
                raise StopIteration

            # Increment and return old value
            self.x = x + 1
            return x

    """ Print numbers from 10 - 20"""
    for i in Test(20):
        print(i)

    """ Nothing will Return"""
    for i in Test(5):
        print(i)
# iter_exam()

def in_built_iters():
    # Sample built-in iterators

    # Iterating over a list
    print("List Iteration")
    l = ["geeks", "for", "geeks"]
    for i in l:
        print(i)

        # Iterating over a tuple (immutable)
    print("\nTuple Iteration")
    t = ("geeks", "for", "geeks")
    for i in t:
        print(i)

        # Iterating over a String
    print("\nString Iteration")
    s = "Geeks"
    for i in s:
        print(i)

        # Iterating over dictionary
    print("\nDictionary Iteration")
    d = dict()
    d['xyz'] = 123
    d['abc'] = 345
    for i in d:
        print("%s  %d" % (i, d[i]))
in_built_iters()