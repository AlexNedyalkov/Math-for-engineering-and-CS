import numpy as np


# columns rainy, nice, cloudy - today
# row rainy, nice, cloudy - tomorrow
A = np.array([[0.5, 0.5, 0.25],
    [0.25, 0, 0.25],
    [0.25, 0.5, 0.5]])

# Assume today is rainy
probability_today = [1, 0, 0]

for i in range(50):
    probability_tomorrow = np.dot(A, probability_today)
    probability_today = probability_tomorrow

print(probability_tomorrow)