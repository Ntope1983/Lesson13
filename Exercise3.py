# Accepts an arbitrary number of numeric arguments (*floats),
# sums them, and returns their arithmetic mean.

def float_average(*floats):
    sum1=0
    for float in floats:
        sum1+=float
    return sum1/len(floats)


print(float_average(2.5,3.5,4.5,2.1,3.5))