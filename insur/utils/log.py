import logging

log = logging.getLogger("Insure")
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
log.addHandler(ch)
