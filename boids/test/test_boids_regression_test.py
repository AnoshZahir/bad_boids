from ..boids import Boids
from nose.tools import assert_almost_equal
import os
import yaml
        
def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','fixture.yml')))
    boid_data=regression_data["before"]
    boids = Boids()
    boids.update_boids(boid_data[0:2], boid_data[2:4])
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=1)