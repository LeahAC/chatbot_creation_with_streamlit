from typing import Dict
from dotenv import load_dotenv
import os
from openai.lib.azure import AzureOpenAI
from typing import Optional


SYSTEM_PROMPT_FOR_FINAL_RESPONSE = """
You are a market and technology research analyst who is responsible for gathering data for making informed decisions about a user and his preferences in software.
You are onboarding a user and are tasked with asking relevant questions and responding to questions by the user. Your goal is to gather user information
and recommend suggestions based on the changing market trends, industrial developments, and  technological advancements. You should not ask too many questions at the same time.
"""
USER_PROMPT_TEMPLATE_FOR_FINAL_RESPONSE = """
{conversation_history}
Input:
{user_query}
Use the following user details to generate precise answer for the {user_query}, include the chat history if any.
You are already be familiar with some of the following user details:
user's name is: {name}
where does the user work?: {company}
what is the user's current role: {role} 
What is the user's mission?: {mission} 
What is the user's budget?: {budget} 
timeline for making purchasing decisions: {timeline} 
if user is the decision maker: {user_as_decision_maker}
decision maker's name: {decision_maker_name} 
decision maker's email: {decision_maker_email}
other invitee's name": {other_invitee_name} 
other invitee's email: {other_invitee_email} 
user's knowledge level": {user_knowledge_level}
these are user's favorite/chosen vendors": {user_vendor_fav} 
additional info: {additional_info}

Keep these instructions in mind:
If there is no query {user_query} or {conversation_history}, you ask the first question.
Stop asking questions if you think you have the answers. 
It is okay if the user cannot answer some questions.
Identify when the user doesn't want to chat anymore from the {user_query}, in which case, display a message and exit.
Answer:
"""

load_dotenv()

llm = AzureOpenAI(
    api_key=os.environ.get('AZURE_OPENAI_API_KEY'),
    api_version=os.environ.get('AZURE_OPENAI_API_VERSION'),
    azure_endpoint=os.environ.get('AZURE_OPENAI_SERVICE_END_POINT'))
 
def run_llm(query: str, name: str, data :Dict, conversation_history: Optional[list[tuple]]= None):
    conversation_history_str = ""
    if len(conversation_history) > 0:
        conversation_history_str = 'Chat History: \n'
        conversation_history_str += '\n'.join(
            [f"{message[0]}: {message[1]}" for message in conversation_history])
        
    user_prompt = USER_PROMPT_TEMPLATE_FOR_FINAL_RESPONSE.format(
        conversation_history=conversation_history_str, user_query=query, name= data["name"], company=data["company"], role=data["role"], 
        mission = data["mission"], budget = data["budget"], timeline = data["timeline"], user_as_decision_maker = data["user_as_decision_maker"],
        decision_maker_name = data["decision_maker_name"], decision_maker_email = data["decision_maker_email"], 
        other_invitee_name = data["other_invitee_name"], other_invitee_email = data["other_invitee_email"], user_knowledge_level = data["user_knowledge_level"],
        user_vendor_fav = data["user_vendor_fav"], additional_info = data["additional_info"]
        )    
    system_prompt = SYSTEM_PROMPT_FOR_FINAL_RESPONSE[:]

    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}]


    response = llm.chat.completions.create(
            model='gpt4',
            messages=messages,
            temperature=0,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
            stream = True
        )
    return response




