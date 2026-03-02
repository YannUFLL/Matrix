from matrix import Vector, Matrix


def vector_matrix_multiplication():
    # test incompatibility size
    try:
        m = Matrix([[7, 5],
                    [2, 3]])
        r = m.mul_vec(Vector([1,2,3]))
        print(r)
    except ValueError as e:
        print(e)

    m = Matrix([[7, 5],
                [2, 3]])

    r = m.mul_vec(Vector([1,2]))
    print(r)

    m = Matrix([[1, 2],
                [3, 4]])

    r = m.mul_vec(Vector([1, 0]))
    print(r)

    r = m.mul_vec(Vector([0, 1]))
    print(r)

    m = Matrix([[1, 2],
                [3, 4],
                [5, 6]])
    r = m.mul_vec(Vector([1, 1]))
    print(r)

    m = Matrix([[1, 2],
                [3, 4],
                [5, 6]])

    r = m.mul_vec(Vector([0, 0]))
    print(r)

    m = Matrix([[1, 2, 3]])
    r = m.mul_vec(Vector([1, 2, 3]))
    print(r)

def matrix_matrix_multiplication():
    try:
        m1 = Matrix([[1, 2, 3],
                     [4, 5, 6]])

        m2 = Matrix([[1, 2, 3],
                     [4, 5, 6]])

        r = m1.mul_mat(m2)
        print(r)
    except ValueError as e:
        print(e)

    m1 = Matrix([[1, 2, 3],
                 [4, 5, 6]])

    m2 = Matrix([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
    r = m1.mul_mat(m2)
    print(r)

    m1 = Matrix([[1, 2, 3],
                 [4, 5, 6]])

    m2 = Matrix([[1, 2, 3, 5],
                 [4, 5, 6, 7],
                 [7, 8, 9, 8]])

    r = m1.mul_mat(m2)
    print(r)

    m1 = Matrix([[1, 0, 0],
                 [0, 1, 0],
                 [0, 0, 1]])

    m2 = Matrix([[14, 2, 7],
                 [7, 9, 8],
                 [4, 1, 2]])

    r = m1.mul_mat(m2)
    print(r)
    r = m2.mul_mat(m1)
    print(r)


    m1 = Matrix([[1, 0, 0],
                 [0, 1, 0],
                 [0, 0, 1]])

    m2 = Matrix([[14, 2, 7, 8],
                 [7, 9, 8, 6],
                 [4, 1, 2, 18]])

    r = m1.mul_mat(m2)
    print(r)

    m1 = Matrix([[1, 2, 3]])

    m2 = Matrix([[4], 
                 [5], 
                 [6]])

    print(m1.mul_mat(m2))

if __name__ == "__main__":
    vector_matrix_multiplication()
    matrix_matrix_multiplication()
