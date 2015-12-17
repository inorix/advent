class Deer:
    pos = 0
    points = 0
    state = 1
    
    def __init__(self, params):
        self.speed = int(params[3])
        self.runtime = int(params[6])
        self.timeleft = int(params[6])
        self.resttime = int(params[13])

    def process(self, pos):
        if pos == self.pos and pos:
            self.points += 1
        if self.state == 1:
            self.pos += self.speed
        self.timeleft -= 1
        if self.timeleft == 0:
            self.timeleft = self.resttime if self.state == 1 else self.runtime
            self.state = -self.state
        return [self.pos, self.points]


deers = []

for l in open('input.txt').readlines():
    deers.append(Deer(l.split()))

max_points = 0
max_pos = 0
for a in range(2503):
    for deer in deers:
        p = deer.process(max_pos)
        max_pos = max(p[0], max_pos)
        max_points = max(p[1], max_points)
    
print max_pos, max_points
