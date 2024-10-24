# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 05:03:47 2021

@author: User
"""
student_ids = [ 'ID9012', 'ID4212', 'ID7809' ]
student_subjects = [ 'Programming Fundamentals', 'Calculus', 'Algebra' ]
student_grades = [ 78, 90, 75 ]
nest_dic= {ids:{subj:grade} for (ids,subj,grade) in  zip(student_ids,student_subjects,student_grades)}
print(nest_dic)