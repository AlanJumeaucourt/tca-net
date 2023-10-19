import requests
from datetime import datetime
from bs4 import BeautifulSoup
import json
import re
import os
from dotenv import load_dotenv
from models import Professor, Room, Course
import pickle


def read_env():
    load_dotenv()  # This reads the environment variables inside .env
    authToken = os.getenv('authToken', "NOT FOUND")

    # Check mandatory variable
    needExit = False
    if authToken == "NOT FOUND":
        print("[ERROR] authToken not found in .env, you must set it in .env file to run this programme")
        needExit = True

    if needExit:
        print("Exiting ...")
        exit()

    return authToken

allLocations = []
linkLocationMaps = {"1-Amphi huma ouest": "",
                    "1-Amphi Chappe": "",
                    "2-TD C": "",
                    "2-TD F(LS)": "",
                    "5-Projet TD B": "",
                    "3-TP Info C": "",
                    "3-TP Info B": "",
                    "1-Amphi mediatheque-Emilie du Chatelet": "",
                    "2-TD E": "",
                    "2-TD D": "",
                    "2-TD D": "",
                    "1-Amphi Chappe + Hall Chappe": "",
                    "3-TP Info E": "",
                    "3-TP Info D": "",
                    "2-TD (C-D-E)": "",
                    " NA": "",
                    "amphi": "",
                    "TP-Telecom": "",
                    "TD": ""}

matieres = ["3TC-Accueil-2023",
            "3TC-ALG-2023",
            "3TC-ANG1-2023",
            "3TC-ANG2-2023",
            "3TC-ARC-2023",
            "3TC-ASDS-2023",
            "3TC-ASTUS-2023",
            "3TC-Autonomie-2023",
            "3TC-Divers-2023",
            "3TC-DLG1-2023",
            "3TC-DLG2-2023",
            "3TC-DRE-2023",
            "3TC-ELP-2023",
            "3TC-ForumRA-2023",
            "3TC-GNS3-2023",
            "3TC-HOP-2023",
            "3TC-International-2023",
            "3TC-IP-2023",
            "3TC-MAC-2023",
            "3TC-MAS-2023",
            "3TC-MET-2023",
            "3TC-MUSIC-2023",
            "3TC-NAS-2023",
            "3TC-NRP-2023",
            "3TC-PALE-2023",
            "3TC-PARRAIN-2023",
            "3TC-PBS-2023",
            "3TC-PBS2-2023",
            "3TC-PBS3-2023",
            "3TC-PIT-2023",
            "3TC-PPC-2023",
            "3TC-PPP-2023",
            "3TC-Pres4TC-2023",
            "3TC-PRESMETIER-2023",
            "3TC-PTIR-2023",
            "3TC-Rab-2023",
            "3TC-RencontrePart-2023",
            "3TC-SDR-2023",
            "3TC-SIS-2023",
            "3TC-SNC2-2023",
            "3TC-SNC22-2023",
            "3TC-SON-2023",
            "3TC-SPO1-2023",
            "3TC-SPO2-2023",
            "3TC-Stage3TC-2023",
            "3TC-THEATRE-2023",
            "3TC-THEATRE1-2023",
            "3TC-TSA-2023",
            "3TC-WEB-2023",
            "3TC-WEI-2023",
            "3TCA-ANG2-2023",
            "3TCA-AppDebrief1-2023",
            "3TCA-AppDebrief2-2023",
            "3TCA-AppDebrief3-2023",
            "3TCA-AppDivers-2023",
            "3TCA-AppSKI-2023",
            "3TCA-AppSOU1-2023",
            "3TCA-AppSoutenance1-2023",
            "3TCA-AppTutorat1-2023",
            "3TCA-DEBRIEF2-2023",
            "3TCA-SPO-2023",
            "4TC-ACCROBRANCHE-2023",
            "4TC-Accueil-2023",
            "4TC-ANG1-2023",
            "4TC-ANG2-2023",
            "4TC-APPDEBRIEF5-2023",
            "4TC-APPDEBRIEF6-2023",
            "4TC-ARM-2023",
            "4TC-ASTUS-2023",
            "4TC-Autonomie-2023",
            "4TC-BLF-2023",
            "4TC-CME-2023",
            "4TC-CNA-2023",
            "4TC-CSC-2023",
            "4TC-Divers-2023",
            "4TC-DLG1-2023",
            "4TC-DLG2-2023",
            "4TC-ExamComp-2023",
            "4TC-ForumRA-2023",
            "4TC-IAT-2023",
            "4TC-INR-2023",
            "4TC-INS1-2023",
            "4TC-INS2-2023",
            "4TC-International-2023",
            "4TC-JEF-2023",
            "4TC-JOURNÉEANCIENS-2023",
            "4TC-PAO-2023",
            "4TC-PPP2-2023",
            "4TC-PRESENTATION5TC-2023",
            "4TC-PRESMETIER-2023",
            "4TC-PresPPH-2023",
            "4TC-PRF-2023",
            "4TC-PSC-2023",
            "4TC-Rab-2023",
            "4TC-RAN-2023",
            "4TC-RencontresPart-2023",
            "4TC-RetourSTA-2023",
            "4TC-RPE-2023",
            "4TC-SimuEnt-2023",
            "4TC-SIR-2023",
            "4TC-SPO1-2023",
            "4TC-SPO2-2023",
            "4TC-SPOC-2023",
            "4TC-SYD-2023",
            "4TC-TCP-2023",
            "4TC-TIP-2023",
            "4TC-TOS-2023",
            "4TC-VIR-2023",
            "4TC-WEI-2023",
            "4TCA-AppANG3-2023",
            "4TCA-AppANG4-2023",
            "4TCA-AppAutonomie-2023",
            "4TCA-AppDebrief4-2023",
            "4TCA-AppDebrief5-2023",
            "4TCA-AppDebrief6-2023",
            "5TC-10ELK-2023",
            "5TC-10PROJreb-2023",
            "5TC-11BTC-2023",
            "5TC-11PRJSAT-2023",
            "5TC-1ARC-2023",
            "5TC-2AWS-2023",
            "5TC-3SRS-2023",
            "5TC-4DMO-2023",
            "5TC-5CIT-2023",
            "5TC-5IAR-2023",
            "5TC-6SMR-2023",
            "5TC-6SPR-2023",
            "5TC-7SAT-2023",
            "5TC-7SVP-2023",
            "5TC-8AUD-2023",
            "5TC-8CDN-2023",
            "5TC-9CQN-2023",
            "5TC-9SAR-2023",
            "5TC-ACCUEIL-2023",
            "5TC-ASTUS-2023",
            "5TC-HUMA-2023",
            "5TC-HUMA2-2023",
            "5TC-PILS-2023",
            "5TC-PPH-2023",
            "5TC-PPP-2023",
            "5TC-Rab-2023",
            "5TC-RET-STA-2023",
            "5TC-SHE-2023",
            "5TC-SIMU-2023",
            "5TC-SOUT-STA-2023",
            "5TC-SPO-2023",
            "IST-ASM",
            "IST-DBM1",
            "IST-DBM2",
            "IST-JAV",
            "IST-MID",
            "IST-NET1",
            "IST-NET2",
            "IST-OPS",
            "IST-SIP1",
            "IST-SIP2",
            "IST-TLRS",
            "IST-WCB",
            "MSTC-ANPM",
            "MSTC-AOS",
            "MSTC-APKI",
            "MSTC-ART",
            "MSTC-ASRF",
            "MSTC-CISO",
            "MSTC-CLSE",
            "MSTC-CONF",
            "MSTC-CYSI",
            "MSTC-GOSE",
            "MSTC-IAM",
            "MSTC-ICR",
            "MSTC-INTR",
            "MSTC-MCYR",
            "MSTC-MNSR",
            "MSTC-PENT",
            "MSTC-PPC",
            "MSTC-RGPD",
            "MSTC-RISE",
            "MSTC-SAW",
            "MSTC-SDD",
            "MSTC-SECP",
            "MSTC-SINF",
            "MSTC-SOUTENANCE",
            "MSTC-SPT",
            "MSTC-VSRA",
            "RESASALLE"]


def getCourBymatiere(matiere):
    url = 'https://tc-net.insa-lyon.fr/edt/std/AffichageEdtTexteMatiere.jsp'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Authorization': f"Basic {authToken}",
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'JSESSIONID=D49EC627435268DCA32F4A3DBD42EC31; AGIMUS=TRACE-878779-qgBamGsmb1RcveoJz3KUlfeTos59PfwYecn9zYKcHJXm3Vfujb-dsi69',
        'DNT': '1',
        'Origin': 'https://tc-net.insa-lyon.fr',
        'Referer': 'https://tc-net.insa-lyon.fr/edt/std/AffichageEdtTexteMatiere.jsp',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"'
    }

    def data(matiere: str):
        return {
            'choixMatiere': f"{matiere}",
            'SelectionMatiere': 'ok'
        }

    try:
        response = requests.post(url, headers=headers,
                                 data=data(matiere=matiere))
    except:
        print(f"Error in requesting {url} for getting {matiere}")
        print(f"Exiting ...")
        exit()
    soup = BeautifulSoup(response.text, 'html.parser')

    print(response)

    # Trouvez la structure de la matière
    # structure_matiere = soup.find('b').text.strip()

    # Trouvez toutes les lignes de données dans la balise <pre>
    data_rows = soup.find_all('pre')

    if data_rows:
        # Enlever la première et la dernière ligne
        ligne = str(data_rows[0]).strip().split('\n')[1:-1]

        # Parser le texte
        baseCourses = []
        for l in ligne:
            # print(l)
            elements = l.split()
            Enseignant = ""
            try:
                Enseignant = re.findall(r'\[(.*?)\]', l)[0]
                # print(Enseignant)
            except:
                Enseignant = ""

            try:
                autre = re.findall(r'\{(.*?)\}', l)[0]
            except:
                autre = ""

            try:
                salle = str(re.findall(r'\]  (.*?)\ {', l)[0])
            except:
                salle = ""

            if salle == "000000000":
                salle = "Pas de salle (000000000)"
            baseCourses.append({
                "Matiere": matiere,
                # Enlève la virgule à la fin de la semaine
                "Semaine": elements[1][:-1],
                "Date": elements[3],
                "Heure": elements[4],
                "Groupe": elements[5],
                "Type": elements[6],
                "Enseignant": Enseignant,
                "Salle": salle,
                "Autres": autre,
            })
        return baseCourses


def getAllCourses():
    baseCourses = []
    for matiere in matieres:
        if "4TC" in matiere and matiere != "4TC-SIR-2023":
            print(f"Crawling : {matiere}")
            listCour = getCourBymatiere(matiere)
            for course in listCour:
                baseCourses.append(course)

    sorted_courses = sorted(
        baseCourses, key=lambda x: datetime.strptime(x['Date'], "%d/%m/%Y"))

    return sorted_courses


def get_professors():
    enseignants = []
    for course in baseCourses:
        if course['Enseignant'] not in enseignants:
            if "," in course['Enseignant']:
                prof = course['Enseignant'].split(",")
                for p in prof:
                    if p not in enseignants and "Cours" not in p:
                        enseignants.append(p.strip('{}[] '))
            else:
                enseignants.append(
                    str(course['Enseignant']).strip().strip("[]"))

    return {name: Professor(trigramm=name) for name in enseignants}


def get_rooms():
    Salles = []

    for course in baseCourses:
        if course['Salle'] not in Salles and course['Salle']:
            Salles.append(course['Salle'])

    return {room: Room(room_name=room) for room in Salles}


def get_courses():
    courses = {}
    for i, data in enumerate(baseCourses):
        start_time = datetime.strptime(
            data["Date"]+" "+data["Heure"].split("-")[0], "%d/%m/%Y %Hh%M")
        end_time = datetime.strptime(
            data["Date"]+" "+data["Heure"].split("-")[1], "%d/%m/%Y %Hh%M")
        courses[i] = courses.get(i, Course(
            id=i,
            matiere=data["Matiere"],
            group=data["Groupe"],
            start_time=start_time,
            end_time=end_time,
            course_info=data["Autres"],
            professors=[prof for i, prof in professors.items() if i ==
                        data["Enseignant"]],
            rooms=[room for i, room in rooms.items() if room.room_name ==
                   data["Salle"]],
        ))
    return courses


def dump_data():
    with open('courses.pkl', 'wb') as fp:
        pickle.dump(courses, fp)

    with open('rooms.pkl', 'wb') as fp:
        pickle.dump(rooms, fp)

    with open('professors.pkl', 'wb') as fp:
        pickle.dump(professors, fp)


authToken = read_env()

baseCourses = getAllCourses()
# print(baseCourses)

professors = get_professors()
# print(professors)

# print("\nprofessors :")
# for i, prof in professors.items():
#     print(f"{prof}")
# print("\n")

rooms = get_rooms()
# print(rooms)

# print("\nrooms :")
# for i, room in rooms.items():
#     print(f"{room}")
# print("\n")

courses = get_courses()
# print(courses)

# for i, course in courses.items():
#     print(course)


dump_data()
