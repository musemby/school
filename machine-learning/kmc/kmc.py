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
				1. Validate the k value provided
				2. Determine the centroids of these k clusters [pick first k items not random]
				Repeat:
					i.   Get the centroid's coordinates for each cluster
					ii.  Calculate distance of each item to the centroid
					iii. Group each item (to the nearest cluster)  
	"""

	def validate_k(k):
		# obviously not 1 or equal to # of items otherwise what's the point?
		# on seconfd thought. We shall support it
		if (k == 1) or (k == len(data)):
			raise Exception("The k value cannot be 1 or same as number of items to cluster")
		return k

	def pick_centroids(k, data):
		centroids = data[:k]


if __name__ == '__main__':
	k_mean(2, two_atts)