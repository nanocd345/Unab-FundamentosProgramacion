import random
import time

class Bus:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        # Simula el movimiento del bus avanzando una distancia aleatoria
        self.position += random.randint(1, 10)

    def __str__(self):
        return f"{self.name}: {'*' * self.position}"

def race(buses, track_length, race_duration):
    start_time = time.time()
    while time.time() - start_time < race_duration:
        # Limpia la pantalla para mostrar el progreso
        print("\033[H\033[J", end="")

        # Mueve los buses y muestra su progreso
        for bus in buses:
            bus.move()
            print(bus)

        # Verifica si algún bus ha alcanzado o superado la longitud de la pista
        winner = None
        for bus in buses:
            if bus.position >= track_length:
                winner = bus.name
                break

        if winner:
            print(f"\n¡El ganador es {winner}!")
            break

        # Espera un momento antes de la siguiente actualización
        time.sleep(1)

if __name__ == "__main__":
    # Configuración de la carrera
    track_length = 50
    race_duration = 30  # Duración de la carrera en segundos

    # Crear una lista de buses
    buses = [Bus("Bus 1"), Bus("Bus 2"), Bus("Bus 3")]

    # Iniciar la carrera
    race(buses, track_length, race_duration)