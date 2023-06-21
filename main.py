class LogSystem():

    def __init__(self, log_file_name, message, log_file_path):
        self.log_file_name = log_file_name
        self.message = message
        self.log_file_path = log_file_path

    
    def write_to_file(self, message):
        with open(self.log_file_path + self.log_file_name, 'a') as log_file:
            log_file.write(message + '\n')

    
    def error(self, message, return_message = False, write_to_file = False):
        
        if return_message:
            print('[ERROR]: ' + message)
        elif return_message != False:
            return '[ERROR]: ' + message
        
        if write_to_file:
            pass
        elif write_to_file != False:
            self.write_to_file('[ERROR]: ' + message)

    def warning(self, message, return_message = False, write_to_file = False):
            
            if return_message:
                print('[WARNING]: ' + message)
            elif return_message != False:
                return '[WARNING]: ' + message
            
            if write_to_file:
                pass
            elif write_to_file != False:
                self.write_to_file('[WARNING]: ' + message)

    def info(self, message, return_message = False, write_to_file = False):
                
            if return_message:
                print('[INFO]: ' + message)
            elif return_message != False:
                return '[INFO]: ' + message
                
            if write_to_file:
                pass
            elif write_to_file != False:
                self.write_to_file('[INFO]: ' + message)

    def debug(self, message, return_message = False, write_to_file = False):

            if return_message:
                 print('[DEBUG]: ' + message)
            elif return_message != False:
                 return '[DEBUG]: ' + message
            
            if write_to_file:
                pass
            elif write_to_file != False:
                self.write_to_file('[DEBUG]: ' + message)

    def critical(self, message, return_message = False, write_to_file = False):
             
                if return_message:
                    print('[CRITICAL]: ' + message)
                elif return_message != False:
                    return '[CRITICAL]: ' + message
                
                if write_to_file:
                    pass
                elif write_to_file != False:
                    self.write_to_file('[CRITICAL]: ' + message)

    def fatal(self, message, return_message = False, write_to_file = False):
                 
                if return_message:
                    print('[FATAL]: ' + message)
                elif return_message != False:
                    return '[FATAL]: ' + message
                    
                if write_to_file:
                    pass
                elif write_to_file != False:
                    self.write_to_file('[FATAL]: ' + message)

                    