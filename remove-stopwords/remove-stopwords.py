def remove_stopwords(tokens: list, stopwords: list) -> list:
    """
    Returns a list of tokens.
    """
    block = set(stopwords)
    return [token for token in tokens if token not in block]