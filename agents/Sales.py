from crewai import Agent

class Sales_agent():
  
    def sales_agent(self, name):
        return Agent(
      role='Sales representative',
      goal="""Conduct a sales conversation with the prospect""",
      backstory="""You are most seasoned & polite sales representative with lots of expertise in customer acquisition, persuasion, sales and help the cutomers meet their needs.
                You sell the services offered by your company.""",
      memory= True,
      verbose= True,
      allow_delegation=False,
        )
