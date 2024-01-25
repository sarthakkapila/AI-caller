from crewai import Crew
from textwrap import dedent

# Importing all the Tasks
from tasks.dial_task import Dial_Task
from tasks.Talk_to_client_task import Talk

# Importing all the agents
from agents.Caller import caller
from agents.STT_agent import STT
from agents.TTS_agent import TTS
from agents.Sales import Sales_agent

