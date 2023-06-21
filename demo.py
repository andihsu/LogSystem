import LogSystem

log = LogSystem.LogSystem('This is a message', level = "INFO")

print(log.error('This is a message',return_message = True , write_to_file = True))