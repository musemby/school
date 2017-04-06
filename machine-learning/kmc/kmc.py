import copy

from data.training_vectors import two_atts

"""
    Implementation of the k-means clustering algorithm
"""

def k_mean(k, data):
    """
        Given the number of clusters and items to cluster, the function should
        return k clusters with their items in them
        Takes `k` (number of clusters expected) as the first arg
            Steps:  
                1. Determine the centroids of these k clusters [pick first k items not random]
                Repeat:
                    i.   Get the centroid's coordinates for each cluster
                    ii.  Calculate distance of each item to the centroid
                    iii. Group each item (to the nearest cluster)  
    """

    def pick_centroids(k, data):
        centroids = copy.deepcopy(data[:k])
        k = 1
        for cent in centroids:
            cent['_centId'] = k
            cent['objects'] = []
            k += 1

        return centroids
        
    def compute_distances(centroids, data):
        for d in data:
            out = []
            for cent in centroids:
                dist = 0
                for key in cent.keys():
                    if (key == '_centId') or (key == 'objects'):
                        continue
                    dist = dist + (d[key] - cent[key])**2
                out.append({'_centId': cent['_centId'], 'distance': dist})
            
            cid = min(out, key=lambda x: x['distance'])['_centId']
            centroid = next((l for l in centroids if l['_centId'] == cid), None)
            centroid['objects'].append(d)

        import pdb
        pdb.set_trace()
        print centroids

    cents = pick_centroids(k, data)
    return compute_distances(cents, data)


if __name__ == '__main__':
    k_mean(4, two_atts)