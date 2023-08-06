import re

string = "\\Users\\DELL\\Desktop\\film-sight\\videoplayback.mp4: 384x640 1 person, 1 chair, 1 tv, 1763.0ms"

pattern = ":(.*?\.[^:\n\r]*)"

match = re.search(pattern, string)

if match:
    print(match.group(1))
else:
    print("No match found")
