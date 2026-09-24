def path_hits_blocked(blocked, path):
    # TODO: check whether any position in `path` also appears in `blocked`
    hits_blocked = False
    for path_n in path:
        if path_n in blocked:
            hits_blocked = True
            break
    return hits_blocked
print(path_hits_blocked({(1,1), (2,2)}, [(0,0), (1,1)]))
