import os
from twilio.rest import Client as TwilioClient
from gradio_client import Client as GradioClient
# from langchain.tools import tool
# from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv
import pyaudio
import speech_recognition as sr

from langchain.chat_models import ChatLiteLLM, SalesGPT  # Import necessary classes from langchain

load_dotenv()  # make sure you have .env file with your API keys, eg., OPENAI_API_KEY=sk-xxx


class LLM:
    @staticmethod
    def Sales_GPT():
        """Context-aware AI Agent for Sales"""

        conversation_stages = {
            '1': "Introduction: Start the conversation by introducing yourself and your company. Be polite and respectful while keeping the tone of the conversation professional. Your greeting should be welcoming. Always clarify in your greeting the reason why you are contacting the prospect.",
            '2': "Qualification: Qualify the prospect by confirming if they are the right person to talk to regarding your product/service. Ensure that they have the authority to make purchasing decisions.",
            '3': "Value proposition: Briefly explain how your product/service can benefit the prospect. Focus on the unique selling points and value proposition of your product/service that sets it apart from competitors.",
            '4': "Needs analysis: Ask open-ended questions to uncover the prospect's needs and pain points. Listen carefully to their responses and take notes.",
            '5': "Solution presentation: Based on the prospect's needs, present your product/service as the solution that can address their pain points.",
            '6': "Objection handling: Address any objections that the prospect may have regarding your product/service. Be prepared to provide evidence or testimonials to support your claims.",
            '7': "Close: Ask for the sale by proposing a next step. This could be a demo, a trial or a meeting with decision-makers. Ensure to summarize what has been discussed and reiterate the benefits.",
            '8': "End: Conclude the conversation by expressing gratitude for their time and attention. Reiterate your contact information and let them know you're available for any further inquiries. Thank them for considering your product/service and leave the door open for future communication or follow-up if needed.",
            '9': "Break: Reaching this stage means that the call is completed and then the call is disconnected" 
        }

        config = dict(
            salesperson_name="Ted Lasso",
            salesperson_role="Business Development Representative",
            company_name="Sleep Haven",
            company_business="Sleep Haven is a premium mattress company that provides customers with the most comfortable and supportive sleeping experience possible. We offer a range of high-quality mattresses, pillows, and bedding accessories that are designed to meet the unique needs of our customers.",
            company_values="Our mission at Sleep Haven is to help people achieve a better night's sleep by providing them with the best possible sleep solutions. We believe that quality sleep is essential to overall health and well-being, and we are committed to helping our customers achieve optimal sleep by offering exceptional products and customer service.",
            conversation_purpose="find out whether they are looking to achieve better sleep via buying a premier mattress.",
            conversation_history=[],
            conversation_type="call",
            conversation_stage=conversation_stages.get('1', "Introduction: Start the conversation by introducing yourself and your company. Be polite and respectful while keeping the tone of the conversation professional."),
            use_tools=True,
            product_catalog="sample_product_catalog.txt"
        )

        # Initialize LiteLLM
        llm = ChatLiteLLM(temperature=0.4, model_name="gpt-3.5-turbo")

        # Initialize SalesGPT
        sales_agent = SalesGPT.from_llm(llm, use_tools=True, verbose=False, **config)

        # Seed the agent
        sales_agent.seed_agent()

        while True:
            # Agent's output
            sales_agent.step()

            # User's input
            user_input = input()
            
            # User's output
            sales_agent.human_step(user_input)

            # Determine conversation stage
            sales_agent.determine_conversation_stage()
            
            if sales_agent.determine_conversation_stage() == 9:
                break
            else: 
                continue

# 🚨
# WILL ADD WHEN EVERYTHING ELSE IS WORKING !
        # # Accessing generated responses
        # generated_response = sales_agent.get_last_response()
        # print("Generated Response:", generated_response)

        # # Accessing conversation history
        # conversation_history = sales_agent.get_conversation_history()
        # print("Conversation History:", conversation_history)

        # # Accessing other agent information
        # agent_info = sales_agent.get_agent_info()
        # print("Agent Information:", agent_info)