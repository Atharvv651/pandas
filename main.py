import numpy
import pandas
import string

exam_data = {
    'name': ['Paul', 'Anna', 'Tom', 'Lucy', 'John', 'Mike', 'Sophia', 'Emma', 'Chris', 'Olivia'],
    'score': [85, 92, numpy.nan, 78, 88, 95, numpy.nan, 80, 90, 84],
    'attempts': [1, 2, 1, 3, 2, 1, 3, 1, 2, 3],
    'qualify': ['yes', 'yes', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'no']
}

lables = list(string.ascii_lowercase[:10])

data_frame = pandas.DataFrame(exam_data, index=lables)
print(data_frame)
