import pickle
from models import Professor, Room, Course
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Open 3 dict with the objects from crawler.py
with open('courses.pkl', 'rb') as file:
    courses = pickle.load(file)
    
print("\courses :")
for i, j in courses.items():
    print(f"{j}")
print("\n")

with open('rooms.pkl', 'rb') as file:
    rooms = pickle.load(file)

print("\nrooms :")
for i, j in rooms.items():
    print(f"{j}")
print("\n")


with open('professors.pkl', 'rb') as file:
    professors = pickle.load(file)

print("\n professors :")
for i, j in courses.items():
    print(f"{j}")
print("\n")


for i, course in courses.items():
    print(course)

load_dotenv()  # This reads the environment variables inside .env
delta = os.getenv('delta', 15)

message1 = ""
# Afficher les cours triés
for i, course in courses.items():
    start_date_minus_delta = course.start_time - timedelta(minutes=float(delta))

    if (course.group == "4TC" or course.group == "4TC-G4"):

        if start_date_minus_delta <= datetime.now() <= course.start_time:
            print(course)
            print("in between")
            print(f"date_debut_cour : {course.start_time}")
            print(f"date_debut_moins_15 : {start_date_minus_delta}")
            message1 = f"""@everyone {("**" + course.matiere + "**")}

**Infos :**
- **Matière :** {course.matiere}
- **Date et Heure :** {course.start_time}
- **Groupe :** {course.group}
- **Type :** {course.group}
- **Enseignant :** {", ".join(str(room) for room in course.professors)}
- **Salle :** {", ".join(str(room) for room in course.rooms)}
- **Autres :** {course.course_info}
"""


        else:
            pass
if message1 == "":
    print(f"message is empty, no courses in less than {delta} minutes")
    print("Exiting ...")
    exit()

print(message1)
