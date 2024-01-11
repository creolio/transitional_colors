from typing import List, Tuple


def calculate_luminance(color: Tuple[int, int, int]) -> float:
    color_normalized = tuple(i / 255 for i in color)
    return sum(w * c for w, c in zip([0.2126, 0.7152, 0.0722], color_normalized))


def adjust_color_to_luminance(color: List[int], target_luminance: float) -> Tuple[int, int, int]:
    lower_limit, upper_limit = 0.25, 0.75
    while not lower_limit <= calculate_luminance(color) <= upper_limit:
        color = [c + 5 if calculate_luminance(color) < lower_limit else c - 5 for c in color]
        color = [max(0, min(255, c)) for c in color]
    return tuple(round(c) for c in color)


def generate_intermediary_colors(
    color1: Tuple[int, int, int], color2: Tuple[int, int, int], number_of_colors_between: int
) -> List[Tuple[int, int, int]]:
    colors = []
    for i in range(1, number_of_colors_between + 1):
        ratio = i / (number_of_colors_between + 1)
        color = [round(color1[j] + (color2[j] - color1[j]) * ratio) for j in range(3)]
        color = adjust_color_to_luminance(color, calculate_luminance(color))
        colors.append(tuple(color))
    return colors


def format_color_code(color: Tuple[int, int, int]) -> Tuple[int, int, int]:
    return adjust_color_to_luminance(color, calculate_luminance(color))


def generate_transitional_colors_list(
    colors: List[Tuple[int, int, int]], number_of_colors_between: int
) -> List[Tuple[int, int, int]]:
    colors_formatted = [format_color_code(color) for color in colors]
    color_range = []
    for i in range(len(colors_formatted) - 1):
        color_range.extend([colors_formatted[i]])
        color_range.extend(
            generate_intermediary_colors(colors_formatted[i], colors_formatted[i + 1], number_of_colors_between)
        )
    color_range.extend([colors_formatted[-1]])
    return color_range


def convert_to_ascending_dictionary(color_list: List[Tuple[int, int, int]]) -> dict:
    return {i: f"rgb{color}" for i, color in enumerate(color_list)}


def generate_transitional_colors_dictionary(colors: List[Tuple[int, int, int]], number_of_colors_between: int) -> dict:
    colors_list = generate_transitional_colors_list(colors, number_of_colors_between)
    return convert_to_ascending_dictionary(colors_list)
