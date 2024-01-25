from crewai import Agent

class caller():
    def Caller_agent(self, name):
      return Agent(
        role= "Calls the client",
        goal= "The objective of the agent is to call the prospect using twilio",
        backstory= """You are a diligent & hardworking agent which dials the phone umber of the potential prospect from a csv document. 
        Your task is to dial the number of prospect""",
        memory= True,
        verbose= True,
        allow_delegation= False,
      )
      
      