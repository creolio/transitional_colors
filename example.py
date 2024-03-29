from transitional_colors import (
    generate_transitional_colors_list,
    generate_transitional_colors_dictionary,
    generate_transitional_colors_string,
)

red = (255, 0, 0)
orange = (255, 127.5, 0)
yellow = (255, 255, 0)
green = (0, 127.5, 0)

lower_luminance_limit = 0.25
upper_luminance_limit = 0.75

colors = [red, orange, yellow, green]
number_of_colors_between = 3
luminance_limits = (lower_luminance_limit, upper_luminance_limit)

red_to_green_colors_list = generate_transitional_colors_list(colors, number_of_colors_between, luminance_limits)
red_to_green_colors_dict = generate_transitional_colors_dictionary(colors, number_of_colors_between, luminance_limits)
red_to_green_colors_stri = generate_transitional_colors_string(red_to_green_colors_dict)

print("red_to_green_colors_list: ", red_to_green_colors_list)
print("red_to_green_colors_dict: ", red_to_green_colors_dict)
print("red_to_green_colors_stri: ", red_to_green_colors_stri)
