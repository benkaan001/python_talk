'''
Given a list of course list that has courseID followed by course abbreviation
find the course that has been taken the most times
and return the matching description of the course referencing the given
course_dictionary 


'''


def find_major(course_list,course_dictionary):
    
    student_dict = {}
    
    for course in course_list:
        if course in student_dict:
            student_dict[course]+=1
        else:
            student_dict[course]=0
    
    max=0
    keyword =''
    for key,value in student_dict.items():
        if (value>max):
            max=value
            keyword = key
    
    for key,value in course_dictionary.items():
        if (key == keyword):
            major = value
 
                

    return major


course_list=[101,'P',102,'P' ,301, 'E',103,'P',104,'P' ,111, 'M' ,112, 'M', 113, 'M',201,'B', 202, 'B']
course_dictionary={'P':'Physics','M':'Math','B':'Biology', 'E':'Engineering'}
major=find_major(course_list,course_dictionary)
print(major)