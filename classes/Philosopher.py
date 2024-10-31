import requests
from random import random
import threading
from time import sleep

class Philosopher(threading.Thread):
    def __init__(self,number) -> None:
        super().__init__()
        self.number = number
        self.state = 'awaiting'


    def run(self):
        while True:
            if self.state == "awaiting":
                self.think()
            if self.state == "awaiting":
                self.eat()

    def eat(self):
        print(f"philosopher {self.number} is trying eat")
        self.state = 'eating'
        response = requests.get(f"http://127.0.0.1:8000/eat/{self.number}")
        if response.status_code != 200:
            print(f"philosopher {self.number} cannot eat")

        print(f"philosopher {self.number} eat in {response.content}")
        self.state = 'awaiting'
        

    def think(self):
        print(f"philosopher {self.number} is thinking")
        time_to_think = random() * 10
        self.state = 'thinking'
        sleep((time_to_think))
        self.state = 'awaiting'

        