#!/usr/bin/env python3

import datetime
from collections import OrderedDict
import sys
import os 

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

def clear():
	os.system('cls' if os.name =='nt' else 'clear')


def menu_loop():
	"""Show the Menu"""
	choice = None

	while choice != 'q':
		clear()
		print("Enter 'q' to quit.")
		for key,value in menu.items():
			print('{}) {}'.format(key,value.__doc__))
		choice = input('Action: ').lower().strip()

		if choice in menu:
			clear()
			menu[choice]()


def add_entry():
	"""Add an entry """

	data = input("Please enter your entry and press enter when finished>>>\n")
	if data: 
			
		Entry.create(content=data)
		print("Saved successfully!")




def view_entry(search_query = None):
	"""View previous entry """
	entries = Entry.select().order_by(Entry.timestamp.desc())
	if search_query:
		entries = entries.where(Entry.content.contains(search_query))

	for entry in entries:
		timestamp = entry.timestamp.strftime('%A %B %d, %Y %I %M%p')
		clear()
		print(timestamp)
		print('=' * len(timestamp))
		print(entry.content)
		print("\n\n"+'='*len(timestamp))
		print('n) for next entry\nq) return to main menu\nd) delete entry')

		next_action = input('Action: [Ndq] ').lower().strip()

		if next_action == 'q':
			break
		elif next_action == 'd':
			delete_entry(entry)


def search_entries():
	"""Search entries for a string """
	view_entry(input('Search query: '))





def delete_entry(entry):
	"""Delete an entry """
	if input("Are you sure [yN]").lower()=='y':
		entry.delete_instance()
		print("Entry deleted!")

menu = OrderedDict([
	('a',add_entry),
	('v',view_entry),
	('s',search_entries)

	])

if __name__ == "__main__":
	initialize()
	menu_loop()