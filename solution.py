import pandas as pd
import numpy as np
import math
import scipy.stats as stats


chat_id =  917079889 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int,
             x_cnt: int,
             y_success: int,
             y_cnt: int) -> bool:
    alpha = 0.08
    control_proportion = x_success / x_cnt
    test_proportion = y_success / y_cnt
    p = (x_success + y_success) / (x_cnt + y_cnt)
    z = (test_proportion - control_proportion) / math.sqrt(p * (1 - p) * (1 / x_cnt + 1 / y_cnt))
    p_value = 1 - stats.norm.cdf(abs(z))
    reject_null_hypothesis = p_value < alpha
    return reject_null_hypothesis
