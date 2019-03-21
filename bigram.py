import operator 

challenge_num = str(input("Which challenge: "))
f = open(challenge_num, "r")
email = f.readline()
freq = {}

for key in email:
    freq[key] = freq.get(key, 0) + 1

sorted_freq = sorted(freq.items(), key=operator.itemgetter(1))

for num in reversed(sorted_freq):
    print(num[0], (float(num[1])/len(email))*100)

