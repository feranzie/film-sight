import detect
import subprocess

# Define the command and arguments
command = ['python', 'detect.py', '--weights', 'yolov5s.pt', '--source', 'IMG_9619.MOV', '--view-img']

# Run the commandimport subprocess
import time

# Define the command and arguments
#command = ['python', 'detect.py', '--source', 'path/to/input', '--weights', 'path/to/weights', '--output', 'path/to/output']

# Run the command every 30 seconds
while True:
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Parse the output and extract the labels
    labels = []
    for line in result.stdout.decode('utf-8').splitlines():
        if line.startswith('      '):
            labels.append(line.strip())
    
    # Print the labels as a list
    print(labels)
    
    # Wait for 30 seconds before running the command again
    time.sleep(30)