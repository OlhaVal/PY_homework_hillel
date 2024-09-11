from homework_10 import log_event_for_test

username = "Expired_name_4"
status = "expired"
log_event_for_test(username, status)

with open('login_system.log', 'r') as file:
    last_line = file.readlines()[-1]
    line_check = last_line[(last_line.find("Login event - Username:")):-1]

print(last_line)
print(line_check)
print(f"Login event - Username: {username}, Status: {status}")
