from .base import *

try:
    from .local import *
    live = False
except:
    live = True
if live:
    # from .production import *
    pass

# from .production import *
#
# try:
#     from .local import *
# except:
#     pass
