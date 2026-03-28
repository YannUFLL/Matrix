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

if __name__ == "__main__":
    rank()
