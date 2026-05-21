from matrix import Vector, Matrix

def row_echelon():
    m = Matrix([
    [0, 2, 3],
    [0, 0, 4],
    [0, 5, 6]
])
    print("matrice:", m)
    print("row_matrice:", m.row_echelon())
    m = Matrix([[2,3,4],
                [4,6,8],
                [1,3,1]])
    print("matrice:", m)
    print("row_matrice:", m.row_echelon())
    m = Matrix([[2,3,4,7],
                [4,6,8,12],
                [1,3,1,5],
                [7,1,2,1]])
    print("matrice:", m)
    print("row_matrice:", m.row_echelon())
    m = Matrix([[-2,-3,-4,-7],
                [-4,5,-8,-12],
                [-1,3,-1,-5],
                [-7,-1,2,-1]])
    print("matrice:", m)
    print("row_matrice:", m.row_echelon())
    m = Matrix([[-2,-3,-4,-7],
                [-4,-6,-8,-12],
                [-1,-3,-1,-5],
                [-7,-1,-2,-1]])
    print("matrice:", m)
    print("row_matrice:", m.row_echelon())

    m = Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])
    print("matrice:", m)
    print("row_matrice:", m.row_echelon())
    m = Matrix([
    [1, 2, 3],
    [1, 5, 6],
    [10, 1, 1]
])
    print("matrice:", m)
    print("row_matrice:", m.row_echelon())
    m = Matrix([
    [1, 2, 3],
    [2, 4, 6], 
    [3, 6, 9]  
])
    print("matrice:", m)
    print("row_matrice:", m.row_echelon())

    m = Matrix([
        [1., 2.],
        [3., 4.]
    ])
    print("matrice:", m)
    print("row_matrice:", m.row_echelon());
    m = Matrix([
        [8, 5,-2, 4, 28],
        [4, 2.5, 20, 4, -4],
        [8, 5, 1, 4, 17]
    ])
    print("matrice:", m)
    print("row_matrice:", m.row_echelon());
    
    m = Matrix([
        [1, 2],
        [2, 4]
    ])
    print("matrice:", m)
    print("row_matrice:", m.row_echelon());

    m = Matrix([
        [1, 2],
        [3, 4]
    ])
    print("matrice:", m)

    print("row_matrice:", m.row_echelon());
    m = Matrix([[1+1j, 2],
                [3, 4-1j]])
    print("matrice (complex):", m)
    print("row_matrice:", m.row_echelon())

    m = Matrix([[1+2j, 2+2j, 3],
                [2+4j, 4+8j, 6],
                [3, 6, 9]])
    print("matrice (complex 2):", m)
    print("row_matrice:", m.row_echelon())
    
if __name__ == "__main__":
    row_echelon()
