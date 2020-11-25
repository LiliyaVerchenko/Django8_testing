from django.urls import reverse
import pytest
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from students.models import Course

@pytest.mark.django_db
def test_get_course(api_client, course_factory):
    url = reverse("courses-list")
    course = course_factory(name="Экономика")
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json[0]["name"] == course.name


@pytest.mark.django_db
def test_courses_list(api_client, course_factory):
    url = reverse("courses-list")
    quantity = 5
    courses = course_factory(_quantity=quantity)
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == quantity


@pytest.mark.django_db
def test_filter_id(api_client, course_factory):
    url = reverse("courses-list")
    quantity = 5
    course = course_factory(_quantity=quantity)
    resp = api_client.get(url, {"id": course[4].id})
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json[0]["id"] == course[4].id


@pytest.mark.django_db
def test_create(api_client):
    url = reverse("courses-list")
    course_name = "Информатика"
    data = {"name": course_name}
    resp = api_client.post(url, data)
    assert resp.status_code == HTTP_201_CREATED
    resp_json = resp.json()
    assert course_name == resp_json["name"]


@pytest.mark.django_db
def test_update(api_client, course_factory):
    course = course_factory(name="Социолгия")
    url = reverse("courses-detail", args=(course.id, ))
    update_name = "Политология"
    data = {"name": update_name}
    resp = api_client.patch(url, data)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert update_name == resp_json["name"]


@pytest.mark.django_db
def test_delete(api_client, course_factory):
    course = course_factory(name="Физика")
    url = reverse("courses-detail", args=(course.id, ))
    resp = api_client.delete(url)
    assert resp.status_code == HTTP_204_NO_CONTENT
    assert len(Course.objects.filter(name="Физика")) == 0
