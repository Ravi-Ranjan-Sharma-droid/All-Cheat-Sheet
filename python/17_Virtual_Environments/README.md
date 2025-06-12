# Virtual Environments in Python

Virtual environments are isolated Python environments that allow you to install packages and dependencies for specific projects without affecting the global Python installation. This section covers everything you need to know about creating, managing, and using virtual environments in Python.

## Why Use Virtual Environments?

Virtual environments solve several common problems in Python development:

1. **Dependency Isolation**: Different projects may require different versions of the same package. Virtual environments allow each project to have its own dependencies, regardless of what dependencies other projects have.

2. **Avoiding Version Conflicts**: Virtual environments prevent conflicts between package versions by isolating project dependencies.

3. **Reproducibility**: Virtual environments make it easier to recreate the exact environment needed to run a project, ensuring consistent behavior across different machines.

4. **Clean Testing Environment**: Virtual environments provide a clean environment for testing code without interference from globally installed packages.

5. **Simplified Dependency Management**: Virtual environments make it easier to track and manage project dependencies.

## Built-in `venv` Module

Python 3.3+ includes the `venv` module, which is the recommended way to create virtual environments.

### Creating a Virtual Environment

```bash
# On Windows
python -m venv myenv

# On macOS/Linux
python3 -m venv myenv
```

This creates a directory called `myenv` containing a Python interpreter, libraries, and scripts.

### Activating a Virtual Environment

Before you can use a virtual environment, you need to activate it:

```bash
# On Windows (Command Prompt)
myenv\Scripts\activate.bat

# On Windows (PowerShell)
myenv\Scripts\Activate.ps1

# On macOS/Linux
source myenv/bin/activate
```

When a virtual environment is activated, your shell prompt will change to show the name of the active environment:

```
(myenv) C:\Users\username>
```

### Deactivating a Virtual Environment

To exit a virtual environment and return to your global Python environment:

```bash
deactivate
```

### Installing Packages in a Virtual Environment

Once a virtual environment is activated, you can use `pip` to install packages, and they will be installed only in the virtual environment:

```bash
# Make sure the virtual environment is activated
(myenv) $ pip install requests
```

### Listing Installed Packages

To see what packages are installed in the current environment:

```bash
(myenv) $ pip list
```

### Saving and Restoring Dependencies

To save the current state of installed packages to a file:

```bash
(myenv) $ pip freeze > requirements.txt
```

To install packages from a requirements file:

```bash
(myenv) $ pip install -r requirements.txt
```

### Creating a Virtual Environment with Specific Python Version

If you have multiple Python versions installed, you can specify which one to use:

```bash
# On Windows
py -3.8 -m venv myenv-py38

# On macOS/Linux
python3.8 -m venv myenv-py38
```

### Creating a Virtual Environment without pip

If you don't want to include pip in your virtual environment:

```bash
python -m venv myenv --without-pip
```

### Creating a Virtual Environment with System Site Packages

To create a virtual environment that has access to the system site packages:

```bash
python -m venv myenv --system-site-packages
```

## Third-Party Tools for Virtual Environments

### `virtualenv`

`virtualenv` is a third-party tool that predates `venv` and offers more features. It works with older versions of Python and has more configuration options.

#### Installation

```bash
pip install virtualenv
```

#### Creating a Virtual Environment

```bash
# Basic usage
virtualenv myenv

# Specify Python version
virtualenv -p python3.8 myenv
```

#### Activating and Deactivating

Activation and deactivation work the same way as with `venv`.

### `virtualenvwrapper`

`virtualenvwrapper` is a set of extensions to `virtualenv` that makes it easier to work with multiple virtual environments.

#### Installation

```bash
# On Windows
pip install virtualenvwrapper-win

# On macOS/Linux
pip install virtualenvwrapper
```

On macOS/Linux, you also need to add the following to your shell startup file (e.g., `.bashrc`, `.zshrc`):

```bash
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/projects
source /usr/local/bin/virtualenvwrapper.sh
```

#### Creating a Virtual Environment

```bash
mkvirtualenv myenv
```

#### Listing Virtual Environments

```bash
lsvirtualenv
```

#### Switching Between Environments

```bash
workon myenv
```

#### Deactivating

```bash
deactivate
```

#### Removing a Virtual Environment

```bash
rmvirtualenv myenv
```

### `conda`

`conda` is a package, dependency, and environment management system that comes with Anaconda and Miniconda. It's particularly popular in data science and scientific computing.

#### Installation

Install Anaconda or Miniconda from their respective websites.

#### Creating a Conda Environment

```bash
# Basic usage
conda create --name myenv

# With specific Python version
conda create --name myenv python=3.8

# With specific packages
conda create --name myenv python=3.8 numpy pandas
```

#### Activating a Conda Environment

```bash
# On Windows
conda activate myenv

# On macOS/Linux
conda activate myenv
```

#### Deactivating a Conda Environment

```bash
conda deactivate
```

#### Listing Conda Environments

```bash
conda env list
```

#### Removing a Conda Environment

```bash
conda env remove --name myenv
```

#### Exporting and Importing Environments

```bash
# Export environment to a file
conda env export > environment.yml

# Create environment from a file
conda env create -f environment.yml
```

### `pipenv`

`pipenv` is a dependency manager that combines `pip` and `virtualenv` into a single tool. It automatically creates and manages a virtual environment for your projects, as well as adds/removes packages from your `Pipfile`.

#### Installation

```bash
pip install pipenv
```

#### Creating a Project with Pipenv

```bash
# Navigate to your project directory
cd myproject

# Install a package (this creates a virtual environment if one doesn't exist)
pipenv install requests
```

#### Activating the Virtual Environment

```bash
pipenv shell
```

#### Installing Dependencies

```bash
# Install all dependencies
pipenv install

# Install development dependencies
pipenv install --dev
```

#### Locking Dependencies

```bash
pipenv lock
```

#### Uninstalling Packages

```bash
pipenv uninstall requests
```

#### Removing the Virtual Environment

```bash
pipenv --rm
```

### `poetry`

`poetry` is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

#### Installation

```bash
# On Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

# On macOS/Linux
curl -sSL https://install.python-poetry.org | python3 -
```

#### Creating a New Project

```bash
poetry new myproject
cd myproject
```

#### Initializing an Existing Project

```bash
cd existing-project
poetry init
```

#### Adding Dependencies

```bash
poetry add requests

# Add development dependency
poetry add --dev pytest
```

#### Installing Dependencies

```bash
poetry install
```

#### Activating the Virtual Environment

```bash
poetry shell
```

#### Updating Dependencies

```bash
poetry update
```

#### Running Commands in the Virtual Environment

```bash
poetry run python script.py
```

## Virtual Environments in IDEs

### PyCharm

PyCharm has built-in support for virtual environments.

#### Creating a New Project with a Virtual Environment

1. Go to `File > New Project`
2. Select the project location
3. Under `Python Interpreter`, select `New environment using` and choose `Virtualenv` or `Conda`
4. Click `Create`

#### Configuring an Existing Project to Use a Virtual Environment

1. Go to `File > Settings` (Windows/Linux) or `PyCharm > Preferences` (macOS)
2. Navigate to `Project: [YourProject] > Python Interpreter`
3. Click the gear icon and select `Add...`
4. Choose `Virtualenv Environment` or `Conda Environment`
5. Select `Existing environment` and browse to your virtual environment's Python interpreter
6. Click `OK`

### Visual Studio Code

VS Code supports virtual environments through its Python extension.

#### Selecting a Virtual Environment

1. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`)
2. Type and select `Python: Select Interpreter`
3. Choose your virtual environment from the list

#### Creating a Virtual Environment

1. Open the Command Palette
2. Type and select `Python: Create Environment`
3. Choose the environment type (`venv`, `conda`, etc.)
4. Follow the prompts to complete the setup

## Best Practices

### 1. Use One Virtual Environment Per Project

Create a separate virtual environment for each project to keep dependencies isolated.

```bash
# Create a virtual environment in the project directory
cd myproject
python -m venv venv
```

### 2. Add Virtual Environment Directories to `.gitignore`

Virtual environments should not be committed to version control. Add them to your `.gitignore` file:

```
# .gitignore
venv/
.env/
.venv/
env/
```

### 3. Use `requirements.txt` or Equivalent

Track your project's dependencies in a `requirements.txt` file or equivalent (`Pipfile`, `pyproject.toml`, etc.).

```bash
# Generate requirements.txt
pip freeze > requirements.txt
```

### 4. Specify Exact Versions

Specify exact versions of dependencies to ensure reproducibility:

```
# requirements.txt
requests==2.28.1
numpy==1.23.4
```

### 5. Use Version Control for Dependency Files

Commit your dependency files (`requirements.txt`, `Pipfile`, `pyproject.toml`, etc.) to version control.

### 6. Document Environment Setup

Include instructions for setting up the virtual environment in your project's README:

```markdown
## Setup

1. Create a virtual environment:
   ```
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
```

### 7. Use Environment Variables for Secrets

Store sensitive information (API keys, passwords, etc.) in environment variables, not in your code.

```python
import os

api_key = os.environ.get("API_KEY")
```

You can use a package like `python-dotenv` to load environment variables from a `.env` file:

```bash
pip install python-dotenv
```

```python
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file
api_key = os.environ.get("API_KEY")
```

Make sure to add `.env` to your `.gitignore` file.

### 8. Regularly Update Dependencies

Regularly update your dependencies to get bug fixes and security patches:

```bash
pip install --upgrade -r requirements.txt
```

Consider using tools like `pip-tools`, `pipenv`, or `poetry` for more sophisticated dependency management.

## Common Pitfalls

### 1. Forgetting to Activate the Virtual Environment

If you install packages without activating the virtual environment, they will be installed globally.

**Solution**: Always check that your virtual environment is activated before installing packages. Look for the environment name in your shell prompt.

### 2. Installing Packages Globally When a Virtual Environment is Needed

Installing packages globally can lead to version conflicts between projects.

**Solution**: Use virtual environments for all your Python projects, even small ones.

### 3. Committing Virtual Environments to Version Control

Virtual environments can be large and contain platform-specific files.

**Solution**: Add virtual environment directories to your `.gitignore` file.

### 4. Not Pinning Dependency Versions

Without pinned versions, different installations might use different package versions.

**Solution**: Use `pip freeze > requirements.txt` to pin exact versions.

### 5. Using the Wrong Python Interpreter

Sometimes, the wrong Python interpreter is used, leading to unexpected behavior.

**Solution**: Verify which Python interpreter is being used:

```bash
# In the activated virtual environment
which python  # On macOS/Linux
where python  # On Windows
```

### 6. Nested Virtual Environments

Creating a virtual environment inside another virtual environment can lead to confusion.

**Solution**: Deactivate the current virtual environment before creating a new one.

### 7. Incompatible Packages

Some packages may have conflicting dependencies.

**Solution**: Use tools like `pip-tools`, `pipenv`, or `poetry` that can resolve dependency conflicts.

### 8. Not Updating the `requirements.txt` File

If you add new packages but don't update `requirements.txt`, others won't have the complete environment.

**Solution**: Regularly update your `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

## Advanced Topics

### Virtual Environments in Docker

When using Docker, you typically don't need a virtual environment inside the container, as the container itself provides isolation.

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

### Virtual Environments in CI/CD

In CI/CD pipelines, you typically create a fresh virtual environment for each build:

```yaml
# .github/workflows/python-app.yml (GitHub Actions)
name: Python application

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Test
      run: |
        pytest
```

### Managing Multiple Python Versions

Tools like `pyenv` allow you to manage multiple Python versions on your system.

#### Installation

```bash
# On macOS
brew install pyenv

# On Linux
curl https://pyenv.run | bash
```

#### Installing Python Versions

```bash
pyenv install 3.8.10
pyenv install 3.9.5
```

#### Setting the Global Python Version

```bash
pyenv global 3.9.5
```

#### Setting a Local Python Version (per directory)

```bash
cd myproject
pyenv local 3.8.10
```

#### Using pyenv with virtualenv

You can use `pyenv-virtualenv` to create virtual environments with specific Python versions:

```bash
# Install pyenv-virtualenv
brew install pyenv-virtualenv  # On macOS

# Create a virtual environment with a specific Python version
pyenv virtualenv 3.8.10 myproject-3.8

# Activate the virtual environment
pyenv activate myproject-3.8

# Deactivate
pyenv deactivate
```

### Creating Self-Contained Python Applications

Tools like `PyInstaller`, `cx_Freeze`, and `py2exe` can create standalone executables that include the Python interpreter and all dependencies.

#### PyInstaller Example

```bash
# Install PyInstaller
pip install pyinstaller

# Create a standalone executable
pyinstaller --onefile app.py
```

### Using Virtual Environments with Jupyter Notebooks

You can create a Jupyter kernel for your virtual environment:

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows

# Install ipykernel
pip install ipykernel

# Create a kernel for this virtual environment
python -m ipykernel install --user --name=myenv --display-name="Python (myenv)"
```

Then, when you open Jupyter Notebook or JupyterLab, you can select this kernel from the kernel menu.

## Next Steps

Now that you understand virtual environments in Python, you're ready to move on to [Pythonic Tips](../18_Pythonic_Tips/README.md).