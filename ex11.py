from matrix import Vector, Matrix

def determinant():
    m = Matrix([[0,3,4,5],
                [7,4,1,3],
                [9,8,7,3]])
    print(m.determinant())

    m = Matrix([[]])
    print(m.determinant())

    m = Matrix([[0,5]])
    print(m.determinant())

    m = Matrix([[0]])
    print(m.determinant())
    m = Matrix([[1]])
    print(m.determinant())
    m = Matrix([[5]])
    print(m.determinant())

    m = Matrix([[1,0],
                [0,1]])
    print(m.determinant())

    m = Matrix([[5,3],
                [-6,2]])
    print(m.determinant())

    m = Matrix([[2, -5, 0],
                [4, 3, 7],
                [-2, 3, 4]])
    print(m.determinant())

    m = Matrix([[-2, -8, 4],
                [4, -23, 4],
                [0, 6, 4]])
    print(m.determinant())

    m = Matrix([[1,0,0,0],
                [0,1,0,0],
                [0,0,1,0],
                [0,0,0,1]])
    print(m.determinant())
    m = Matrix([[1,-3,-4,7],
                [-4,-6,-8,-12],
                [-1,-3,-1,5],
                [-7,-1,-2,-1]])
    print(m.determinant())


    
if __name__ == "__main__":
    determinant()
