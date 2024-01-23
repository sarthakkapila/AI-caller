import os
from twilio.rest import Client
# from langchain.tools import tool
# from langchain_community.llms import HuggingFaceHub
from gradio_client import Client
from langchain.chat_models import ChatLiteLLM
from dotenv import load_dotenv


from dotenv import load_dotenv
load_dotenv() # make sure you have .env file with your API keys, eg., OPENAI_API_KEY=sk-xxx


class Tools:
    
#   @tool("Dial a phone number")
    @staticmethod
    def call_number():
        """Calls phone number"""
        account_sid = 'ACea6a7def2b53a8ad97298f9ba69fccf8'
        auth_token = '7d1f0b090ec6cd9460786898798ee6dc'

        to_number = '+916280438234'
        from_number= '+16692023622'
    
        client = Client(account_sid, auth_token)

        call = client.calls.create(
            to=to_number,
            from_=from_number,
            url='http://demo.twilio.com/docs/voice.xml'
        )
        return call.sid

# Use microsoft/speecht5_tts if this api doesn't work 

#   @tool("Text to Speech tool")
    @staticmethod
    def TTS(text, file_path, voice, second_voice, split_by_newline):
            """Converts text to speech"""
            client = Client("https://manmay-tortoise-tts.hf.space/")
            result = client.predict(
                text,
                file_path,
                voice,
                second_voice,
                split_by_newline,
                api_name="/predict"   
                
#                                   TESTING   
# # Example of using the TTS method
# text_to_convert = "Hey this is Emily from XYZ productions, Is this mr. Kevin talking?!"
# file_path_or_url = "example.txt"
# voice_option = "angie,angie"
# second_voice_option = "angie,angie"
# split_by_newline_option = "Yes"
            )
            # print(result)


#   @tool("Speech to text")
    @staticmethod
    def SST():
        """Converts speech to text"""
        
        
        
        
        
        
#   @tool("Context-aware AI Agent for Sales")
    @staticmethod
    def LLM():
        """Context-aware AI Agent for Sales"""

        # Initialize LiteLLM
        llm = ChatLiteLLM(temperature=0.4, model_name="gpt-3.5-turbo")

        # Initialize SalesGPT agent
        sales_agent = SalesGPT.from_llm(llm, use_tools=True, verbose=False,
                                       product_catalog="sample_product_catalog.txt",
                                       salesperson_name="Ted Lasso",
                                       salesperson_role="Sales Representative",
                                       company_name="Sleep Haven",
                                       company_business='''Sleep Haven 
                                       is a premium mattress company that provides
                                       customers with the most comfortable and
                                       supportive sleeping experience possible. 
                                       We offer a range of high-quality mattresses,
                                       pillows, and bedding accessories 
                                       that are designed to meet the unique 
                                       needs of our customers.'''
                                       )

        # Seed the agent
        sales_agent.seed_agent()

        # Determine conversation stage (optional for demonstration)
        sales_agent.determine_conversation_stage()

        # Agent's turn
        sales_agent.step()

        # User's input (you can replace this with your own input logic)
        user_input = input('Your response: ')

        # User's turn
        sales_agent.human_step(user_input)

        # Determine conversation stage again (optional)
        sales_agent.determine_conversation_stage()

        # Agent's next turn
        sales_agent.step()

        # You can continue the conversation as needed

        # Example: Accessing generated responses
        generated_response = sales_agent.get_last_response()
        print("Generated Response:", generated_response)

        # Example: Accessing conversation history
        conversation_history = sales_agent.get_conversation_history()
        print("Conversation History:", conversation_history)

        # Example: Accessing other agent information
        agent_info = sales_agent.get_agent_info()
        print("Agent Information:", agent_info)

        # You can return or use any relevant information from the agent as needed