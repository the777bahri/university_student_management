import random

class Subject:
    def __init__(self):
        self.subject_name = ''

    def create_subject_id(self):
        return f"{random.randint(100, 999)}"

    def subject_mark(self):
        return random.randint(25, 100)

    def subject_grade(self,subject_mark):
        if subject_mark < 50:
            return 'Z'
        elif 50 <= subject_mark < 65:
            return 'P'
        elif 65 <= subject_mark < 75:
            return 'C'
        elif 75 <= subject_mark < 85:
            return 'D'
        else:
            return 'HD'
        
    def create_subject(self):
        print("\n creating a Subject....")
        subject_id = self.create_subject_id()
        subject_mark = self.subject_mark()
        subject_grade = self.subject_grade(subject_mark)
        print(f"\nsubject {subject_id} has a mark of {subject_mark} and grade of {subject_grade}")
        return subject_id, subject_mark, subject_grade
