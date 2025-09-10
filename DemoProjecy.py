"""
ev_wall_charger_flowchart_matplotlib.py
- วาด flowchart แบบเรียบง่ายด้วย matplotlib (ไม่ต้องมี Graphviz)
- ผลลัพธ์: ev_wall_charger_flowchart_matplotlib.png
- pip install matplotlib
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.figure(figsize=(6,10))
ax = plt.gca()
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)
ax.axis('off')

def box(x, y, text, w=8, h=1.0):
    rect = FancyBboxPatch((x - w/2, y - h/2), w, h,
                          boxstyle="round,pad=0.3", linewidth=1)
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center', fontsize=9)

def diamond(x, y, text):
    # draw simple diamond
    coords = [(x, y+0.6), (x+1.5, y), (x, y-0.6), (x-1.5, y)]
    poly = plt.Polygon(coords, closed=True, edgecolor='k', facecolor='w')
    ax.add_patch(poly)
    ax.text(x, y, text, ha='center', va='center', fontsize=9)

def arrow(x1,y1,x2,y2):
    arr = FancyArrowPatch((x1,y1),(x2,y2), arrowstyle='->', mutation_scale=12)
    ax.add_patch(arr)

# nodes (x center, y position)
box(5,13, "Start\n(ขอข้อมูลลูกค้า)", h=1)
box(5,11.5, "1. Site survey\nตำแหน่ง, ระยะสาย")
box(5,10, "2. Choose location\nใกล้ Panel, ปลอดภัย")
box(5,8.5, "3. Check electrical capacity\nPanel & breaker")
diamond(5,7, "Capacity OK?")
box(5,5.5, "5. Select charger & specs")
box(5,4, "6. Prepare circuit\nConduit & wiring")
box(5,2.5, "7. Mount charger")
box(5,1, "8. Connect to panel\nและ Test")
box(5,-0.5, "Final inspection\nHandover", h=1)

# branch for No -> upgrade
box(8,7, "Upgrade panel\n(if needed)", w=4, h=0.9)

# arrows
arrow(5,12,5,11.1)
arrow(5,10.4,5,9.1)
arrow(5,8.9,5,7.7)
arrow(5,6.3,5,5.9)
arrow(5,4.6,5,4.1)
arrow(5,3.1,5,2.6)
arrow(5,1.6,5,0.1)
arrow(5,-0.3,5,-0.45)

# branch arrows
arrow(4.2,6.6,6.5,6.8) # from diamond to upgrade
arrow(8,6.2,5.3,5.8)   # upgrade back to select_charger

plt.savefig('ev_wall_charger_flowchart_matplotlib.png', bbox_inches='tight', dpi=150)
print("Flowchart generated: ev_wall_charger_flowchart_matplotlib.png")
