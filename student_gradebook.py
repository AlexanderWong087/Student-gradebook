import time

gradebook={}
#student format: "[Name]": {Subject:score}
#student's name: name
#student's score dict: gradebook[name]
#student's score in subject: gradebook[name][subject]

def add_student(gradebook,name):
    gradebook[name]={}
    
def add_marks(gradebook,name,subject,mark):
    gradebook[name][subject]=mark

def view_student(gradebook,name):
    print(f'Student name: {name}')
    for i in gradebook[name]:
        print(f'{i}: {gradebook[name][i]}')

def average_marks(gradebook,name):
    ctr=0
    total=0
    for i in gradebook[name]:
        ctr+=1
        total+=int(gradebook[name][i])
    return round(total/ctr)

def top_student(gradebook):
    highest=0
    for i in gradebook:
        if average_marks(gradebook,i)>highest:
            highest=average_marks(gradebook,i)
    return highest

def list_all_students(gradebook):
    for i in gradebook:
        view_student(gradebook,i)

def request_input(gradebook):
    action=input('Choose one of the following actions: Add Students, Add Marks, View Student, View Average, Top Student, See Every Students, or Exit: ')
    if action.lower()=="add students":
        add_student(gradebook,input("Student name: "))
    elif action.lower()=="add marks":
        add_marks(gradebook,input("Student name: "),input("Subject: "),input("New or updated score: "))
    elif action.lower()=="view student":
        view_student(gradebook,input("Student name: "))
    elif action.lower()=="view average":
        print(average_marks(gradebook,input("Student name: ")))
    elif action.lower()=="top student":
        print("The top student has scored an average of: ",int(top_student(gradebook)))
    elif action.lower()=="see every students":
        list_all_students(gradebook)
    else:
        return "Terminate loop"

gradebook = { 
    "Alice": {"Maths": 85, "English": 90, "Science": 88}, 
    "Bob": {"Maths": 78, "English": 72, "Science": 80}, 
    "Charlie": {"Maths": 92, "English": 88, "Science": 95} 
} 
 

while True:
    if request_input(gradebook)=="Terminate loop":
        break
    time.sleep(1)
