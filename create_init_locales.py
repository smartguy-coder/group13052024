import os
import subprocess

langs = ['en', 'uk', 'ru']
pot_file = 'transl.pot'
locale_dir = 'locale'

subprocess.run([
    'xgettext',
    '-i',
    'translate_app.py',
    '-o',
    pot_file,
    '-d',
    'this_project',
])


# for lang in langs:
#     os.makedirs(os.path.join(locale_dir, lang, 'LC_MESSAGES'), exist_ok=True)
#
#     subprocess.run([
#         'msginit',
#         '-i',
#         pot_file,
#         '-o',
#         os.path.join(locale_dir, lang, 'LC_MESSAGES', 'this_project.po'),
#         '-l',
#         lang
#     ])


for lang in langs:
    # ╰─ msgfmt  locale/uk/LC_MESSAGES/this_project.po -o locale/uk/LC_MESSAGES/this_project.mo
    subprocess.run([
        'msgfmt',
        os.path.join(locale_dir, lang, 'LC_MESSAGES', 'this_project.po'),
        '-o',
        os.path.join(locale_dir, lang, 'LC_MESSAGES', 'this_project.mo'),
    ])