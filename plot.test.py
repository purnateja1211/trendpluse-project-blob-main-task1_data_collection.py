import seaborn as sns
tit=sns.load_dataset("titanic")
sns.pairplot(data=tit,
             kind="scatter",
             diag_kind="hist",
             hue="sex",height=30,
             plot_kws={'alpha':0.6,'s':30,'linewidth':1},
             diag_kws=dict(bins=5,fill=False))