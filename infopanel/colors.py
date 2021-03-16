"""Colors."""

import webcolors


def name_to_rgb(color_name):
    """Get a rgb color from a color name."""
    rgb = webcolors.name_to_rgb(color_name)
    return rgb
