import logging
from sqlalchemy.orm import sessionmaker
from student_data_modul import engine, Course, Student

Session = sessionmaker(bind=engine)
session = Session()


def add_student_to_course(first_name, last_name, course_name):
    course = session.query(Course).filter_by(name=course_name).first()

    if not course:
        logging.error(f"Course '{course_name}' not found.")
        return

    student = session.query(Student).filter_by(first_name=first_name, last_name=last_name).first()

    if not student:
        student = Student(first_name=first_name, last_name=last_name)
        session.add(student)
        logging.info(f"Student {first_name} {last_name} added to the database.")

    if course not in student.courses:
        student.courses.append(course)
        logging.info(f"Course '{course_name}' added to student {first_name} {last_name}.")
    else:
        logging.info(f"Student {first_name} {last_name} is already enrolled in the course '{course_name}'.")

    try:
        session.commit()
        logging.info(f"Student {first_name} {last_name} successfully added to the course '{course_name}'.")
    except Exception as e:
        session.rollback()
        logging.error(f"An error occurred while adding student {first_name} {last_name} to the course '{course_name}': {e}")

