from matrix import Vector, angle_cos


def cos_vector():
    v = Vector([1,0])
    print(angle_cos(v, Vector([1,0])))
    print(angle_cos(v, Vector([0,1])))
    print(angle_cos(v, Vector([-1,0])))
    print(angle_cos(v, Vector([100,0])))
    print(angle_cos(v, Vector([0,100])))
    print(angle_cos(v, Vector([-100,0])))
    print(angle_cos(v, Vector([1,1])))
    print(angle_cos(v, Vector([10,10])))
    v = Vector([3])
    print(angle_cos(v, Vector([9])))
    print(angle_cos(v, Vector([-4])))
    try:
        print(angle_cos(v, Vector([0])))
    except ZeroDivisionError as e:
        print(e)
    v = Vector([18,27,47])
    print(angle_cos(v, Vector([31,-45,41])))
    print(angle_cos(v, Vector([18,27,47])))
    v = Vector([0,2])
    print(angle_cos(v, Vector([2,2])))
    print(angle_cos(v, Vector([2,1])))
    print(angle_cos(v, Vector([1.732,1])))
    
if __name__ == "__main__":
    cos_vector()
