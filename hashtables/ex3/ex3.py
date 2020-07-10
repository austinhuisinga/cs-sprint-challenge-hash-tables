def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}

    for i in range(len(arrays)):
        for j in arrays[i]:
            if j not in cache:
                cache[j] = 1
            else:
                cache[j] += 1
    
    arr = []

    for key, value in cache.items():
        if value >= len(arrays):
            arr.append(key)
    
    return arr


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
