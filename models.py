from typing import List
from datetime import datetime

class Professor:
    def __init__(self, trigramm, first_name=None, last_name=None):
        self.trigramm = trigramm
        self.first_name = first_name
        self.last_name = last_name
        self.courses = []

    def __str__(self):
        return f"{self.trigramm} : {self.first_name} {self.last_name}"


class Room:
    def __init__(self, room_name):
        self.room_name = room_name
        self.courses = []

    def __str__(self):
        return self.room_name


class Course:
    def __init__(self, id: int, matiere: str, group: str, start_time: datetime, end_time: datetime, course_info: str = "", professors: List[Professor] = [], rooms: List[Room] = []):
        self.id = id
        self.matiere = matiere
        self.group = group
        self.start_time = start_time
        self.end_time = end_time
        self.course_info = course_info
        self.professors = professors
        self.rooms = rooms

        if professors:
            for prof in professors:
                prof.courses.append(self)
        # if room:
        #     room.courses.append(self)

    def __str__(self):
        # room_name = self.room.room_name if self.room else "N/A"
        room_name_str = ", ".join(str(room) for room in self.rooms)

        professors_str = ", ".join(str(prof) for prof in self.professors)
        return f"Prof {professors_str} - {self.group} - {self.matiere} - {self.start_time} à {self.end_time} - Salle {room_name_str}"


class Group:
    def __init__(self, id):
        self.id = id
