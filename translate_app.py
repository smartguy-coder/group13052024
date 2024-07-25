from gettext import translation

import sys

language = sys.argv[1]


# langs = ['en', 'uk', 'ru']
# language = input(f'Enter language you prefer {langs} >>> ')
# language = 'uk'


translator = translation('this_project', localedir='locale', languages=[language], fallback=True)
_ = translator.gettext


warning_text = _('Warning')
print(warning_text)


welcome_text = _('Welcome text')
print(welcome_text)


ask_age_msg = _('Tell me about your age')
print(ask_age_msg)


new_thing = _('New thing happened')
print(new_thing)
