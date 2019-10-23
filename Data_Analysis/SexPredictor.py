from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier


clf = tree.DecisionTreeClassifier()
neigh = KNeighborsClassifier(n_neighbors=3)
lg = LogisticRegression()
gnb = GaussianNB()
frst = RandomForestClassifier(n_estimators=2)

#[height , weight , shoe size]
X = [[181, 80 , 44] , [177, 70 , 43] ,[160 , 90 , 41] , [190 , 75 ,45],
    [162 , 609 ,38], [181 , 85,43] , [171,75, 42], [190, 90, 47], [154, 54, 37]
    , [174, 69, 40], [179 , 78, 42], [163, 42, 37], [191, 72, 42]]

Y = ['male','female','male','female','male','male',
    'female','male','female','male','male','female','male']


typ = lg.fit(X,Y)

prediction = typ.predict([[161, 75, 44]])

print(prediction)