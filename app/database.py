from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

#Where the database is located SQLALCHEMY_DATABASE_URL = "postgresql://username:password@postgresserver/db" db= databasename
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

#connection string to pass into SQL alchemy, create the engine, for sqlalchemy to connect to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#make use of a session, autocomit = if you want it to auto save
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#all the models that we define to create our tables in postgres will extend the base class
Base = declarative_base()

# Dependency database session or request to the session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# #Connecting to DATABASE and use raw SQL with posgres instead of SQL alchemy
# while True:

#     try:
#         connection = psycopg2.connect(host ='localhost', database= 'fastAPI', user='postgres',
#         password='INPUT PASSWORD',cursor_factory=RealDictCursor)
#         cursor = connection.cursor()
#         print("Connected Successfully")
#         break
#     except Exception as error:
#         print("Connecting Failed")
#         print("Error: ",error)
#         time.sleep(5)