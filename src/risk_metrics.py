import numpy as np

def VaR(L: np.ndarray, alpha: float) -> float:
       return np.quantile(L, q=alpha)

def CVaR(L: np.ndarray, alpha: float) -> float:
       VaR = np.quantile(L, q=alpha)
       filtered = L[L >= VaR]
       return np.mean(filtered)

       