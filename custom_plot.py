import matplotlib.pyplot as plt

def set_size(width, fraction=1, ratio=None):
    """ Set aesthetic figure dimensions to avoid scaling in latex.

    Parameters
    ----------
    width: float
            Width in pts
    fraction: float
            Fraction of the width which you wish the figure to occupy

    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    if width == "nips":
        width_pt = 397.48499
    else:
        width_pt = width
    
    # Width of figure
    fig_width_pt = width_pt * fraction

    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    golden_ratio = (5**.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    if ratio is None:
        fig_height_in = fig_width_in * golden_ratio
    else:
        fig_height_in = fig_width_in * ratio

    fig_dim = (fig_width_in, fig_height_in)

    return fig_dim

def savefig(path, format='pdf'):
    plt.savefig(path, format=format, bbox_inches='tight')