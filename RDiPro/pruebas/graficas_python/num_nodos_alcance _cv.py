"""
========
Barchart
========

A bar plot with errorbars and height labels on individual bars
"""
import numpy as np
import matplotlib.pyplot as plt

N = 6
rdipro_means = (4, 32, 59, 99, 124, 149)
rdipro_std = (3, 3, 3, 3, 3, 3)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, rdipro_means, width, color='r', yerr=rdipro_std)

netflood_means = (17, 49, 74, 99, 123, 149)
netflood_std = (3, 3, 3, 3, 3, 3)
rects2 = ax.bar(ind + width, netflood_means, width, color='y', yerr=netflood_std)

# add some text for labels, title and axes ticks
ax.set_ylabel('N. de nodos que recibieron el mensaje')
ax.set_xlabel('N. de nodos')
ax.set_title('Alcance variando el n. de nodos (contando broadcast para vecinos)')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('25', '50', '75', '100', '125', '150'))

ax.legend((rects1[0], rects2[0]), ('RDiPro', 'Flooding'), loc="upper left")


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

#plt.show()
plt.savefig('numnodos_alcance_con_vecinos.png', dpi = 300)
plt.close()
