import geopy.distance
from geopy.geocoders import Nominatim

def obtener_coordenadas(ciudad):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(ciudad)
    if not location:
        raise ValueError(f"No se pudieron obtener coordenadas para {ciudad}")
    return (location.latitude, location.longitude)

def calcular_distancia(origen, destino):
    coords_origen = obtener_coordenadas(origen)
    coords_destino = obtener_coordenadas(destino)
    distancia_km = geopy.distance.distance(coords_origen, coords_destino).km
    distancia_millas = geopy.distance.distance(coords_origen, coords_destino).miles
    return distancia_km, distancia_millas

def duracion_viaje(distancia_km, medio_transporte):
    velocidades = {
        'auto': 100,
        'bus': 80,
        'bicicleta': 15,
        'a pie': 5
    }
    velocidad = velocidades.get(medio_transporte.lower(), 0)
    if velocidad == 0:
        return None
    horas = distancia_km / velocidad
    return horas

def main():
    while True:
        print("Ingrese la letra 's' para salir.")
        origen = input("Ciudad de Origen: ")
        if origen.lower() == 's':
            break
        destino = input("Ciudad de Destino: ")
        if destino.lower() == 's':
            break

        medio_transporte = input("Medio de transporte (auto, bus, bicicleta, a pie): ").lower()
        if medio_transporte == 's':
            break

        try:
            distancia_km, distancia_millas = calcular_distancia(origen, destino)
            duracion = duracion_viaje(distancia_km, medio_transporte)
            if duracion is None:
                print(f"Medio de transporte '{medio_transporte}' no reconocido.")
                continue

            print(f"Distancia entre {origen} y {destino}:")
            print(f"{distancia_km:.2f} km")
            print(f"{distancia_millas:.2f} millas")
            print(f"Duración del viaje en {medio_transporte}: {duracion:.2f} horas")
            print(f"Narrativa del viaje: El viaje desde {origen} hasta {destino} en {medio_transporte} dura aproximadamente {duracion:.2f} horas.")
        except Exception as e:
            print(f"Error al calcular la distancia: {e}")

if __name__ == "__main__":
    main()
