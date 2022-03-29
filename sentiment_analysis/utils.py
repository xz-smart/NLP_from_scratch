
def create_dict(words):
    """
    calculate the frequency of words in a list of words
    input: a list of words
    output: dict, key: word; value: frequency
    """
    output = {}
    for word in words:
        if word in output:
            output[word] += 1
        else:
            output[word] = 1
    return output
