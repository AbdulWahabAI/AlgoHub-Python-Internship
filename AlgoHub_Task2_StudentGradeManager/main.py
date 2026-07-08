# Importing the custom module built for student tracking
import student_module

def start_app():
    records = []
    
    print("--- AlgoHub Academic Record System ---")
    
    while True:
        print("\n[Menu Options]")
        print("1) Add New Student Entry")
        print("2) Show All Performance Reports")
        print("3) Shutdown Program")
        
        user_input = input("Select an action: ")
        
        if user_input == "1":
            name = input("Enter Full Name: ")
            roll_no = input("Enter Roll Number / ID: ")
            
            # Creating object instance
            obj = student_module.Student(name, roll_no)
            
            try:
                count = int(input("How many courses to add? "))
                for i in range(count):
                    course = input(f"Course {i+1} Name: ")
                    marks = float(input(f"Enter marks achieved in {course}: "))
                    obj.assign_mark(course, marks)
                
                records.append(obj)
                print(f"Record successfully updated for {name}.")
            except ValueError:
                print("Error: Please enter a valid number for counts/marks.")
                
        elif user_input == "2":
            if len(records) == 0:
                print("Database empty. No entries found.")
            else:
                print("\n================ STUDENT MARKSHEETS ================")
                for item in records:
                    final_avg = item.get_average_score()
                    grade_result = item.compute_final_grade()
                    print(f"Roll No: {item.roll_number} | Student: {item.student_name} | Avg: {final_avg:.1f} | Result: {grade_result}")
                print("====================================================")
                
        elif user_input == "3":
            print("Exiting application console. Goodbye!")
            break
        else:
            print("Invalid input. Type 1, 2, or 3.")

if __name__ == "__main__":
    start_app()