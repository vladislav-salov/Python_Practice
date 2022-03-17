from random import randint, choice
import matplotlib.pyplot as plt
import time


class Agent:
    MAX = 20
    MATES = 10
    PERCENT = 0.8

    def __init__(self, group):
        self.x = randint(0, self.MAX)
        self.y = randint(0, self.MAX)
        self.group = group

    def distance(self, other: 'Agent') -> float:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def happy(self, others):
        mates = 0

        ms = []
        for other in others:
            ms.append((self.distance(other), other))

        ms.sort(key=lambda x: x[0])
        for i in range(self.MATES):
            if ms[i][1].group == self.group:
                mates += 1

        return mates >= self.MATES * self.PERCENT

    def update(self, others):
        if not self.happy(others):
            while True:
                nx, ny = randint(0, self.MAX), randint(0, self.MAX)
                for other in others:
                    if other.x == nx and other.y == ny:
                        continue
                self.x, self.y = nx, ny
                break


def sim(grs, field, k, p):

    Agent.PERCENT = p
    Agent.MAX = field
    Agent.MATES = k

    groups = ['1', '2']

    agents = [Agent(groups[0]) for i in range(grs[0])] + [Agent(groups[1]) for i in range(grs[1])]
    happy = []

    plt.ion()

    for i in range(20):
        c_h = 0
        for agent in agents:
            agent.update(agents)
            if agent.happy(agents):
                c_h += 1
        if c_h == len(agents):
            break
        happy.append(c_h / len(agents))
        x = [[], []]
        y = [[], []]
        for agent in agents:
            group = groups.index(agent.group)
            x[group].append(agent.x)
            y[group].append(agent.y)

        plt.clf()

        plt.plot(x[0], y[0], 's', markerfacecolor='white', markersize=10)
        plt.plot(x[1], y[1], 's', markerfacecolor='black', markersize=10)

        plt.draw()
        plt.gcf().canvas.flush_events()

        time.sleep(0.2)
    plt.ioff()
    plt.clf()
    plt.plot(happy)
    plt.show()


if __name__ == '__main__':
    sim((80, 80), 20, 10, 0.8)