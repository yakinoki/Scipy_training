from scipy import stats

p = 0.4

#ベルヌーイ関数を定義。
rv = stats.bernoulli(p)

print("0をとる確率は"+str(rv.pmf(0))+"です。")

#累積密度関数はrv.cdfにより定義される。

print("平均値は"+str(rv.mean())+",分散は"+str(rv.var())+"です。")