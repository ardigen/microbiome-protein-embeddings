import numpy as np
import pandas as pd

from pandas.api import types

import holoviews as hv
import datashader as ds

from holoviews.operation.datashader import datashade, shade, dynspread, spread, rasterize

hv.extension('bokeh','matplotlib')
dynspread.max_px = 10
dynspread.threshold = 0.9

def to_hex(rgb):
    return "#%02x%02x%02x" % tuple(rgb)


def random_rgb():
    return np.random.choice(range(256), size=3)


def gen_color_key(values):
    return {k: to_hex(random_rgb()) for k in values}

def _cont_scatter(df, x, y, color=None, title='', **kwargs):

    points = hv.Scatter(
        df,
        kdims=[x, y],
        vdims=color,
        label=title,
    )

    scatterplot = rasterize(
        points,
        aggregator=ds.mean(color) if color else 'default',
        # width=2400,
        # height=2400,
    )

    opts = dict(
        cmap="coolwarm",
        cnorm="eq_hist",
        colorbar=True,
        clabel=color,
    )
    return scatterplot.opts(**opts)


def _cat_scatter(df, x, y, color=None, title='', **kwargs):

    # Skipping obtrusive warning
    import logging
    logging.getLogger("param").setLevel(logging.ERROR)

    points = {
        c: hv.Scatter(data, kdims=[x, y], vdims=color, label=title)
        for c, data in df.groupby(color)
    }
    color_key = gen_color_key(df[color].unique())

    scatterplot = datashade(
        hv.NdOverlay(points, kdims=color),
        aggregator=ds.count_cat(color),
        color_key=color_key,
    )

    opts = dict()
    opts.update(**kwargs)
    return scatterplot.opts(**opts)

def scatterplot(df, x, y, color=None, px=None, **kwargs):


    # If the color column is continous
    if types.is_numeric_dtype(df[color]):
        scatterplot = _cont_scatter(df, x, y, color, **kwargs)
    # If the color column is categorical
    # elif types.is_string_dtype(df[color]):
    else:
        scatterplot = _cat_scatter(df, x, y, color, **kwargs)

    if px:
        scatterplot = spread(scatterplot, px=px)

    opts = dict(
        width=600,
        height=600,
        tools=['hover'],
        fontsize={'title': 12, 'labels': 11, 'xticks': 9, 'yticks': 9},
        fontscale=1.6
    )
    opts.update(**kwargs)

    return scatterplot.opts(
        **opts
    )
