"""
this file is to storage the information about the information such as school sets and students sets
"""

from settings.config import num_schools, mean_num_subjects_in_school


class school_set:
    def __init__(self):
        self.num_schools = num_schools
        self.mean_num_subjects_in_school = mean_num_subjects_in_school
        self.school_list = []
    """
    school list : a list of school objects, every students need a school list to generate preference
    mean num subjects in school : to generate subjects
    """

    def gen_school_list(self):
        for i in range(self.num_schools):
