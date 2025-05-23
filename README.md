# Cancer and Therapy Pathway Dashboard

## Project Description
This project built an online dashboard to show the pathway flowing from various cancers to their corresponding therapies, with patient data including age and gender incorporated. This allows users to identify the characteristics of patients for each specific cancer, find the most recommended therapy for different diseases, and compare the difference in distribution of patients' age and gender between different cancers. This dashboard contains interactive visualizations like Sankey diagrams and tables, and static ones like bar plot and box plot. The interactive diagrams can take in real time user input from checkbox, sliders, and dropdown menu on the dashboard side bar, then the diagrams are re-rendered and manipulated based on users' desire to gain insights.

## Dashboard Images
![Sankey Diagram](https://github.com/user-attachments/assets/88d40a75-09f6-447c-8844-a10792faf4d6)
![Data Table](https://github.com/user-attachments/assets/c268c029-7783-4dbc-979a-8697acef59cc)
![Dataset Analysis Plot 1 & 2](https://github.com/user-attachments/assets/1e72bbd2-e6cb-4e52-8a95-854c8024ebb9)
![Dataset Analysis Plot 3 & 4](https://github.com/user-attachments/assets/223c92f3-7bd9-49b7-885f-b3012b6b83d6)


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
This dashboard has three tabs, being Network, Data Table, and Dataset Analysis. The Network tab includes an interactive Sankey diagram with four layers, from the left to right are cancer, age, gender, and therapy layer. A layer has multiple boxes/categories, for example, the cancer layer has eight boxes since there are eight different cancers in the dataset. When hover over a layer box, information of its name, incoming flow, and outgoing flow are shown. For example, "Male, incoming flow: 70, outgoing flow: 70" means this is the male category in the gender layer, and there are 70 data flow coming in and out of that box. Next, each data flow can contain 1 or more number of records, which is indicated by the number on the left when a flow is hovered. For example, one data flow with 7 records going through lung cancer, pre senior, and male means there are 7 patients who all got lung cancer, who are in the age group of pre senior, and they are male. The thickness of the data flow is based on the number of records it contains, where more records results in a thicker flow and vice versa. For the data table tab, it shows the data used to built this dashboard in a tabular format through an interactive table, which is the same as the csv file. The table has 248 rows indicating 248 patient records, and it has 5 columns indicating the index key and informatino of 4 layers in the Sankey diagram. The Dataset Analysis tab contains several graphs for the general analysis of the dataset used, such as a box plot showing the distribution of the age of male and female patients, which allows users to better understand the dataset in different aspects. Lastly, the sidebar locates on the left side of the dashboard, which contains different tools for users to manipulate the Sankey diagram, including a two sliders, one checkbox, and one dropdown menu. The sidebar can be toggled to give more space for the visualizations.

### Interactive Functionalities:
- Sankey Diagram (Network tab)

The first interactive tool you can use on the sidebar is a slider called min patient count, which allows you to decide a minimum theshold of the number of records for each data flow. If you increase it to 3, then the sankey diagram will shrink since only those data flows with at least 3 records will remain. The second tool is a checkbox that comes with two boxes, one for age and one for gender, which represent the two middle layers of the Sankey diagram. IF you check both boxes, then both middle layers remain, but when you uncheck age for example, the age layer will be removed. Of course, if you uncheck both boxes, then both the age and gender layers are removed so you'll now have a two layer Sankey diagram with just the cancer and therapy layers. The third tool comes with two sliders called width and height, which allows you to adjust the height and width of the Sankey diagram. It's straightforward as the more you increase the value by dragging the sliders to the right, the larger the dimension of the diagram gets in its height and width, vice versa. The last tool is a dropdown menu, where you can select one of the four layers from the first dropdown, and select one of the category of the selected layer from the second dropdown. This alters the Sankey diagram as for your selected layer, only the selected category/box remains while the rest are excluded. For example, if you only care about the male patients, then you can select "Gender" and "Male" from the dropdown menu, which left you with a diagram that only includes the cancer diagnosis, age, and therapy information for those male patients. Overall, using these four interactive tools on the sidebar, you can freely play around and manipulate the Sankey diagram based on your desire to gain insights from the dataset and the pathway between various cancers and therapies.
- Table (Data Table tab)

In the Data Table tab, there are a few buttons next to the table, including prev, next, first, last, as well as page 1, 2, 3, 4, 5 and so on. These buttons allows users to navigate to different pages of the data table, including the next page, previous page, first page, last page, or any other page by directly clicking the number. This allows users to focus on only a few rows/patient records at a time rather than looking at the entire table with 248 rows as it might be distracting or cause confusion. Lastly, when hover over a row, that row turns blue while the rest remain grey to indicate which row you're currently looking at. overall, this table allows users to directly observe the data not through a multi-layer approach using Sankey diagram, but in a tabular form through a table.

### Interpreting Static Visualizations:
The first plot in the Dataset Analysis tab is a box plot, showing the age distribution of male and female patients from the dataset. It's a side-by-side box plot that the two boxes correspond to the two genders. When hover over each box, statistical information including the q1, median, q3, and total number of patients are shown. The second plot is a pie chart showing the percentage distribution between male and female patients, and the numerical percentage value is shown when you hover over the pie area. The third plot is a horizontal stacked bar chart showing the number of diagnosis of different cancers for males and females, where each cancer has its own bar and each bar is stacked as it includes the number of patients from both genders. The last plot is another horizontal stacked bar chart, but showing the number of diagnosis of different cancers across different races. Again, each cancer has its own stacked bar and the bar is composed of different segments corresponding to different races of the patients who got that specific cancer. Overall, these four plots allows users to understand the dataset more from a statistical viewpoint, including aspects of patients' age, gender, races, and number of diagnosis for different cancers.

## Analysis You Can Do Using This Dashboard
- Given a patient's age, gender, and the cancer he got, how to find the most recommended therapy for him?
- Given a patient's age, gender, and the therapy he's treated with, how to know which cancer does he have?
- Given a specific cancer, are male or female patients more likely to get the disease over the other?
- Given a specific cancer, which age group is the most or least likely to get the disease?
- Given a same disease, is there a difference in the therapy used between male and female patients? Is it the same between younger and older patients?

## Contributors
1. Kuan-Chun Chiu (Myself) - beagledirk1@gmail.com
2. Atharva Nilapwar - nilapwar.a@northeastern.edu
4. Souren Prakash - prakash.so@northeastern.edu
