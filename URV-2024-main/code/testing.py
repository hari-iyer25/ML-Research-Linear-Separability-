#for testing lin_sep 

from lin_sep import lp_sphere
from lin_sep import lp_scipy
from ucimlrepo import fetch_ucirepo
import time
import unittest




#uci datasets
iris = fetch_ucirepo(id=53) #dimensionality 4
glass = fetch_ucirepo(id=42) #dimensionality 9
banknote = fetch_ucirepo(id=267) #dimensionality 4


#converting the datasets into tuples

iris_points = list(iris.data.original.itertuples(index=False, name=None))
glass_points = list(glass.data.original.itertuples(index=False, name=None))
banknote_points = list(banknote.data.original.itertuples(index=False, name=None))

iris_setosa_points = []
iris_virginica_points = []
iris_versicolor_points = []

for iris_point in iris_points:
    if iris_point[4] == "Iris-setosa":
        iris_setosa_points.append(iris_point[0:4])
    elif iris_point[4] == "Iris-virginica":
        iris_virginica_points.append(iris_point[0:4])
    elif iris_point[4] == "Iris-versicolor":
        iris_versicolor_points.append(iris_point[0:4])

glass_1_points = []
glass_2_points = []
glass_other_points = []



for glass_point in glass_points:
    if glass_point[9] == 1:
        glass_1_points.append(glass_point[0:9])
    elif glass_point[9] == 2:
        glass_2_points.append(glass_point[0:9])
    else:
        glass_other_points.append(glass_point[0:9])


banknote_0_points = []
banknote_1_points = []

for banknote_point in banknote_points:
    if banknote_point[4] == 0:
        banknote_0_points.append(banknote_point[0:4])
    elif banknote_point[4] == 1:
        banknote_1_points.append(banknote_point[0:4])

#unittests

class TestLinSep(unittest.TestCase):

    def setUp(self):
        self.startTime = time.time()
    def tearDown(self):
        t= time.time() - self.startTime
        print("runtime: " + str(t))

    def basicTestOne(self):
        self.assertFalse(lp_sphere.lin_sep([(1,1,1), (0,0,1), (1,0,0), (0,1,0)], [(0,1,1), (1,0,1),(0,0,0), (1,1,0)], 3))
    def basicTestTwo(self):
        self.assertTrue(lp_sphere.lin_sep([(0,0,0), (1,0,0), (0,1,0), (1,1,0)], [(0,0,1), (1,0,1), (0,1,1),(1,1,1)], 3))
    def basicTestThree(self):
        self.assertFalse(lp_sphere.lin_sep([(1,0,0),(0,1,0), (1,0,1), (0,1,1)], [(0,0,0),(1,1,0), (1,1,1), (0,0,1)], 3))
    def test2DSamePoints(self):
        self.assertFalse(lp_sphere.lin_sep([(1,1), (0,1)], [(1,1), (0,1)], 2))


    def testIris1(self):
        print("iris test 1")
        self.assertTrue(lp_sphere.lin_sep(iris_setosa_points, iris_virginica_points + iris_versicolor_points, 4))

    def testIris2(self):
        print("iris test 2")
        self.assertFalse(lp_sphere.lin_sep(iris_virginica_points, iris_setosa_points+ iris_versicolor_points, 4))
    
    def testGlass1(self):
        print("glass test 1")
        self.assertFalse(lp_sphere.lin_sep(glass_1_points, glass_2_points + glass_other_points, 9))

    def testGlass2(self):
        print("glass test 2")
        self.assertFalse(lp_sphere.lin_sep(glass_2_points, glass_1_points + glass_other_points, 9))

    def testBanknotes(self):
        print("banknotes test")
        self.assertFalse(lp_sphere.lin_sep(banknote_0_points, banknote_1_points, 4))

    



if __name__ == "__main__":
    unittest.main()
  