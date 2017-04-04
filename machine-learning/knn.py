"""
Implementation of the k-nearest nodes algorithm
"""

def knn(class_count, sample_data, test):
	"""
	Expects `class_count`, number of possible different classes, as first arg 
	Expects `sample_data` as a list of dicts with as many attributes as desired
	with the last one being the label i.e. 
	{
	    'works_out': 3,
	    'eats_vegies': 2,
	    'healthy': 3
    }
    `healthy` is the label in this case [ranges from 1 to 5]
    The third arg is `test` a dict with n-1 fields where n is the number of
    fields in the sample data. The algorithm should compute this missing label
	"""
	
	# 1. Determine the k-value to use
		# - be an odd number
		# - not be a multiple of number of classes
	def find_key():
		spl = sample_data[0]
		num = len(spl.keys()) - 1 # minus the label
		if (num % 2) == 0: # even
			num += 1 # oddify
			k = num
		else:
			k = num



		return k



