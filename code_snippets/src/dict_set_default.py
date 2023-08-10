# create empty dict
d = {}

# this line will initailise the dict if it has no entry for 1 with an empty list, and append ('a', 'b') into it later
d.setdefault(1, []).append(('a','b'))
print(f"after d.setdefault(1, []).append(('a','b')) --> d={d}")

#after another set edfualt to a key that already exists, the dictionary does not change
d.setdefault(1, [])
print(f"after d.setdefault(1, []) --> d={d}")