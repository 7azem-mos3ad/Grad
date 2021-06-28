from os import sep
from posixpath import split
import speech_recognition as sr

import db as database 
def main():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Please say something")

        audio = r.listen(source)

        print("Recognizing Now .... ")

        # recognize speech using google

        try:
            db = database.cursor 
            query =("INSERT INTO users (name, user_name) VALUES (%s, %s)")
            values = (r.recognize_google(audio),r.recognize_google(audio))

            db.execute(query,values)
            
            database.db.commit()

            db.close()
            


            # query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
            # values = (r.recognize_google(audio),'aaa' )
            # db.execute(query, values)

            # database.cursor.commit()

            # print(db.rowcount, "record inserted")
            print(r.recognize_google(audio))
            # print(r.recognize_google(audio).split(sep=" "))
            # # print("Audio Recorded Successfully \n ")
        
            #     # print(split())
        except Exception as e:
            print("Error :  " + str(e))

if __name__ == "__main__":
    main()
