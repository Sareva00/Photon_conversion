import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import seaborn as sns
import tol_colors as tc
 
# --- Figure dimensions ---
 
width    = 508.0   # full two-column width in pt (A&A / ApJ / MNRAS)
widthcol = 244.0   # single column width in pt
width_jcap = 440.0  # JCAP column width in pt
 
def set_size(width, fraction=1.0, subplots=(1,1), ratio=None):
    fig_width_pt = width * fraction
    inches_per_pt = 1 / 72.27
    if ratio is None:
        ratio = (5**0.5 - 1) / 2  # golden ratio default
    fig_width_in = fig_width_pt * inches_per_pt
    fig_height_in = fig_width_in * ratio * (subplots[0] / subplots[1])
    return (fig_width_in, fig_height_in)
 
 
# --- Scientific notation formatter ---
 
def sci_formatter() -> ScalarFormatter:
    """Return a ScalarFormatter that always uses scientific notation."""
    f = ScalarFormatter(useOffset=False, useMathText=True)
    f.set_scientific(True)
    f.set_powerlimits((0, 0))
    return f
 
 
# --- Color palettes ---
 
def set_colors(num: int, palette: str = "rocket") -> list:
    """Return a list of `num` colors from the specified palette.
 
    Built-in named palettes
    -----------------------
    'personal'      : 8-color custom palette
    'dark_photons'  : 5-color palette for dark photon plots
    'tol:<name>'    : tol_colors colorset, e.g. 'tol:vibrant', 'tol:bright'
    'sns:<name>'    : seaborn palette, e.g. 'sns:rocket', 'sns:bright'
    Any matplotlib colormap name (e.g. 'Spectral', 'viridis')
    """
    if palette == "personal":
        colors = ['#c3121e', '#0348a1', '#ffb01c', '#027608',
                  '#0193b0', '#9c5300', '#949c01', '#7104b5']
        if num > len(colors):
            raise ValueError(f"'personal' palette only has {len(colors)} colors; requested {num}.")
        return colors[:num]
 
    if palette == "dark_photons":
        colors = ["#5386e4", "#4c4b63", "#ce5374", "#ffba08", "#629677"]
        if num > len(colors):
            raise ValueError(f"'dark_photons' palette only has {len(colors)} colors; requested {num}.")
        return colors[:num]
 
    if palette.startswith("tol:"):
        name = palette[4:]
        if name not in tc.colorsets:
            raise ValueError(f"tol_colors colorset '{name}' not recognised. Available: {list(tc.colorsets.keys())}")
        colors = list(tc.colorsets[name])
        if num > len(colors):
            raise ValueError(f"'tol:{name}' only has {len(colors)} colors; requested {num}.")
        return colors[:num]
 
    if palette.startswith("sns:"):
        name = palette[4:]
        return sns.color_palette(name, num)
 
    if palette in plt.colormaps:
        return plt.colormaps[palette].resampled(num).colors[:num]
 
    raise ValueError(
        f"Palette '{palette}' not recognised. "
        "Use 'personal', 'dark_photons', 'tol:<name>', 'sns:<name>', or a matplotlib colormap."
    )

