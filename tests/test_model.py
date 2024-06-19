import pytest

from model import Taximetro

@pytest.fixture
def my_taximetro():
	return Taximetro()

def test_start(my_taximetro):
	my_taximetro.start()
	assert my_taximetro.start_road == True