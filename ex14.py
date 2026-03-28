from matrix import Vector, Matrix, projection

def test():
    fov = 90.0
    ratio = 1.0
    near = 0.1
    far = 100.0

    try:
        proj_mat = projection(fov, ratio, near, far)
        
        for i in range(4):
            row = proj_mat.data[i]
            print(f"{row[0]}, {row[1]}, {row[2]}, {row[3]}")
            
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    test()