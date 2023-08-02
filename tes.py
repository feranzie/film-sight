from bardapi import Bard 

from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()
import os
token = os.environ.get('BARD_API_KEY')
print(Bard(token).get_answer("what is the most likely context of an image with a school bag two persons a car and a traffic lig")["content"])
#print(token)

