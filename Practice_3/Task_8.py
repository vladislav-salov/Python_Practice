import matplotlib.pyplot as plt


BASE_0 = 0x5A4A  # число 23114
BASE_1 = 0x0248  # число 584
BASE_2 = 0xB753  # число 46931


pairs = "..LEXEGEZACEBISOUSESARMAINDIREA.ERATENBERALAVETIEDORQUANTEISRION"
galaxy = []


def tweakseed(s):
    temp = s[0] + s[1] + s[2]
    s[0] = s[1]
    s[1] = s[2]
    s[2] = temp
    return s


def stripout(s, c):
    s = s.replace(c, '')
    return s


def makesystem(s):
    longnameflag = s[0] & 64
    thissys = [0, 0, '']
    thisname = [''] * 12
    thissys[0] = (s[1] >> 8) % 256
    thissys[1] = (s[0] >> 8) % 256
    pair1 = 2 * ((s[2] >> 8) & 31)
    s = tweakseed(s)
    pair2 = 2 * ((s[2] >> 8) & 31)
    s = tweakseed(s)
    pair3 = 2 * ((s[2] >> 8) & 31)
    s = tweakseed(s)
    pair4 = 2 * ((s[2] >> 8) & 31)
    s = tweakseed(s)
    thisname[0] = pairs[pair1]
    thisname[1] = pairs[pair1 + 1]
    thisname[2] = pairs[pair2]
    thisname[3] = pairs[pair2 + 1]
    thisname[4] = pairs[pair3]
    thisname[5] = pairs[pair3 + 1]
    if longnameflag:
        thisname[6] += pairs[pair4]
        thisname[7] += pairs[pair4 + 1]
    thisname = ''.join(thisname)
    thissys[2] = stripout(thisname, '.')
    return thissys


seed = [BASE_0, BASE_1, BASE_2]
for i in range(0, 256):
    galaxy.append(makesystem(seed))


xs = range(0, 256)
plt.title('First Galaxy')
for i in range(0, 256):
    plt.scatter(galaxy[i][0], 256 - galaxy[i][1], c = 'red')
    plt.text(galaxy[i][0], 256 - galaxy[i][1], galaxy[i][2])
plt.show()
