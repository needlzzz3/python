import pytest
from fixture.app import App



@pytest.fixture(scope = "session")
def app(request):
    fixture = App()
    request.addfinalizer(fixture.destroy)
    return fixture