from models import __linear_regression_model_executor__ as Mot
from models import __random_forest_model_executor__ as Ran
from temp_destination.controller import testController as Con

if __name__ == '__main__':
    r = Ran.RandomForestRegression()
    Con.test1(r)











