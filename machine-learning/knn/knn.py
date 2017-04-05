import math
from collections import Counter
from .training_vectors import two_atts

"""
Implementation of the k-nearest nodes algorithm
"""

def knn(class_count, sample_data, test, label):
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
        # - equal to or greater than the number of classes

    def find_k():
        k = class_count + 1
        if (k % 2) == 0:
        	k += 1

        return k

    def euclidean_distance():
        for el in sample_data:
            d = 0
            for key in test.keys():
                d = d + (el[key] - test[key])**2
            el['distance'] = math.sqrt(d)

        return sorted(sample_data, key=lambda k: k['distance'])
    
    k = find_k()
    top_k_vals = euclidean_distance()[:k]
    label = Counter(i['healthy'] for i in top_k_vals).most_common(1)[0][0]
    return label


if __name__ == '__main__':
    test = {
        'works_out': 3,
        'eats_vegies': 3
    }
    print knn(5, two_atts, test, 'healthy')

# TODO: create a simple sample data generator for testing MLAs