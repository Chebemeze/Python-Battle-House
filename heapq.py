import heapq

n = [5,4,10,1,2,3,4]
print(f"n is initially {n}")
lowest = heapq.heappop(n)
heapq.heappush(n, 8)
print(f"The lowest is {lowest}")
print(f"n is now {n}")

n = {"name": "efe", 0: 20, "school":"magic touch secondary school"}

print(n.pop(0))
print(n)
