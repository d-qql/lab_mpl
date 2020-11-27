import matplotlib.pyplot as plt

fig, ax = plt.subplots(5, figsize = (15, 50))

for i in range(5):
    with open(f"./dead_moroz/00{i + 1}.dat", 'r') as f:
        n = int(f.readline())
        x, y = [], []
        for _ in range(n):
            coords = [float(a) for a in f.readline().split()]
            x.append(coords[0])
            y.append(coords[1])
        ax[i].scatter(x, y)
        ax[i].axis('scaled')
plt.show()
