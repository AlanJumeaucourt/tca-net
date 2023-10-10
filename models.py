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
    def __init__(self, id, start_time, end_time, course_info, professors=None, room=None):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.course_info = course_info
        self.professors = professors
        self.room = room

        # if professors:
        #     for prof in professors:
        #         prof.courses.append(self)
        # if room:
        #     room.courses.append(self)

    def __str__(self):
        return f"{self.professors} - {self.start_time} à {self.end_time} - Salle {self.room}"

class Group:
    def __init__(self, id):
        self.id = id
