"""
Implementation of the k-nearest nodes algorithm
"""

def knn(sample_data, test):
	"""
	Expects `sample_data` as a list of dicts with as many attributes as desired
	with the last one being the label i.e. 
	{
    'works_out': 3,
    'eats_vegies': 2,
    'healthy': 3
    }
    `healthy` is the label in this case
    The second arg is `test` a dict with n-1 fields where n is the number of
    fields in the sample data. The algorithm should compute this missing label
	"""
	
	# 1. Determine the k-value to use
		# - be an odd number
		# - not be a multiple of number of classes
