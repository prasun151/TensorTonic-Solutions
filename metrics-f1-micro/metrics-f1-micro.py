def f1_micro(y_true, y_pred) -> float:
    
    assert len(y_true) == len(y_pred)

    TP = FP = FN = 0

    for t, p in zip(y_true, y_pred):
        if p == t:
            TP += 1
        else:
            FP += 1
            FN += 1

    denom = 2 * TP + FP + FN
    return 0.0 if denom == 0 else 2 * TP / denom
