import numpy as np
import matplotlib.pyplot as plt

# Generador de números aleatorios con una semilla fija
rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)

# Crear el histograma
plt.hist(matematicas, bins=10, edgecolor='black')

# Personalizar el histograma
plt.title('Distribución de las calificaciones de Matemáticas')
plt.xlabel('Calificaciones')
plt.ylabel('Número de estudiantes')

# Mostrar el histograma
plt.show()
