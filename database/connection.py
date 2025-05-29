from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Cria engine e sessão
engine = create_engine('sqlite:///biblioteca.db')
Session = sessionmaker(bind=engine)
session = Session()