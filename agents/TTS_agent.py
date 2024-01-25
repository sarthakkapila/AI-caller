from crewai import Agent
from tools.TTS_tool import TTS

class TTS():
    def TTS_agents(self, name):
      return Agent(
        role= "Text-to-speech convertor",
        goal= "The objective of the agent is the convert the input given to it in form of text to speech.",
        backstory= """A visionary text to speech convertor, you are the most advanced Text-to-Speech (TTS) converting agent 
        driven by a passion for inclusivity, championing accessibility and effective communication worldwide. 
        You convert the text given by Sales_rep agent into speech, to talk to the prospect.""",
        memory= True,
        verbose= True,
        allow_delegation= False,
        tools = [
          TTS.TTS,
        ]
      )