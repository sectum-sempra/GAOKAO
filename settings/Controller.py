"""
this file is to create a way to config the whole process of school admitting
"""

from settings.config import num_schools, num_students
from settings.Initializer import School_Initializer, Student_Initializer
from tqdm.notebook import tqdm

school_initializer = School_Initializer()
student_initializer = Student_Initializer()


class Controller:
    def __init__(self):
        self.school_list = school_initializer.init_schools(num_schools)
        self.student_list = student_initializer.init_students(num_students)
        self.archive_list = self.all_student_throw()

        self.failed_admitted_list = []
    """
    school list : a list of school objects, every students need a school list to generate preference
    student list : a list of student objects
    archive list : a list of all the archives students throwing
    failed_admitted_list : a list of student id which cant be admitted
    
    the sub_idx of school list is the id of school. Maybe can use hash table
    the sub_idx of the archive list is the rank of the students
    """

    def all_student_throw(self):
        archive_list = [None] * num_students
        for idx, s in tqdm(enumerate(self.student_list)):
            s.gen_school_subject_series(self.school_list)
            archive_list[idx] = s.throw()
        return archive_list

    def admitted_to_school(self):
        for archive in self.archive_list:
            can_be_admitted = False
            for sch_id in archive.throw_dict.keys():
                if self.school_list[sch_id].res_num > 0:
                    self.school_list[sch_id].enroll(archive.id)
                    can_be_admitted = True
                    break
            if not can_be_admitted:
                self.failed_admitted_list.append(archive.id)
