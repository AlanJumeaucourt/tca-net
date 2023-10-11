import pickle
from models import Professor, Room, Course
from datetime import datetime, timedelta
# Open 3 dict with the objects from crawler.py
with open('courses.pkl', 'rb') as file:
    courses = pickle.load(file)

with open('rooms.pkl', 'rb') as file:
    rooms = pickle.load(file)

with open('professors.pkl', 'rb') as file:
    professors = pickle.load(file)

for i, course in courses.items():
    print(course)

message1 = ""
# Afficher les cours triés
for i, course in courses.items():
    date_debut_moins_15 = course.start_time - timedelta(minutes=float(99))

    if (course.group == "4TC" or course.group == "4TC-G4"):

        if date_debut_moins_15 <= datetime.now() <= course.start_time:
            print(course)
            print("in between")
            print(f"date_debut_cour : {course.start_time}")
            print(f"date_debut_moins_15 : {date_debut_moins_15}")
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
    print("message is empty, no courses in less than 15min")
    print("Exiting ...")
    exit()

print(message1)
