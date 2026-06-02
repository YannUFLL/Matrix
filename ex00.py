from matrix import Matrix, Vector

def add_vector_real():
    v = Vector([1,8,2])
    v.add(Vector([2,2,2]))
    print(v)

def add_vector_complex():
    v = Vector([8 + 1j, 8 + 3j, 2 + 5j])
    v.add(Vector([2 + 7j, 2 + 3j, 2 + 1j]))
    print(v)

def sub_vector_real():
    v = Vector([7,4,3])
    v.sub(Vector([10,9,8]))
    print(v)

def sub_vector_complex():
    v = Vector([7 + 1j, 4 + 8j, 3 + 2j])
    v.sub(Vector([10 + 14j, 9 + 2j, 8 + 1j]))
    print(v)

def scale_vector_real():
    v = Vector([2,2,3])
    v.scl(3)
    print(v)

def scale_vector_complexe():
    v = Vector([2 + 3j, 1 + 4j, 5 + 9j])
    v.scl(3)
    print(v)

def add_matrix_real():
    m = Matrix([[3,1,5],
                [4,8,6],
                [1,3,7]])

    m.add(Matrix([[2,4,6],
                  [8,1,2],
                  [4,6,7]]))
    print(m)

def add_matrix_complexe():
    m = Matrix([[3 + 2j, 1 + 8j, 5 + 2j],
                [4 + 3j, 8 + 1j, 6 + 5j],
                [1 + 2j, 3 + 1j, 7 + 2j]])

    m.add(Matrix([[2 + 1j, 4 + 9j, 6 + 3j],
                  [8 + 2j, 1 + 1j, 2 + 3j],
                  [4 + 6j, 6 + 8j, 7 + 2j]]))
    print(m)

def sub_matrix_real():
    m = Matrix([[3,1,5],
                [4,8,6],
                [1,3,7]])

    m.sub(Matrix([[2,4,6],
                  [8,1,2],
                  [4,6,7]]))
    print(m)

def sub_matrix_complexe():
    m = Matrix([[3 + 2j, 1 + 8j, 5 + 2j],
                [4 + 3j, 8 + 1j, 6 + 5j],
                [1 + 2j, 3 + 1j, 7 + 2j]])

    m.sub(Matrix([[2 + 1j, 4 + 9j, 6 + 3j],
                  [8 + 2j, 1 + 1j, 2 + 3j],
                  [4 + 6j, 6 + 8j, 7 + 2j]]))
    print(m)

def scl_matrix_real():
    m = Matrix([[3,1,5],
                [4,5,6],
                [1,3,5]])
    m.scl(2)
    print(m)

def scl_matrix_complexe():
    m = Matrix([[3 + 2j, 1 + 8j, 5 + 2j],
                [4 + 3j, 8 + 1j, 6 + 5j],
                [1 + 2j, 3 + 1j, 7 + 2j]])
    m.scl(2)
    print(m)

if __name__ == "__main__":
    print("\ntest: add_vector_real")
    add_vector_real()
    print("\ntest: add_vector_complex")
    add_vector_complex()
    print("\ntest: sub_vector_real")
    sub_vector_real()
    print("\ntest: sub_matrix_complexe")
    sub_matrix_complexe()
    print("\ntest: scale_vector_real")
    scale_vector_real()
    print("\ntest: scale_vector_complexe")
    scale_vector_complexe()
    print("\ntest: add_matrix_real")
    add_matrix_real()
    print("\ntest: add_matrix_complexe")
    add_matrix_complexe()
    print("\ntest: sub_matrix_real")
    sub_matrix_real()
    print("\ntest: sub_matrix_complexe")
    sub_matrix_complexe()
    print("\ntest: scl_matrix_real")
    scl_matrix_real()
    print("\ntest: scl_matrix_complexe")
    scl_matrix_complexe()




