import re
from PIL import Image

def hex_to_rgba(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 8:  # RGBA
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4, 6))
    elif len(hex_color) == 6:  # RGB, add alpha channel
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4)) + (255,)
    elif len(hex_color) == 4:  # RGBA shorthand
        return tuple(int(hex_color[i]*2, 16) for i in range(4))
    elif len(hex_color) == 3:  # RGB shorthand, add alpha channel
        return tuple(int(hex_color[i]*2, 16) for i in range(3)) + (255,)
    else:
        raise ValueError("Invalid hex color format")

with open('C:\\Users\\021-j\\Documents\\GitHub\\coral-reef-theme\\themes\\Coral Reef-color-theme.json', 'r') as file:
    json_string = file.read()

# Regular expression pattern to match hex color codes
pattern = r"#([A-Fa-f0-9]{6})([A-Fa-f0-9]{2})?"
matches = re.findall(pattern, json_string)

# Extract full hex color codes including optional alpha channel
full_matches = ["#" + match[0] + (match[1] if match[1] else "") for match in matches]

unique_colors = set(full_matches)

hex_colors = sorted(unique_colors)
rgba_colors = [hex_to_rgba(color) for color in hex_colors]

# Calculate the dimensions and create the image
num_colors = len(rgba_colors)
image_size = int(num_colors ** 0.5)
if image_size ** 2 < num_colors:
    image_size += 1

image = Image.new("RGBA", (image_size, image_size))

# Set each pixel to the corresponding color
for i, color in enumerate(rgba_colors):
    x = i % image_size
    y = i // image_size
    image.putpixel((x, y), color)

image.save("output.png")
image.show()

