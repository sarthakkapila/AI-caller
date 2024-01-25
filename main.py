from crewai import Crew
from textwrap import dedent

from tools.call_number_tool import call_number
from Agents import TTS_agent
from Agents import STT_agent
from Agents import Caller_agent

from Tasks import Tasks.dial
from Tasks import Talk_to_client

from tools 