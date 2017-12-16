n = int(input(""))

strings = [input("") for i in range(n)]

q = int(input(""))
queries = [input("") for i in range(q)]

if 1<=n<=1000 and 1<=q<=1000:
    for s in strings:
        if not 1<=len(s)<=20:
            exit()
    for q in queries:
        if not 1<=len(q)<=20:
            exit()

    for q in queries:
        print(strings.count(q))
