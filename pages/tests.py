from django.test import Client

from django.urls import reverse


def test_home_page_exists(client: Client):
    response = client.get(reverse('pages:home'))

    assert response.status_code == 200

def test_about_page_exists(client: Client):
    response = client.get(reverse('pages:about'))

    assert response.status_code == 200
