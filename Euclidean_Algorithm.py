import math

phiN = int(input("ϕn: "))
e = int(input("e: "))
a = phiN
b = e
r = 1
aL = []
bL = []
qL = []

while r != 0:
    i = 0

    if a < b:
        b = a
        a = b

    r = a % b
    q = a / b
    q = math.trunc(q)
    aL.append(a)
    bL.append(b)
    qL.append(q)

    a = b
    b = r
    i += 1
    g = a

# print(e)      #9
# print(qL[i])  #2
# print(phiN)   #1120
# print(qL[0])  #124

print(str((qL[i] * qL[0] + 1) * e - qL[i] * phiN) + " = " + str(qL[i] * qL[0] + 1) + "(" + str(e) + ") - " + str(qL[i]) + "(" + str(phiN) + ")")

d = qL[i] * qL[0] + 1
print(d)
