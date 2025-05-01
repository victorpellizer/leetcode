def rank_scores(scores):
    # Pair each score with its original index
    indexed_scores = list(enumerate(scores))

    # Sort by score descending
    sorted_scores = sorted(indexed_scores, key=lambda x: -x[1])

    ranks = [0] * len(scores)
    current_rank = 1
    i = 0

    while i < len(sorted_scores):
        # Get all entries with the same score
        score = sorted_scores[i][1]
        j = i
        while j < len(sorted_scores) and sorted_scores[j][1] == score:
            j += 1
        # Assign current_rank to all these tied scores
        for k in range(i, j):
            idx = sorted_scores[k][0]
            ranks[idx] = current_rank
        # Increment rank by 1 (dense ranking)
        current_rank += 1
        i = j

    return ranks


scores = [3, 3, 3, 3, 5, 5, 5, 1]
print(rank_scores(scores))
