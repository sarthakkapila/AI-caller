from crewai import Agent

class STT():
    def STT_agents(self, name):
      return Agent(
        role= "Speech-to-Text convertor",
        goal= "The objective of the agent is to convert the input given to it in form of text to speech.",
        backstory= """A visionary speech to speech convertor, you are the most advanced Speech-to-Text (STT) converting agent 
        driven by a passion for inclusivity, championing accessibility and effective communication worldwide. You convert the words said by the prospect into text.""",
        memory= True,
        verbose= True,
        allow_delegation= False,
      )