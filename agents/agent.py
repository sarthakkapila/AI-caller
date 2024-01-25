from crewai import Agent

from tools.call_tool import CallNumber
from tools.LLM_tool import LLM
from tools.STT_tool import STT
from tools.TTS_tool import TTS

class Agents():
    
    def Caller_agent(self, name):
      return Agent(
        role= "Calls the client",
        goal= "The objective of the agent is to call the prospect using twilio",
        backstory= """You are a diligent & hardworking agent which dials the phone umber of the potential prospect from a csv document. 
        Your task is to dial the number of prospect""",
        memory= True,
        verbose= True,
        allow_delegation= False,
        tools = [
          CallNumber.make_call,
        ]    
      )
      
    def sales_agent(self, name):
        return Agent(
      role='Sales representative',
      goal="""Conduct a sales conversation with the prospect""",
      backstory="""You are most seasoned & polite sales representative with lots of expertise in customer acquisition, persuasion, sales and help the cutomers meet their needs.
                You sell the services offered by your company.""",
      memory= True,
      verbose= True,
      allow_delegation=False,
      tools = [
        LLM.LLM,
      ]
        )

    def STT_agents(self, name):
      return Agent(
        role= "Speech-to-Text convertor",
        goal= "The objective of the agent is to convert the input given to it in form of text to speech.",
        backstory= """A visionary speech to speech convertor, you are the most advanced Speech-to-Text (STT) converting agent 
        driven by a passion for inclusivity, championing accessibility and effective communication worldwide. You convert the words said by the prospect into text.""",
        memory= True,
        verbose= True,
        allow_delegation= False,
        tools = [
          STT.speech_to_text,
        ]
      )
      
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
      
    