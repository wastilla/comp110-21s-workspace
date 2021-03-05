"""Range Example."""

start: int = 0
stop: int = 101
step: int = 10

a_range = range(start, stop, step)
print(a_range[1])
print(f"Max value in range: {a_range[len(a_range)-1]}")


a_range = range(10, 100) #Default step value is 1
a_range = range(10) # Default start is 0, default step is 1