"""
File title: sankey
Author: Souren Prakash, Kuan Chun Chiu, Atharva Nilapwar
Description: The sankey library containing the make_sankey function and multi_layer_sankey function
Date: 2024/10/14
"""

# This file is made to only construct the multi_layer_sankey() functions, so no main() function is constructed
# or called at the end. This file only serves as a library so that files from future work can import this library and
# call the sankey function within, in order to make the sankey diagrams.

import pandas as pd
import plotly.graph_objects as go

def multi_layer_sankey(cancer_df, *args, **kwargs):
    """
    Purpose: Make a multi-layer sankey diagram with unlimited number of intermediate layers
    Parameter1: cancer_df (df), the dataframe containing the cancer datasets
    Parameter2: args (tuple), the tuple containing the column names of the intermediate layer
    Parameter3: kwargs (dict), the dictionary containing the width and height of the sankey diagram
    Return: fig, the multi-layer sankey diagram object from plotly
    Contributor: Atharva Nilapwar, Kuan Chun Chiu
    """
    if len(args) < 2:
        raise ValueError("At least two layers (source and target) are required.")
    all_columns = pd.concat([cancer_df[col] for col in args])
    label = list(all_columns.unique())
    indices = [cancer_df[col].apply(lambda x: label.index(x)) for col in args]
    source = pd.concat(indices[:-1])
    target = pd.concat(indices[1:])
    value = pd.concat([cancer_df["Patient_count"]] * (len(args) - 1))
    link = {"source": source, "target": target, "value": value}
    node = {"pad": 50, "thickness": 50, "label": label}
    sk = go.Sankey(link=link, node=node)
    fig = go.Figure(sk)
    width = kwargs.get("width", 1500)
    height = kwargs.get("height", 800)
    fig.update_layout(autosize=False, width=width, height=height)
    return fig