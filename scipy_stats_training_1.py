from scipy import stats
from scipy.special import comb

p = 0.4

#ベルヌーイ関数を定義。
rv = stats.bernoulli(p)

print("パラメータ"+str(p)+"のベルヌーイ分布に従う確率変数が0をとる確率は"+str(rv.pmf(0))+"です。")

#累積密度関数はrv.cdfにより定義される。

print("平均値は"+str(rv.mean())+",分散は"+str(rv.var())+"です。")


print("5個のものから2つを選ぶ方法は"+str(comb(5,2))+"通りあります。")

print("幾何分布とは，確率 p で表が出るコインを何回も投げたときに，初めて表が出るのは何回目になるかの分布を表す，離散型確率変数です。")
p = 0.7
rv = stats.geom(p)
print("パラメータ"+str(p)+"の幾何分布に従う確率変数が2をとる確率は"+str(round(rv.pmf(2),4))+"です。")

lam = 0.1
rv = stats.poisson(lam)
print("パラメータ"+str(lam)+"のポアソン分布に従う確率変数が3をとる確率は"+str(round(rv.pmf(3),5))+"です。")