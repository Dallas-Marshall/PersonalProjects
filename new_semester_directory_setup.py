"""Script to create new subject folders and weekly folders (1-13) for a new semester in my JCU One Drive."""

import os

number_of_subjects = int(input("Number of Subjects: "))
year = input("Year: ")
study_period = input("Study period: ")
subject_codes = []
for subject in range(number_of_subjects):
    subject_code = input("Subject Code: ")
    subject_codes.append(subject_code)

os.chdir('/Users/marsh/OneDrive - James Cook University')

# check if year exists (already had a study period in that year)
is_dir = os.path.isdir(year)
if not is_dir:
    os.makedirs(year)

os.chdir(os.path.join('/Users/marsh/OneDrive - James Cook University', year))

# form study period directory name following my naming convention
study_period_file_name = "StudyPeriod0{}".format(study_period)
os.makedirs(study_period_file_name)
os.chdir(os.path.join('/Users/marsh/OneDrive - James Cook University', year, study_period_file_name))

# create each directory for each subject code and add weekly folders 1-13 following naming conventions.
for subject_code in subject_codes:
    os.makedirs(os.path.join(os.getcwd(), subject_code))
    for i in range(1, 14):
        if i < 10:
            os.makedirs(os.path.join(os.getcwd(), subject_code, "Week0{}".format(i)))
        else:
            os.makedirs(os.path.join(os.getcwd(), subject_code, "Week{}".format(i)))
