from bardapi import Bard 

from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()
import os
token = os.environ.get('BARD_API_KEY')
print(Bard(token).get_answer("how old is the earth")["content"])
#print(token)

