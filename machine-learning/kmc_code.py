import sys
import math
import random
import collections

num_itr = 50
in_itr = num_itr
start = 0
itt = 0
obj = []
cnt = 0
stini = [[] for c in range(num_itr)]

def creatingDataset():

    # opening files
    file1 = sys.argv[1]
    datafile = open(file1)
    data = []
    data_line = datafile.readline()
    # reading dataset files
    while (data_line != ''):
        data_value = data_line.split(',')
        data_value_no = []
        for i in range(len(data_value)):
            # import pdb; pdb.set_trace()
            data_value_no.append(float(data_value[i]))
        # creating data matrix
        data.append(data_value_no)
        data_line = datafile.readline()
    datafile.close()
    num_clusters=int(sys.argv[2])
    findInitials(data, num_clusters)

def findInitials(data,num_clusters):
    global in_itr
    for i in range(num_itr):
        initial = random.sample(data, num_clusters)
        stini[i] = initial
        old_centroid = []
        rt = kmeans(data, num_clusters, initial,old_centroid)
        if(rt == 0):
            in_itr -= 1
            continue


def kmeans(data, k , centroids,old_centroid):
    # Pick out k random points to use as our initial centroids
    global cnt
    lists = [[] for c in range(k)]
    rows = len(data)
    cols = len(data[0])
    number_centroid = len(centroids)
    distance =[]
    min_dis = 0

    for i in range(rows):
        distance = []
        for j in range(number_centroid):
            c = math.sqrt(sum([(a - b) ** 2 for a, b in zip(data[i], centroids[j])]))
            distance.append(c)
        if not distance:
            break
        index = distance.index(min(distance))
        lists[index].append(data[i])
        min_dis = sum(distance)

    summ = 0
    for i in range(len(centroids)):
        summ += sum(centroids[i])

    if(old_centroid != centroids):
        old_centroid = centroids;
        rt = calculateMean(data,k,lists,old_centroid)
        if(rt == 0):
            cnt += 1
            return 0
    else:
        if (start == 1):
            calculateOutput(data, lists)
        if (start == 0):
            pickupInitial(data,k,summ)


def calculateMean(data,k,lists,old_centroid):
    list_number = len(lists)
    mean_list = []
    for num in range(list_number):
        list = lists[num]
        if not list:
            return 0
        rows = len(list)
        cols = len(list[0])
        mean_lists =[]
        for j in range(cols):
            mean = float(0)
            count = 0.0001
            for i in range(rows):
                mean += float(list[i][j])
                count = count + 1
            mean = mean / count
            mean_lists.append(mean)
        mean_list.append(mean_lists)
    pt = kmeans(data,k,mean_list,old_centroid)
    if(pt == 0):
        return 0

def calculateOutput(data,lists):
    for i in range(len(data)):
        data_value = data[i]
        for j in range(len(lists)):
            if(data_value in lists[j]):
                print(j," ",i)
                break

def pickupInitial(data,k,summ):
    obj.append(summ)
    if(len(obj) == in_itr):
        index = obj.index(min(obj))
        findCluster(data,k,stini[index])

def findCluster(data,k,centroid):
    global start
    start = 1
    old_centroid =[]
    kmeans(data, k, centroid, old_centroid)

creatingDataset()