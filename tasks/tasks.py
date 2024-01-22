from crewai import Task
from textwrap import dedent

class Tasks():
  def dialer(self, agent, csv):
    return Task(description=dedent(f"""
      By using twilio api, call the prospect/client's phone number
      given in a .csv file.
      Your only Task is to dial the phone number using the Twilio api and 
      let other agents handle the rest.
    
      You will give a confirmation when the call gets connected to the client.
      If there are any issues with connecting or if the line is busy, move onto the next number in the file.
      
      If all the numbers in the file have been dialed once simply return all numbers done and your task will be over.
      
      RULES
      -----
      - Dial a number one at a time, once the first call is finished then only dial the next number from the file.
      - Make sure not to use too much money on my twilio account.
      - When all number have been dialed at least once your task is done.
        
        {self.__tip_section()}
        
      """),
      agent=agent
      
    )
    
  def Intro(self, agent): 
    return Task(description=dedent(f"""
        
        
        
        
        {self.__tip_section()}

      """),
      agent=agent
    )

  def Talk_to_client(self, agent):
    return Task(description=dedent(f"""
        
        
        
        
        
        
        {self.__tip_section()}        
      """),
      agent=agent
    )


  def Refusal(self, agent):
    return Task(description=dedent(f"""
        
        
        
        
        
        
        
    
        {self.__tip_section()}
      """),
      agent=agent
    )

  def __tip_section(self):
    return "If you do your BEST WORK, I'll give you a $10,000 commission!"