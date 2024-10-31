from fastapi import FastAPI
from random import random
import asyncio
import json

app = FastAPI()


@app.get("/eat/{place}")
async def eat(place:int):
    
    if not control_use_fork(place): return {"message": f"cannot use"}
    time_to_eat = random() * 10
    print(time_to_eat)
    await asyncio.sleep((time_to_eat))
    control_realese_fork(place)

    return {"message": f"{time_to_eat}"}

def control_use_fork(place):
    dict_place_fork = {1:[5,1], 2:[1,2], 3:[2,3], 4:[3,4], 5:[4,5]}

    if not use_fork(dict_place_fork[place][0]): return False
    if not use_fork(dict_place_fork[place][1]): 
        realease_fork(dict_place_fork[place][0])
        return False

    return True


def control_realese_fork(place):
    dict_place_fork = {1:[5,1], 2:[1,2], 3:[2,3], 4:[3,4], 5:[4,5]}
    
    realease_fork(dict_place_fork[place][0])
    realease_fork(dict_place_fork[place][1])
    


def use_fork(fork_number) -> bool:
    path = r"philosophy_problem\api\resource.json"
    with open(path, 'r') as file:
        forks = json.load(file)
    print(forks)
    if forks[str(fork_number)]['is_free'] == False: return False
    
    forks[str(fork_number)]['is_free'] = False
    with open(path, 'w') as file:  # Salvar as alterações de volta ao arquivo
        json.dump(forks, file)
    return True

def realease_fork(fork_number):
    path = r"philosophy_problem\api\resource.json"
    with open(path, 'r') as file:
        forks = json.load(file)
    print(forks)
    forks[str(fork_number)]['is_free'] = True
    with open(path, 'w') as file:  # Salvar as alterações de volta ao arquivo
        json.dump(forks, file)