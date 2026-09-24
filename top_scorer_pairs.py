def top_scorers(results):
    # TODO: find the highest score, collect all players who achieved it,
    # and return their names as a sorted tuple
    highest_score = 0
    score_sheet= []
    for player, score in results:
        if highest_score < score:
            highest_score = score
            score_sheet.append(player)
        elif highest_score == score:
            score_sheet.append(player)
    return tuple(sorted(score_sheet))

print(top_scorers([("Ada", 90), ("Bola", 90)]))
