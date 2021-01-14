marksheet = []
markscore = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    marksheet += [[name,score]]
    markscore += [score]
x = sorted(set(markscore))[1]
for n , s in sorted(marksheet):
    if s == x:
        print(n)
