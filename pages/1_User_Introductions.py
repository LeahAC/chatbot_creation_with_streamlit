import streamlit as st
from streamlit_chat import message

from database import add_user_details

st.set_page_config(page_title="introductions")

st.markdown("# Let us get to know you.")
st.sidebar.header("User Onboarding")

if ("name" not in st.session_state):
    st.session_state["name"] = ""

st.write("<font color='orange'>Let's start with your name.</font>",unsafe_allow_html=True)

name = st.text_input("Name", placeholder="Enter your name.", key='name_input')    
st.session_state["name"] = name

st.write("<font color='orange'>What is your company?</font>",unsafe_allow_html=True)

company = st.text_input("Company", placeholder="Enter your company.",key='company_input') 

st.write("<font color='orange'>What is your role?</font>",unsafe_allow_html=True)

role = st.text_input("Role", placeholder="Enter your role.", key='role_input')

st.write("<font color='orange'>What is your mission?</font>",unsafe_allow_html=True)

mission = st.text_input("Mission", placeholder="Enter your mission.",key='mission_input')


st.write("<font color='orange'>What is your monthly budget in USD?</font>",unsafe_allow_html=True)

budget = st.text_input("Budget", placeholder="Enter your budget.", key='budget_input')


st.write("<font color='orange'>What is your timeline for this purchase in months?</font>",unsafe_allow_html=True)

timeline = st.text_input("Timeline", placeholder="Enter your timeline.", key='timeline_input')

user_as_decision_maker = 'Yes'
decision_maker_name = ""
decision_maker_email = ""
other_invitee_name = ""
other_invitee_email = ""
user_vendor_fav = ""
additional_info = ""

st.write("<font color='orange'>Are you the decision maker for the project?</font>",unsafe_allow_html=True)
opt_1 = st.selectbox('Are you the decision maker for the project?', ['Yes', 'No'], label_visibility= "hidden" )

if opt_1 == 'No':
    user_as_decision_maker = 'No'
    st.write("<font color='orange'>Would you like to provide the name and address of the decision maker?</font>",unsafe_allow_html=True)
    opt_2 = st.selectbox('Would you like to provide the name and address of the decision maker?', ['No', 'Yes'],label_visibility= "hidden")
    if opt_2 == 'Yes':
        decision_maker_name = st.text_input("Name of decision maker", placeholder="Enter the name of the decision maker.", key='decision_maker_name_input')
        decision_maker_email = st.text_input("Email of decision maker", placeholder="Enter the email of the decision maker.", key='decision_maker_email_input')

st.write("<font color='orange'>Would you like to invite someone else?</font>",unsafe_allow_html=True)         
opt_3 = st.selectbox('Would you like to invite someone else?', ['No', 'Yes'],label_visibility= "hidden")
if opt_3 == 'Yes':
    other_invitee_name = st.text_input("Name of invitee", placeholder="Enter the name of invitee.",  key='invitee_name_input')
    other_invitee_email = st.text_input("Email of invitee", placeholder="Enter the email of invitee.", key='invitee_email_input') 

st.write("<font color='orange'>What is your knowledge level of the domain?</font>",unsafe_allow_html=True)
user_knowledge_level = st.selectbox('What is your knowledge level of the domain?', ['Beginner', 'Intermediate', 'Expert'],label_visibility= "hidden")

st.write("<font color='orange'>Do you already have vendors in mind?</font>",unsafe_allow_html=True)
opt_4 = st.selectbox('Do you already have vendors in mind?', ['Yes', 'No'],label_visibility= "hidden")

if opt_4 == 'Yes':
    user_vendor_fav = st.text_input("Name of vendors", placeholder="Enter the names of vendors seperated by commas.", key='user_vendor_fav_input')

st.write("<font color='orange'>Is there someone whose opinion you\'re most concerned about regarding this purchase, and why?</font>",unsafe_allow_html=True)
opt_5 = st.selectbox('Is there someone whose opinion you\'re most concerned about regarding this purchase, and why?', ['No', 'Yes'],label_visibility= "hidden")
if opt_5 == 'Yes':
    additional_info = st.text_input("Enter here", placeholder="Enter the additional info.", key='additional_info')


add_user_details(name, company, role, mission, budget, timeline, user_as_decision_maker, decision_maker_name, decision_maker_email, 
                     other_invitee_name, other_invitee_email, user_knowledge_level, user_vendor_fav, additional_info)
    
if st.button('Submit'):
    st.markdown("You can try our AI assistant. See sidebar! 👈")


