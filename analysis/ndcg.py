import numpy as np

# pagerank の順位が高いほど高スコアを付与 (その変化を見る)

def ndcg(rel_true, rel_pred, p=None, form="linear"):
    """ Returns normalized Discounted Cumulative Gain
    Args:
        rel_true (1-D Array): relevance lists for particular user, (n_songs,)
        rel_pred (1-D Array): predicted relevance lists, (n_pred,)
        p (int): particular rank position
        form (string): two types of nDCG formula, 'linear' or 'exponential'
    Returns:
        ndcg (float): normalized discounted cumulative gain score [0, 1]
    """
    rel_true = np.sort(rel_true)[::-1]
    p = min(len(rel_true), len(rel_pred))
    discount = 1 / (np.log2(np.arange(p) + 2))

    if form == "linear":
        idcg = np.sum(rel_true[:p] * discount)
        dcg = np.sum(rel_pred[:p] * discount)
    elif form == "exponential" or form == "exp":
        idcg = np.sum([2**x - 1 for x in rel_true[:p]] * discount)
        dcg = np.sum([2**x - 1 for x in rel_pred[:p]] * discount)
    else:
        raise ValueError("Only supported for two formula, 'linear' or 'exp'")

    return dcg / idcg

def ndcg_tyama(pr_original, pr_sample, x):
    
    # 元グラフのPR値
    rel_true = list(pr_original.values())

    # サンプリンググラフの頂点ID
    sample_keys = list(pr_sample.keys())

    # サンプリンググラフの上位頂点の元グラフでのPR値　
    rel_pred = []
    for tmp_key in sample_keys:
        rel_pred.append(pr_original[tmp_key])
        
    # nDCG の適用範囲を指定して計算    
    N = len(rel_pred) # 元グラフの頂点数
    y = int(N*x) # nDCG の提供範囲
    
    return ndcg(rel_true, rel_pred, form="exp")
    
    