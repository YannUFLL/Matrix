from matrix import Vector, Matrix

def row_echelon():
    m = Matrix([[2,3,4],
                [4,6,8],
                [1,3,1]])
    print(m.row_echelon())
    m = Matrix([[2,3,4,7],
                [4,6,8,12],
                [1,3,1,5],
                [7,1,2,1]])
    print(m.row_echelon())
    m = Matrix([[-2,-3,-4,-7],
                [-4,5,-8,-12],
                [-1,3,-1,-5],
                [-7,-1,2,-1]])
    print(m.row_echelon())
    m = Matrix([[-2,-3,-4,-7],
                [-4,-6,-8,-12],
                [-1,-3,-1,-5],
                [-7,-1,-2,-1]])
    print(m.row_echelon())
    m = Matrix([
    [0, 2, 3],
    [0, 0, 4],
    [0, 5, 6]
])
    print(m.row_echelon())
    m = Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])
    print(m.row_echelon())
    m = Matrix([
    [1, 2, 3],
    [1, 5, 6],
    [10, 1, 1]
])
    print(m.row_echelon())
    m = Matrix([
    [1, 2, 3],
    [2, 4, 6], 
    [3, 6, 9]  
])
    print(m.row_echelon())
    
if __name__ == "__main__":
    row_echelon()
