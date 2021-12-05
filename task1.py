class AbstractHandler(object):
 

 
    def __init__(self, nxt):

 
        self._nxt = nxt
 
    
    def handle_request(self, text):
        pass
    

class addition(AbstractHandler):
 
    def handle_request(self, text):
        
        array = text.split(' ')
        if array[1] == '+':
            print(int(array[0]) + int(array[2]))
            return (int(array[0]) + int(array[2]))
        
class substruction(AbstractHandler):
 
 
    def handle_request(self, text):
        
        array = text.split(' ')
        if array[1] == '-':
            print(int(array[0]) - int(array[2]))
            return (int(array[0]) - int(array[2]))
class division(AbstractHandler):
 
 
    def handle_request(self, text):
        
        array = text.split(' ')
        if array[1] == '/':
            print(int(array[0]) / int(array[2]))
            return (int(array[0]) / int(array[2]))
class multiplication(AbstractHandler):
 
 
    def handle_request(self, text):
        
        array = text.split(' ')
        if array[1] == '*':
            print(int(array[0]) * int(array[2]))
            return (int(array[0]) * int(array[2]))
           
 
if __name__ == "__main__":
    
    
    
    operation3 = multiplication(operation2)

    print(operation3.handle_request("2 * 3"))