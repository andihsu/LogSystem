class LogSystem():

    def __init__(self, log_file_name = "Log.txt", messages = "\n", log_file_path = "", level = "INFO"):
        
        self.log_file_name = log_file_name
        self.message = messages
        self.log_file_path = log_file_path
        self.level = level

        if self.level != "INFO" or self.level != "DEBUG" or self.level != "WARNING" or self.level != "ERROR" or self.level != "CRITICAL":
            self.level = "INFO"
            self.info("Level is not valid, defaulting to INFO")


    
    def write_to_file(self, messages):

        with open(self.log_file_path + self.log_file_name, 'a') as log_file:
            log_file.write(messages + '\n')

    
    def error(self, messages, return_message = False, write_to_file = False):
        
        if return_message:
            print('[ERROR]: ' + messages)
        elif return_message != False:
            return '[ERROR]: ' + messages
        
        if write_to_file:
            pass
        elif write_to_file == True:
            self.write_to_file('[ERROR]: ' + messages)

    def warning(self, messages, return_message = False, write_to_file = False):
            
            if return_message:
                print('[WARNING]: ' + messages)
            elif return_message != False:
                return '[WARNING]: ' + messages
            
            if write_to_file:
                pass
            elif write_to_file != False:
                self.write_to_file('[WARNING]: ' + messages)

    def info(self, messages, return_message = False, write_to_file = False):
                
            if return_message:
                print('[INFO]: ' + messages)
            elif return_message != False:
                return '[INFO]: ' + messages
                
            if write_to_file:
                pass
            elif write_to_file != False:
                self.write_to_file('[INFO]: ' + messages)

    def debug(self, messages, return_message = False, write_to_file = False):

            if return_message:
                 print('[DEBUG]: ' + messages)
            elif return_message != False:
                 return '[DEBUG]: ' + messages
            
            if write_to_file:
                pass
            elif write_to_file != False:
                self.write_to_file('[DEBUG]: ' + messages)

    def critical(self, messages, return_message = False, write_to_file = False):
             
                if return_message:
                    print('[CRITICAL]: ' + messages)
                elif return_message != False:
                    return '[CRITICAL]: ' + messages
                
                if write_to_file:
                    pass
                elif write_to_file != False:
                    self.write_to_file('[CRITICAL]: ' + messages)

