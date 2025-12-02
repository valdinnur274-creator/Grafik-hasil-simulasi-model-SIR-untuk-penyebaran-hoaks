# --- IMPORT LIBRARY ---
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# --- PARAMETER UMUM ---
gamma = 0.2        # laju klarifikasi (tetap)
N = 1000           # total populasi

# --- KONDISI AWAL ---
S0 = 900
I0 = 100
R0 = 0
y0 = [S0, I0, R0]

# --- RENTANG NILAI BETA UNTUK UJI SENSITIVITAS ---
beta_values = [0.2, 0.4, 0.6]

# --- WAKTU SIMULASI ---
t = np.linspace(0, 50, 500)

# --- MODEL SIR ---
def sir_model(y, t, beta, gamma, N):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

# --- PLOT ---
plt.figure(figsize=(10,6))

for beta in beta_values:
    sol = odeint(sir_model, y0, t, args=(beta, gamma, N))
    I = sol[:, 1]
    plt.plot(t, I, label=f"β = {beta}")

plt.xlabel("Waktu (t)")
plt.ylabel("Jumlah Penyebar I(t)")
plt.title("Sensitivitas Model SIR terhadap Variasi β (Beta)")
plt.grid(True)
plt.legend()
plt.show()

# --- PARAMETER UMUM ---
beta = 0.4        # laju penyebaran tetap
N = 1000          # total populasi

# --- KONDISI AWAL ---
S0 = 900
I0 = 100
R0 = 0
y0 = [S0, I0, R0]

# --- RENTANG NILAI GAMMA UNTUK UJI SENSITIVITAS ---
gamma_values = [0.1, 0.2, 0.3]

# --- WAKTU SIMULASI ---
t = np.linspace(0, 50, 500)

# --- MODEL SIR ---
def sir_model(y, t, beta, gamma, N):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

# --- PLOT ---
plt.figure(figsize=(10,6))

for gamma in gamma_values:
    sol = odeint(sir_model, y0, t, args=(beta, gamma, N))
    I = sol[:, 1]
    plt.plot(t, I, label=f"γ = {gamma}")

plt.xlabel("Waktu (t)")
plt.ylabel("Jumlah Penyebar I(t)")
plt.title("Sensitivitas Model SIR terhadap Variasi γ (Gamma)")
plt.grid(True)
plt.legend()
plt.show()
