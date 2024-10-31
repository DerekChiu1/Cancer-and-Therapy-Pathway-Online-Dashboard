"""
File title: Cancer_explore
Description: The backend program that calls the API functions and connects to the panel dashboard
Author: Souren Prakash, Kuan Chun Chiu, Atharva Nilapwar
Date: 2024/10/14
"""

from Cancer_API import CANAPI
from sankey import multi_layer_sankey
import panel as pn
from panel.widgets import Tabulator

# Initialize the API object
# Contributor: Kuan Chun Chiu
pn.extension()
file_name = "CTDC_Participants_download 2024-10-04 12-59-58.csv"
can_api = CANAPI()

# Load the cancer file
# Contributor: Kuan Chun Chiu
can_df = can_api.load_can(file_name)
can_df = can_api.clean_can()
can_df = can_api.create_age_ranges()

# Search widgets
# Contributor: Kuan Chun Chiu
min_patient_count = pn.widgets.IntSlider(name="Min patient count", start=1, end=5, value=1)
checkbox_group = pn.widgets.CheckBoxGroup(name="Sankey layer checkbox",
                                          value=["Age", "Gender"],
                                          options=["Age", "Gender"], inline=True)

# Plot widgets
# Contributor: Kuan Chun Chiu
width = pn.widgets.IntSlider(name="Diagram width", start=250, end=2000, step=125, value=1500)
height = pn.widgets.IntSlider(name="Diagram height", start=200, end=2500, step=100, value=800)


# menu widget
# Contributor: Atharva Nilapwar
data_table = Tabulator(can_df, pagination='remote', page_size=10, sizing_mode='stretch_width')

def grab_selection(selected_val):
    """
    Purpose: Grab the selection value for a selected column by the dashboard user
    Parameter: selected_val, the user-selected value for a specific column from the dashboard
    Return: The unique selected value names if selected_val exists, or else return an empty list
    Contributor: Souren Prakash
    """
    if selected_val:
        selection = can_api.get_unique_vals(selected_val)
        return selection
    return []

def update_values_dropdown(selected_column = None):
    """
    Purpose: Update the selected dropdown values based on the user input of selected column from the dashboard
    Parameter: selected_column (panel widget), the selected column name from the menu widget, the default value is None
    Return: N/A
    Contributor: Souren Prakash
    """
    if selected_column == "Remove Filter":
        values_dropdown.options = []
    else:
        options = grab_selection(selected_column)  # Get unique values from the selected column
        values_dropdown.options = options

# Menu items
# Contributor: Souren Prakash
columns_dropdown = pn.widgets.Select(name='Select Column', options=["Remove Filter"] + list(can_df.columns))
values_dropdown = pn.widgets.Select(name = 'Select Value', options = [])

# Callback functions:
def get_plot(min_patient_count, checkbox_group, width, height, selected_column, selected_val):
    """
    Purpose: Generate the multi-layer sankey diagram by calling the functions from the sankey library
    Parameter1: min_patient_count (int), the minimum patient count for each data flow in the sankey diagram
    Parameter2: checkbox_group (panel widget), a list of intermediate layer column names
    Parameter3: width (panel widget), the width of the sankey diagram
    Parameter4: height (panel widget), the height of the sankey diagram
    Parameter5: selected_column (panel widget), the selected column name from the menu widget
    Parameter6: selected_val (str), the selected data value from the selected column
    Return: fig, the plotly multi-layer sankey diagram object
    Contributor: Atharva Nilarwar, Kuan Chun Chiu
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

# Callback bindings
# Contributor: Kuan Chun Chiu
plot = pn.bind(get_plot, min_patient_count, checkbox_group, width, height,
               columns_dropdown.param.value, values_dropdown.param.value)

# Dashboard widgets card
# Contributor: Souren Prakash, Kuan Chun Chiu, Atharva Nilapwar
card_width = 320
search_card = pn.Card(
    pn.Column(
        min_patient_count,
        checkbox_group
    ),
    title="Search", width=card_width, collapsed=True
)

plot_card = pn.Card(
    pn.Column(
        width,
        height
    ),
    title="Plot", width=card_width, collapsed=True
)

menu_card = pn.Card(
    pn.Column(
    columns_dropdown,
    pn.bind(update_values_dropdown, columns_dropdown.param.value),
        values_dropdown),
    title= "Dropdown", width=card_width, collapsed=True
)

# Dashboard layout
# Contributor: Souren Prakash, Kuan Chun Chiu, Atharva Nilapwar
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
            active=0
        )
    ],
    header_background='#a93226'
)

layout.servable()
layout.show()