# Modified from
# https://matplotlib.org/stable/gallery/color/named_colors.html#sphx-glr-gallery-color-named-colors-py

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def plot_colortable(color_d, title):
    islist = False
    if not isinstance(color_d, dict):
        color_d = {len(color_d): color_d}
        islist = True

    nrows = 1
    for k,v in color_d.items():
        if len(v) > nrows:
            nrows = len(v)
    if islist:
        ncols = 4
    else:
        ncols = len(color_d)

    cell_width = 22
    cell_height = 22
    swatch_width = 18
    margin = 12
    topmargin = 40

    width = cell_width * ncols +  margin
    height = cell_height * nrows + margin + topmargin
    dpi = 72

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(margin/width, margin/height,
                        (width-margin)/width, (height-topmargin)/height)
    ax.set_xlim(0, cell_width * ncols)
    ax.set_ylim(cell_height * (nrows-0.5), -cell_height*2)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()
    ax.set_title(title, fontsize=24, y=1.004, loc="left", pad=10)

    col = 0
    for n,colors in color_d.items():
        if islist:
            lbl = ""
        else:
            lbl = n
        ax.text(col*cell_width+cell_width/2, -cell_height, lbl, 
                fontsize=14, horizontalalignment='center', 
                verticalalignment='center')
        for i, c in enumerate(colors):
            row = i
            y = row * cell_height

            swatch_start_x = cell_width * col
            text_pos_x = cell_width * col + swatch_width + 7

            ax.text(text_pos_x, y, "", fontsize=14,
                    horizontalalignment='left',
                    verticalalignment='center')

            ax.add_patch(
                Rectangle(xy=(swatch_start_x, y-9), width=swatch_width,
                          height=18, facecolor=colors[i], edgecolor='0.7')
            )
        col += 1

    return fig

