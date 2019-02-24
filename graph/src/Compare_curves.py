import sys, os
import numpy as np

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from frechetdist import frdist

a = [[5,0.05411],
[10,0.02498],
[15,1.68914],
[20,3.50233],
[25,5.73283],
[30,2.11324],
[35,3.12394],
[40,12.76868]]

b = [[5,0.05411],
[10,0.03746],
[15,1.38599],
[20,3.86277],
[25,6.08305],
[30,2.54065],
[35,3.54065],
[40,15.17554]]

c = [[5,0.17903],
[10,5.04448],
[15,18.06757],
[20,26.50588],
[25,17.93629],
[30,15.93676],
[35,11.99633],
[40,7.2321]]

d = [[5,2.03744],
[10,3.93495],
[15,29.31478],
[20,23.28149],
[25,10.98102],
[30,19.96778],
[35,9.04275],
[40,5.30423]]

print frdist(d, c)