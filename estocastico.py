import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10*np.pi ,100)
c = np.cos(t)
s = np.sin(t)
plt.figure('cosseno', figsize=(10,6))
plt.plot(t, c)
plt.title('Gráfico do cosseno')
plt.xlabel('tempo [s]')
plt.ylabel('Amplitude')
plt.show()

plt.figure('seno', figsize=(10, 6))
plt.plot(t, s)
plt.title('Gráfico do Seno')
plt.xlabel('tempo [s]')
plt.ylabel('Amplitude')
plt.show()
