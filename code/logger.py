import datetime

def log_event(username, action):
    timestamp = datetime.datetime.now()
    log_entry = f"{timestamp} | User: {username} | Action: {action}"
    
    with open("activity.log", "a") as log_file:
        log_file.write(log_entry + "\n")
