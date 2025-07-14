student = {
    'name': 'John',
    'details': {
        'subjects': {
            'math': {
                'marks': 90,
                'grade': 'A'
            }
        }
    }
}

# Access the most inner value: marks in math
math_marks = student['details']['subjects']['math']['marks']
print("Math Marks:", math_marks)