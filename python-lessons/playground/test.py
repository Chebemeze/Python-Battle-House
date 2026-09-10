# import requests
# import json

# response = requests.get("https://api.github.com/users/octocat")
# data = response.json()
# with open("test.json", "w") as file:
#     json.dump(data, file, indent=4)

# from datetime import datetime, timezone
# future_date= datetime.fromisoformat("2026-08-22T01:58:05Z")
# now = datetime.now().astimezone()
# time_difference = future_date - now
# print(f"future date: {future_date}")
# print(f"now: {now}")
# print(f"time_difference: {time_difference}")

# new_dict = {}
# new_dict["first"] = new_dict.get("first", 0) + 1
# print(new_dict)

def bracket(a: str):
    length_of_string = len(a)
    num_of_runs = int(length_of_string/2)
    next_num = length_of_string - 1

    list_of_bracket_characters = {")": "(", "]": "[", "}": "{" }
    for j in range(num_of_runs):
        if a[j] == list_of_bracket_characters[a[next_num]]:
            next_num -= 1
        else:
            return False
    return True

c = bracket("(()[])")

print(c)

names = "Eben=Golden=Ben=Chris=Agu"
new_list = names.split("=",2)
print(new_list)