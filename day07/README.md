# Day 7 Book API

A small FastAPI book API used throughout the training journal.

## What it does
- Logs in a demo user and returns a bearer token.
- Lists books, with optional author filtering.
- Returns a simple inventory summary for the current book list.
- Returns a single book by id.
- Creates, updates, and deletes books for authenticated users.

## Authentication
There are no built-in login credentials or signing keys. Before starting the API,
set these environment variables privately:

| Variable | Purpose |
| --- | --- |
| `SECRET_KEY` | Random JWT signing key, at least 32 bytes; never share it. |
| `DEMO_USERNAME` | Your chosen local demo username. |
| `DEMO_PASSWORD` | A new, unique demo password, not one used by another account. |

Missing or blank values, or a signing key shorter than 32 bytes, stop startup.
The signing algorithm and token expiration duration are public configuration,
not secrets.

### Start locally from PowerShell

From the repository root, after activating your Python environment:

```powershell
python -m pip install -r day07/requirements.txt
$env:SECRET_KEY = python -c "import secrets; print(secrets.token_urlsafe(48))"
$env:DEMO_USERNAME = Read-Host "Choose a local demo username"
$env:DEMO_PASSWORD = [System.Net.NetworkCredential]::new('', (Read-Host "Choose a new demo password" -AsSecureString)).Password
python -m uvicorn app:app --app-dir day07 --host 127.0.0.1 --port 8000 --reload
```

The key is generated locally and assigned without printing it. The password
prompt hides your input. These variables exist only in that terminal session
and processes started from it; do not print or commit their contents. Record your
chosen login privately. Use those values with `POST /login` or enter them in the
Day 14 frontend, whose login fields now start empty.

For the VS Code debugger instead, open the repository root, select your Python
environment, copy [the blank template](../.env.example) to a local `.env`, fill in
fresh values privately, and select **Debug FastAPI Day07**. The debugger reads
that ignored file. Ordinary Python/uvicorn commands do **not** automatically load
it; use the PowerShell environment setup above for terminal launches.

The response returns an `access_token` and `token_type` of `bearer`.

### Security boundaries

This remains a single-user learning demo, not production authentication. For a
real deployment, use a proper user store/password hashing or an identity
provider, HTTPS, restricted CORS, rate limiting, and a secret manager. Store a
stable random signing key in the deployment's secret settings, not the source.
Changing the signing key invalidates existing tokens. Never reuse credentials
from an older revision of this repository. See [publication safety](../SECURITY.md).

## Endpoints

### `POST /login`
Authenticates the demo user.

### `GET /books`
Returns all books.

Optional query parameter:
- `author`: filters books by author substring, case-insensitively.

Examples:
- `GET /books`
- `GET /books?author=john`

### `GET /books/stats`
Returns a summary of the current inventory.

Response fields:
- `total_books`
- `physical_books`
- `ebook_books`

### `GET /books/{book_id}`
Returns one book by numeric id.

### `POST /books`
Creates a new book.

Requires a bearer token in `Authorization`.

### `PUT /books/{book_id}`
Updates an existing book.

Requires a bearer token in `Authorization`.

### `DELETE /books/{book_id}`
Deletes a book.

Requires a bearer token in `Authorization`.

## Data model
Each book has these fields:
- `id`
- `title`
- `author`
- `year`
- `book_type`
- `extra_info`

## Behavior notes
- The repository is in memory, so data resets when the process restarts.
- Duplicate titles are rejected on create, case-insensitively.
- Author filtering does not require an exact match.
- The stats endpoint is derived from the same in-memory book list, so it reflects the current state immediately.

## Verification
From the repository root:

```powershell
python -m pytest -q day07/tests
```

Tests generate disposable random credentials and do not require your real
environment values or a local `.env` file. They cover book API behavior,
missing/blank secret settings, short signing keys, valid login, and rejected
invalid/expired tokens. The GitLab training pipeline runs the same test folder.
