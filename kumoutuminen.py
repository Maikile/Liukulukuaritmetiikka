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

exponents = [10,20,40,80,120,160,200]

#epästabiili: sqrt(1 + x) - sqrt(x), stabiili: 1/(sqrt(1 + x) + sqrt(x))
for key, value in Precisions.items():
    print()
    print(f"{key}:")
    print(f"{'x':<10} {'Epästabiili':<20} {'Stabiili'}")
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

            