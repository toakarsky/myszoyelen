#!/usr/bin/env python3
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from myelen import app
from myelen.database import db


manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
