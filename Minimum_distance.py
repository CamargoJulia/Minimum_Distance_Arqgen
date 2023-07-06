import math

# Calcular a distância entre dois pontos 
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Lista dos pontos e suas respectivas coordenadas(x, y)
points = [
    (3, 11),  # A
    (6, 11),  # B
    (6, 14),  # C
    (10, 14),  # D
    (10, 8),  # E
    (6, 8),  # F
    (6, 6),  # G
    (7, 6),  # H
    (8, 4),  # I
    (4, 4),  # J
    (4, 2),  # K
    (7, 2),  # L
    (7, 0),  # M
    (0, 0),  # N
    (0, 3),  # O
    (3, 3)  # P
]

# Menor distância
min_distance = float('inf')

# Interar sobre todos os pares de pontos
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]
        
        # Calcular a distancia entre o par de pontos atual
        distance = calculate_distance(x1, y1, x2, y2)
        
        # Atualizar a distancia se for a menor encontrada
        if distance < min_distance:
            min_distance = distance

# Print a menor distância
print("A menor disTãncia entre as arestas é:", min_distance)