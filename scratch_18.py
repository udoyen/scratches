g = 'george'
gh = []

for i in range(len(g) - 1, -1, -1): # you need to use -1 here becos
    gh.append(g[i])                 # python range stops at a number that
    print(i)                        # is less than the stop value

print("".join(gh))

[gh.append(g[i]) for i in range(len(g) - 1, -1, -1)]
print("".join(gh))
