import threading
import time

# Define the function that continuously updates the variable
def update_variable():
    global variable
    for i in range(10):  # Modify the loop condition as per your requirements
        # Your logic to update the variable goes here
        variable = i
        time.sleep(1)  # Simulating the update process

# Define the function that prints the variable value every 30 seconds
def print_variable():
    while True:
        #print("Variable value:", variable) 
        print(variable) # Replace "variable" with the name of your variable
        time.sleep(30)  # Wait for 30 seconds before printing again

# Start the update_variable thread
update_thread = threading.Thread(target=update_variable)
update_thread.start()

# Start the print_variable thread
print_thread = threading.Thread(target=print_variable)
print_thread.start()
