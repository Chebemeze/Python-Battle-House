def longest_streaks(daily_records):
    # Identify all students across every day, then track each student's
    # current and longest streak of consecutive "present" days

    longest_streak = {}
    temp_streak = {}
    is_absent = False
    for dictionary in daily_records:
        for key, value in dictionary.items():
            if value == "present":
                temp_streak[key]= temp_streak.get(key, 0)+1
            elif value == "absent":
                longest_streak[key]= temp_streak.get(key, 0)
                temp_streak[key] = 0
                is_absent = True
            
            if not is_absent:
                longest_streak[key] = temp_streak[key]

            # print(temp_streak[key])
            # print(longest_streak[key])
            if temp_streak[key] > longest_streak[key]:
                longest_streak[key]= temp_streak[key]

    return longest_streak

print(longest_streaks([{"Ada": "present"}, {"Bola": "present"}]))