from ElderHDatabase import sajDiseaseSearch
from ElderHDatabase import anySearch

#changed line 13 in ElderHDatabase to:
#engine = sql.create_engine("sqlite:///Backend/elder_database.db")#, echo=True) 
#to mute the echoes coming from engine.

print("=======================")
#text="Arthritis"
#sajDiseaseSearch("Arthritis")#works!
anySearch()
