import os

def create_folder_structure(base_path):

    courses = {
        "Year_1": {
            "Semester_A": [
                "Calculus_A",
                "Linear_Algebra_A",
                "Discrete_Mathematics",
                "Introduction_to_Computer_Science",
                "Creativity_and_Innovation",
                "Research_Methods"
            ],
            "Semester_B": [
                "Calculus_B",
                "Linear_Algebra_B",
                "Data_Structures",
                "Logic_and_Set_Theory",
                "Innovation_and_Entrepreneurship_in_Organizations",
                "C_Programming"
            ],
        },
        "Year_2": {
            "Semester_A": [
                "Discrete_Mathematics",
                "Algorithms",
                "Digital_Architectures",
                "Introduction_to_Probability",
                "Guest_Lectures_Computer_Science",
                "Advanced_Programming"
            ],
            "Semester_B": [
                "Logic_and_Set_Theory",
                "Operating_Systems",
                "Product_Design_Prototyping_and_User_Experience",
                "Product_Management",
                "Computational_Learning",
                "Computational_Models"
            ],
        },
        "Year_3": {
            "Semester_A": [
                "Computer_Networks",
                "Practical_Seminar_in_Entrepreneurship",
                "Complexity_Theory",
                "CO-OP_Startup_Experience",
                "Human_Resources_for_Innovation",
                "Positive_Psychology"
            ],
            "Semester_B": [
                "AI_Tools_for_Entrepreneurs",
                "Innovation_in_Project_Management",
                "Decision_Making_in_Entrepreneurship"
            ],
        }
    }

    subfolders = ["Lectures", "Tutorials", "Assignments", "Assignment_Solutions", "Exam_Review/Summaries", "Exam_Review/My_Exams"]

    for year, semesters in courses.items():
        year_path = os.path.join(base_path, year)
        os.makedirs(year_path, exist_ok=True)

        for semester, course_list in semesters.items():
            semester_path = os.path.join(year_path, semester)
            os.makedirs(semester_path, exist_ok=True)

            for course in course_list:
                course_path = os.path.join(semester_path, course)
                os.makedirs(course_path, exist_ok=True)

                for subfolder in subfolders:
                    subfolder_path = os.path.join(course_path, subfolder)
                    os.makedirs(subfolder_path, exist_ok=True)

    print(f"Folder structure created successfully at {base_path}")


base_path = "/Users/your_username/Documents/Academics"
create_folder_structure(base_path)
