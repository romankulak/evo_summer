import numpy as np

# Function generates 10*10*10 array with random integers [0;9]
def random_integers(low=0, high=9, elements=10, dimension=3):
    arr3d = np.random.randint(low, high=high, size=elements**dimension)
    return arr3d.reshape((elements,)*3)

vec = random_integers() # default 10*10*10 array with random integers [0;9]

# Function returns the maximum sum of columns and columns coordinates
def max_sum_coord(vec, n):
    coordinates=[]
    all_sum=[]
    for matrix in xrange(n):
        for column in xrange(n):
            for row in xrange(n):
                # summing throught all mutually perpendicular
                all_sum.append(sum(sum([vec[matrix,:,column],vec[matrix,row,:],vec[:,row,column]])))
                # coordinates appending
                coordinates.append([matrix,column,row])

    # maximum of sums
    max_index=all_sum.index(max(all_sum))
    return max(all_sum), coordinates[max_index]

n=vec.shape[0]
max_sum,coordinates=max_sum_coord(vec, n)

# Returns 3 perpendicular columns ( numpy arrays)  which sum is the maximum
def max_columns(vec, coordinates):
    matrix,column,row=coordinates[0],coordinates[1],coordinates[2]
    vectors = []
    return vec[matrix,:,column], vec[matrix,row,:], vec[:,row,column]

print max_columns(vec, coordinates)
