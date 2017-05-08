import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
from mpl_toolkits.axes_grid1 import make_axes_locatable


def heatmap(w, vmin=None, vmax=None, diverge_color=False,
            plot_name=None, vocab=["A", "C", "G", "T"]):
    """Plot a heatmap from weight matrix w

    vmin, vmax = z axis range
    diverge_color = Should we use diverging colors?
    plot_name = plot_title
    vocab = vocabulary (corresponds to the first axis)
    """
    # Generate y and x values from the dimension lengths
    assert len(vocab) == w.shape[0]
    plt_y = np.arange(w.shape[0] + 1) + 0.5
    plt_x = np.arange(w.shape[1] + 1) - 0.5
    z_min = w.min()
    z_max = w.max()

    if vmin is None:
        vmin = z_min
    if vmax is None:
        vmax = z_max

    if diverge_color:
        color_map = plt.cm.RdBu
    else:
        color_map = plt.cm.Blues

    fig, ax = plt.subplots()
    im = ax.pcolormesh(plt_x, plt_y, w, cmap=color_map,
                       vmin=vmin, vmax=vmax, edgecolors="white")
    ax.grid(False)
    ax.set_yticklabels([""] + vocab, minor=False)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xticks(np.arange(w.shape[1] + 1))
    ax.set_xlim(plt_x.min(), plt_x.max())
    ax.set_ylim(plt_y.min(), plt_y.max())

    # nice scale location:
    # http://stackoverflow.com/questions/18195758/set-matplotlib-colorbar-size-to-match-graph
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    fig.colorbar(im, cax=cax)

    if plot_name is not None:
        ax.set_title(plot_name)
    ax.set_aspect('equal')
    return ax