# Custom module to handle student properties
class Student:
    def __init__(self, student_name, roll_number):
        self.student_name = student_name
        self.roll_number = roll_number
        # Stores subject names as keys and scores as values
        self.course_marks = {}

    def assign_mark(self, course_name, score):
        self.course_marks[course_name] = score

    def get_average_score(self):
        if len(self.course_marks) == 0:
            return 0.0
        
        total = 0
        for score in self.course_marks.values():
            total += score
            
        return total / len(self.course_marks)

    def compute_final_grade(self):
        avg = self.get_average_score()
        
        # Grading scale matching university-style logic
        if avg >= 85:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 65:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "Fail"