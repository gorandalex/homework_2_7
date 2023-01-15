from sqlalchemy.orm import outerjoin
from sqlalchemy.sql import func
from sqlalchemy import desc, and_

from database.db import session
from database.models import Grade, Group, Student, Subject, Teacher


def select_1():
    results = session.query(Student, func.avg(Grade.grade).label('avg')).join(Grade).group_by(Student).order_by(desc('avg')).limit(5).all()
    print('SELECT 1')
    for result in results:
        print(result.Student.firstname, result.Student.lastname, round(result.avg, 2))


def select_2(subject_id):    
    results = session.query(Student, func.avg(Grade.grade).label('avg')).join(Grade).group_by(Student).filter(Grade.subject_id == subject_id)\
            .order_by(desc('avg')).limit(1).all()
    print('SELECT 2')
    for result in results:
        print(result.Student.firstname, result.Student.lastname, round(result.avg, 2))
        

def select_3(subject_id):
    results = session.query(Group, func.avg(Grade.grade).label('avg')).outerjoin(Student, Group.id == Student.group_id)\
            .outerjoin(Grade, Student.id == Grade.student_id).group_by(Group).filter(Grade.subject_id == subject_id).all()
    print('SELECT 3')
    for result in results:
        print(result.Group.name, round(result.avg, 2))
        
        
def select_4():
    results = session.query(func.avg(Grade.grade).label('avg')).all()
    print('SELECT 4')
    for result in results:
        print(round(result.avg, 2))
    

def select_5(teacher_id):
    results = session.query(Subject).join(Teacher).filter(Teacher.id == teacher_id).all()
    print('SELECT 5')
    for result in results:
        print(result.name)
    
    
def select_6(group_id):
    results = session.query(Student).filter(Student.group_id == group_id).all()
    print('SELECT 6')
    for result in results:
        print(result.firstname, result.lastname)
    
def select_7(group_id, subject_id):
    results = session.query(Student, Grade.grade).join(Grade).filter(and_(Student.group_id == group_id, Grade.subject_id == subject_id))\
            .order_by(Student.firstname, Student.lastname).all()
    print('SELECT 7')
    for result in results:
        print(result.Student.firstname, result.Student.lastname, result.grade)


def select_8(teacher_id):
    results = session.query(func.avg(Grade.grade).label('avg')).join(Subject).filter(Subject.teacher_id == teacher_id).all()
    print('SELECT 8')
    for result in results:
        print(round(result.avg, 2))
 

def select_9(student_id):
    results = session.query(Subject).join(Grade).filter(Grade.student_id == student_id).all()
    print('SELECT 9')
    for result in results:
        print(result.name)

def select_10(student_id, teacher_id):
    results = session.query(Subject).join(Grade).filter(and_(Grade.student_id == student_id, Subject.teacher_id == teacher_id)).all()
    print('SELECT 10')
    for result in results:
        print(result.name)

    
if __name__ == '__main__':
    select_1()
    select_2(1)
    select_3(1)
    select_4()
    select_5(5)
    select_6(1)
    select_7(1, 1)
    select_8(1)
    select_9(1)
    select_10(1, 1)