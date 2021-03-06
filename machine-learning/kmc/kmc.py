from __future__ import division
import copy

"""
    Implementation of the k-means clustering algorithm
"""


def set_identifier(arr, identifier_name):
        """ Give me an list of dicts and I shall give each dict an identifier
            matching the identifier_name
        """
        k = 1
        for a in arr:
            a[identifier_name] = k
            k += 1

        return arr


def preparation(k, data):
    """
        Prep work for the algorithm namely:
            1. Get the centroids given k
            2. Give each cluster an identifier
            3. Initialize objects --> holds data items in that cluster
            4. Give each data item an identifier
            5. Initialize current_clusters list
    """
    centroids = copy.deepcopy(data[:k])
    for cent in centroids:
        cent['objects'] = []

    set_identifier(centroids, '_centId')
    set_identifier(data, '_id')

    return (centroids, data)

centroids, data = preparation(k, data)


def k_mean(centroids, data):
    """
        Given the number of clusters and items to cluster, the function should
        return k clusters with their items in them
        Takes `k` (number of clusters expected) as the first arg
            Steps:  
                1. Determine the centroids of these k clusters [pick first k items not random(for now)]
                Repeat:
                    i.   Get the centroid's coordinates for each cluster
                    ii.  Calculate distance of each item to the centroid
                    iii. Group each item (to the nearest cluster)  
    """
    # current round and current state of clusters
        
    status = []
    def similar(x, y):
        cids = [i._centId for i in x]
        for cid in cids:
            yaX = next((d for d in x if d.id == cid), None)['objects']
            yaY = next((d for d in y if d.id == cid), None)['objects']
            if len(yaX) != len(yaY): # if there is different number of objects there is no need to keep going
                return False
            else:
                # setify for easier comparison
                idsX = {j._id for j in yaX}
                idsY = {k._id for k in yaY}

                return idsX == idsY

    def cluster(centroids, data):
        for d in data:
            out = []
            for cent in centroids:
                dist = 0
                for key in cent.keys():
                    if key in ['_centId', 'objects', '_id']:
                        continue
                    dist = dist + (d[key] - cent[key])**2
                out.append({'_centId': cent['_centId'], 'distance': dist})
            
            cid = min(out, key=lambda x: x['distance'])['_centId']
            centroid = next((l for l in centroids if l['_centId'] == cid), None)
            centroid['objects'].append(d)
        return centroids

    new_cents = cluster(centroids, data)

    if similar(status, new_cents):
        return new_cents

    status = new_cents
    for cent in new_cents:
        for key in cent['objects'][0].keys(): # get keys from first sample
            if key == '_id':
                continue
            val = 0
            sm = sum(i[key] for i in cent['objects'])
            size = len(cent['objects'])
            cent[key] = round(sm / size, 3)
    compute_distances(new_cents, data)

    cents = compute_distances(centroids, data)
    print cents


if __name__ == '__main__':
    centroids, data = preparation(4, data)
    k_mean(centroids, two_atts)
