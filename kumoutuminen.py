import numpy as np
import mpmath
import warnings

warnings.filterwarnings("ignore")

Precisions = {
    "Half (16 bittiä)": {"sign": 1, "bits": 16, "exp": 5, "mantissa": 10, "np": np.float16},
    "Single (32 bittiä)": {"sign": 1, "bits": 32, "exp": 8, "mantissa": 23, "np": np.float32},
    "Double (64 bittiä)": {"sign": 1, "bits": 64, "exp": 11, "mantissa": 52, "np": np.float64},
    "Quadruple (128 bittiä)": {"sign": 1, "bits": 128, "exp": 15, "mantissa": 112, "mp": 113},
    "Octuple (256 bittiä)": {"sign": 1, "bits": 256, "exp": 19, "mantissa": 236, "mp": 237}
}

#Esimerkki 1: epävakaa: sqrt(1 + x) - sqrt(x), vakautettu: 1/(sqrt(1 + x) + sqrt(x))
exponents = [10,20,40,80,120,160,200]
print("Esimerkki 1: sqrt(1 + x) - sqrt(x)")

for key, value in Precisions.items():
    print()
    print(f"{key}:")
    print(f"{'x':<10} {'Epävakaa':<20} {'Vakautettu'}")
    for i in exponents:
        if "np" in value:
            precision = value["np"]
            x = precision(2.0) ** precision(i)
            if np.isfinite(x) == False:
                print(f"2^{i:<8} ylivuoto")
                continue
            unstable = np.sqrt(1.0 + x) - np.sqrt(x)
            stable = 1.0/(np.sqrt(1.0 + x) + np.sqrt(x))
            print(f"2^{i:<8} {unstable:<20.6e} {stable:.6e}")
        
        else:
            mpmath.mp.prec = value["mp"]
            x = mpmath.mpf(2.0) ** i
            unstable = mpmath.sqrt(1.0 + x) - mpmath.sqrt(x)
            stable = 1.0/(mpmath.sqrt(1.0 + x) + mpmath.sqrt(x))
            print(f"2^{i:<8} {unstable:<20.6e} {stable:.6e}")

print()
#Esimerkki 2: epästabiili: a^-b^2, stabiilimpi: (a-b)(a+b)
print("Esimerkki 2: a^2 - b^2  (a = x + 0.5, b = x)")

exponents = [2,4,6,8,10]

for key, value in Precisions.items():
    print()
    print(f"{key}:")
    print(f"{'x':<10} {'Epävakaa':<20} {'Vakautettu':<20} {'Oikea tulos'}")
    for i in exponents:
        if "np" in value:
            precision = value["np"]
            x = 10**i
            a = precision(x + 0.5)
            b = precision(x)
            if np.isfinite(a**2) == False:
                print(f"2^{i:<8} ylivuoto")
                continue
            unstable = a**2 - b**2
            stable = (a-b)*(a+b)
            correct_ans = x + 0.25
            print(f"10^{i:<7} {unstable:<20.2f} {stable:<20.2f} {correct_ans:.2f}")     
        else:
            mpmath.mp.prec = value["mp"]
            x = mpmath.mpf(10.0) ** i
            a = x + mpmath.mpf("0.5")
            b = x
            unstable = a**2 - b**2
            stable = (a-b)*(a+b)
            correct_ans = x + 0.25
            print(f"10^{i:<7} {unstable:<20.2f} {stable:<20.2f} {correct_ans:.2f}") 
            
