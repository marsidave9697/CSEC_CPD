s = input().strip()
upper_count = sum(1 for c in s if c.isupper())
lower_count = len(s) - upper_count

print(s.upper() if upper_count > lower_count else s.lower())
