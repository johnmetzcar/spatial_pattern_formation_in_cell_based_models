"""
Script used to build a Scree Plot from PhysiCell data
"""
import scipy.io as sio

def get_coordinates_file(data_file):
    data = sio.loadmat(data_file)
    
    return data

def k_means(k, data_set):
    clusters = {}

def build_scree_plot(data_file):
    # Get data from file
    data = get_coordinates_file(data_file)["cells"]

    # Get the coordinates into a friendly file
    coords = []
    for i in range(len(data[0])):
        if int(data[5,i]) != 2:
            coords.append( (int(data[5,i]), (data[1,i], data[2,i]) ) )
    
    # Run successive k-means clustering

if __name__ == '__main__':
    # Get data from file
    print("Test: get_coordinates_file()")
    data = get_coordinates_file("test.mat")
    #print(data)
    #print(data["cells"])
    print(data["cells"][5,0])

    # Make plot
    print("\nTest: build_scree_plot")
    build_scree_plot("test.mat")