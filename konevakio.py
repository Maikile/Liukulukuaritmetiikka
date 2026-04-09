import numpy as np
import mpmath
import matplotlib.pyplot as plt

#IEEE 754 -standardin mantissan bittimäärät eri tarkkuuksilla:
#Half      = 10 bittiä
#Single    = 23 bittiä
#Double    = 52 bittiä
#Quadruple = 112 bittiä
#Octuple   = 236 bittiä

Precisions = {
    "Half (16 bittiä)": {"sign": 1, "bits": 16, "exp": 5, "mantissa": 10, "np": np.float16},
    "Single (32 bittiä)": {"sign": 1, "bits": 32, "exp": 8, "mantissa": 23, "np": np.float32},
    "Double (64 bittiä)": {"sign": 1, "bits": 64, "exp": 11, "mantissa": 52, "np": np.float64},
    "Quadruple (128 bittiä)": {"sign": 1, "bits": 128, "exp": 15, "mantissa": 112, "mp": 113},
    "Octuple (256 bittiä)": {"sign": 1, "bits": 256, "exp": 19, "mantissa": 236, "mp": 237}
}

epsilon_calculated = []
epsilon_theoretical = []
#Konevakion laskeminen
for key, value in Precisions.items():
    if "np" in value:
        precision = value["np"]
        epsilon = 1.0
        while precision(1.0 + epsilon / 2.0) > 1.0:
            epsilon = epsilon / 2.0
        print(f"{key}: epsilon = {epsilon:.5e}")
        calculatedEps = float(epsilon)
    else:
        mpmath.mp.prec = value["mp"]
        epsilon = mpmath.mpf(1.0)
        while (mpmath.mpf(1.0) + epsilon / mpmath.mpf(2.0)) > mpmath.mpf(1.0):
            epsilon = epsilon / mpmath.mpf(2.0)
        print(f"{key}: epsilon = {epsilon:.5e}")
        calculatedEps = float(epsilon)

    theoreticalEps = 2 ** -value["mantissa"]
    epsilon_calculated.append(calculatedEps)
    epsilon_theoretical.append(theoreticalEps)

#Kuvaajan piirtäminen
labels = list(Precisions.keys())
x = [0,1,2,3,4]

fig, ax = plt.subplots(figsize =(10,7))

ax.plot(x,epsilon_calculated, marker="s", label="Kokeellinen konevakio", markersize=7, color = "red")
ax.plot(x,epsilon_theoretical, marker="o", linestyle="--", label = "Teoreettinen konevakio", color = "blue")

ax.set_yscale("log")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_xlabel("Liukulukuformaatti")
ax.set_ylabel("Konevakio")
ax.set_title("Konevakio eri bittitarkkuuksilla")
ax.legend()
ax.grid()


plt.show()