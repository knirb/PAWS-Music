import json
import pytest
from helloworld.application import app


@pytest.fixture
def client():
    return app.test_client()



