import logging
from add_student import session
from student_data_modul import Course, Student

logging.basicConfig(level=logging.INFO)

def get_students_by_course(course_name):
    course = session.query(Course).filter_by(name=course_name).first()

    if not course:
        logging.error(f"Course '{course_name}' not found.")
        return

    students = course.students
    if not students:
        logging.info(f"No students are registered for the course '{course_name}'.")
        return

    logging.info(f"Students enrolled in the course '{course_name}':")
    for student in students:
        logging.info(f"{student.first_name} {student.last_name}")


def get_courses_by_student(first_name, last_name):
    student = session.query(Student).filter_by(first_name=first_name, last_name=last_name).first()

    if not student:
        logging.error(f"Student {first_name} {last_name} not found.")
        return

    courses = student.courses
    if not courses:
        logging.info(f"Student {first_name} {last_name} is not enrolled in any courses.")
        return

    logging.info(f"Courses that {first_name} {last_name} is enrolled in:")
    for course in courses:
        logging.info(course.name)


def update_student(student_id, new_first_name=None, new_last_name=None):
    student = session.query(Student).filter_by(id=student_id).first()

    if not student:
        logging.error(f"Student with ID {student_id} not found in the database.")
        return

    if not new_first_name and not new_last_name:
        logging.info("No new data provided for update. Exiting.")
        return

    if new_first_name:
        student.first_name = new_first_name
    if new_last_name:
        student.last_name = new_last_name

    try:
        session.commit()
        logging.info(f"Student with ID {student_id} successfully updated in the database.")
    except Exception as e:
        session.rollback()
        logging.error(f"An error occurred while updating student with ID {student_id}: {e}")


def delete_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()

    if not student:
        logging.error(f"Student with ID {student_id} not found in the database.")
        return

    try:
        session.delete(student)
        session.commit()
        logging.info(f"Student with ID {student_id} successfully deleted from the database.")
    except Exception as e:
        session.rollback()
        logging.error(f"An error occurred while deleting student with ID {student_id}: {e}")
