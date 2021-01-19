"""
Script to create new subject folders and weekly folders (1-13) for a new Study Period.
Hierarchy Structure for each Subject:
    Year (e.g. '2021')
        Study Period (e.g. 'Study Period 01')
            Week Folders 1-13 (e.g 'Week 01')
"""

import os

print("Welcome to my Automatic University Folder Creator:")
print("--- Created by Dallas Marshall")
print("Program will create folders in a specified directory with the following hierarchy structure for each Subject:")
print("\tYear (e.g. '2021')\n\t\tStudy Period (e.g. 'Study Period 01')\n\t\t\tWeek Folders 1-13 (e.g 'Week 01')\n")

path_to_directory = input(
    'Path to Parent Directory (Where you want the year file to be placed) e.g. /Users/name/OneDrive: ')
year = input("Year of Study: ")
study_period = int(input("Study Period # (e.g. 1): "))
number_of_subjects = int(input("Number of Subjects Studied: "))

subject_codes = []
for subject in range(number_of_subjects):
    subject_code = input("Subject Code: ")
    subject_codes.append(subject_code)

os.chdir(path_to_directory)
is_dir = os.path.isdir(year)
if not is_dir:  # Year directory doesn't already exist
    os.makedirs(year)

os.chdir(os.path.join(path_to_directory, year))  # Move into year directory

study_period_file_name = "StudyPeriod{:02d}".format(study_period)
is_dir = os.path.isdir(study_period_file_name)
if not is_dir:  # Study Period directory doesn't already exist
    os.makedirs(study_period_file_name)

os.chdir(os.path.join(path_to_directory, year, study_period_file_name))  # Move into study period directory

for subject_code in subject_codes:
    os.makedirs(os.path.join(os.getcwd(), subject_code))
    for week_number in range(1, 14):  # Folders for weeks 1-13
        os.makedirs(os.path.join(os.getcwd(), subject_code, "Week{:02d}".format(week_number)))
