import math

def log_loss(y_true: list, y_pred: list, eps: float = 1e-15) -> list:
    ans = []
    for y,p in zip(y_true,y_pred):
        p = min(1-eps,max(eps,p))
        l = -(y*math.log(p)+(1-y)*math.log(1-p))
        ans.append(float(l))
        
    return ans