"""Improved version of course_order that watches out for duplicate course and prerequisite.
Example when given prerequisites such as [(2,0),(2,0),(2,0)] we only use one (2,0) and ignore
 the repeated ones by using the set() and add the course and increments the dependecy only when the course
 is not yet inside the set"""

def course_order(num_courses, prerequisites):
    """
        Args:
            num_courses: int = This is the total number of courses that requires ordering
            prerequisites: list = course arrangements in the form of a tuple. (course, prereq)
        
        Return:
            completed_courses: list = a list of properly ordered completed courses if no cyclic cases
            are met. It returns [] if no valid ordering exists.
        
        Example:
        >>> from course_prerequisite import course_order
        >>> print(course_order(4, [(1,0), (2,0), (3,1), (2,0), (3,2)]))
        >>> [0, 1, 2, 3]
        >>> print(course_order(4, [(1,0), (0,1)]))
        >>> []
    """
    # TODO: produce a valid ordering of courses respecting all prerequisites,
    # always choosing the lowest-numbered available course next.
    # Return [] if no valid ordering exists.

    # In this code "dep" means the number of dependencies a course has that has not been completed.  
    # It gradually counts their dependencies

    course_dict = {i: {"courses": set(), "dep":0} for i in range(num_courses)}
    for course, prereq in prerequisites:
        if course not in course_dict[prereq]["courses"]:
            course_dict[prereq]["courses"].add(course)
            course_dict[course]["dep"] +=1
    available_courses = []
    completed_courses = []

    for key, value in course_dict.items():
        if value["dep"] == 0:
            available_courses.append(key)
    while available_courses:
        available_courses.sort()
        lowest_course = available_courses.pop(0)
        for course in course_dict[lowest_course]["courses"]:
            course_dict[course]["dep"] -= 1
            if course_dict[course]["dep"] == 0:
                available_courses.append(course)
        completed_courses.append(lowest_course)
    if len(completed_courses) != num_courses:
        return []
    return completed_courses

print(course_order(4, [(1,0), (2,0), (3,1), (2,0), (3,2)]))
print(course_order(6, [(1, 0), (5, 1), (2,0), (3,1), (4,2)]))
print(course_order(2, [(1,0),(0,1),(0,1)]))
print(course_order(4, []))
print(course_order(4, [(1,0)]))
