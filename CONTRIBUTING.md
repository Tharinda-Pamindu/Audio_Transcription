# 🤝 Contributing to Audio Transcription

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the Audio Transcription project.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Code Style](#code-style)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

---

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment. Be kind, constructive, and professional in all interactions.

---

## Getting Started

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Voice-Activity-Detector.git
   cd Voice-Activity-Detector
   ```
3. **Create a branch** for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

---

## Development Setup

### Prerequisites

- Python 3.8+
- FFmpeg installed and in PATH
- Git

### Environment Setup

```bash
# Create virtual environment
python -m venv .venv

# Activate it
.venv\Scripts\activate      # Windows
# source .venv/bin/activate  # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Run the development server
python app.py
```

The app will be available at `http://127.0.0.1:5000`.

---

## How to Contribute

### 🐛 Reporting Bugs

- Use the [GitHub Issues](https://github.com/Tharinda-Pamindu/Voice-Activity-Detector/issues) page
- Include a clear title and description
- Provide steps to reproduce the issue
- Include your OS, Python version, and GPU info (if applicable)
- Attach relevant logs or screenshots

### 💡 Suggesting Features

- Open an issue with the **Feature Request** label
- Describe the feature and why it would be useful
- Include mockups or examples if possible

### 🔧 Submitting Code

1. Ensure your code follows the [Code Style](#code-style) guidelines
2. Test your changes thoroughly
3. Update documentation if applicable
4. Submit a [Pull Request](#pull-request-process)

---

## Code Style

### Python (Backend)

- Follow **PEP 8** conventions
- Use **type hints** where applicable
- Add **docstrings** to functions and classes
- Keep functions focused and under 50 lines when possible

### HTML / CSS / JavaScript (Frontend)

- Use **2-space indentation** for HTML and CSS
- Use **camelCase** for JavaScript variables and functions
- Add comments for complex logic
- Maintain the Liquid Glass design language

### General

- Write descriptive variable and function names
- Remove unused imports and dead code
- Keep files focused on a single responsibility

---

## Commit Messages

Follow the **Conventional Commits** standard:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types

| Type       | Description                                      |
| ---------- | ------------------------------------------------ |
| `feat`     | New feature                                      |
| `fix`      | Bug fix                                          |
| `docs`     | Documentation changes                            |
| `style`    | Code style changes (formatting, no logic change) |
| `refactor` | Code refactoring                                 |
| `perf`     | Performance improvement                          |
| `test`     | Adding or updating tests                         |
| `chore`    | Build, tooling, or dependency changes            |

### Examples

```
feat(ui): add waveform visualization to audio player
fix(whisper): handle empty audio files gracefully
docs: update README with GPU setup instructions
style(css): adjust glass card border radius
```

---

## Pull Request Process

1. **Update your branch** with the latest `main`:

   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Push** your branch:

   ```bash
   git push origin feature/your-feature-name
   ```

3. **Open a Pull Request** on GitHub with:
   - A clear title following commit conventions
   - Description of what the PR does and why
   - Screenshots for UI changes
   - Reference to related issues (e.g., `Closes #42`)

4. **Wait for review** — maintainers will review your PR and may request changes

5. Once approved, your PR will be **merged** 🎉

---

## 🙏 Thank You!

Every contribution, no matter how small, helps make this project better. Whether it's fixing a typo, reporting a bug, or implementing a feature — **thank you!**
