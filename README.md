# Cancer and Therapy Pathway Dashboard

## Description
This project built an online dashboard to show the pathway flowing from various cancers to their corresponding therapies, with patient data including age and gender incorporated. This allows users to identify the characteristics of patients for each specific cancer, find the most recommended therapy for different diseases, and compare the difference in distribution of patients' age and gender between different cancers. This dashboard contains interactive visualizations like Sankey diagrams and tables, and static ones like bar plot and box plot. The interactive diagrams can take in real time user input from checkbox, sliders, and dropdown menu on the dashboard side bar, then the diagrams are re-rendered and manipulated based on users' desire.

## How to Install and Run the Dashboard
### Dependencies:
  - panel >= 1.5.0
  - matplotlib >= 3.9.2
  - plotly >= 5.22.0
  - seaborn >= 0.13.2
  - pandas >= 2.2.2
  - numpy >= 1.26.4
### Instructions:
  1. Make sure all libraries in the above dependency list are installed to your current working environment
  2. Download the csv file and two py files from this repository, in which the csv file contains the data while the py files contain the python code to launch the online dashboard
  3. Run the Dashboard_backend.py file and the dashboard should launch in a few seconds on the browser
### Troubleshooting:
  - If there's error reading the csv file, make sure it's in the same directory as your two py files, and its name isn't modified after downloaded
  - If there's error with the libraries used, make sure they're all properly installed to your current environment, and the version are the same or newer than the versions in the dependency list
  - If there's error with launching the dashboard, make sure you have stable and reliable internet connection. If necessary, reinstall the browser or restart your computer before running the file again

## How to Use the Dashboard
### Dashboard Overview:
This dashboard has three tabs, being Network, Data Table, and Dataset Analysis. The Network tab includes an interactive Sankey diagram with four layers, from the left to right are cancer, age, gender, and therapy layer. A layer has multiple boxes/categories, for example, the cancer layer has eight boxes since there are eight different cancers in the dataset. When hover over a layer box, information of its name, incoming flow, and outgoing flow are shown. For example, "Male, incoming flow: 70, outgoing flow: 70" means this is the male category in the gender layer, and there are 70 data flow coming in and out of that box. Next, each data flow can contain 1 or more number of records, which is indicated by the number on the left when a flow is hovered. For example, one data flow with 7 records going through lung cancer, pre senior, and male means there are 7 patients who all got lung cancer, who are in the age group of pre senior, and they are male. The thickness of the data flow is based on the number of records it contains, where more records results in a thicker flow and vice versa. For the data table tab, it shows the data used to built this dashboard in a tabular format through an interactive table, which is the same as the csv file. The table has 248 rows indicating 248 patient records, and it has 5 columns indicating the index key and 4 layers in the Sankey diagram. The Dataset Analysis tab contains several graphs for the general analysis of the dataset used, such as a box plot showing the distribution of the age of male and female patients, which allows users to better understand the dataset in different aspects. Lastly, the sidebar locates on the left side of the dashboard, containing different tools for the users to manipulate the diagrams, which can be toggled to give more space for the visualizations.
## Interactive Functionalities:



