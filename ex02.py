from matrix import Matrix, Vector, lerp

def linear_interpolation_scalar():
    print(lerp(42, 100, 0))
    print(lerp(100, 100, 1))
    print(lerp(2.1, 1.05, 0.7))
    print(lerp(18, 5, 0.2))

def linear_interpolation_vector():
    v1 = Vector([42,42])
    v2 = Vector([100, 100])

    print(lerp(v1, v2, 0.0))
    print(lerp(v1, v2, 1.0))

    v1 = Vector([1,1])
    v2 = Vector ([2,2])
    v3 = lerp(v1, v2, 0.7)

    print(v3)

def linear_interpolation_matrix():
    m1 = Matrix([[100,100],
                 [100,100]])
    m2 = Matrix([[42,42],
                 [42,42]])
    print(lerp(m1,m2,0.0))
    print(lerp(m1,m2,1.0))

    m1 = Matrix([[0,6],
                 [1,5]])
    m2 = Matrix([[2,3],
                 [4,5]])
    m3 = lerp(m1, m2, 0.7) 
    print(m3)


if __name__ == "__main__":
    linear_interpolation_scalar()
    linear_interpolation_vector()
    linear_interpolation_matrix()

