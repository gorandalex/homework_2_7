import configparser
import pathlib

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 8
NUMBER_TEACHERS = 5
NUMBER_GRADES = 20


file_config = pathlib.Path(__file__).parent.parent.joinpath("config.ini")
config = configparser.ConfigParser()
config.read(file_config)

username = config.get('DB_DEV', 'USER')
password = config.get('DB_DEV', 'PASSWORD')
db_name = config.get('DB_DEV', 'DB_NAME')
host = config.get('DB_DEV', 'HOST')
port = config.get('DB_DEV', 'PORT')

url_to_db = f"postgresql://{username}:{password}@{host}:{port}/{db_name}"

engine = create_engine(url_to_db, echo=True, pool_size=5)
Session = sessionmaker(bind=engine)
session = Session()