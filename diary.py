#!/usr/bin/env python3

import datetime
from collections import OrderedDict
import sys

from peewee import *

db = SqliteDatabase('diary.db')



class Entry(Model):
	content = TextField()
	timestamp = DateTimeField(default = datetime.datetime.now)

	class Meta:
		database = db

def initialize():
	"""Create the database and the table if they do not exist"""
	db.connect()
	db.create_tables([Entry],safe=True)


def menu_loop():
	"""Show the Menu"""
	choice = None

	while choice != 'q':
		print("Enter 'q' to quit.")
		for key,value in menu.items():
			print('{}) {}'.format(key,value.__doc__))
		choice = input('Action: ').lower().strip()

		if choice in menu:
			menu[choice]()


def add_entry():
	"""Add an entry """
	print("Enter your entry. Press crtl+d when finished.")
	data = sys.stdin.read().strip()

	if input ('Save entry [Yn]'.lower() != 'n'): 
		Entry.create(content=data)
		print("Saved successfully!")


def view_entry():
	"""View previous entry """



def delete_entry():
	"""Delete an entry """

menu = OrderedDict([
	('a',add_entry),
	('v',view_entry)

	])

if __name__ == "__main__":
	initialize()
	menu_loop()