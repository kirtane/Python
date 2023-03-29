from abc import ABC, abstractmethod

class human(ABC):
    def __init__(self) -> None:
        print("human init")
    
    @abstractmethod
    def speak(self):
        print("human can speak")
        pass

    @abstractmethod
    def walk(self):
        print("human should walk")
        pass

    def nature(self):
        pass

class dad(human):
    def __init__(self) -> None:
        super().__init__()
        print("dad init")


    def speak(self):
        print("dad can speak")

    def walk(self):
        print("dad can walk")

    def nature(self):
        print("reading news paper")

dadobj = dad()
dadobj.speak()
dadobj.walk()
dadobj.nature()

