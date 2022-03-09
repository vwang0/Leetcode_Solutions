THEME_COLOR_BACKGROUND =  '#ffffff'
THEME_COLOR_PRIMARY =  '#1890ff'
THEME_COLOR_PRIMARY_HOVER =  '#40a9ff'
THEME_COLOR_FONT =  '#000000'
THEME_COLOR_GRAY =  '#fafafa'


def hex_to_rgb(h):
    return tuple(int(h[1:][i:i+2], 16) for i in (0, 2, 4))

def interpolate(color_a, color_b, t):
    # 'color_a' and 'color_b' are RGB tuples
    # 't' is a value between 0.0 and 1.0
    # this is a naive interpolation
    list = []
    for a, b in zip(color_a, color_b):
        i = int(a + (b - a) * t)
        if i < 0:
            i = 0
        elif i > 255:
            i = 255
        list.append(i)
    return tuple(list)
    # return tuple( int(a + (b - a) * t) for a, b in zip(color_a, color_b))