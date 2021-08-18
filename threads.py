from threading import Thread
from time import sleep

def car(car_name, speed):
    track = 0
    while track <= 100:
        print(f"{car_name}: {track}km")
        track += speed
        sleep(0.5)  # segundos

# car("Carro 1", 10)
# car("Carro 2", 20)

t_car_1 = Thread(target=car, args=["Carro 1", 1])
t_car_2 = Thread(target=car, args=["Carro 2", 1.5])

t_car_1.start()
t_car_2.start()
