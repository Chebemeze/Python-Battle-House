def course_order(num_courses, prerequisites):
    # TODO: produce a valid ordering of courses respecting all prerequisites,
    # always choosing the lowest-numbered available course next.
    # Return [] if no valid ordering exists.
    
    #steps to follow
    # loops through the prerequisites. rearrange them in (biggest, smallest) asin (prereq, course)
    # for each loop save prev = (preq, course)
    # first one, get the beginning prev then continue
    # compare the prev if current preq and course is lesser than
    # merge them else if prev[0] == current[-1] and current[0]== prev[-1]
    # num_courses refers to the number of courses that'll be in the list

    
    # if num_courses and len(prerequisites) <= 0:
    #     return [i for i in range(num_courses)]

    # is_cyclic = False
    # course_list = []
    # # def compare_courses(current, prev):
    # #     if current[0]< prev[1] and current[1]< prev[1]:
    # #         if prev[0] not in course_list and prve[1] not in course_list:
    # #             course_list.append(prev[0])
    # #             course_list.append(prev[1])
    # #     elif current[0]< prev[1] and current[1]>= prev[1]:
    # #         # print(prev)
    # #         # print(current)
    # #         if prev[0] not in course_list and prev[1] not in course_list and current[1] not in course_list:
    # #             course_list.append(prev[0])
    # #             course_list.append(prev[1])
    # #             course_list.append(current[1])
    # #             prev = [prev[0], current[1]]

    # for index, prerequisite in enumerate(prerequisites):
    #     print(index)
    #     if index == 0:
    #         prev = [prerequisite[1], prerequisite[0]]
    #         if index == len(prerequisites)-1:
    #             course_list.append(prev[0])
    #             course_list.append(prev[1])
    #         continue
    # # (0,1),(1,0)
    # #[(1, 0), (2, 0), (3, 1), (3, 2)]
    # # (0,1), (0,2), (1,3), (2,3)
    #     current = [prerequisite[1], prerequisite[0]]
    #     print(prev)
    #     print(current)
    #     if prev == [current[1], current[0]]:
    #         is_cyclic = True
    #         break
    #     # compare_courses(current, prev)
    #     if current[0]< prev[1] and current[1]< prev[1]:
    #         if prev[0] not in course_list:
    #             course_list.append(prev[0])
    #         if prve[1] not in course_list:
    #             course_list.append(prev[1])

    #     elif current[0] <= prev[1] and current[1]>= prev[1]:
    #         if prev[0] not in course_list:
    #             course_list.append(prev[0])
    #         if  prev[1] not in course_list and current[0] == prev[1]:
    #             course_list.append(prev[1])
    #             prev = [prev[0], current[1]]

    #         if current[0] not in course_list and current[0] < prev[1]:
    #             course_list.append(current[0])
    #             prev = [prev[0], current[0]]

    #         if current[1] not in course_list and current[1] < prev[1]:
    #             course_list.append(current[1])
    #             prev = [prev[0], current[0]]

    #         # prev = [prev[0], current[1]]
    #     # print(prev)
    # if is_cyclic:
    #     return []
    # return course_list

# print(course_order(4, [(1,0)]))
    courses = [None]*num_courses
    # None None None None
    for low, high in prerequisites:
        if courses[high] is None:
            courses[high] = {"courses": [low], "count": 0}
            if courses[low] is None:
                courses[low] = {"courses": [], "count": 1}
            else:
                courses[low]["count"]+=1
        else:
            courses[high]["courses"].append(low)
            if courses[low] is None: 
                courses[low]= {"courses": [], "count": 1} 
            else:
                courses[low]["count"]= +1

    available_courses = []
    completed_course= []
    for index, course in enumerate(courses):
        if course and (course["count"] == 0 or course["count"] is None):
            available_courses.append(index)
    while available_courses:
        available_courses.sort()
        lowest = available_courses.pop(0)
        for course in courses[lowest]["courses"]:
            courses[course]["count"] -= 1
            if courses[course]["count"] == 0:
                available_courses.append(course)
        completed_course.append(lowest)
    if num_courses != len(completed_course):
        return []
    return completed_course

print(course_order(4, [(1,0), (2,0), (3,1), (3,2)]))
print(course_order(6, [(1, 0), (0, 1), (2,0), (3,1), (3,2)]))
# {0:[1,2], 1:[3], 2:[3], 3:[]}