def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """

    a = set(relevant)
    top_k = recommended[:k]
    b = float(sum(1 for item in top_k if item in a))
    precision = b/k
    recall = b/len(a)
    return [precision,recall]