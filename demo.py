import LogSystem

log = LogSystem.LogSystem(level = "INFf")

print(log.error('This is a message',return_message = True , write_to_file = True))
print(log.info('This is a message',return_message = True , write_to_file = True))