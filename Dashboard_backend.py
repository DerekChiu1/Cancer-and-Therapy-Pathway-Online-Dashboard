"""
File title: Dashboard_backend.py
Description: The backend program that calls the API functions and connects to the panel dashboard
Author: Kuan Chun Chiu
Date: 2024/10/14
"""

from panel.widgets import Tabulator
import plotly.graph_objects as go
from Dashboard_API import CANAPI
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import pandas as pd
import numpy as np
import panel as pn

def initialize_api():
    """
    Purpose: Initialize the API object to load a csv file into a data frame
    Parameter: N/A
    Return: can_df (data frame), a data frame storing data from the cancer csv file
    """
    pn.extension()
    file_name = "Cancer_therapy.csv"
    can_api = CANAPI()
    can_df = can_api.load_can(file_name)
    can_df = can_api.clean_can()
    can_df = can_api.create_age_ranges()
    return (can_df, can_api)

def create_widgets(can_df):
    """
    Purpose: Create the search, plot, and dropdown menu widget object
    Parameter: can_df (data frame), a data frame storing data from the cancer csv file
    Return: all_widgets (dict), a dictionary storing all widget objects created
    """
    min_patient_count = pn.widgets.IntSlider(name="Min patient count", start=1, end=5, value=1)
    checkbox_group = pn.widgets.CheckBoxGroup(name="Sankey layer checkbox", value=["Age", "Gender"],
                                              options=["Age", "Gender"], inline=True)
    width = pn.widgets.IntSlider(name="Diagram width", start=250, end=2000, step=125, value=1500)
    height = pn.widgets.IntSlider(name="Diagram height", start=200, end=2500, step=100, value=800)
    columns_dropdown = pn.widgets.Select(name="Select Column", options=["Remove Filter"] + list(can_df.columns))
    values_dropdown = pn.widgets.Select(name = "Select Value", options = [])
    all_widgets = (min_patient_count, checkbox_group, width, height, columns_dropdown, values_dropdown)
    return all_widgets

def plot_age_distribution(can_df):
    api = CANAPI()
    df = api.load_can("Cancer_therapy.csv")
    df = api.clean_can()
    fig = px.box(df, y="Age", color="Gender")
    fig.update_layout(
        title = "Age Distribution of Patients",
        xaxis_title = "Gender",
        yaxis_title = "Age"
    )
    return fig

def plot_sex_distribution(can_df):
    gender_count = can_df["Gender"].value_counts()
    fig = px.pie(values=gender_count, names=gender_count.index)
    fig.update_layout(
        title = "Gender Distribution of Patients"
    )
    return fig

def plot_diag_per_gender(can_df):
    copy_df = can_df.copy()
    copy_df = copy_df.groupby(["Diagnosis", "Gender"]).size().reset_index(name="count")
    fig = px.bar(copy_df, x="count", y="Diagnosis", color="Gender", barmode="stack")
    fig.update_layout(
        title = "Cancer Diagnosis per Gender",
        xaxis_title = "Number of diagnosis",
        yaxis_title = "Cancer",
        width = 800
    )
    return fig

def plot_diag_per_race():
    api = CANAPI()
    df = api.load_can("Cancer_therapy.csv")
    df = api.clean_can(race=True)
    df = df.groupby(["Diagnosis", "Race"]).size().reset_index(name="count")
    fig = px.bar(df, x="count", y="Diagnosis", color="Race", barmode="stack")
    fig.update_layout(
        title = "Cancer Diagnosis per Race",
        xaxis_title = "Number of diagnosis",
        yaxis_title = "Cancer",
        width = 1200
    )
    return fig

def multi_layer_sankey(cancer_df, *args, **kwargs):
    """
    Purpose: Make a multi-layer sankey diagram with unlimited number of intermediate layers
    Parameter1: cancer_df (df), the dataframe containing the cancer datasets
    Parameter2: args (tuple), the tuple containing the column names of the intermediate layer
    Parameter3: kwargs (dict), the dictionary containing the width and height of the sankey diagram
    Return: fig, the multi-layer sankey diagram object from plotly
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

def get_plot(min_patient_count, checkbox_group, width, height, selected_column, selected_val, can_df, can_api):
    """
    Purpose: Generate the multi-layer sankey diagram by calling the functions from the sankey library
    Parameter1: min_patient_count (int), the minimum patient count for each data flow in the sankey diagram
    Parameter2: checkbox_group (panel widget), a list of intermediate layer column names
    Parameter3: width (panel widget), the width of the sankey diagram
    Parameter4: height (panel widget), the height of the sankey diagram
    Parameter5: selected_column (panel widget), the selected column name from the menu widget
    Parameter6: selected_val (str), the selected data value from the selected column
    Return: fig, the plotly multi-layer sankey diagram object
    """
    if selected_column == "Remove Filter":
        filtered_df = can_df
    elif selected_column and selected_val:
        filtered_df = can_df[can_df[selected_column] == selected_val]
    else:
        filtered_df = can_df
    layers = ["Diagnosis"] + checkbox_group + ["Therapy"]
    group_list = layers
    cancer_df = can_api.group_df(group_list, min_patient_count, df=filtered_df)
    fig = multi_layer_sankey(cancer_df, *layers, width=width, height=height)
    return fig

def grab_selection(selected_val, can_api):
    """
    Purpose: Grab the selection value for a selected column by the dashboard user
    Parameter: selected_val, the user-selected value for a specific column from the dashboard
    Return: The unique selected value names if selected_val exists, or else return an empty list
    """
    if selected_val:
        selection = can_api.get_unique_vals(selected_val)
        return selection
    return []

def update_values_dropdown(values_dropdown, can_api, selected_column = None):
    """
    Purpose: Update the selected dropdown values based on the user input of selected column from the dashboard
    Parameter: selected_column (panel widget), the selected column name from the menu widget, the default value is None
    Return: N/A
    """
    if selected_column == "Remove Filter":
        values_dropdown.options = []
    else:
        options = grab_selection(selected_column, can_api)
        values_dropdown.options = options

def create_widget_cards(all_widgets, can_api):
    min_patient_count, checkbox_group, width, height, columns_dropdown, values_dropdown = all_widgets
    card_width = 320
    search_card = pn.Card(
        pn.Column(
            min_patient_count,
            checkbox_group
        ),
        title="Search", width=card_width, collapsed=False
    )
    plot_card = pn.Card(
        pn.Column(
            width,
            height
        ),
        title="Plot", width=card_width, collapsed=False
    )
    columns_dropdown.param.watch(lambda event: update_values_dropdown(values_dropdown, can_api, event.new), "value")
    menu_card = pn.Card(
        pn.Column(
            columns_dropdown,
            values_dropdown
        ),
        title="Dropdown", width=card_width, collapsed=False
    )
    all_cards = [search_card, plot_card, menu_card]
    return all_cards

def launch_dashboard(all_cards, plot, data_table, all_dataset_plots):
    age_plot, sex_plot, gender_plot, race_plot = all_dataset_plots
    search_card, plot_card, menu_card = all_cards
    layout = pn.template.FastListTemplate(
        title="The Diagnosis & Therapy Linkage Dashboard",
        sidebar=[
            search_card,
            plot_card,
            menu_card
        ],
        theme_toggle=False,
        main=[
            pn.Tabs(
                ("Network", plot),
                ("Data Table", data_table),
                ("Dataset Analysis", pn.Column(age_plot, sex_plot, gender_plot, race_plot)),
                active=0
            )
        ],
        header_background="#a93226"
    )
    layout.servable()
    layout.show()

def main():
    can_df, can_api = initialize_api()
    age_plot = plot_age_distribution(can_df)
    sex_plot = plot_sex_distribution(can_df)
    gender_plot = plot_diag_per_gender(can_df)
    race_plot = plot_diag_per_race()
    all_dataset_plots = [age_plot, sex_plot, gender_plot, race_plot]
    all_widgets = create_widgets(can_df)
    min_patient_count, checkbox_group, width, height, columns_dropdown, values_dropdown = all_widgets
    plot = pn.bind(get_plot, min_patient_count, checkbox_group, width, height,
                   columns_dropdown.param.value, values_dropdown.param.value, can_df, can_api)
    data_table = Tabulator(can_df, pagination='remote', page_size=10, sizing_mode='stretch_width')
    all_cards = create_widget_cards(all_widgets, can_api)
    launch_dashboard(all_cards, plot, data_table, all_dataset_plots)

if __name__ == "__main__":
    main()