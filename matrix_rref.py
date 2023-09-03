import numpy as np

def is_zero_col(v):
    return np.all(v == 0)

def get_indices(v, i):
    while v[i] == 0:
        i += 1
    
    return i

def get_pivot_element(m, i, j):
    # Get non-zero columm
    while i < m.shape[0] and is_zero_col(m[:, i]):
        i += 1
    
    # Get row from column
    j = get_indices(m[:, i], j)

    return i, j

def is_ref(m):
    is_ref = True
    i = 0
    lead_ind = -1

    while i < m.shape[0] and is_ref:
        j = 0
        has_lead = False

        while j < m.shape[1] and not(has_lead) and is_ref:
            if m[i][j] == 1:
                if j > lead_ind:
                    has_lead = True
                    lead_ind = j
                else:
                    is_ref = False
            elif m[i][j] == 0:
                j += 1
            else:
                is_ref = False
        
        if not(has_lead) and i != m.shape[0] - 1:
            is_ref = False

        i += 1
    
    return is_ref

def ref(m):
    i = 0
    j = 0

    while(not(is_ref(m))):
        c, r = get_pivot_element(m, i, j)

        # Swap pivot row and index row
        m[[i, r]] = m[[r, i]]

        # multiply inv(m[pR][pC]) * m[pR]
        m[i] = (1.0 / m[i][j]) * m[i]

        for k in range(i+1, m.shape[0]):
            m[k] = -1.0 * m[k][j] * m[i] + m[k]

        i += 1
        j += 1
        

    print(m)

def is_rref(m):
    is_rref = True

    if is_ref(m):
        i = 0
        j = 0
        while i < m.shape[0]:
            is_col_clear = False

            while j < m.shape[1] and not(is_col_clear) and is_rref:
                if m[i][j] == 1 and np.count_nonzero(m[:,j]) == 1: 
                    is_col_clear = True
                    j += 1
                elif m[i][j] == 0:
                    j += 1
                else:
                    is_col_clear = False
                    is_rref = False
            
            # Zero row
            if not(is_col_clear) and np.count_nonzero(m[i,:]) != 0:
                is_rref = False

            i += 1
    else:
        is_rref = False

    return is_rref

def rref(m):
    pass

"""
[[ 1.   1.  -2.5  1.   2. ]
 [ 0.   0.   2.   3.   4. ]
 [ 0.   2.   3.  -4.   1. ]
 [ 0.  -2.  -1.   7.   3. ]]

 [ 1.   1.  -2.5  1.   2. ]
 [ 0.   1.   1.5 -2.   0.5]
 [ 0.   0.   1.   1.5  2. ]
 [ 0.   0.   0.   0.   0. ]
"""

mA = np.array([ [0, 2, 3, -4, 1],
                [0, 0, 2, 3, 4],
                [2, 2, -5, 2, 4],
                [2, 0, -6, 9, 7]])

mB = np.array([ [0.0, 2.0, 3.0, -4.0, 1.0],
                [0.0, 0.0, 2.0, 3.0, 4.0],
                [2.0, 2.0, -5.0, 2.0, 4.0],
                [2.0, 0.0, -6.0, 9.0, 7.0]])

mC = np.array([[1,2,4],
               [1,3,1],
               [-1,4,-1]])

mD = np.array([[1,2,4],[0,1,-3],[0,0,1]])

mI = np.array([[1,0,0],[0,1,0],[0,0,1]])

mE = np.array([[1,0,0,0,4],
               [0,0,1,0,3]])

print(is_ref(mI))
print(is_rref(mI))

print(is_ref(mB))
print(is_rref(mB))

print(is_ref(mI))
print(is_rref(mI))