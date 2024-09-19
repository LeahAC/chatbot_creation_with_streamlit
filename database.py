from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Optional, List

# Create a database engine
engine = create_engine('sqlite:///my_database.db')

# Define a base class for declarative class definitions
Base = declarative_base()


# Create the database table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    company = Column(String)
    role = Column(String)
    mission = Column(String)
    budget = Column(String)
    timeline = Column(String)
    user_as_decision_maker = Column(String)
    decision_maker_name = Column(String)
    decision_maker_email = Column(String)
    other_invitee_name = Column(String)
    other_invitee_email = Column(String)
    user_knowledge_level = Column(String)
    user_vendor_fav = Column(String)
    additional_info = Column(String)
        

Base.metadata.create_all(engine)        
# Create a session
Session = sessionmaker(bind=engine)
session = Session()


def get_a_user(session,name):
    #print(session.query(User).filter_by(name=name).first().__dict__)
    return session.query(User).filter_by(name=name).first().__dict__

def add_user_details(
        name: str, company: Optional[str] = None, role: Optional[str] = None,  mission: Optional[str] = None,
        budget: Optional[str] = None, timeline: Optional[str] = None, user_as_decision_maker: Optional[str] = None,
        decision_maker_name: Optional[str] = None, decision_maker_email: Optional[str] = None,
        other_invitee_name: Optional[str] = None, other_invitee_email: Optional[str] = None, user_knowledge_level: Optional[str] = None, 
        user_vendor_fav: Optional[str] = None, additional_info: Optional[str] = None):
    
    existing_user = session.query(User).filter_by(name=name).first()
    if existing_user:
        # Update existing user
        existing_user.company = company
        existing_user.role = role
        existing_user.mission = mission
        existing_user.budget = budget
        existing_user.timeline = timeline
        existing_user.user_as_decision_maker = user_as_decision_maker
        existing_user.decision_maker_name = decision_maker_name
        existing_user.decision_maker_email = decision_maker_email
        existing_user.other_invitee_name = other_invitee_name
        existing_user.other_invitee_email = other_invitee_email
        existing_user.user_knowledge_level = user_knowledge_level
        existing_user.user_vendor_fav = user_vendor_fav
        existing_user.additional_info = additional_info
    else:
        # Create new user
        new_user = User(name=name, company=company, role=role, mission = mission, budget = budget, 
                        timeline = timeline, user_as_decision_maker = user_as_decision_maker,
                        decision_maker_name = decision_maker_name, decision_maker_email = decision_maker_email,
                        other_invitee_name = other_invitee_name, other_invitee_email = other_invitee_email, user_knowledge_level = user_knowledge_level,
                        user_vendor_fav = user_vendor_fav, additional_info = additional_info
                        )
        session.add(new_user)
    
    session.commit()
    

# Query all users
def get_user_details(name: str):
    user = get_a_user(session, name)
    return {
        "name": user['name'],
        "company": user['company'], 
        "role": user['role'], 
        "mission": user['mission'], 
        "budget": user['budget'], 
        "timeline": user['timeline'], 
        "user_as_decision_maker": user['user_as_decision_maker'],
        "decision_maker_name": user['decision_maker_name'], 
        "decision_maker_email": user['decision_maker_email'],
        "other_invitee_name": user['other_invitee_name'], 
        "other_invitee_email": user['other_invitee_email'], 
        "user_knowledge_level": user['user_knowledge_level'],
        "user_vendor_fav": user['user_vendor_fav'], 
        "additional_info": user['additional_info']

    }
       

       

    

    






# Insert data
#user = User(name='John', age=30)
#session.add(user)
#session.commit()

# Query the data
#users = session.query(User).all()
#for user in users:
#    print(user.name, user.age)