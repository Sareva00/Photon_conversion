#========================================================================
# Author: Sara Evangelista
#========================================================================
# This contains the plotting style I use for my papers and presentations.


# Plotting setup
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.ticker import AutoMinorLocator, MaxNLocator, ScalarFormatter
import seaborn as sns

plt.rcParams['font.size']=14
width =  508.0  # in pt, for two columns papers in A&A, ApJ, MNRAS
widthcol = 244

f =  ScalarFormatter(useOffset=False, useMathText=True)
f.set_scientific(True)
f.set_powerlimits((0, 0))

def set_size(width, fraction=1,subplots=(1, 1)):
    """Set figure dimensions to avoid scaling in LaTeX.

    Parameters
    ----------
    width float
            Document textwidth or columnwidth in pts
    fraction float, optional
            Fraction of the width which you wish the figure to occupy

    Returns
    -------
    fig_dim tuple
            Dimensions of figure in inches, since the matplotlib's figsize parameter expects dimensions in inches
    """
    # Width of figure (in pts)
    fig_width_pt = width * fraction

    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    # httpsdisq.usp2940ij3
    golden_ratio = (5**.5 - 1)  / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio* (subplots[0] / subplots[1])

    fig_dim = (fig_width_in, fig_height_in)

    return fig_dim

#========================================================================
# Author: Francesco Marchisotti
# Functions for plotting learning curves and highlighting best epoch
#========================================================================


def set_ticks(ax: Axes) -> None:
    """Set customised ticks style for a given Axes object."""
    ax.xaxis.set_major_locator(MaxNLocator("auto", integer=True))
    ax.minorticks_on()
    ax.tick_params(direction='in', right=True, top=True)
    ax.tick_params(labelsize=12)
    ax.tick_params(labelbottom=True, labeltop=False, labelright=False, labelleft=True)
    ax.tick_params(direction='in', which='minor', length=4, bottom=True, top=True, left=True, right=True)
    ax.tick_params(direction='in', which='major', length=8, bottom=True, top=True, left=True, right=True)

    ax.grid(which='major', axis='y', linestyle='--', linewidth=0.3, alpha=0.5)  # Solo major su x
    ax.grid(which='both', axis='x', linestyle='--', linewidth=0.3, alpha=0.5)   # Major+minor su y
    

def set_labels(ax: Axes, x_label: str, x_log: bool, y_label: str, y_log: bool, title: str) -> None:
    """Set customised labels and title for a given Axes object."""
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    if title is not None:
        ax.set_title(title, fontsize=20, fontweight='bold', pad=15)

    if x_log:
        ax.set_xscale('log')
    if y_log:
        ax.set_yscale('log')

def set_colors(num: int, palette: str = "rocket") -> list:
    """Return a list of colors from a specified palette.
       
        Common palettes I use are:
        - "personal": a custom palette of 8 colors I created for my plots
        - Seaborn palettes: e.g., "rocket", "mako", "viridis", etc.
        - Matplotlib colormaps: e.g., "Spectral", "viridis", etc.
        """

    if palette == "personal" and num <= 8:
        colors4 = ['#c3121e', '#0348a1', '#ffb01c', '#027608', '#0193b0', '#9c5300', '#949c01', '#7104b5']       
        return colors4[:num]
    elif palette == "dark_photons" and num <= 5:
        colors_dp = ["#5386e4","#4c4b63","#ce5374","#ffba08","#629677"]
        return colors_dp[:num]
    elif palette in sns.palettes.SEABORN_PALETTES:
        return sns.color_palette(palette, num)
    elif palette in plt.colormaps:
        return plt.colormaps[palette].resampled(num)
    else:
        raise ValueError(f"Palette '{palette}' not recognized. Please choose from seaborn palettes or matplotlib colormaps.") 

 




