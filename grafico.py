import numpy as np
import matplotlib.pyplot as plt

a = 1/4
b = 1/4
c = 1/2
d = 3/7
e = 5/21
f = 1/3
g = 6/13
h = 5/13
i = 2/13

# Inizializziamo la matrice A
A = np.array([[a, d, g],\
              [b, e, h],\
              [c, f, i]])

# Creazione dello stato iniziale random
x0 = np.random.rand(3, 1)

# Normalizzazione del vettore x0
x0 = x0 / np.sum(x0)

# Numero di passi per garantire la convergenza
npassi = 20

# Lista per memorizzare l'evoluzione di x0, trasformo l'array bidimensionale in unidimensionale.
x0_history = [x0.flatten()]

# Calcolo dello stato
for _ in range(npassi):
    x0 = A @ x0
    x0_history.append(x0.flatten())     #Inserisco nella lista x0_history lo storico di x0

# Converto la lista in un array numpy
x0_history = np.array(x0_history)

# Plot dell'evoluzione di x0
plt.figure()
for i in range(x0_history.shape[1]):        #Itero da 0 fino al numero di colonne di x0_history
    plt.plot(x0_history[:, i], label=f'x{i+1}')     #Estraggo la i-esima colonna
plt.xlabel('Passi')
plt.ylabel('Valore di x0')
plt.title('Evoluzione di x0')
plt.legend()
plt.grid(True)
print("Stato x0 dopo 20 passi: ", x0)
plt.show()
