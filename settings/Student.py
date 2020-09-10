"""
2020.9.10
student class contains the information of each student and it contains the function to let
student apply some schools
"""


class student:
    def __init__(self, id, score, rank, position, feature, subject_weight):
        self.id = id
        self.score = score
        self.rank = rank
        self.position = position
        self.subject_weight = subject_weight
        self.feature = feature
    """
    id : the unique number of this student, like exam number
    score : the score of the exam
    rank : the rank of the exam
    position : the school which have the same position will get higher weight of position in feature
    feature : a n_dim vector which pointed out the weight preference of [school rank, position, other]
    subject_weight : a 2dim regular vector, means the weight of a student's preference to a school or a subject
    """

