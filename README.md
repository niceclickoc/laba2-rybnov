
## 2.9. `README.md`
```markdown
# ci-cd-calculator

Небольшой учебный проект калькулятора с тестами и CI/CD на GitHub Actions.

## Запуск тестов локально
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
pytest
