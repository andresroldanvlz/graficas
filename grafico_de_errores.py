import numpy as np
import matplotlib.pyplot as plt

# Generador de números aleatorios con una semilla fija
rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Calcular los promedios
promedio_matematicas = np.mean(matematicas)
promedio_ciencias = np.mean(ciencias)
promedio_literatura = np.mean(literatura)

# Datos de errores para el gráfico de barras de error
errores_matematicas = rng.uniform(2, 5, 20)
errores_ciencias = rng.uniform(1, 4, 20)
errores_literatura = rng.uniform(3, 6, 20)

# Calcular los errores promedio
error_matematicas = [np.mean(errores_matematicas), np.mean(errores_matematicas)]
error_ciencias = [np.mean(errores_ciencias), np.mean(errores_ciencias)]
error_literatura = [np.mean(errores_literatura), np.mean(errores_literatura)]

# Crear el gráfico de barras de error
materias = ['Matemáticas', 'Ciencias', 'Literatura']
promedios = [promedio_matematicas, promedio_ciencias, promedio_literatura]
errores = [error_matematicas, error_ciencias, error_literatura]

plt.bar(materias, promedios, yerr=errores, capsize=5)

# Personalizar el gráfico
plt.title('Calificaciones promedio y errores en Matemáticas, Ciencias y Literatura')
plt.xlabel('Materias')
plt.ylabel('Calificaciones Promedio')
plt.legend(['Matemáticas', 'Ciencias', 'Literatura'])

# Mostrar el gráfico
plt.show()
