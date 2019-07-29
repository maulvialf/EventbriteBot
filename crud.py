# controller.py
from model import Event
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func, select
import config

def connectToDatabase():
    """
    Connect to our SQLite database and return a Session object
    """
    engine = create_engine("sqlite:///{}".format(config.database), echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

# pengen biar makin crud
def addRecord(data):
    # connect to session and commit data to database
    session = connectToDatabase()
    session.add(data)
    session.commit()
    session.close()


def getEventBelumPosting():
    """
    Get all records and return them
    """
    
    session = connectToDatabase()
    result = session.query(Event)                \
        .filter(Event.status == 0)               \
        .order_by(func.random())                 \
        .limit(10)                               

    session.close()     
           
    x =  result.first()
    return result.first()

def updateDone(event):
    session = connectToDatabase()
    result = session.query(Event).filter(Event.id == event.id).first()
    # udah diposting
    result.status = 1
    session.add(result)
    session.commit()
    session.close()     

    return 0   

def checkdata(event):
    session = connectToDatabase()
    # yang dijadiin key disini yaitu link
    result = session.query(Event).filter(Event.link == event.link).first()
    session.close()     
    
    if(result == None):
        return False
    else:
        return True