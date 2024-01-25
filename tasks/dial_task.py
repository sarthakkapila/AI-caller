from crewai import Task
from textwrap import dedent

class Dial_Task():
  def dial(self, agent, csv):
    return Task(description=dedent(f"""
      By using twilio api, call the prospect/client's phone number
      given in a .csv file.
      Your only Task is to dial the phone number using the Twilio api and 
      let other agents handle the rest.
            
      RULES
      -----
      - Dial a number one at a time, once the first call is finished then only dial the next number from the file.
      - Make sure not to use too much money on my twilio account.
      - When all number have been dialed at least once your task is done.
      - While calling log "Calling prospect" in the terminal.
      - When call is ended log "Call ended, caliing the next prospect"
      - When all the phone numbers in the csv files are dialed simply log "All numbers dialed" and also return complete info about the task which should include:
      1.) Total clients called
      2.) Called connected
      3.) Calls failed
      
      - If there are any issues with connecting or if the line is busy, move onto the next number in the file, by logging "Couldn't connect call, calling next prospect" 
      in the terminal.

        At the end return/log all the info about 
        
    "If you do your BEST WORK, I'll give you a $1,000 commission!"
        MY LIFE DEPEND ON YOU FOLLOWING IT!

      """),
      agent=agent
      
    )