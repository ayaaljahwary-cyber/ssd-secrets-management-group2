# ssd-secrets-management-group2

## Group Members
| Name | Student ID |
|---|---|
| Aya Said Suliman Aljahwary | 2316751 |
| Tuqa TODO-LAST-NAME (GitHub: toqa374) | TODO-ID |

## Topic
**Secrets Management** (CYSE303 - Secure Software Development)

## Summary of the Vulnerability
Developers sometimes hardcode secrets (API keys, database passwords, cloud credentials) in source code or commit `.env` files to Git. Anyone who can read the repository, including its commit history, can reuse these secrets. Deleting the file later does not help, because the secret stays in Git history. The real fix is to keep secrets out of the code, block them before commit, and rotate any secret that leaked (CWE-798).

## Tools and Technologies
- Python 3 and Flask (demo app)
- python-dotenv (load secrets from environment)
- detect-secrets by Yelp (scanning, used as the "attack" and for verification)
- pre-commit (hook that blocks commits containing secrets)
- Git and GitHub (history and push protection)

All secrets in this repo are FAKE demo values.

## Repository Structure
    slides/            presentation
    vulnerable-code/   insecure app (hardcoded secrets + committed .env)
    fixed-code/        secure app (environment variables)
    demo-video/        backup demo video
    references.md      sources

## How to Run

Install requirements:

    pip3 install flask python-dotenv detect-secrets pre-commit

### Vulnerable version (port 5000)

    python3 vulnerable-code/app.py

Open http://127.0.0.1:5000/status

### Attack: scan for secrets

    detect-secrets scan vulnerable-code --all-files
    git log -p --all -S "DB_PASSWORD" --oneline

### Fixed version (port 5001)

Secrets come from the environment:

    API_KEY=env_demo_key_1234 DB_PASSWORD=env_demo_pass_5678 python3 fixed-code/app.py

Open http://127.0.0.1:5001/status

### Re-test

    detect-secrets scan fixed-code --all-files

Expected result: `"results": {}`

### Prevention: pre-commit hook

    pre-commit install

Any commit that adds a secret is now rejected.

## Backup Demo Video
TODO: add link or file in demo-video/
