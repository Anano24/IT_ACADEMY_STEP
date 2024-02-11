# დავალება 2.

# შექმენით კლასი სახელწოდებით Student ატრიბუტებით,
# როგორიცაა name, student_id და courses(კურსების სია, რომელშიც სტუდენტი არის ჩარიცხული).
# აღწერეთ სტუდენტის ინფორმაციის და კურსების ჩვენების მეთოდები.
# შექმენით რამდენიმე ობიექტი და დაარეგისტრირეთ სხვადასხვა კურსებზე.


class Student:

    def __init__(self, name, student_id, courses=[]):
        self.name = name
        self.student_id = student_id
        self.courses = courses


    def student_info(self):
        print(f"I am {self.name}")

    
    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"{self.name} was enrolled in {course} already!")


    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{self.name} is not enrolled in {course}") 

    
    def display_courses(self):
        courses_str = f"{self.name}'s courses:\n"
        for course in self.courses:
            courses_str += f"- {course}\n"
        return courses_str
        

    
student = Student("John", 1, ["Math", "English"])
student.student_info()
student.add_course("English")
print(student.display_courses())


student2 = Student("Emily", 2, ["Physics", "History", "Biology"])
student2.student_info()
print(student2.display_courses())
student2.remove_course("History")
print(f"{student2.name} removed a course.")
print(student2.display_courses())


    