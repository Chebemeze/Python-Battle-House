def rank_players(scores):
    new_dict = {}
    leader_board = []
    for name, score in scores:
        new_dict[name]= new_dict.get(name, score)

    maxim_num = max(new_dict.values())

    index = 0
    rank = index+1
    for name, score in new_dict.items():
        if score == maxim_num:
            score_tupple = (name, rank)
            leader_board.append(score_tupple)
        elif score < maxim_num:
            maxim_num = score #updates maximum score to the current score
            score_tupple = (name, index+1)
            leader_board.append(score_tupple)
            rank = index+1 # updates the rank to the curent rank
 
        index += 1

    return leader_board

print(rank_players([("A", 10), ("B", 10), ("C", 10), ("D", 8)]))
print(rank_players([("Ada", 100), ("Bola", 90), ("Chidi", 80)]))
print(rank_players([("Ada", 100), ("Bola", 100), ("Chidi", 90)]))
print(rank_players([("Ada", 50)]))

#Note: sort can be used to improve this function such that the arguments passed to
# rank_players() doesnt have to be ordered, the only side effect is that order of the final
# result - leader_board will be different from the input entered if done.
    #sorted_dict = sorted(new_dict.items(), key= lambda x: x[1])
    #sorted returns a list of tupple whent the iterable is a dictionary