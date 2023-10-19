from typing import List
from datetime import datetime


class Professor:
    
    def __init__(self, trigramm: str, first_name: str = "", last_name: str = ""):
        """_summary_

        Args:
            trigramm (str): Prof's trigramm (ex: "JOE")
            first_name (str, optional): Prof's first name (ex: "John"). Defaults to "".
            last_name (str, optional): Prof's last name (ex: "Doe"). Defaults to "".
        """
        self.trigramm = trigramm
        self.first_name = first_name
        self.last_name = last_name
        self.courses = []

    def __str__(self):
        if self.first_name == "" and self.last_name == "":
            return f"{self.trigramm}"
        else:
           return f"{self.trigramm} : {self.first_name} {self.last_name}"


class Room:
    def __init__(self, room_name: str):
        """Room object to store room's name and courses

        Args:
            room_name (str): room's name (ex: "TD F")
        """
        self.room_name = room_name
        self.courses = []

    def __str__(self):
        return self.room_name


class Course:
    def __init__(self, id: int, matiere: str, group: str, start_time: datetime, end_time: datetime, course_info: str = "", professors: List[Professor] = [], rooms: List[Room] = []):
        """Course object to store course's informations

        Args:
            id (int): unique identifier
            matiere (str): base name of the course (ex: "4TC-ANG1-2023")
            group (str): tc's group (ex: "4TC or 4-TC-G4")
            start_time (datetime): start time of the course
            end_time (datetime): end time of the course
            course_info (str, optional): any others information about the course . Defaults to "".
            professors (List[Professor], optional): list of professor'object . Defaults to [].
            rooms (List[Room], optional): list of rooms. Defaults to [].
        """
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
