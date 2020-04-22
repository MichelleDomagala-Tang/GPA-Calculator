#File: gpa.py
#Author: Michelle Domagala-Tang
#Last Edited: 04-22-2020
#Brief: Python program built to calculate cumulative GPA

grade_dict = {
    '1DO4 COMP' : ['4','12'],
    '1ZB3 CALC II' : ['3','12'],
    '1ZC3 LIN ALG' : ['3','11'],
    '1MO3 MATLS' : ['3','12'],
    '1EO3 PHILOS' : ['3','11'],
    '1EO3 ELEC PHYS' : ['3','9'],
    '1EO3 CHEM' : ['3','12'],
    '1BO3 MICRO' : ['3','12'],
    '1CO3 DESIGN' : ['3','12'],
    '1PO3 ENG PROF' : ['3','12'],
    '1ZA3 CALC I' : ['3','11'],
    '1DO3 MECH' : ['3','11'],
    '2AA2 ENG MNG' : ['2','12'],
    '2Z03 CALC III' : ['3','10'],
    '2DA4 SYSTEMS' : ['4','12'],
    '2SO3 PROGRAM' : ['3','10'],
    '2XA3 SOFTDEV' : ['3','12'],
    '2DM3 DISCRETE' : ['3','11'],
    '2FA3 DISCRETE' : ['3', '12'],
    '2C03 ALGOR' : ['3', '11'],
    '2XB3 PRACT' : ['3', '11'],
    '2MA3 MARKET' : ['0', '10'],
    '2AA4 DEVEL' : ['0', '11']
}

def main():
    user_input = input("Enter in format 'course_code, course_weighting, grade': \nType exit to escape, calc to calculate gpa, or list for current grades: ")
    if (user_input.casefold() == "exit"):
        exit()
    elif (user_input.casefold() == "calculate" or user_input.casefold() == "calc"):
        gpa = calculate_gpa()
        print("Current GPA on 12-pnt Scale: %.2f \nCurrent GPA on 4-pnt Scale: %.2f" % (gpa[0], gpa[1]))
        main()
    elif (user_input.casefold() == "list"):
        print_grades()
    else:
        add_to_dict(user_input)

#Adds new grade to grade_dict
def add_to_dict(user_input):
    new_grade = user_input.split(',',3)
    
    if (len(new_grade) != 3):
        print("Incorrect format.")
        main()
        
    grade = [new_grade[1], new_grade[2]]
    grade_dict[new_grade[0]] = grade
    main()
    
#Calculates GPA on 12-point and 4-point scale
def calculate_gpa():
    grade_points = 0
    grade_points_4 = 0
    credits = 0
    
    for item in grade_dict:
        grade = int(grade_dict[item][1])
        credits += int(grade_dict[item][0])
        grade_points += grade*int(grade_dict[item][0])
        grade_points_4 += convert_grade_scale(grade)*int(grade_dict[item][0])
        
    twel_scale = grade_points/credits
    four_scale = grade_points_4/credits
    
    return (twel_scale, four_scale)
    
#Prints course code, weighting, and grades in tabular format
def print_grades():
    print('\n{:<15s}{:>10s}{:>10s}'.format("COURSE", "WEIGHT", "GRADE")) 
    for item in grade_dict:
        grade = grade_dict[item]
        print('{:<15s}{:>10s}{:>10s}'.format(item, grade[0], grade[1]))
    main()
    
#Converts grade from 12-point scale to 4-point scale
def convert_grade_scale(grade):
    switch = {
        12 : 4,
        11 : 3.9,
        10 : 3.7,
        9 : 3.3,
        8 : 3,
        7 : 2.7,
        6 : 2.3,
        5 : 2,
        4 : 1.7,
        3 : 1.3,
        2 : 1,
        1 : 0.7,
        0 : 0
    }
    return (switch[grade])
        
    
main()