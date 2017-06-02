import copy
import csv
import json
import math
import random
import sys


class Centroid():
    def __init__(self, coordinates, _id):
        self.id = _id
        self.coordinates = coordinates
        self.elements = []
        self.previous_elements = []
        self.round = 1
        self.matches = 0
        self.mismatches = 0

    def __repr__(self):
        return 'Centroid: ' + str(self.id)

    @property
    def count(self):
        return len(self.elements)

    def add_element(self, element, _round):
        if self.round == _round:
            if element in self.elements:
                pass
            else:
                self.elements.append(element)
        else:
            self.round = _round
            if element in self.elements:
                self.matches += 1
            else:
                self.mismatches += 1
                self.elements.append(element)

    def recalculate_coordinates(self):
        x = (sum(y)/len(y) for y in zip(*self.elements))
        self.coordinates = x

    def reset_elements(self):
        self.matches = 0
        self.mismatches = 0

    @property
    def converged(self):
        return not self.mismatches


class Kmeans():
    def __init__(self):
        self.k = int(sys.argv[2])
        self.prepare_data()
        self.round = 1

    def prepare_data(self):
        filename = sys.argv[1]
        self.dataset = []
        with open(filename, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ')
            for row in reader:
                tuplified = tuple(map(float, row))
                self.dataset.append(tuplified)
        self.create_centroids()

    def create_centroids(self):
        self.centroids = []
        for i in xrange(self.k):
            chosen = random.choice(self.dataset)
            cent = Centroid(chosen, i+1)
            self.centroids.append(cent)

def main():
    k = Kmeans()
    def iterate(k):
        if k.round == 1:
            pass
        else:
            for centroid in k.centroids:
                centroid.recalculate_coordinates()
                centroid.reset_elements()
        for item in k.dataset:
            candidates = []
            for centroid in k.centroids:
                z = zip(item, centroid.coordinates)
                squares = map(lambda x: (x[0]-x[1])**2, z)  
                added = sum(squares)
                edistance = math.sqrt(added)
                candidates.append((centroid, edistance))
            winner = min(candidates, key=lambda x: x[1])
            winner[0].add_element(item, k.round)

        k.round += 1

        status_list = []
        for centroid in k.centroids:
            boole = centroid.converged
            status_list.append(boole)

        if False in status_list:
            iterate(k)
        return
    iterate(k)
    print "Reached convergence after {} rounds".format(k.round)
    print "Number of clusters: {}".format(k.k)

    data = {
        'number_of_clusters': k.k,
        'number_of_rounds_ran': k.round,
        'clusters': []
    }

    for centroid in k.centroids:
        ele = {
            'name': 'cluster_{}'.format(centroid.id),
            'elements': centroid.elements
        }
        data['clusters'].append(ele)

    with open('clusters.json', 'w') as file:
        json.dump(data, file, indent=4, sort_keys=False)
        print "Output written to clusters.json"

if __name__ == '__main__':
    main()
