def has_conflict(meetings):
    # TODO: return True if any two meetings overlap in time, False otherwise
    sorted_meeting = sorted(meetings)
    has_conflict = False
    for index, meeting in enumerate(sorted_meeting):
        if index == 0:
            prev = meeting
            continue
        if meeting[0] < prev[1] or meeting[1]<=prev[1]:
            has_conflict = True
            break
        prev = meeting
    return has_conflict

print(has_conflict([]))