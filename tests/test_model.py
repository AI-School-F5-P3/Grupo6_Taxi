import pytest
import time

from model import Taximetro

@pytest.fixture
def taximeter():
	return Taximetro()

def test_start(taximeter):
	taximeter.start()
	assert taximeter.start_road == True

def test_trip_start_to_finish(taximeter):
	taximeter.start()
	time.sleep(4)
	taximeter.finish_road()
	exp_fare = 4 * taximeter.fare_stop
	assert taximeter.fare_total == exp_fare,\
		f"El total esperado es: {exp_fare}, no {taximeter.fare_total}"

def test_trip_movement(taximeter):
	taximeter.start()
	taximeter.continue_road()
	time.sleep(10)
	taximeter.stop()
	time.sleep(4)
	taximeter.finish_road()
	exp_fare = (10 * taximeter.fare_movement) + (4 * taximeter.fare_stop)
	assert taximeter.fare_total == exp_fare, \
		f"El total esperado es: {exp_fare}, no {taximeter.fare_total}"
