from functools import reduce
class Course:
    """
            A class to represent a Course.
            ...
            Attributes
            ----------
            grade_course : int
                grade of the course
            name_course : str
                name of the course
            Methods
            -------
            setGrade(self, grade):
            Gets a grade. Updates the grade when the grade is between 0 and 100
            """

    def __init__(self, name):
        """
                        Constructs all the necessary attributes for the course object.

                        Parameters
                        ----------
                            grade_course : int
                                grade of the course
                            name_course : str
                                name of the course
                        """
        self.grade_course = 101
        self.name_course = name
    def setGrade(self, grade):
        '''
                    Gets a grade. Updates the grade when the grade is between 0 and 100.
                     Parameters:
                    grade (int): A decimal integer
                '''
        if grade >=0 and grade<= 100:
            self.grade_course = grade

    def __repr__(self):
        """
                :return: Name of class
                """
        return 'name of course: ' + f'{self.name_course}' + '   grade: ' + f'{self.grade_course}'
        #return 'Course()'

    def __str__(self):
        """
                :return: name and grade of course.
                """
        return 'name of course: ' + f'{self.name_course}' + '   grade: ' + f'{self.grade_course}'

class Student:
    """
                A class to represent a Student.
                ...
                Attributes
                ----------
                name_student : str
                    name of the student
                _id : str
                    id of the student
                course_list : course
                    list of student courses
                Methods
                -------
                getID(self):
                return id
                addCourse(self, newCourse):
                Adds the course to the list if the grade in the course is correct - between 0 and 100

                """
    def __init__(self, name_student, _id):
        """
                Constructs all the necessary attributes for the student object.

                Parameters
                ----------
                name_student : str
                name of the student
                _id : str
                id of the student
                course_list: course
                list of student courses

                """
        self.name_student = name_student
        self._id = _id
        self.course_list = []
    def getID(self):
        """
                :return: id
                """
        return self._id
    def addCourse(self, newCourse):
        """
                Adds the course to the list if the grade in the course is correct - between 0 and 100
                :param newCourse: Object type course
                """
        if newCourse.grade_course >= 0 and newCourse.grade_course <= 100:
            self.course_list.append(newCourse)

    def __repr__(self):
        """
                :return: Name of class
                """
        return 'name of student: ' + f'{self.name_student}' + '  id: ' + f'{self._id}' + '  courses:  ' + f'{self.course_list}'
        #return 'Student()'
    def __str__(self):
        """
                :return: name, id, list of courses of the student.
                """
        return 'name of student: ' + f'{self.name_student}' + '  id: ' + f'{self._id}' + '  courses:  ' + f'{self.course_list}'

name_file = input("Enter a name of the file: ")

try:
    students_list = []
    with open(name_file, "r") as f:
        line = f.readlines()

    for i in range(len(line)):
        tmp = line[i].split('\t')
        name_student = tmp[0]
        _id = tmp[1]
        course_list = tmp[2].split(";")
        student_test = Student(name_student, _id)
        course_test = []
        for j in range(len(course_list)):
            course_test += course_list[j].split('#')
        index_to_remove = []
        for check1 in range(0, len(course_test), 2):
            for check2 in range((check1 + 2), len(course_test), 2):
                if (course_test[check1] == course_test[check2]):
                    index_to_remove.append(check1)
                    index_to_remove.append(check1 + 1)
        index_to_remove_final = set(index_to_remove)
        index_to_remove_final = list(index_to_remove_final)
        #print(index_to_remove_final)
        course_test_final = []
        check3 = 0
        for k in range(0, len(index_to_remove_final)):
            while index_to_remove_final[k] != check3:
                course_test_final.append(course_test[check3])
                check3 = check3 + 1
            check3 = check3 + 1
        index_last = index_to_remove_final[-1] + 1
        for item in range(index_last, len(course_test)):
            course_test_final.append(course_test[item])
        length = int(len(course_test_final) / 2)
        index = 0
        for k in range(length):
            course1 = Course(course_test_final[index])
            course1.setGrade(int(course_test_final[index + 1]))
            index = index + 2
            student_test.addCourse(course1)
        students_list.append(student_test)


    choice = True
    while choice:
        print("""
1.Calculating the average of a particular student.
2.Calculating the average in a particular course.
3.Average of all students.
4.Exit the program.""")

        choice = input("Please enter one of the following options:")
        if choice == "1":
            name_of_student = input("Please enter the name of the student: ")

            def is_student_exist(student):
                """
                Returns true if student names are the same
                :param student: Object of student type
                :return: True or False
                """
                return name_of_student == student.name_student

            def grade_in_course(course):
                """
                :param course: Object of course type
                :return: grade of course
                """
                return int(course.grade_course)

            student_obj = list(filter(is_student_exist, students_list))
            if student_obj:
                grades = list(map(grade_in_course, student_obj[0].course_list))
                print("ID: ", student_obj[0]._id, "  Average:  ", sum(grades) / len(grades))
            else:
                print("The student " + name_of_student + " does not exist")
        elif choice == "2":
            course_not_exist = 0
            course_name = input("Please enter the name of the course: ")

            def all_courses(student):
                """
                Returns the courses list
                :param student: Object of student type
                :return: courses list
                """
                return student.course_list

            def is_studying(course):
                """
                Returns true if course names are the same
                :param course: Object of student type
                :return: True or False
                """
                return course_name == course.name_course

            def find_course(courses_of_student):
                """
                Returns a list of existing courses
                :param courses_of_student:  list of courses
                :return: list of existing courses
                """
                return list(filter(is_studying, courses_of_student))

            def find_grade(student_course):
                """
                return grade of course
                :param student_course: Object of course type
                :return: grade of course
                """
                return student_course.grade_course

            def return_grade(course_and_grade):
                """
                return list of grade of courses
                :param course_and_grade: Object of student type
                :return: list of grade of courses
                """
                return list(map(find_grade, course_and_grade))

            def remove_empty(courses2):
                """
                return true if the list of courses is empty
                :param courses2: list of courses
                :return: True or False
                """
                return courses2 != []

            def receive_list_and_return_grade(grade_list):
                """
                receive list and return grade
                :param grade_list: list of grades
                :return: grade
                """
                return int(grade_list[0])

            list_of_all_courses = list(map(all_courses, students_list))
            list_of_courses_of_relevant_students = list(map(find_course, list_of_all_courses))
            relevant_grades = list(map(return_grade, list_of_courses_of_relevant_students))
            updated_grades = (list(filter(remove_empty, relevant_grades)))
            only_grades = list(map(receive_list_and_return_grade, updated_grades))
            if len(only_grades) == 0:
                print("Course :", course_name, "not found")
                continue
            print("Course: ", course_name, "grade average in this course: ", sum(only_grades) / len(only_grades))

        elif choice == "3":
            file_name = input('Enter name of file, Please: ')
            string_list = list(map(lambda
                                       student_1: f'{student_1.getID()} {sum(map(lambda student_2: student_2.grade_course, student_1.course_list)) / len(list(map(lambda student_2: student_2.grade_course, student_1.course_list)))}\n',
                                   students_list))
            print(string_list)

            with open(f'{file_name}.txt', 'w') as file:
                full_string_list = reduce(lambda first_s, second_s: first_s + second_s, string_list)
                file.write(full_string_list)
            file.close()

        elif choice == "4":
            print("Goodbye")
            exit()
        elif choice != "": \
            print("Not Valid Choice Try again")



except OSError as err:
    print(f"OS error: {err}.")
    exit(1)
