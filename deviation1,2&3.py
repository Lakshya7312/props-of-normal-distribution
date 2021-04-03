import statistics
import csv
import pandas as pd

data = pd.read_csv("StudentsPerformance.csv")
height = data["writing score"]

mean = sum(height) / len(height)

median = statistics.median(height)

mode = statistics.mode(height)

deviation = statistics.stdev(height)

first_stddev_start, first_stddev_end = mean - deviation, mean + deviation
listoffirst_stddev = [result for result in height if result > first_stddev_start and result < first_stddev_end]
print("{}%".format(len(listoffirst_stddev) * 100 / len(height)))

second_stddev_start, second_stddev_end = mean - (2 * deviation), mean + (2 * deviation)
listofsecond_stddev = [result for result in height if result > second_stddev_start and result < second_stddev_end]
print("{}%".format(len(listofsecond_stddev) * 100 / len(height)))

third_stddev_start, third_stddev_end = mean - (3 * deviation), mean + (3 * deviation)
listofthird_stddev = [result for result in height if result > third_stddev_start and result < third_stddev_end]
print("{}%".format(len(listofthird_stddev) * 100 / len(height)))