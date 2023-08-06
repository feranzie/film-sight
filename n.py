input_string = "video 1/1 (1/29162) C:\\Users\\DELL\\Desktop\\film-sight\\videoplayback.mp4: 384x640 1 person, 1 chair, 1 tv, 1763.0msus"

# Split the string at the semicolon
split_parts = input_string.split(':')

if len(split_parts) > 1:
    extracted_text = split_parts[1].strip()
    print(extracted_text)
else:
    print("No text found after semicolon.")