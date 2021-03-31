from ElderHDatabase import searchPatients
from ElderHDatabase import searchIdentification
from ElderHDatabase import searchMedical

#changed line 13 in ElderHDatabase to:
#engine = sql.create_engine("sqlite:///Backend/elder_database.db")#, echo=True) 
#to mute the echoes coming from engine.

print("=======================")
#searchPatients('','','','','Male') #works
#searchIdentification()  #test with arguments now

searchMedical()      #problems
