
#function, elapsed, delay
actions = []

def addAction(func, delay):
    actions.append([func, 0, delay])

def check(elapsed):
    for action in actions:
        action[1] += elapsed

        if action[1] > action[2]:
            action[1] = 0
            action[0]()