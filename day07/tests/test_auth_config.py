"""Check auth configuration in fresh processes, never using real credentials."""

import os
from pathlib import Path
import secrets
import subprocess
import sys

import pytest


API_DIR = Path(__file__).resolve().parents[1]
AUTH_VARIABLES = ("SECRET_KEY", "DEMO_USERNAME", "DEMO_PASSWORD")


def run_auth(code, overrides=None):
    environment = os.environ.copy()
    # Always overwrite inherited credentials with disposable test-only values.
    environment.update(
        SECRET_KEY=secrets.token_urlsafe(48),
        DEMO_USERNAME="test-" + secrets.token_hex(8),
        DEMO_PASSWORD=secrets.token_urlsafe(32),
    )
    for name, value in (overrides or {}).items():
        if value is None:
            environment.pop(name, None)
        else:
            environment[name] = value
    return subprocess.run(
        [sys.executable, "-B", "-c", code],
        cwd=API_DIR,
        env=environment,
        capture_output=True,
        text=True,
        timeout=20,
    )


@pytest.mark.parametrize("name", AUTH_VARIABLES)
@pytest.mark.parametrize("value", [None, "", "   "])
def test_application_rejects_missing_or_blank_auth_configuration(name, value):
    result = run_auth("import app", {name: value})
    assert result.returncode != 0
    assert name in result.stderr
    assert "must be set to a non-empty value" in result.stderr


def test_application_rejects_short_signing_key_without_echoing_it():
    short_key = secrets.token_hex(4)
    result = run_auth("import app", {"SECRET_KEY": short_key})
    assert result.returncode != 0
    assert "SECRET_KEY must contain at least 32 bytes" in result.stderr
    assert short_key not in result.stderr


def test_configured_auth_login_tokens_and_rejection_paths():
    result = run_auth(
        """
import os
from datetime import datetime, timedelta, timezone
import jwt
from fastapi import HTTPException
import auth

username = os.environ['DEMO_USERNAME']
password = os.environ['DEMO_PASSWORD']
assert auth.verify_login(username, password)
assert not auth.verify_login(username, password + '!')
assert not auth.verify_login(username + '!', password)
assert auth.get_current_user(auth.create_access_token(username)) == username

expired = jwt.encode(
    {'sub': username, 'exp': datetime.now(timezone.utc) - timedelta(minutes=1)},
    os.environ['SECRET_KEY'], algorithm='HS256',
)
wrong_key = jwt.encode({'sub': username}, 'x' * 64, algorithm='HS256')
missing_subject = jwt.encode({}, os.environ['SECRET_KEY'], algorithm='HS256')
for token in ('not-a-token', expired, wrong_key, missing_subject):
    try:
        auth.get_current_user(token)
    except HTTPException as error:
        assert error.status_code == 401
    else:
        raise AssertionError('Invalid token was accepted')
""",
        {"DEMO_USERNAME": "test-\u00e9", "DEMO_PASSWORD": secrets.token_urlsafe(32) + "\u00e9"},
    )
    assert result.returncode == 0, result.stderr