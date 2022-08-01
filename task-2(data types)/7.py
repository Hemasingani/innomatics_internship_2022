def average(array):
    for n in range(0,101):
        array = set(array)
        avg = float(sum(array)/len(array))
    return avg
