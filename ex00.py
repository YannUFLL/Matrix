from matrix import Matrix, Vector

def add_vector():
    v = Vector([1,8,2])
    v.add(Vector([2,2,2]))
    print(v)

def sub_vector():
    v = Vector([7,4,3])
    v.sub(Vector([10,9,8]))
    print(v)

def scale_vector():
    v = Vector([2,2,3])
    v.scl(3)
    print(v)

def add_Matrix():
    m = Matrix([[3,1,5],
                [4,8,6],
                [1,3,7]])

    m.add(Matrix([[2,4,6],
                  [8,1,2],
                  [4,6,7]]))
    print(m)

def sub_Matrix():
    m = Matrix([[3,1,5],
                [4,8,6],
                [1,3,7]])

    m.sub(Matrix([[2,4,6],
                  [8,1,2],
                  [4,6,7]]))
    print(m)

def scl_Matrix():
    m = Matrix([[3,1,5],
                [4,5,6],
                [1,3,5]])
    m.scl(2)
    print(m)

if __name__ == "__main__":
    add_vector()
    sub_vector()
    scale_vector()
    add_Matrix()
    sub_Matrix()
    scl_Matrix()




