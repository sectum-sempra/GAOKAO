"""
2020.9.10
this file is about the basic information of schools, but still dont know how to describe the interaction
of schools and their subject
"""


class school:  # subject belongs to schools
    def __init__(self, id, subject_list, school_score, position):
        self.id = id
        self.subjects = subject_list
        self.score = school_score
        self.position = position
        self.res_num = self.get_total_res_num()
        self.enrolled_student = []
    """
    id : id of schools
    subjects : subject dict list of the school
    score : (can be expanded by some quotas) a score which can show the level of the school
    position : the position id of this school
    res_num : total remaining number of the school
    enrolled_student : a list of student id (student object?) which has been enrolled in this school
    """

    def get_total_res_num(self):
        res_num = 0
        for s in self.subjects:
            res_num += s['res_num']
        return res_num

    def enroll(self, student_id):  # enroll a student
        self.enrolled_student.append(student_id)

    def


class subject:
    def __init__(self, id, subject_score, subject_class_id, total_num):
        self.id = id
        self.class_id = subject_class_id
        self.score = subject_score
        self.res_num = total_num
    """
    id : id of subject (unique)
    class_id : for major class enrollment
    score : a score which can show the level of this subject
    total_num : the remaining number of this subject in enrollment
    
    
    subject belongs to school
    """

    def gen_subject_dict(self):  # gen a dict which can describe this subject
        return {
            'id' : self.id,
            'class_id' : self.class_id,
            'score:' : self.score,
            'res_num' : self.res_num
        }

    def enroll_a_student(self):
        self.res_num -= 1



