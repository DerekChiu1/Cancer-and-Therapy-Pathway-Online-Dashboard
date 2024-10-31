"""
File title: Cancer_API
Description: The API that mediates the data passing between the backend program and frontend dashboard interface
Author: Souren Prakash, Kuan Chun Chiu, Atharva Nilapwar
Date: 2024/10/14
"""

import pandas as pd

class CANAPI:
    """
    Purpose: The dashboard api class which establishes functions to load and clean the data file, and support
             the search/plot/menu widgets of the dashboard page
    Contributor: Souren Prakash, Kuan Chun Chiu
    """
    can = None
    def load_can(self, filename):
        """
        Purpose: Read the cancer csv dataset into a pandas dataframe
        Parameter: filename (str), the file path of the cancer csv file
        Return: self.can (df), the dataframe containing the cancer data
        Contributor: Souren Prakash
        """
        self.can= pd.read_csv(filename)
        return self.can

    def clean_can(self):
        """
        Purpose: Clean the dataframe by removing irrelevant columns and only pick the first therapy from each field of
                 the therapy column
        Parameter: N/A
        Return: self.can (df), the cleaned dataframe with proper value in the therapy column
        Contributor: Kuan Chun Chiu
        """
        self.can = self.can[["Diagnosis", "Age", "Sex", "Targeted Therapy"]]
        self.can.columns = ["Diagnosis", "Age", "Gender", "Therapy"]
        self.can["Therapy"] = self.can["Therapy"].apply(lambda x: x.replace("[", "").replace("]", "").split(",")[0])
        self.can["Therapy"] = self.can["Therapy"].apply(lambda x: "No_therapy_listed" if x == "" else x)
        return self.can

    def get_unique_vals(self,selected_col):
        """
        Purpose: To get a list of selected names of one of the sankey layer for the menu widgets
        Parameter: selected_col, the input name for the selected column. Ex: name "asthma" for the "Diagnosis" column
        Return: val_lst (list), the unique name list
        Contributor: Souren Prakash
        """
        val_lst = list(self.can[selected_col].unique())
        return val_lst

    def create_age_ranges(self):
        """
        Purpose: Add a new age range column to the self.can dataframe
        Parameter 1: N/A
        Return: self.can (df), the dataframe with the age range column added
        Contributor: Souren Prakash
        """
        self.can["Age"] = self.can["Age"].astype(int)
        youngest_marker = self.can["Age"].quantile(0.25)
        middle_marker = self.can["Age"].median()
        oldest_marker = self.can["Age"].quantile(0.75)
        def classify_age(age):
            """
            Purpose: Classify the patient's age into different age ranges
            Parameter: age (int), patient's age
            Return: A age range string for different ages
            Contributor: Souren Prakash
            """
            if age <= youngest_marker:
                return "youngest_age"
            elif age > youngest_marker and age <= middle_marker:
                return "middle_age"
            elif age > middle_marker and age <= oldest_marker:
                return "older_middle_age"
            else:
                return "oldest_age"
        self.can["Age"] = self.can["Age"].apply(classify_age)
        return self.can

    def group_df(self, group_list, min_patient_count, df):
        """
        Purpose: Group the df by two desired columns and add a artist_count column. Exclude rows where its artist_count
                 value is less than 20
        Parameter 1: group_list (list), the list of columns to group by
        Parameter 2: min_patient_count (int), the minimum count of patient in each flow of data in the sankey diagram
        Return: cancer_df, the df with patient count based on grouping the entered group columns
        Contributor: Kuan Chun Chiu
        """
        cancer_df = df
        if len(group_list) == 2:
            group_col1, group_col2 = group_list[0], group_list[1]
            cancer_df = cancer_df.groupby([group_col1, group_col2]).size().reset_index(name="Patient_count")
        elif len(group_list) == 3:
            group_col1, group_col2, group_col3 = group_list[0], group_list[1], group_list[2]
            cancer_df = cancer_df.groupby([group_col1, group_col2, group_col3]).size().reset_index(name="Patient_count")
        elif len(group_list) == 4:
            group_col1, group_col2, group_col3, group_col4 = group_list[0], group_list[1], group_list[2], group_list[3]
            cancer_df = cancer_df.groupby([group_col1, group_col2,
                                           group_col3, group_col4]).size().reset_index(name="Patient_count")
        cancer_df = cancer_df[cancer_df["Patient_count"] >= min_patient_count]
        return cancer_df

def main():
    """
    Purpose: Test and execute the CANAPI class and its functions within
    Parameter: N/A
    Return: N/A
    Contributor: Souren Prakash
    """
    canapi = CANAPI()
    can_df = canapi.load_can(filename)
    can_df = canapi.create_age_ranges()
    print(can_df)

if __name__ == '__main__':
    main()