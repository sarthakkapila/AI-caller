from crewai import Task
from textwrap import dedent

class Task():
  def dial(self, agent, csv):
    return Task(description=dedent(f"""
      Call the prospect/client's phone number using tools provided
      Pay special attention to dial a number once only and that too one by one from the csv file.
            
      RULES
      -----
      - Dial a number one at a time, once the first call is finished then only dial the next number from the file.
      - Make sure the keep in mind the max_calls of the make_call tool.
      - When all number have been dialed at least once your task is done.
      - While calling log "Calling prospect" in the terminal/console.
      - When call is ended log "Call ended, caliing the next prospect"
      - When all the phone numbers in the csv files are dialed simply log "All numbers dialed" and also return complete info about the task which should include:
      1.) Total clients called
      2.) Called connected
      3.) Calls failed
      
      - If there are any issues with connecting or if the line is busy, move onto the next number in the file, by logging "Couldn't connect call, calling next prospect" 
      in the terminal.
        
    "If you do your BEST WORK, I'll give you a $1,000 commission!"
        MY LIFE DEPEND ON YOU FOLLOWING IT!

      """),
      agent=agent
      
    )


# 🚨🚨🚨
  def Talk_to_client(self, agent):
    return Task(description=dedent(f"""
        
      This task takes a client's response from speech-to-text tool then, after this and uses uses the Sales-tool to decide what should be said to client in the 
      form of text, then that text is converted into speech using the Text-to-speech tool.
      Focus should be mainly on completing this 3 step task with accuracy and as fast as possible.
        
      RULES
      ----
      - Do not end the task until the call is ended, failed or disconnected.
      - Make sure to do this task like a conversation is done by humans. Only difference is that, You think with the Sales_tool which gives a text ouput
          then, You speak when by converting Text output to speech using Text-to-speech tool. Then listen with the Speech-to-text tool, then that text from speech to text 
          is thought on again by Sales-tool and this process goes on till call is disconnected.
      - If there are any errors during the execution of the task they will need to be handled grace.
      - All the text should be logged in the terminal.
      
      Your final answer will be log of the whole conversation between prospect and the sales_agent.
                
      "If you do your BEST WORK, I'll give you a $10,000 commission!"
                
          MY LIFE DEPEND ON YOU FOLLOWING IT!

      """),
      agent=agent
    )