# Cancer and Therapy Pathway Dashboard

## Description
This project built an online dashboard to show the pathway flowing from various cancers to their corresponding therapies, with patient data including age and gender incorporated. This allows users to identify the characteristics of patients for each specific cancer, find the most recommended therapy for different diseases, and compare the difference in distribution of patients' age and gender between different cancers. This dashboard contains interactive visualizations like Sankey diagrams and tables, and static ones like bar plot and box plot. The interactive diagrams can take in real time user input from checkbox, sliders, and dropdown menu on the dashboard side bar, then the diagrams are re-rendered and manipulated based on users' desire.

## How to Install and Run the Dashboard
### Dependencies:
  panel >= 1.5.0
  matplotlib >= 3.9.2
  plotly >= 5.22.0
  seaborn >= 0.13.2
  pandas >= 2.2.2
  numpy >= 1.26.4
### Instructions:
  1. Make sure all libraries in the above dependency list are installed to your current working environment
  2. Download the csv file and two py files from this repository, in which the csv file contains the data while the py files contain the python code to launch the online dashboard
  3. Run the Dashboard_backend.py file and the dashboard should launch in a few seconds on the browser

### Troubleshooting:
  - If there's error reading the csv file, make sure it's in the same directory as your two py files, and its name isn't modified after downloaded
  - If there's error with the libraries used, make sure they're all properly installed to your current environment, and the version are the same or newer than the versions in the dependency list
  - If there's error with launching the dashboard, make sure you have stable and reliable internet connection. If necessary, reinstall the browser or restart your computer before running the file again

## How to Use the Dashboard
