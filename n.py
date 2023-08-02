from bardapi import Bard 

token = "ZAifszlN0IlRz_QW5VyhNTuKAyJjRXRqumse4r4gSIGVNKJLIEdMDRBV88DpWJbNB9aSnA."
print(Bard(token).get_answer("what is the most likely context of an image with a school bag two persons a car and a traffic lig")["content"])
#print(token)

