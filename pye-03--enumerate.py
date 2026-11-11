"""
PYTHON EVERYDAY — ENUMERATE: STOP MANAGING LOOP COUNTERS
Access a count and value together while looping. Compare a manual counter
with enumerate(), number a checklist from one, and avoid confusing labels
with list indexes.

Programmer: python_scripts (Abhijith Warrier)
"""

# 1. The manual version: correct, but extra bookkeeping.
tasks = ["Read", "Code", "Test"]
print("Manual counter:")
index = 0
for task in tasks:
    print(index, task)
    index += 1

# 2. enumerate() supplies (count, value); the loop unpacks each pair.
# The default count starts at 0. No imports are needed.
print("Enumerate:")
for index, task in enumerate(tasks):
    print(index, task)

# 3. Start at 1 for human-facing labels, such as checklist numbers.
print("Checklist:")
for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")

# 4. start changes the count, NOT the list's zero-based indexing.
print("First list item:", tasks[0])
# Use task directly above. tasks[number] would select the wrong item
# and eventually raise IndexError in this example.

# 5. Other iterables work too. Here we enumerate a string.
print("String:")
for position, letter in enumerate("PY"):
    print(position, letter)

# 6. An enumerate object is an iterator: it is consumed as you advance it.
# list() is used ONLY here to display the remaining pairs for illustration.
pairs = enumerate(tasks)
print("First pair:", next(pairs))
print("Remaining pairs:", list(pairs))
print("After exhaustion:", list(pairs))
# Make a fresh enumerate(tasks) to start a new pass over this list.
