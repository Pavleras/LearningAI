import datetime as dt

activeUsers = ['Pablo','Eric','Antonio','Josep']
print(activeUsers)
inactiveUsers = activeUsers.pop()
currentTime = dt.datetime.now().strftime("%d/%m/%Y,%H:%M:%S")
print(f"{inactiveUsers.title()} was disconnected at {currentTime}")