# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
import json
from datetime import datetime, timedelta
from discord.ext import commands
import random
import os
from dotenv import load_dotenv
import time

load_dotenv()  # This reads the environment variables inside .env
DiscordToken = os.getenv('DiscordToken', "NOT FOUND")
channelId = os.getenv('channelId', "NOT FOUND")

# Check mandatory variable
needExit = False
if DiscordToken == "NOT FOUND":
    print("[ERROR] DiscordToken not found in .env, you must set it in .env file to run this programme")
    needExit = True

if channelId == "NOT FOUND":
    print("[ERROR] channelId not found in .env, you must set it in .env file to run this programme")
    needExit = True

if needExit:
    print("Exiting ...")
    exit()


delta = os.getenv('delta', 15)

cours_tries = []
message1 = ""
now = datetime.now()

print(f"now = {now}")


def blague_cours(cours):
    blagues = [
        f"Salut les bolosses, il y a cours de {cours} dans moins de 15 minutes. Préparez-vous à une explosion de connaissances !",
        f"Hey tout le monde, le cours de {cours} commence bientôt. Préparez-vous à décrocher la lune en {cours} !",
        f"Bonjour les amis, ne ratez pas le cours de {cours} qui démarre dans moins de 15 minutes. C'est le moment de devenir des maîtres en {cours} !",
        f"Aujourd'hui, nous plongeons dans le monde mystérieux de {cours}. Attachez vos ceintures !",
        f"C'est l'heure du cours de {cours}. Sortez vos baguettes magiques !",
        f"Attention, attention ! Le cours de {cours} commence dans quelques instants. Préparez-vous à une aventure inoubliable !",
        f"Le cours de {cours} est comme un voyage dans le temps. Préparez-vous à explorer différentes époques !",
        f"Préparez-vous à déchiffrer les secrets du cosmos dans le cours de {cours} !",
        f"Le cours de {cours} est un rendez-vous avec l'histoire. Êtes-vous prêts à être les héros ?",
        f"Dans le cours de {cours}, chaque formule est un poème. Préparez-vous à écrire des vers en {cours} !",
        f"Le cours de {cours} est comme un livre d'énigmes. Préparez-vous à résoudre les mystères !",
        f"Pour le cours de {cours}, laissez votre curiosité vous guider vers des mondes inexplorés !",
        f"Le cours de {cours} est une aventure passionnante. Préparez-vous à des découvertes extraordinaires !",
        f"Les étoiles brillent, le cours de {cours} est là pour illuminer votre journée !",
        f"Ne laissez pas le cours de {cours} vous intimider. Vous êtes prêts à conquérir le monde !",
        f"Le cours de {cours} est une fenêtre ouverte sur l'univers. Regardez à travers !",
        f"Dans le cours de {cours}, chaque concept est une œuvre d'art. Préparez-vous à devenir des artistes en {cours} !",
        f"Le cours de {cours} est un voyage épique dans le temps. Préparez-vous à affronter des dragons (devoirs) !",
        f"Pour le cours de {cours}, laissez vos rêves vous guider. Le monde de {cours} vous attend !",
        f"Le cours de {cours} est comme une boîte de surprises. Ouvrez-la avec curiosité !",
        f"Préparez-vous à une averse de connaissances dans le cours de {cours} !",
        f"Dans le cours de {cours}, chaque minute est une opportunité d'apprendre quelque chose de nouveau !",
        f"Le cours de {cours} est un voyage vers l'inconnu. Êtes-vous prêts à explorer ?",
        f"Pour le cours de {cours}, laissez votre esprit vagabonder dans les contrées lointaines de la pensée !",
        f"Le cours de {cours} est une aventure passionnante. Préparez-vous à repousser les limites !",
        f"Le cours de {cours} est un trésor d'opportunités. Découvrez les richesses de la connaissance !",
        f"Rien ne peut vous arrêter dans le cours de {cours}. Soyez intrépides !",
        f"Dans le cours de {cours}, chaque page est une nouvelle aventure. Préparez-vous à tourner la page !",
        f"Le cours de {cours} est l'occasion parfaite de briller comme une étoile. Faites briller votre lumière !",
        f"Pour le cours de {cours}, laissez votre curiosité vous guider vers l'infini et au-delà !",
        f"Le cours de {cours} est comme une boîte de trésors. Préparez-vous à explorer !",
        f"Préparez-vous à plonger dans le monde étonnant du cours de {cours} !",
        f"Le cours de {cours} est un trésor d'opportunités. Découvrez les richesses de la connaissance !",
        f"Rien n'est impossible dans le cours de {cours}. Soyez prêts à tout conquérir !",
        f"Dans le cours de {cours}, chaque question est un défi à relever. Préparez-vous à être des héros !",
        f"Le cours de {cours} est l'endroit où les rêves prennent vie. Rêvez en grand !",
        f"Pour le cours de {cours}, laissez votre imagination s'épanouir. Les possibilités sont infinies !",
        f"Le cours de {cours} est une aventure qui vous attend. Préparez-vous à partir à l'aventure !",
        f"Prêt ou pas, le cours de {cours} est là. Soyez prêts à briller comme des étoiles !",
        f"Dans le cours de {cours}, chaque jour est une opportunité de grandir et de devenir meilleur. Saisissez-la !",
        f"Le cours de {cours} est comme un jardin de connaissances. Cultivez votre esprit !",
        f"Le cours de {cours} est l'occasion parfaite de montrer vos talents cachés. Faites étinceler votre génie !",
        f"Pour le cours de {cours}, laissez votre créativité s'exprimer. Créez l'inimaginable !",
        f"Le cours de {cours} est une aventure qui vous attend. Préparez-vous à repousser les limites !",
        f"Le cours de {cours} est un voyage vers l'excellence. Soyez les meilleurs !",
        f"Dans le cours de {cours}, chaque leçon est une perle de sagesse. Collectionnez-les toutes !",
        f"Le cours de {cours} est l'endroit où les rêves deviennent réalité. Rêvez en grand !",
        f"Pour le cours de {cours}, laissez votre imagination courir sauvage. Les possibilités sont infinies !",
        f"Le cours de {cours} est une aventure qui vous attend. Préparez-vous à être émerveillés !",
        f"Le cours de {cours} est un voyage vers l'infini et au-delà. Explorez de nouveaux mondes !",
        f"Dans le cours de {cours}, chaque instant est une opportunité d'apprendre et de grandir. Saisissez-le !",
        f"Le cours de {cours} est le moment idéal pour libérer votre créativité. Laissez vos idées s'envoler !",
        f"Pour le cours de {cours}, laissez votre esprit s'ouvrir aux possibilités infinies. Explorez de nouvelles perspectives !",
        f"Le cours de {cours} est une aventure qui vous attend. Préparez-vous à être étonnés !",
        f"Le cours de {cours} est un voyage vers l'infini. Explorez l'univers de la connaissance !",
        f"Dans le cours de {cours}, chaque concept est une énigme à résoudre. Préparez-vous à être des détectives du savoir !",
        f"Le cours de {cours} est l'endroit où les rêves prennent vie. Rêvez en grand !",
        f"Pour le cours de {cours}, laissez votre imagination courir sauvage. Explorez des mondes imaginaires !",
        f"Le cours de {cours} est une aventure qui vous attend. Préparez-vous à être éblouis !",
        f"Le cours de {cours} est un voyage vers l'inconnu. Explorez des terres inexplorées !",
        f"Prêt ou pas, le cours de {cours} arrive à grands pas. Préparez-vous à être épatés !",
        f"Dans le cours de {cours}, chaque jour est une opportunité d'apprendre et de grandir. Saisissez-la !",
        f"Le cours de {cours} est comme un trésor caché. Découvrez ses mystères !",
        f"Le cours de {cours} est l'occasion parfaite de laisser votre créativité s'exprimer. Soyez des artistes du savoir !",
        f"Pour le cours de {cours}, laissez votre esprit s'éveiller à de nouvelles idées. Explorez de nouvelles horizons !",
        f"Le cours de {cours} est une aventure qui vous attend. Préparez-vous à être enchantés !",
        f"Dans le cours de {cours}, chaque instant est une opportunité d'apprendre et de grandir. Saisissez-le !",
        f"Le cours de {cours} est le moment idéal pour libérer votre créativité. Laissez vos idées s'épanouir !",
        f"Pour le cours de {cours}, laissez votre esprit s'ouvrir aux possibilités infinies. Explorez de nouvelles perspectives !",
        f"Le cours de {cours} est une aventure qui vous attend. Préparez-vous à être étonnés !",
        f"Le cours de {cours} est un voyage vers l'infini. Explorez l'univers de la connaissance !",
        f"Dans le cours de {cours}, chaque concept est une énigme à résoudre. Préparez-vous à être des détectives du savoir !",
        f"Le cours de {cours} est l'endroit où les rêves prennent vie. Rêvez en grand !",
        f"Pour le cours de {cours}, laissez votre imagination courir sauvage. Explorez des mondes imaginaires !",
        f"Le cours de {cours} est une aventure qui vous attend. Préparez-vous à être éblouis !",
        f"Le cours de {cours} est un voyage vers l'inconnu. Explorez des terres inexplorées !",
        f"Prêt ou pas, le cours de {cours} arrive à grands pas. Préparez-vous à être épatés !",
        f"Dans le cours de {cours}, chaque jour est une opportunité d'apprendre et de grandir. Saisissez-la !",
        f"Le cours de {cours} est comme un trésor caché. Découvrez ses mystères !",
        f"Le cours de {cours} est l'occasion parfaite de laisser votre créativité s'exprimer. Soyez des artistes du savoir !",
        f"Pour le cours de {cours}, laissez votre esprit s'éveiller à de nouvelles idées. Explorez de nouvelles horizons !",
        f"Le cours de {cours} est une aventure qui vous attend. Préparez-vous à être enchantés !"
    ]

    blague_aleatoire = random.choice(blagues)
    return blague_aleatoire


with open('data.json', 'r') as fp:
    cours_tries = json.load(fp)

    # Afficher les cours triés
    for c in cours_tries:
        date_debut_cour = datetime.strptime(
            c['Date']+" "+c['Heure'].split("-")[0], "%d/%m/%Y %Hh%M")
        date_debut_moins_15 = date_debut_cour - timedelta(minutes=float(delta))

        if (c["Groupe"] == "4TC" or c["Groupe"] == "4TC-G4"):

            if date_debut_moins_15 <= now <= date_debut_cour:
                print(c)
                print("in between")
                print(f"date_debut_cour : {date_debut_cour}")
                print(f"date_debut_moins_15 : {date_debut_moins_15}")
                message1 = f"""@everyone {blague_cours("**" + c['Matiere'] + "**")}

**Infos :**
- **Matière :** {c['Matiere']}
- **Date et Heure :** {c['Date']} de {c['Heure']}
- **Groupe :** {c['Groupe']}
- **Type :** {c['Type']}
- **Enseignant :** {c['Enseignant']}
- **Salle :** {c['Salle']}
- **Autres :** {c['Autres']}
"""

            else:
                pass
    if message1 == "":
        print("message is empty, no courses in less than 15min")
        print("Exiting ...")
        exit()

intents = discord.Intents.default()
intents.typing = False  # Désactive la surveillance de la frappe
intents.presences = False  # Désactive la surveillance des présences (status)

# Créez un objet bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Fonction pour envoyer un message


async def envoyer_message():
    channel = bot.get_channel(int(channelId))

    if channel:
        await channel.send(message1)
    else:
        print("Le canal n'a pas été trouvé.")

# Événement de démarrage du bot


@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')

    # Appelez la fonction envoyer_message lorsque le bot est prêt
    await envoyer_message()
    time.sleep(3)
    exit()

# Lancez le bot
bot.run(token=DiscordToken)
