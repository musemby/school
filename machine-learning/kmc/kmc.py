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
        centroids = data[:k]

if __name__ == '__main__':
    k_mean(2, two_atts)