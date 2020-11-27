from numpy import linspace
import matplotlib.pyplot as plt

with open("frames.dat", 'r') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 2):
        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_xlim(0, 15.7)
        ax.set_ylim(-12, 12)
        ax.set_yticks(linspace(-10, 10, 11))
        x, y = [float(a) for a in lines[i].split()], [float(a) for a in lines[i + 1].split()]
        ax.plot(x, y)
        ax.set_title(f'Frame {i//2}')
        plt.savefig(f'./frames/{i//2}.png')

# Результат можно посмотреть отдельными кадрами в папке frames или открыть гифку "2_output.gif"
