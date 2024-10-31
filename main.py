from classes.Philosopher import Philosopher



for i in range(1, 6):
    philosopher = Philosopher(number=i)  # Instancia o filósofo
    philosopher.start()  # Inicia o filósofo