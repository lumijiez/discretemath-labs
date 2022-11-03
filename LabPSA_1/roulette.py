import random
import matplotlib.pyplot as plt


def get_winnings(tries, chance):
    total_winnings = 0
    for _ in range(tries):
        winnings = 20
        x = random.randint(0, 37)
        if x <= chance - 1:
            winnings += 20
        else:
            winnings -= 20
        total_winnings += winnings
    return total_winnings / tries


def get_winnings_number(tries, chance):
    wallet = 0
    for _ in range(tries):
        winnings = 20
        rand = random.randint(0, 37)
        if rand <= chance - 1:
            winnings *= 35
        else:
            winnings -= 20
        wallet += winnings
    return wallet / tries


def plot_graphs(tries):
    wallet = 10000
    for i in range(tries):
        wallet -= 20
        rand = random.randint(1, 38)
        if rand > 20:
            wallet += 40
        xg.append(i)
        yg.append(wallet)
    plt.plot(xg, yg, label="Bets 20 on red")
    plot_number(tries)


def plot_number(tries):
    wallet = 10000
    for i in range(tries):
        wallet -= 20
        rand = random.randint(1, 38)
        if rand == 1:
            wallet += 20*35
        gx.append(i)
        gy.append(wallet)
    plt.plot(gx, gy, label="Bets 20 on number")
    plt.legend()
    plt.show()


xg = []
yg = []
gx = []
gy = []
print(get_winnings(10000, 18))
print(get_winnings_number(10000, 1))
plot_graphs(500)
