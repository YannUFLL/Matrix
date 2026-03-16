from matrix import Vector, Matrix

def determinant():
    m = Matrix([[2,0,0],
                [0,2,0],
                [0,0,2]])
    print("matrice:", m)
    print("determinant:",m.determinant())

    m = Matrix([[0,3,4,5],
                [7,4,1,3],
                [9,8,7,3]])
    print("matrice:", m)
    print("determinant:",m.determinant())

    m = Matrix([[8,5,-2,4],
                [4,2.5,20,4],
                [8,5,1,4],
                [28,-4,17,1]])
                
    print("matrice:", m)
    print("determinant:",m.determinant())

    m = Matrix([[]])
    print("matrice:", m)
    print("determinant:",m.determinant())

    m = Matrix([[0,5]])
    print("matrice:", m)
    print("determinant:",m.determinant())

    m = Matrix([[0]])
    print("matrice:", m)
    print("determinant:",m.determinant())

    m = Matrix([[1]])
    print("matrice:", m)
    print("determinant:",m.determinant())

    m = Matrix([[5]])
    print("matrice:", m)
    print("determinant:",m.determinant())

    m = Matrix([[1,0],
                [0,1]])
    print("matrice:", m)
    print("determinant:",m.determinant())

    m = Matrix([[5,3],
                [-6,2]])
    print("matrice:", m)
    print("determinant:",m.determinant())

    m = Matrix([[2, -5, 0],
                [4, 3, 7],
                [-2, 3, 4]])
    print("matrice:", m)
    print("determinant:",m.determinant())

    m = Matrix([[-2, -8, 4],
                [4, -23, 4],
                [0, 6, 4]])
    print("matrice:", m)
    print("determinant:",m.determinant())

    m = Matrix([[1,0,0,0],
                [0,1,0,0],
                [0,0,1,0],
                [0,0,0,1]])
    print("matrice:", m)
    print("determinant:",m.determinant())

    m = Matrix([[1,-3,-4,7],
                [-4,-6,-8,-12],
                [-1,-3,-1,5],
                [-7,-1,-2,-1]])
    print("matrice:", m)
    print("determinant:",m.determinant())



    
if __name__ == "__main__":
    determinant()
