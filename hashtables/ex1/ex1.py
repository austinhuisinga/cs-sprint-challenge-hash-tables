def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    weights_dict = {i: limit - weights[i] for i in range(0, length)}
    answer = None

    for j in weights_dict:
        if weights_dict[j] in weights:
            answer = (j, weights.index(weights_dict[j]))
            
    return answer


