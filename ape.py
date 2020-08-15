class Ape():

    def __init__(self, banana):
        self.banana = banana
    
    def eat_banana(self):
        return f"I eat a banana with flavor {self.banana.get_flavor()}"