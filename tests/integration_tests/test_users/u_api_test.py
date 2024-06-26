import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "email,password,status_code",
    [
        ("kot@pes.com", "kotopes", 201),
        ("kot@pes.com", "kot0pes", 409),
        ("pes@kot.com", "pesokot", 201),
        ("abcde", "pesokot", 422),
    ],
)
async def test_register(email, password, status_code, ac: AsyncClient):
    response = await ac.post(
        "/v1/users/register",
        json={
            "email": email,
            "password": password,
        },
    )

    assert response.status_code == status_code


@pytest.mark.parametrize(
    "email,password,status_code",
    [
        ("test@test.com", "test", 200),
        ("artem@example.com", "artem", 200),
        ("wrong@person.com", "artem", 401),
    ],
)
async def test_login(email, password, status_code, ac: AsyncClient):
    response = await ac.post(
        "/v1/users/login",
        json={
            "email": email,
            "password": password,
        },
    )

    assert response.status_code == status_code
