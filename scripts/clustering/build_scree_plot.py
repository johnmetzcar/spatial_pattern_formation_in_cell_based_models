"""
Script used to build a Scree Plot from PhysiCell data
"""
import scipy.io as sio
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import random, operator

def plotClusters(clusters):
    colors = ('r','b','y')
    marker = ('.','.','.')
    x = ([], [], [])
    y = ([], [], [])

    for i in clusters:
        x[2].append(i[0])
        y[2].append(i[1])
        for j in clusters[i]:
            if i != j[1]:
                x[j[0]].append(j[1][0])
                y[j[0]].append(j[1][1])

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    # A cells
    ax.scatter(x[0], y[0], color='blue', marker='.')
    # B cells
    ax.scatter(x[1], y[1], color='#FFFF00', marker='.', label='0')
    # Centers
    ax.scatter(x[2], y[2], color='red', marker='^', label='1')
    counter = 0
    for i in clusters:
        ax.add_patch(patches.Circle( i, radius=cluster_size(i, clusters[i]), facecolor='none', edgecolor='r'))
        counter = counter + 1
    #plt.xlim(-250,250)
    #plt.ylim(-250,250)
    plt.show()

def plotSkree(data):
    x = []
    y = []

    for i in range(len(data)):
        x.append(data[i][0])
        y.append(data[i][1])

    plt.plot(x, y, color='red', marker='.')
    plt.show()

def cluster_size(center, cluster):
    max_distance = 0

    for i in range(len(cluster)):
        dist = EulerDistance(center, cluster[i][1])
        if dist > max_distance:
            max_distance = dist

    return max_distance

def EulerDistance(p1, p2):
    dist = 0
    assert len(p1) == len(p2)

    for i in range(len(p1)):
        dist += pow((p1[i] - p2[i]), 2)

    return pow(dist, 0.5)

def Centers_To_Clusters(centers, points):
    clusters = {}
    for i in centers:
        clusters[i] = []

    for i in points:
        minCenter = centers[0]
        minVal = EulerDistance(i[1], centers[0])
        for j in range(1, len(centers)):
            if EulerDistance(i[1], centers[j]) < minVal:
                minCenter = centers[j]
                minVal = EulerDistance(i[1], centers[j])
        clusters[minCenter].append(i)

    return clusters

def Clusters_To_Centers(m, clusters):
    centers = []
    for i in clusters:
        length = len(clusters[i])

        if length != 0:
            centerComponents = tuple([0]*m)
            for j in clusters[i]:
                centerComponents = tuple(map(operator.add, centerComponents, j[1]))
            centers.append(tuple(map(operator.truediv, centerComponents, tuple([length]*m))))
        else:
            centers.append(i[1])

    return centers

"""
    Take two m dimentional coordinates c1 and c2 and return True if they are the same, False if not
"""
def same(c1, c2):
    if c1 == None or c2 == None:
        return False

    compare = c2.copy()

    for i in c1:
        if i not in compare:
            return False
        del compare[compare.index(i)]

    if len(compare) > 0:
        return False

    return True

"""
    k = number of clusters
    m = dimensions
    point = array of points (each point is a touple)
"""
def K_MeanClustering(k, m, points):
    assert len(points) >= k

    centers = []
    clusters = {}
    for i in range(k):
        centers.append(points[i][1])

    old_centers = None
    while not same(centers, old_centers):
        clusters = Centers_To_Clusters(centers, points)
        #print("cen to clu", clusters)
        #plotClusters(clusters)

        centers, old_centers = Clusters_To_Centers(m, clusters), centers

    return clusters

"""
    Caculates within cluster sum of squares by cluster given clusters
    https://discuss.analyticsvidhya.com/t/what-is-within-cluster-sum-of-squares-by-cluster-in-k-means/2706
    https://stats.stackexchange.com/questions/147007/a-proof-of-total-sum-of-squares-being-equal-to-within-cluster-sum-of-squares-and?newreg=022352a1252c4586900dcdb9fea23b01
"""
def WSS(clusters):
    # Calculate mean
    wss = 0

    for i in clusters:
        for j in range(len(clusters[i])):
            wss += (EulerDistance(clusters[i][j][1], i)) **2

    return wss
    

def build_scree_plot(start_k, end_k, m, points):
    # Run successive k-means clustering
    results = []
    for k in range(start_k, end_k):
        clusters = K_MeanClustering(k, m, points)
        #plotClusters(clusters)
        wss = WSS(clusters)
        results.append( (k, wss) )
    print(results)
    plotSkree(results)

def load_iris(path):
    f = open(path, 'r').readlines()
    data = []

    for i in range(1, len(f)):
        row = f[i].split(',')
        row = row[:-1]

        for j in range(0, len(row)):
            row[j] = float(row[j])

        data.append((0, tuple(row)))

    return data

if __name__ == '__main__':
    data = load_iris("iris.csv")
    build_scree_plot(2, 15, 4, data)

    exit()


    print("\nTest: build_scree_plot")
    # Get data from file
    data = sio.loadmat("test.mat")["cells"]

    # Get the coordinates into a friendly file
    coords = []
    for i in range(len(data[0])):
        if int(data[5,i]) != 2:
            coords.append( (int(data[5,i]), (data[1,i], data[2,i]) ) )
    build_scree_plot(2, 15, 2, coords)
 
    exit()

    # Test data from https://rpubs.com/GourabNath/Loopfunctionapplications
    points = [ [5.1, 3.5, 1.4, 0.2], [4.9, 3.0, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2], [4.6, 3.1, 1.5, 0.2], [5.0, 3.6, 1.4, 0.2], [5.4, 3.9, 1.7, 0.4],]
    build_scree_plot(2, 4, 4, points)