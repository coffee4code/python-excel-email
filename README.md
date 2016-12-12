## Read Excel and Send Email by Python
---

### Dependencies
* Python3.4
* pip3
* virtualenv


### Packages
* xlrd
* Jinja2==2.8
* MarkupSafe==0.23

```(more in requirements.txt)```


### Setup
1. Create virtual env
    ```bash
        virtualenv -p /usr/bin/python3.4 --no-site-packages .venv
    ```
2. Setup ```Pycharm``` Project Interpreter
    ```bash
        Settings -> Project:current -> Project Intercepreter -> dropdown and choose .venv
    ```
    
3. Install dependencies
    ```bash
        pip3 install -r requirements.txt
    ```
    
4. Run
    ```bash
        python3.4 index.py
    ```
    
Contributor

* [Yin Gang](https://github.com/smallyin/) 