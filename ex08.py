from matrix import Vector, Matrix


def trace():
    m = Matrix([[1, 0],
                [0, 1]])
    print(m.trace())

    m = Matrix([[2, -5, 0],
                [4, 3, 7],
                [-2, 3, 4]])
    print(m.trace())

    m = Matrix([[-2, -8, 4],
                [4, -23, 4],
                [0, 6, 4]])
    print(m.trace())
    

if __name__ == "__main__":
    trace()
