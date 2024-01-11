from transitional_colors import generate_transitional_colors, convert_to_ascending_dictionary

red = (255, 0, 0)
orange = (255, 127.5, 0)
yellow = (255, 255, 0)
green = (0, 127.5, 0)

red_to_green = generate_transitional_colors([red, orange, yellow, green], 1)
red_to_green = convert_to_ascending_dictionary(red_to_green)

print(red_to_green)
