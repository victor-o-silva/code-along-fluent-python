import bisect

haystack = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
needle = 19
position = bisect.bisect_left(haystack, needle)
print(position)
haystack.insert(position, needle)
print(haystack)

# Simpler version
haystack2 = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
needle = 19
bisect.insort(haystack2, needle)
print(haystack2)
