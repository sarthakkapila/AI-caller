from crewai import Crew
from textwrap import dedent

# Importing all the Tasks
from tasks.tasks import Task

# Importing all the agents
from agents.agent import agents

from dotenv import load_dotenv
load_dotenv()

# 🚨🚨🚨
# FIX THE FUNCTION ARGUMENTS OF ALL

class CallerCrew:
  #NEED TO EDIT THIS ONE FOR SURE OR MAYBE JUST REMOVE IT
  def __init__(self, number):
    self.number = number

  def run(self):
    tasks = Task()
    agents = Agents()
    
    calling_agent = agents.Caller_agent()
    sales_agent = agents.sales_agent()
    STT_agent = agents.STT_agents()
    TTS_agent = agents.TTS_agents()
    
    dialing = tasks.dial()
    talking_to_client = tasks.Talk_to_client()
    
    crew = Crew(
      agents = [
        calling_agent,
        sales_agent,
        STT_agent,
        TTS_agent
      ],
      tasks = [
        dialing,
        talking_to_client,
      ],
      verbose=True
    )
    
    result = crew.kickoff()
    return result
  
if __name__ == "__main__":
  print("## Welcome to AI COLD CALLER")
  print('-------------------------------')
  
  # PART OF ARGUMENTS (need fixes)
  
  # company = input(
  #   dedent("""
  #     What is the company you want to analyze?
  #   """))
  
  financial_crew = FinancialCrew(company)
  result = financial_crew.run()
  print("\n\n########################")
  print("## Here is the summary")
  print("########################\n")
  print(result)  
  
  