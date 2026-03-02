from matrix import Vector

def dot_product_vector():
    v1 = Vector([1,0])
    print(v1.dot(Vector([0,1])))
    print(v1.dot(Vector([1,0])))
    print(v1.dot(Vector([-1,0])))
    v1 = Vector([2,5])
    print(v1.dot(Vector([2,5])))
    v1 = Vector([2])
    print(v1.dot(Vector([1])))
    try:
        v1 = Vector([2])
        print(v1.dot(Vector([1,5])))
    except ValueError as v:
        print(v)
    v1 = Vector([7,54,198,74,1241,145,368])
    print(v1.dot(Vector([96,144,633,541,7470,779,2])))


if __name__=="__main__":
    dot_product_vector()