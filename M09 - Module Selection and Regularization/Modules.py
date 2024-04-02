#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def cprint(text: str, color: str = 'yellow'):
  """Uses a few basic colors to print messages/warnings to the console."""
  lookup_dict = {'black': 30, 'red': 31, 'green': 32, 'yellow': 33, 'blue': 34, 'magenta': 35, 'cyan': 36, 'white': 37,
                 'bred': 91, 'bgreen':92, 'byellow': 93, 'bblue': 94, 'bmagenta': 95, 'bcyan': 96, 'bwhite': 97}
  if color not in lookup_dict.keys():
    message = "Color not in code. Possible values: " + str(list(lookup_dict.keys()))
    cprint(text = message, color = '31')
    return
  print("\033[{}m{}\033[00m".format(lookup_dict[color], text))
  return