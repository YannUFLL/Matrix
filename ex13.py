from matrix import Vector, Matrix
import math
def rank():
    m = Matrix([[1, 0],
                [0, 1],
                ])
    print("matrice:", m)
    print("rank:", m.rank())

    m = Matrix([[1, 0],
                [0, 0],
                ])
    print("matrice:", m)
    print("rank:", m.rank())

    m = Matrix([[1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]])
    print("matrice:", m)
    print("rank:", m.rank())

    m = Matrix([[1, 2, 0, 0],
                [2, 4, 0, 0],
                [-1, 2, 1, 1]])
    print("matrice:", m)
    print("rank:", m.rank())

    m = Matrix([[8, 5, -2],
                [4, 7, 20],
                [7, 6, 1 ],
                [21, 18, 7]])
    print("matrice:", m)
    print("rank:", m.rank()) 

    m = Matrix([[0, 1, 0],
                [0, 0, 1],
                [0, 0, 0 ]])
    print("matrice:", m)
    print("rank:", m.rank()) 

    m = Matrix([[1+1j, 0],
                [0, 0]])
    print("matrice (complex):", m)
    print("rank:", m.rank())

    m = Matrix([[1+1j, 2+2j, 3],
                [2+2j, 4+4j, 6],
                [0, 0, 0]])
    print("matrice (complex 2):", m)
    print("rank:", m.rank())

if __name__ == "__main__":
    rank()
