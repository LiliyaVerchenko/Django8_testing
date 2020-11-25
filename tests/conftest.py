import pytest
from rest_framework.test import APIClient
from model_bakery import baker

@pytest.fixture()
def api_client():
    """Фикстура для клиента API."""
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(**kwargs):
        course = baker.make("students.Course", **kwargs)
        return course
    return factory


@pytest.fixture
def student_factory():
    def factory(**kwargs):
        student = baker.make("students.Student", **kwargs)
        return student
    return factory

