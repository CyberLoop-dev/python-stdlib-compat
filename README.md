<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:0f766e&height=170&section=header&text=python%20stdlib%20compat&fontSize=36&fontColor=ffffff&animation=twinkling" alt="Animated wave header"/></p>
<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=2800&pause=900&color=14B8A6&center=true&vCenter=true&width=760&lines=python%20stdlib%20compat%20%7C%20inspect%2C%20understand%2C%20improve" alt="Animated title"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/python-stdlib-compat?style=for-the-badge" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/python-stdlib-compat?style=for-the-badge" alt="Language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/python-stdlib-compat?style=for-the-badge" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/python-stdlib-compat?style=for-the-badge" alt="Last commit"/></p>
<p align="center"><img src="assets/mark.svg" alt="python-stdlib-compat project mark" width="520"/></p>

## 🧭 Overview

`python-stdlib-compat` scans Python source without importing or executing it. A curated rule set identifies selected standard-library modules and symbols added after your declared minimum Python version.

## ✨ Features

- 🧭 Checks imports against a chosen target version
- 🔍 Recognizes selected module and symbol introduction versions
- 🛡️ Parses source with `ast`; project code is never imported or executed
- 📄 Supports readable text and machine-readable JSON reports
- ⚙️ Skips common virtual-environment and cache folders

## 🧪 Demo

Run `python main.py sample --target 3.10`. The sample imports `tomllib`, which entered the standard library in Python 3.11. No hosted demo is published.

## 🚀 Quick Start

```bash
python main.py sample --target 3.10
python main.py ./src --target 3.11 --json
python -m unittest discover -s tests
```
The tool uses only the standard library. Python 3.10 or newer is recommended.

## 🧰 Tech Stack

- **Stack:** Python 3.10+ (standard library only)
- **Approach:** small, local-first tooling with clear output

## 🗂️ Folder Structure

```text
python-stdlib-compat/
├── assets/mark.svg
├── sample/app.py
├── tests/test_main.py
├── main.py
├── pyproject.toml
├── .gitignore
├── LICENSE
└── README.md
```

## 🛣️ Roadmap

- Expand the curated compatibility database with reviewed API-level rules
- Add SARIF output for code-scanning workflows

## 🤝 Contributing

Issues and focused pull requests are welcome. Explain the use case, keep changes small, and add tests for behavior changes. Run the project using the Quick Start instructions before submitting.

## 📄 License

Released under the [MIT License](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:0f172a&height=120&section=footer&animation=twinkling" alt="Animated wave footer"/></p>
