# get_coordinates.py
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

print("Finding your map...")
current_dir = os.path.dirname(os.path.abspath(__file__))

# Try different possible locations
possible_paths = [
    os.path.join(current_dir, "static", "india_map.png"),
    os.path.join(current_dir, "india_map.png"),
    "static/india_map.png",
    "india_map.png"
]

image_path = None
for path in possible_paths:
    if os.path.exists(path):
        image_path = path
        print(f"✓ Found map at: {path}")
        break

if not image_path:
    print("❌ Could not find india_map.png")
    print("\nSearching for image files...")
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg')):
                print(f"  Found: {os.path.join(root, file)}")
    exit(1)

# Load and show the image
img = mpimg.imread(image_path)
height, width = img.shape[:2]
print(f"📏 Map size: {width} x {height} pixels")

plt.figure(figsize=(12, 14))
plt.imshow(img)
plt.title(f"INDIA MAP - Click to get coordinates | Size: {width}x{height}")
plt.axis('on')  # Show coordinates

print("\n" + "="*70)
print("INSTRUCTIONS:")
print("1. Click on each city location ONCE")
print("2. The coordinates will appear below")
print("3. After 5 clicks, close the window")
print("4. Copy the coordinates into graph_logic.py")
print("="*70)
print("\nClick on these cities in order:")
print("1. Delhi (top-center)")
print("2. Jaipur (west of Delhi)")
print("3. Bhopal (center)")
print("4. Nagpur (south-center)")
print("5. Hyderabad (south)")

# Store clicks
clicks = []

def on_click(event):
    if event.xdata is not None and event.ydata is not None:
        x, y = int(event.xdata), int(event.ydata)
        clicks.append((x, y))
        
        # Mark the point
        plt.plot(x, y, 'ro', markersize=10)
        
        city_names = ["Delhi", "Jaipur", "Bhopal", "Nagpur", "Hyderabad"]
        if len(clicks) <= len(city_names):
            city = city_names[len(clicks)-1]
            plt.text(x + 15, y - 15, city, fontsize=12, color='white',
                    bbox=dict(boxstyle="round", facecolor='red', alpha=0.8))
        
        plt.draw()
        print(f"Click {len(clicks)}: ({x}, {y})")

plt.gcf().canvas.mpl_connect('button_press_event', on_click)
plt.show()

# Print results
if clicks:
    print("\n" + "="*70)
    print("COORDINATES COLLECTED:")
    print("="*70)
    print("\nCopy this to graph_logic.py in the draw_india_map() function:")
    print("\npos = {")
    city_names = ["Delhi", "Jaipur", "Bhopal", "Nagpur", "Hyderabad"]
    for i, (x, y) in enumerate(clicks):
        if i < len(city_names):
            print(f'    "{city_names[i]}": ({x}, {y}),')
    print("}")
else:
    print("\nNo clicks recorded.")