# References

## Tools
- Yelp detect-secrets: https://github.com/Yelp/detect-secrets
- pre-commit framework: https://pre-commit.com
- Flask: https://flask.palletsprojects.com
- python-dotenv: https://github.com/theskumar/python-dotenv
- GitHub Secret Scanning and Push Protection: https://docs.github.com/en/code-security/secret-scanning

## Guidance
- OWASP Secrets Management Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
- CWE-798: Use of Hard-coded Credentials: https://cwe.mitre.org/data/definitions/798.html
- GitHub: Removing sensitive data from a repository: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository

## Real-world incidents (verify details before presenting)
- Uber 2016 breach: AWS credentials found in a GitHub repository (TODO: add a news/official source link)
- Toyota 2022: access key exposed in public GitHub code (TODO: add Toyota official statement link)

## Notes
- All secrets in this repository are fake demo values.
- Vulnerable app written by the group; the fix (environment variables, .gitignore, .env.example, pre-commit hook) is our own work.
- AI assistance (Claude) was used for guidance while building the demo.
