from src.black_box import run


data = [9, 3, 7, 1, 8, 2, 6]
result = run("A", data)

print("input:", data)
print("output:", result.values)
print("comparisons:", result.comparisons)
print("writes:", result.writes)
print("nanoseconds:", result.nanoseconds)
