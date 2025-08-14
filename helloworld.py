# For the simple code, hjere it is:
print("Hello world")

# In graphic style
import matplotlib.pyplot as plt

def draw_letter(ax, lines, offset_x=0, offset_y=0):
    for (x0, y0, x1, y1) in lines:
        ax.plot([x0+offset_x, x1+offset_x], [y0+offset_y, y1+offset_y], color='black', linewidth=2)

# Define each letter as a set of lines (start_x, start_y, end_x, end_y)
letters = {
    'H': [ (0,0,0,40), (20,0,20,40), (0,20,20,20) ],
    'E': [ (20,0,0,0), (0,0,0,40), (0,20,15,20), (0,40,20,40) ],
    'L': [ (0,0,0,40), (0,0,20,0) ],
    'O': [ (0,0,20,0), (20,0,20,40), (20,40,0,40), (0,40,0,0) ],
    'W': [ (0,40,5,0), (5,0,10,20), (10,20,15,0), (15,0,20,40) ],
    'R': [ (0,0,0,40), (0,40,15,40), (15,40,20,35), (20,35,15,20), (15,20,0,20), (10,20,20,0) ],
    'D': [ (0,0,0,40), (0,40,15,35), (15,35,15,5), (15,5,0,0) ]
}

word = "HELLO WORLD"

fig, ax = plt.subplots(figsize=(12,3))
ax.set_aspect('equal')
ax.axis('off')

x = 0
for ch in word:
    if ch == ' ':
        x += 20  # space between words
        continue
    draw_letter(ax, letters[ch], offset_x=x)
    x += 30  # space between letters

plt.xlim(-10, x+10)
plt.ylim(-10, 50)
plt.savefig('hello_world_graphic.png', bbox_inches='tight')
print("Saved 'hello_world_graphic.png'.")
