
class Talk():
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