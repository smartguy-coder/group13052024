# group13052024

- python -m venv venv
- win -- .\venv\Scripts\activate
- mac -- source ./venv/bin/activate
- mac -- which python3

auto code formatting
- Ctrl - Alt - l
- Ctrl - Shift - f   - search everywhere

pip or pip3

- pip3 list
- pip3 install pywebio

pip3 freeze > requirements.txt 
pip3 install -r requirements.txt


pytest .
pytest -v  .
pytest -v -s  . 
pytest -v  test_utils.py::TestAddTwoNumbers::test_add_two_combined 
pytest -v  test_utils.py::TestAddTwoNumbers

