from matrix import Vector, Matrix

def inverse():
    m = Matrix([[1, 0, 0],
                [0, 1,0],
                [0, 0,1]])
    print("matrice:", m)
    print("inverse:", m.inverse())

    m = Matrix([[2, 0, 0],
                [0, 2, 0],
                [0, 0, 2]])
    print("matrice:", m)
    print("inverse:", m.inverse())

    m = Matrix([[0.5 ,0 , 0],
                [0, 0.5, 0],
                [0, 0, 0.5]])
    print("matrice:", m)
    print("inverse:", m.inverse())


    m = Matrix([[8, 5, -2],
                [4, 7, 20],
                [7, 6, 1]])
    print("matrice:", m)
    print("inverse:", m.inverse())
    
if __name__ == "__main__":
    inverse()
