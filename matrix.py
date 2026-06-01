import math

def is_zero(x, epsilon=1e-10):
    return abs(x) < epsilon

class Vector: 
    def __init__(self, data):
        self.data = list(data)

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        content = " ".join(str(v) for v in self.data)
        return f"[{content}]"

    def __setitem__(self, index, value):
        self.data[index] = value

    def size(self):
        return len(self.data)
    
    def reshape(self, rows, cols):
        if rows * cols > self.size():
            raise ValueError("Dimensions incompatibles")
        new_data = []
        for i in rows:
            new_data.append(self.data[ i * cols : i * cols + cols])
        return Matrix(new_data)

    def copy(self):
        return Vector(self.data.copy())
    
    def add(self, v):
        if v.size() != self.size():
            raise ValueError("Size incompatibles")
        else:
            for i in range(v.size()):
                self.data[i] += v[i]

    def sub(self, v):
        if v.size() != self.size():
            raise ValueError("Size incompatibles")
        else:
            for i in range(v.size()):
                self.data[i] -= v[i]

    def scl(self, a):
        for i in range(self.size()):
            self.data[i] *= a

    def dot(self, v):
        if not isinstance(v, Vector):
            raise ValueError("dot excepts one Vector instance as argument.")
        if self.size() != v.size():
            raise ValueError("Size incompatibles")
        res = 0
        for i in range(v.size()):
            res += self[i].conjugate() * v[i]
        return res

    def norm_1(self):
        n1 = 0
        for i in range(self.size()):
            n1 += abs(self[i])
        return n1 

    def norm(self):
        n1 = 0
        for i in range(self.size()):
            val = self[i]
            if isinstance(val, complex):
                n1 += val.real**2 + val.imag**2
            else:
                n1 += val * val
        return n1 ** 0.5

    def norm_inf(self):
        n1 = 0
        for i in range(self.size()):
            n1 = max(n1, abs(self[i]))
        return n1



class Matrix:
    def __init__(self, data):
        self.data = [[x for x in row] for row in data]  

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        res = "[\n"
        for row in self.data:
            res += f"  {row}\n"
        res += "]"
        return res
    
    def shape(self):
        return (len(self.data), len(self.data[0]) if self.data else 0)

    def is_square(self):
        s = self.shape()
        return s[0] == s[1]

    def reshape(self):
        flat = []
        for row in self.data:
            flat.extend(row)
        return Vector(flat)

    def copy(self):
        new_data = [row.copy() for row in self.data]
        return Matrix(new_data)

    def add(self, m):
        if m.shape() != self.shape():
            raise ValueError("Size incompatibles")
        row, col = m.shape()
        for i in range(row):
            for j in range(col):
                self.data[i][j] += m[i][j]

    def sub(self, m):
        if m.shape() != self.shape():
            raise ValueError("Size incompatibles")

        rows, cols = self.shape()
        for i in range(rows):
            for j in range(cols):
                self.data[i][j] -= m[i][j]

    def scl(self, a):
        rows, cols = self.shape()
        for i in range(rows):
            for j in range(cols):
                self.data[i][j] *= a

    def mul_vec(self, vec):
        if not isinstance(vec, Vector):
            raise ValueError("mul_vec excepts a matrice instance as argument.")
        m_rows, m_cols = self.shape()
        v_rows = vec.size()
        ret = Vector([0.0] * m_rows)
        tmp = 0
        if m_cols != v_rows:
            raise ValueError("The number of matrice column must be the same as vector row")
        for i in range(m_rows):
            tmp = 0
            for j in range (m_cols):
                tmp += self[i][j] * vec[j]
            ret[i] = tmp
        return ret

    def mul_mat(self, mat):
        if not isinstance(mat, Matrix):
            raise ValueError("mul_mat excepts a matrice instance as argument.")
        
        m1_rows, m1_cols = self.shape()
        m2_rows, m2_cols = mat.shape()
        if m1_cols != m2_rows:
            raise ValueError("The number of matrice column must be the same as vector row")
        res_data = [[0.0 for _ in range(m2_cols)] for _ in range(m1_rows)]
        tmp = 0
        for i in range(m1_rows):
            for j in range (m2_cols):
                tmp = 0
                for k in range (m2_rows):
                    tmp += self[i][k] * mat[k][j]
                res_data[i][j] = tmp
        return Matrix(res_data)

    def trace(self):
        m_rows, m_cols = self.shape()
        if (m_rows != m_cols): 
            raise ValueError("Can't compute trace with no square Matrix.")
        t = 0
        for i in range(m_rows):
            t += self[i][i]
        return (t)

    def transpose(self):
        m_rows, m_cols = self.shape()
        r = Matrix([[0.0 for _ in range(m_rows)] for _ in range(m_cols)])
        for i in range(m_rows):
            for j in range(m_cols):
                r[j][i] = self[i][j]
        return (r)

    def _forward_elimination(self, normalize=False):
        m_rows, m_cols = self.shape()
        r = Matrix([[self[i][j] for j in range(m_cols)] for i in range(m_rows)])
        p_y = 0
        i = 0
        swaps = 0
        while i < m_rows and p_y < m_cols:
            tmp = 0 
            line_to_swap = i
            # step 1: find the pivot (a big pivot allow lower loose of float precision when we divided)
            for j in range(i, m_rows):
                if abs(r[j][p_y]) > tmp and not is_zero(r[j][p_y]):
                    tmp = abs(r[j][p_y])
                    line_to_swap = j
            if tmp == 0:
                p_y += 1
                continue
            
            # step 2: swap line
            if line_to_swap != i:
                tmp = r[i]
                r.data[i] = r.data[line_to_swap]
                r.data[line_to_swap] = tmp
                swaps += 1
            # step 3: elimination of the others unknow bellow the pivot
            for j in range(i + 1, m_rows):
                if is_zero(r[i][p_y]):
                    continue
                factor = r[j][p_y] / r[i][p_y] 
                # factorisation of the line
                # elimination of x 
                for k in range(p_y, m_cols):
                    r[j][k] -= (r[i][k] * factor)

            # step 4: normalisation of the diagonale
            if normalize:
                pivot = r[i][p_y]
                if not is_zero(pivot):
                    for j in range(p_y, m_cols):
                        r[i][j] /= pivot
            p_y += 1 
            i += 1
        return(r, swaps)


    def row_echelon(self):
        r,_ = self._forward_elimination(True)
        m_rows, m_cols = self.shape()
        # if a pivot is found, elimination of the other unknows above him
        for i in range(m_rows - 1, -1, -1):
            p_y = -1
            # search of the first pivot
            for c in range(i, m_cols):
                if not is_zero(r[i][c]):
                    p_y  = c
                    break; 
            if p_y == -1:
                continue
            for j in range(i - 1, -1, -1):
                if not is_zero(r[j][p_y]):
                    factor = r[j][p_y] / r[i][p_y]
                    for k in range(p_y, m_cols):
                        r[j][k] -= (r[i][k] * factor)
        return(r)


    def determinant(self):
        m_rows, m_cols = self.shape()
        if m_rows != m_cols:
            raise ValueError("Matrix must be square to compute determinant.")
        if m_rows > 4:
            raise ValueError("Determinant for matrices larger than 4x4 is not implemented.")
        if m_rows == 1:
            return self[0][0]
        # Cramer rule
        if m_rows == 2: 
            return ((self[0][0] * self[1][1]) - (self[0][1] * self[1][0]))
        # Saru rule
        if m_rows == 3:
            return (((self[0][0] * self[1][1] * self[2][2]) 
                    + (self[0][1] * self[1][2] * self[2][0])
                    + (self[0][2] * self[1][0] * self[2][1])) - 
                     ((self[0][2] * self[1][1] * self[2][0])
                    + (self[0][0] * self[1][2] * self[2][1])
                    + (self[0][1] * self[1][0] * self[2][2])))
        # Gauss method
        if m_rows == 4:
            m_ech, swaps = self._forward_elimination(False)
            det = m_ech[0][0] * m_ech[1][1] * m_ech[2][2] * m_ech[3][3]
            if swaps % 2 != 0:
                det = -det
            return  (det)

    def inverse(self):
        m_rows, m_cols = self.shape()
        if m_rows != m_cols:
            raise ValueError("Only square matrice can be inverted.")
        m_ref,_ = self._forward_elimination(False)
        d = m_ref[0][0]
        for i in range(1, m_rows):
            d *= m_ref[i][i]
        if is_zero(d):
            raise ValueError("Matrix is singular, no inverse exists.")
        augmented_data = Matrix([[self[i][j] for j in range(m_cols)] + [ 0 if j != i else 1 for j in range (m_cols)]for i in range(m_rows)])
        res_rref = augmented_data.row_echelon()
        inverse_data = Matrix([res_rref[row][m_cols:] for row in range(m_rows)])
        return(inverse_data)

    def rank(self):
        m_ech, _ = self._forward_elimination(False)
        m_rows, m_cols = m_ech.shape()
        rank  = 0
        for i in range(m_rows):
            for j in range (m_cols):
                if not is_zero(m_ech[i][j]):
                    rank += 1
                    break
        return (rank)

def linear_combination(u : list, coefs : list):
    if not isinstance(u, list):
        raise ValueError("linear_combination excepts a list of Vector instances as first argument.")
    if len(u) != len(coefs):
        raise ValueError("Size incompatibles")

    v_size = u[0].size()
    new_vector = Vector([0.0] * v_size)

    for i in range(len(u)):
        temp = Vector(u[i].data.copy())
        temp.scl(coefs[i])
        new_vector.add(temp)

    return new_vector

def lerp(u, v, t):
    if isinstance(u , Vector) or isinstance(u, Matrix):
        res = u.copy()
        res.scl(1-t)
        temp = v.copy()
        temp.scl(t)
        res.add(temp)
        return (res)
    else:
        return (u * (1 - t) + v * t)

def angle_cos(u,v):
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise ValueError("angle_cos excepts two Vector instances as arguments.")
    if u.size() != v.size():
        raise ValueError("Size incompatibles.")
    norm_u = u.norm()
    norm_v = v.norm()
    if norm_u == 0 or norm_v == 0:
        raise ValueError("Cannot compute angle with zero vector.")
    dot = u.dot(v)
    if isinstance(dot, complex):
        dot = abs(dot)
    cos = dot / (norm_u * norm_v)
    return cos

def cross_product(u, v):
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise ValueError("cross_product excepts two Vector instances as arguments.")
    x = u[1] * v[2] - u[2] * v[1]
    y = - (u[0] *  v[2]- u[2] *v[0])  
    z =  u[0] * v[1]- u[1] * v[0]
    return Vector([x,y,z])

def projection(fovY, aspectRatio, near, far):
    rad_fovY = math.radians(fovY)
    tangent = math.tan(rad_fovY / 2)
    top = near * tangent
    right = top * aspectRatio
    
    p_matrice = Matrix([[(near / right), 0, 0, 0],
                        [0, near/top, 0, 0], 
                        [0, 0, -far / (far - near), -(far * near) / (far - near)], 
                        [0, 0, -1, 0]])
    return p_matrice.transpose()