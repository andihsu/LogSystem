import LogSystem

log = LogSystem.LogSystem(level = "INFO")

print(log.error('This is a message',return_message = True , write_to_file = True))
