import matplotlib.pyplot as plt
from matplotlib_venn import venn3

set_1 = {5, 10, 15, 20, 25, 30}
set_2 = {2,4,6,8,10,12,14,16,18,20,22,24,26,28,30}
set_3 = {1,4,9,16,25}

venn3([set_1, set_2, set_3], ('x<30 and x>1', 'y-even', 'z%5==0'))

plt.show()