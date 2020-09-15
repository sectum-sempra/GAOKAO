"""
2020.9.10
student class contains the information of each student and it contains the function to let
student apply some schools
"""
import numpy as np
from settings.config import total_people_num


class student:
    def __init__(self, id, score, rank, position, school_feature, subject_feature, school_subject_weight):
        self.id = id
        self.score = score
        self.rank = rank
        self.position = position
        self.school_subject_weight = school_subject_weight
        self.school_feature = school_feature
        self.subject_feature = subject_feature
        self.is_admitted = False

        self.ranked_school_subject_list = []  # only consider the first batch throwing
    """
    id : the unique number of this student, like exam number
    score : the score of the exam
    rank : the rank of the exam
    position : the school which have the same position will get higher weight of position in feature
    school_feature : a n_dim vector which pointed out the weight preference of [school score, position]
    subject_feature : like school feature, a vector which describes the preference of subjects
    school_subject_weight : a 2dim regular vector, means the weight of a student's preference to a school or a subject
    """

    def gen_school_subject_series(self, school_data):
        """
        this function is to generate a student favorite (school, subject) depend on his school feature,
        subject feature and school subject weight
        :param school_data: a list of school object(maybe need to expand to a dataframe like object)
        :return: a score list of sorted (school,subject,score) tuple
        """
        for sch in school_data:  # sch is a school object
            sch_id = sch.id
            same_position = 1 if sch.position == self.position else 0
            school_feature = np.array([sch.score, same_position])
            school_score = np.dot(school_feature, self.school_feature)
            for sub in sch.subjects:  # sub is a subject object
                sub_id = sub.id
                sub_feature = np.array([sub.employment, sub.study])
                sub_score = np.dot(sub_feature, self.subject_feature)
                total_score = np.array([school_score, sub_score])
                weighted_score = np.dot(total_score, self.school_subject_weight)
                self.ranked_school_subject_list.append((sch_id, sub_id, weighted_score))
        self.ranked_school_subject_list = sorted(self.ranked_school_subject_list, key=lambda s: s[2], reverse=True)

    def throw(self):
        """
        a function to describe how a student fill his wanted list
        :return: a dict like {school_id: [sub_id1,sub_id2,...]}
        """
        quantile = self.rank / total_people_num[self.position]
        school_quantile = max(int(quantile * len(self.ranked_school_subject_list)), 6)
        throw_school_ids = [t[0] for t in self.ranked_school_subject_list[school_quantile-6:school_quantile+6]]
        result = {}
        for school in throw_school_ids:  # school is id
            part_ranked_list = []
            for t in self.ranked_school_subject_list:
                if t[0] == school:
                    part_ranked_list.append(t)
            result[school] = part_ranked_list[:5]
        return result























