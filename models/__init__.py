#!/usr/bin/python3
"""this executes everytime the package is called"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
