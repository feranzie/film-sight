from bardapi import Bard 

from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()
import os
token = os.environ.get('BARD_API_KEY')
print(Bard(token).get_answer("form a sentence describing whats going on within an image of a school bag, trafficlight, 2 persons and a motorcycle detected")["content"])
#print(token)

