import sqlite3

class Requests_MentalHeal:

    def __init__(self):
        self.connected = sqlite3.connect('D:\Etia\CURSUS_SCOLAIRE\PROJETS_SCOLAIRES\ADMINISTRATION_BASE_DE_DONNEES\Base de données\mental-heal.db')
     
        self.selection_user = str(input("Please select your CITY or your POSTAL CODE: "))
        self.validate()

        self.connected.commit()

    def validate(self):
        query = '''
            SELECT NAME, WORK_CITY, WORK_POSTAL_CODE, Psychologist_Information FROM Psychologist 
            WHERE WORK_CITY LIKE ? OR WORK_POSTAL_CODE LIKE ? || '%'
        '''
        result = self.connected.execute(query, (self.selection_user, self.selection_user[:2]))

        for row in result:
            print(row)

Test = Requests_MentalHeal()
Test.validate()

