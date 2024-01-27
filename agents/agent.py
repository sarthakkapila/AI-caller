from crewai import Agent

from tools.call_tool import CallNumber
from tools.LLM_tool import LLM
from tools.STT_tool import STT
from tools.TTS_tool import TTS

# MISTAKE NEEDED TO BE FIXED ->
# You are treating agent as a task, treat agent like a person and edit stuff in tasks

class Agents():
    
    def Caller_agent(self, name):
      return Agent(
        role= "Calls the client/prospect",
        goal= "The objective of this agent is to call the prospect/client",
        backstory= """
        You are a diligent & hardworking agent which calls a potential prospect. 
        Equipped with all the latest tools needed You dial the phone number of prospect/client.
        """,
        memory= True,
        verbose= True,
        allow_delegation= True,
        tools = [
          CallNumber.make_call,
          CallNumber.read_number,
        ]    
      )
      
      
# Thinking of adding multiple tasks and tool to one agent i.e. conversation
      
    def sales_agent(self, name):
        return Agent(
      role='Sales representative',
      goal="""Conduct a sales conversation with the prospect""",
      backstory="""
        You are most seasoned & polite sales representative with lots of expertise in customer acquisition, persuasion, sales and help the customers meet their needs.
        You sell the services offered by your company. 
        You use a tool which is a Large language Model which tells you what to conversate with the client by generating answers in a conversation.""",
      memory= True,
      verbose= True,
      allow_delegation=False,
      tools = [
        LLM.Sales_GPT,
      ]
        )

    def STT_agents(self, name):
      return Agent(
        role= "Speech-to-Text convertor",
        goal= "The objective of the agent is to convert the input given to it in form of speech (of the client) to text.",
        backstory= """A visionary speech to speech convertor, you are the most advanced Speech-to-Text (STT) converting agent.
        You are driven by a passion for inclusivity, championing accessibility and effective communication worldwide. 
        You convert the words said by the prospect/client into text using a tool named speech_to_text which uses openai-whisper api.""",
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
        You convert the text given by Sales_rep agent into speech, to talk to the prospect using a tool which uses tortoise TTS api.""",
        memory= True,
        verbose= True,
        allow_delegation= False,
        tools = [
          TTS.Tortoise_TTS,
        ]
      )