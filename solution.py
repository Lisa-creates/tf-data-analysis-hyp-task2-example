import pandas as pd
import numpy as np
from scipy import stats

chat_id = 854074776 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    res = stats.anderson_ksamp([x,y])
    return res.pvalue < 0.03 # Ваш ответ, True или False
