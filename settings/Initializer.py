"""
this file provides a way to initialize the school data and student data
"""


from settings.School import school, subject
from settings.Student import student
import numpy as np
import random


class School_Initializer:
    @staticmethod
    def init_a_subject(idx, class_id, employment_score, study_score, res_num):
        return subject(idx, class_id, employment_score, study_score, res_num)

    @staticmethod
    def init_a_school(idx, subject_list, school_score, position):
        return school(idx, subject_list, school_score, position)

    def init_schools(self, num_schools):
        """
        using initializer to initialize a list of random schools
        school scores is distributed by a normal distribution (2,0.5)
        num_subjects in a school [1,11)
        class id is all set as 0
        features of the subject is initialized by N(2,0.3)
        res_num of a subject is (1,50]
        total number of subjects is 10 which is indexed by int [1,21)
        :return: a list of school object
        """
        school_list = []
        scores = np.random.normal(2, 0.5, num_schools)
        num_subjects = np.random.randint(1, 11, num_schools)
        for idx in range(num_schools):
            subject_list = []
            sub_ids = random.sample(range(1, 21), num_subjects[idx])
            for sub_idx in range(num_subjects[idx]):
                employment_score = np.random.normal(2, 0.3)
                study_score = np.random.normal(2, 0.3)
                res_num = np.random.randint(1, 51)
                subject_list.append(self.init_a_subject(sub_ids[sub_idx], 0, employment_score, study_score,
                                                        res_num))
            position = np.random.randint(0, 4)
            school_list.append(self.init_a_school(idx, subject_list, scores[idx], position))
        return school_list


class Student_Initializer:
    @staticmethod
    def init_a_student(idx, score, rank, position, school_feature, subject_feature, school_subject_weight):
        return student(idx, score, rank, position, school_feature, subject_feature, school_subject_weight)

    def init_students(self, num_students):
        """
        initialize a list of students and a list
        :return: a list of student object
        """
        students_list = []
        scores = list(np.round(np.random.normal(550, 50, num_students)))
        students_info = list(zip(range(num_students), scores))  # gen a (id,score) tuple
        students_info = sorted(students_info, key=lambda s: s[1], reverse=True)
        for rank, (idx, score) in enumerate(students_info):
            position = np.random.randint(0, 4)
            temp_random = np.random.uniform()
            school_subject_weight = np.array([temp_random, 1-temp_random])
            temp_random = np.random.uniform()
            school_feature = np.array([temp_random, 1-temp_random])
            temp_random = np.random.uniform()
            subject_feature = np.array([temp_random, 1-temp_random])
            students_list.append(self.init_a_student(idx, score, rank, position, school_feature,
                                                     subject_feature, school_subject_weight))
        return students_list



