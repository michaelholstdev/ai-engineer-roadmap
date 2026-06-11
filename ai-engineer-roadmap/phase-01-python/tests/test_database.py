import pytest

from ai_roadmap.database import DATABASE_URL_ENV, get_database_url


def test_get_database_url_returns_configured_url(monkeypatch):
    api_key = "Here-is-some-database-url"
    monkeypatch.setenv(DATABASE_URL_ENV, api_key)
    assert get_database_url() == api_key


def test_get_database_url_failed_for_non_configured_url(monkeypatch):
    monkeypatch.delenv(DATABASE_URL_ENV, raising=False)

    with pytest.raises(RuntimeError):
        get_database_url()


def test_get_database_url_raises_for_blank_url(monkeypatch):
    monkeypatch.setenv(DATABASE_URL_ENV, "   ")

    with pytest.raises(RuntimeError):
        get_database_url()
