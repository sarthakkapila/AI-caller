from crewai import Agent

class Agents():
    def Sales_rep(self, name):
        return Agent(
      role='Sales representative',
      goal="""Conduct a sales conversation with the prospect""",
      backstory="""You are most seasoned & polite sales representative with lots of expertise in customer acquisition, persuasion, sales and help the cutomers meet their needs.
                You sell the services offered by your company.""",
      llm= "",          
      memory= True,
      verbose= True,
      allow_delegation=False,
        )
    
    def TTS_agent(self, name):
      return Agent(
        role= "Text-to-speech convertor",
        goal= "The objective of the agent is the convert the input given to it in form of text to speech.",
        backstory= """A visionary text to speech convertor, you are the most advanced Text-to-Speech (TTS) converting agent 
        driven by a passion for inclusivity, championing accessibility and effective communication worldwide """,
        llm= "",
        memory= True,
        verbose= True,
        allow_delegation= False,
      )
      
    def STT_agent(self, name):
      return Agent(
        role= "Speech-to-Text convertor",
        goal= "The objective of the agent is the convert the input given to it in form of text to speech.",
        backstory= """A visionary speech to speech convertor, you are the most advanced Speech-to-Text (STT) converting agent 
        driven by a passion for inclusivity, championing accessibility and effective communication worldwide """,
        llm= "",
        memory= True,
        verbose= True,
        allow_delegation= False,
      )