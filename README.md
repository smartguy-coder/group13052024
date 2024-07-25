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


╰─ xgettext -i *.py -o transl.pot -d this_project
╰─ mkdir -p locale/uk/LC_MESSAGES
╰─ msginit -i transl.pot -o locale/ru/LC_MESSAGES/this_project.po -l ru
╰─ msgfmt  locale/ru/LC_MESSAGES/this_project.po -o locale/ru/LC_MESSAGES/this_project.mo
╰─ msgmerge --update locale/ru/LC_MESSAGES/this_project.po transl.pot

