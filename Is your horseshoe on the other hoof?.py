s1, s2, s3, s4 = input().split()

unique_colors = set()
unique_colors.add(s1)
unique_colors.add(s2)
unique_colors.add(s3)
unique_colors.add(s4)

additional = 4 - len(unique_colors)

print(additional)
