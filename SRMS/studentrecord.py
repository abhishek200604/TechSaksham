#student record management system

students={}  #initialising the dictionary for store data
student_ids=[] #list to track the students id


while True:
    print("/n1.Add the Student Data")
    print("2.View All the Students")
    print("3.Searching of the Students")
    print("4.Update the Students Data")
    print("5.Delete the Students Data")
    print("6.Exit")
    
    choice=input("Enter Your Choice.")
    
    if  choice =='1':
        student_id = input("Enter Student id: ")
        name = input("Enter Student Name: ")
        age = input("Enter Age of Student: ")
        grade = input("Enter Students Grade: ")
        students[student_id] = {'name': name, 'age':age,'grade':grade}
        student_ids.append(student_id)
        print("Student Added Successfully..!")
        
    elif choice == '2':
        if not students:
            print("No students Found")
        else:
            for student_id in student_ids:
                student = students[student_id] 
                print(f"ID: {student_id}, Name: {student['name']},Age: {student['age']}, Grade: {student['grade']}")
                
    elif choice =='3':
        student_id = input("Enter student ID to search: ")
        if student_id in students:
            student = students[student_id]
            print(f"ID: {student_id}, Name: {student['name']}, Age:{student['age']},Grade; {student['grade']}")
        else:
            print("Student not found")
            
    elif choice == '4':
        student_id= input("Enter student ID to update: ")
        if student_id in students:
            name = input("Enter new name: ")
            age = input("Enter new Age: ")
            grade = input("Enter new grade: ")
            students[student_id]={'name':name, 'age': age,'grade':grade}
            print("Students Information updated Successfully!")
        else:
            print("Student not found")
            
    elif  choice =='5':
        student_id = input("Enter student ID to Delete: ")
        if student_id in students:
            del students[student_id]
            student_ids.remove(student_id)
            print("Student record deleted Successfully!")
        else:
            print("Student not found")
    elif choice =='6':
        print("Exiting...")
        break
    
    else:
        print("Invalid Choice.Please try again")        
    
