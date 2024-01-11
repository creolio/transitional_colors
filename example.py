from transitional_colors import generate_transitional_colors_list, generate_transitional_colors_dictionary

red = (255, 0, 0)
orange = (255, 127.5, 0)
yellow = (255, 255, 0)
green = (0, 127.5, 0)

red_to_green_colors_list = generate_transitional_colors_list([red, orange, yellow, green], 1)
red_to_green_colors_dict = generate_transitional_colors_dictionary([red, orange, yellow, green], 1)

print(red_to_green_colors_dict)
