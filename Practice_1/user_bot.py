def script(check, x, y):
    if check("gold", x, y):
        return "take"
    if check("level") == 1:
        if not check("wall", x + 2, y):
            return "right"
        return "down"
    if check("level") == 2:
        if check("gold", x + 1, y):
            return "right"
        if check("gold", x, y + 1):
            return "down"
        if check("gold", x, y - 1):
            return "up"
        if check("gold", x, y - 2):
            return "up"
        if check("gold", x, y - 3):
            return "up"
        if check("gold", x, y - 4):
            return "up"
        if not check("wall", x + 2, y):
            return "right"
    if check("level") == 3:
        if check("gold", x + 1, y - 1) and check("gold", x, y - 1):
            return "up"
        for i in range(10):
            if check("gold", x + i, y):
                return "right"
            elif check("wall", x + i, y):
                break
        if check("wall", x, y + 1):
            if check("wall", x - 1, y):
                return "up"
            '''
            if check("wall", x + 1, y):
                return "left"
            '''
            return "left"
        if check("wall", x, y - 1):
            '''
            if check("wall", x - 1, y):
                return "right"
            '''
            if check("wall", x + 1, y):
                return "down"
            return "right"
        if check("wall", x - 1, y):
            if check("wall", x, y - 1):
                return "right"
            '''
            if check("wall", x, y + 1):
                return "up"
            '''
            return "up"
        if check("wall", x + 1, y):
            '''
            if check("wall", x, y - 1):
                return "down"
            '''
            if check("wall", x, y + 1):
                return "left"
            return "down"
        if check("wall", x + 1, y + 1):
            return "down"
        if check("wall", x - 1, y + 1):
            return "left"
        if check("wall", x - 1, y - 1):
            return "up"
        if check("wall", x + 1, y - 1):
            return "right"
    if check("level") == 4:
        b = False
        i = 1
        while 1 <= i <= 10:
            if check("gold", x + i, y):
                for j in range(1, i):
                    if not check("wall", x + j, y):
                        continue
                    else:
                        b = True
                        break
                if b:
                    break
                return "right"
            i += 1
        b = False
        i = 1
        while 1 <= i <= 10:
            if check("gold", x - i, y):
                for j in range(1, i):
                    if not check("wall", x - j, y):
                        continue
                    else:
                        b = True
                        break
                if b:
                    break
                return "left"
            i += 1
        b = False
        i = 1
        while 1 <= i <= 10:
            if check("gold", x, y + i):
                for j in range(1, i):
                    if not check("wall", x, y + j):
                        continue
                    else:
                        b = True
                        break
                if b:
                    break
                return "down"
            i += 1
        b = False
        i = 1
        while 1 <= i <= 10:
            if check("gold", x, y - i):
                for j in range(1, i):
                    if not check("wall", x, y - j):
                        continue
                    else:
                        b = True
                        break
                if b:
                    break
                return "up"
            i += 1
        if check("wall", x, y - 1):
            '''
            if check("wall", x - 1, y):
                return "right"
            '''
            if check("wall", x + 1, y):
                return "down"
            return "right"
        if check("wall", x, y + 1):
            if check("wall", x - 1, y):
                return "up"
            '''
            if check("wall", x + 1, y):
                return "left"
            '''
            return "left"
        if check("wall", x + 1, y):
            '''
            if check("wall", x, y - 1):
                return "down"
            '''
            if check("wall", x, y + 1):
                return "left"
            return "down"
        if check("wall", x - 1, y):
            if check("wall", x, y - 1):
                return "right"
            '''
            if check("wall", x, y + 1):
                return "up"
            '''
            return "up"
        if check("wall", x + 1, y - 1):
            return "right"
        if check("wall", x - 1, y + 1):
            return "left"
        if check("wall", x + 1, y + 1):
            return "down"
        if check("wall", x - 1, y - 1):
            return "up"

