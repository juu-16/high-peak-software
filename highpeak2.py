v= open("F:\highpeak\input.txt", "r") #inputfile is stored at F:\highpeak folder
goodies = dict()
data = list(v)
line = data[0]

for a in line.split():
    if a.isnumeric():
        c = int(a)

for line in data[3:]:
    if ":" in line:
        s = line.split(':')
        goodies[s[0]] = int(s[1])

data = open("output.txt", "w")

nmin = 0
omin = 999999999999
st = 0
ps1 = 0
ps2 = 0
goodies1 = dict(sorted(goodies.items(), key=lambda x: x[1]))
end = c - 1
price = list(goodies1.values())

while end < len(price):
    nmin = price[end] - price[st]
    if omin >= nmin:
        ps1 = st
        ps2 = end
        omin = nmin
    st += 1
    end += 1

goodies1 = list(goodies1.items())
data.write("Number of Employees: " + str(c) + "\n")
data.write("Here the goodies that are selected for distribution are:\n")

for i in range(ps1, ps2 + 1):
    data.write(goodies1[i][0] + ": " + str(goodies1[i][1]) + "\n")

data.write("And the difference between the chosen goodie with highest price and the lowest price is ")
data.write(str(omin) + "\n")
data.close()