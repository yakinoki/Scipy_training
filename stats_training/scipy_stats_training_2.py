import numpy as np
from scipy import stats

# データ生成
np.random.seed(0)
sample1 = np.random.normal(5, 2, 100)  # 母集団1からのサンプルデータ
sample2 = np.random.normal(7, 2, 100)  # 母集団2からのサンプルデータ

# 帰無仮説と対立仮説の設定
# 帰無仮説: 2つの母集団の平均に差がない（μ1 = μ2）
# 対立仮説: 2つの母集団の平均に差がある（μ1 ≠ μ2）

# t検定を実行
t_stat, p_value = stats.ttest_ind(sample1, sample2)

# 有意水準を設定
alpha = 0.05

# p値と有意水準を比較し、帰無仮説を棄却するか判定
if p_value < alpha:
    print("帰無仮説を棄却します。2つの母集団の平均に差があります。")
else:
    print("帰無仮説を棄却しません。2つの母集団の平均に差がないと結論します。")
