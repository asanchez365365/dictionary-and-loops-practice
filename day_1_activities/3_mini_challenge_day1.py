# Project Prompt:

# You are hired to build a Student Lookup Tool for a school front office. The secretary must be able to:

    # Enter a student’s full name

    # Instantly see:

            # CPS ID

            # Homeroom

            # Grade Level

            # Primary Email

            # Students must:

            # Describe the search process

## be able to add new data
# Your program must allow the secretary to ADD a brand new student
# into the system while the program is running.

# Your job is to let the secretary type in a new student just like filling out a registration form.
# Once the form is complete, your program must turn that information into a dictionary and add it to the main list of students.
# If the student already exists (same CPS ID), your program must block the entry to prevent duplicates.

# The program should:
    # 1. Ask the user for the following information:
    #    - CPS ID
    #    - First Name
    #    - Last Name
    #    - Middle Name
    #    - Homeroom
    #    - Grade Level
    #    - Primary Email
    #    - Secondary Email

students = []   # This is the main list of students
#open brackets so I can use later

cps_id = input("CPS ID: ").strip()                  # CPS ID
first_name = input("First Name: ").strip().title()   # First Name
last_name = input("Last Name: ").strip().title()     # Last Name
middle_name = input("Middle Name: ").strip().title() # Middle Name
homeroom = input("Homeroom: ").strip()               # Homeroom
grade = input("Grade Level: ").strip()               # Grade Level
primary_email = input("Primary Email: ").strip()     # Primary Email
secondary_email = input("Secondary Email: ").strip() # 5Secondary Email



# 2. Combine the First and Last name into this format:
    #    "Last, First"  

full_name = f"{last_name}, {first_name}"

# 3. Store all of the new information into ONE dictionary
    #    that matches the structure of the existing student data.
new_student = {
        "cps_id": cps_id,
        "name": full_name,
        "middle_name": middle_name,
        "homeroom": homeroom,
        "grade": grade,
        "primary_email": primary_email,
        "secondary_email": secondary_email
    }

# 4. Add (append) that new dictionary into the main students list.
duplicate = False
if not duplicate:
    students.append(new_student)

# 5. After adding the student, the program must:
    #    - Print a confirmation message
    #    - Print the total number of students in the system
    #    - Print the newly added student record
print("\n Student successfully added!")                # 5.a Confirmation message
print("Total number of students:", len(students))        # 5.b Total number of students
print("New Student Record:")                              # 5.c Newly added student record
print(new_student)
# 6. The program must NOT delete or overwrite any existing students.
# 7. If the CPS ID already exists in the system:
        #    - Do NOT add the student
        #    - Display an error message saying the CPS ID is already taken

duplicate = any(student["cps_id"] == cps_id for student in students)
















students = []   # This is the main list of students
#open brackets so I can use later

cps_id = input("CPS ID: ").strip()                  # CPS ID
first_name = input("First Name: ").strip().title()   # First Name
last_name = input("Last Name: ").strip().title()     # Last Name
middle_name = input("Middle Name: ").strip().title() # Middle Name
homeroom = input("Homeroom: ").strip()               # Homeroom
grade = input("Grade Level: ").strip()               # Grade Level
primary_email = input("Primary Email: ").strip()     # Primary Email
secondary_email = input("Secondary Email: ").strip() # 5Secondary Email



# 2. Combine the First and Last name into this format:
    #    "Last, First"  

full_name = f"{last_name}, {first_name}"

# 3. Store all of the new information into ONE dictionary
    #    that matches the structure of the existing student data.
new_student = {
        "cps_id": cps_id,
        "name": full_name,
        "middle_name": middle_name,
        "homeroom": homeroom,
        "grade": grade,
        "primary_email": primary_email,
        "secondary_email": secondary_email
    }

# 4. Add (append) that new dictionary into the main students list.
duplicate = False
if not duplicate:
    students.append(new_student)

# 5. After adding the student, the program must:
    #    - Print a confirmation message
    #    - Print the total number of students in the system
    #    - Print the newly added student record
print("\n Student successfully added!")                # 5.a Confirmation message
print("Total number of students:", len(students))        # 5.b Total number of students
print("New Student Record:")                              # 5.c Newly added student record
print(new_student)
# 6. The program must NOT delete or overwrite any existing students.
# 7. If the CPS ID already exists in the system:
        #    - Do NOT add the student
        #    - Display an error message saying the CPS ID is already taken

duplicate = any(student["cps_id"] == cps_id for student in students)

