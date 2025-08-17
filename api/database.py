""" Database configuration"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db"


# Creer un moteur de database (engine) qui établit la connexion avec notre SQLite (movies.db)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}

)

#Définir SessionLocal, qui permet de créer des sessions pour interagir avec la base de données.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Définir Base, qui servira de classe de base pour nos modèles SQLAlchemy.

Base = declarative_base ()

#if __name__=="__main__":
#    try:
#       with engine.connect () as conn:
#            print("connection à la database reuissi ")
#    except Exception as e:
#        print("Oops! quelque chose n'a pas marché : {e} ")

        




