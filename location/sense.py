p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1


def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = (world[i] == Z)
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
    s = sum(q)
    n = [q[j] / s for j in range(len(q))]
    return n


# for i in range(len(measurements)):
#    p = sense(p, measurements[i])


def move(p, U):
    q = []
    for i in range(len(p)):
        s = p[(i - U) % len(p)] * pExact
        s = p[(i - 1 - U) % len(p)] * pOvershoot + s
        s = p[(i + 1 - U) % len(p)] * pUndershoot + s
        q.append(s)
    return q


for i in range(len(motions)):
    p = sense(p, measurements[i])
    p = move(p, motions[i])

print p
