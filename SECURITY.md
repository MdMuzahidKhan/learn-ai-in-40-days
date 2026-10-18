# Public repository safety

This is a learning project, not production-ready authentication or a place to
store real user/company data.

## Credentials

- Configure `SECRET_KEY`, `DEMO_USERNAME`, and `DEMO_PASSWORD` privately before
  starting the Day 7 API. See [setup](day07/README.md#authentication).
- Use a cryptographically random signing key of at least 32 bytes and a unique
  password. There are no built-in secret defaults.
- The only committed environment template, [.env.example](.env.example), has
  blank values. Never put actual credentials into it. Copy it to an ignored local
  `.env` for VS Code debugging, or set environment variables in your terminal.
- The browser must never contain a signing key, preset password, or service
  token. Enter your chosen username and password at login.
- Tests create temporary random credentials. They do not need deployment secrets.

## If an old credential may have been used online

1. Treat previously published keys and passwords as compromised.
2. Replace them in every deployed app or account where they were used. Use your
   hosting service's secret settings; do not paste secrets into chat or issues.
3. Restart/redeploy to load the replacements. Rotating the JWT signing key
   invalidates tokens signed with the old key.
4. Review access logs if a real service was exposed.

Deleting a file or rewriting Git history cannot revoke a credential or erase
copies someone already downloaded. Existing clones, forks, pull-request refs,
and cached commit views can retain old content. If sensitive cached GitHub views
remain after a history cleanup, follow GitHub's sensitive-data removal process
and contact GitHub Support as appropriate. Use a fresh clone after a history
rewrite; do not merge or push the old history back.

## What belongs in Git

**Keep:** source code, tests, learning notes, dependency manifests, shareable
configuration, SQL schema/seed scripts, and reviewed synthetic examples.

**Do not commit:** real passwords/tokens/private keys, personal/company documents,
virtual environments, installed dependencies, caches, coverage reports, local
databases, runtime agent memory, logs, or redundant local backups.

The [.gitignore](.gitignore) contains safeguards for common local files, but it is
not a secret scanner. It also does not untrack files already committed. Before
each push, review every staged diff in VS Code Source Control, check the remote
owner, and run the affected tests. Never force-add ignored secret files.

For public bug reports, use dummy data and redact credentials, tokens, personal
details, and request headers. Never upload a real `.env` as an attachment.