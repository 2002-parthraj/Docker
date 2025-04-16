# app.py
import sys

nums = list(map(int, sys.argv[1:]))
print(f"Sum: {sum(nums)}")

