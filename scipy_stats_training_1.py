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

#正規分布を定義。
rv = stats.norm(2, 0.5)
print(rv.mean())
print(rv.var())

print("確率密度関数の１における値は"+str(rv.pdf(1)))
print("確率密度関数が2以下の値をとる確率は"+str(rv.cdf(2)))
print("上側30%点は"+str(rv.isf(0.3)))
print("80%区間は"+str(rv.interval(0.8)))

#指数分布を定義。
rv = stats.expon(scale=1/2)
print(rv.mean())
print(rv.var())

#自由度10のカイ二乗分布を定義。
rv = stats.chi2(10)
print(rv.rvs(5))
#歪度
print(stats.skew(rv.rvs(5)))
#尖度(3を引かない)
print(stats.kurtosis(rv.rvs(5), fisher=False))


#自由度10のt分布を定義。
rv = stats.t(10)
print(rv.rvs(5))
#母平均150に対しt検定統計量とp値を返す。
sample = [145, 150, 155, 153]
t, p = stats.ttest_1samp(sample, 150)
print(t, p)

#自由度3,10のt分布を定義。
rv = stats.f(3,10)
print(rv.rvs(5))