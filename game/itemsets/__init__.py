# -*- coding: utf-8 -*-
"""
Item Sets
 - ItemSet.dbc
"""

from .. import *
from ..globalstrings import *


class ItemSet(Model):
	pass

class ItemSetTooltip(Tooltip):
	def tooltip(self):

		items = self.obj.getItems()
		maxItems = len(items)

		self.append("name", ITEM_SET_NAME % (self.obj.getName(), 0, maxItems), color=YELLOW)

		requiredSkill, requiredSkillLevel = self.obj.getRequiredSkillInfo()
		if requiredSkill and requiredSkillLevel:
			self.append("requiredSkill", ITEM_MIN_SKILL % (requiredSkill, requiredSkillLevel))

		for item in items:
			self.append("item", "  %s" % (item.getName()), color=GREY)

		self.appendEmptyLine()

		for bonus, pieces in self.obj.getBonusInfo():
			self.append("bonus", ITEM_SET_BONUS_GRAY % (pieces, bonus.getDescription()), color=GREY)

		return self.flush()
ItemSet.Tooltip = ItemSetTooltip

class ItemSetProxy(object):
	"""
	WDBC proxy for item sets
	"""
	def __init__(self, cls):
		from pywow import wdbc
		self.__file = wdbc.get("ItemSet.dbc", build=-1)

	def get(self, id):
		return self.__file[id]

	def getBonusInfo(self, row):
		from ..spells import Spell
		from operator import itemgetter
		ret = []
		for i in range(1, 9):
			spell = row._raw("bonus_%i" % (i))
			pieces = getattr(row, "required_items_%i" % (i))
			if spell:
				ret.append((Spell(spell), pieces))

		ret.sort(key=itemgetter(1))
		return ret

	def getItems(self, row):
		from ..items import Item
		ret = []
		for i in range(1, 18):
			id = row._raw("item_%i" % (i))
			if id:
				ret.append(Item(id))

		return ret

	def getRequiredSkillInfo(self, row):
		requiredSkillLevel = row.required_skill_level
		if row.required_skill:
			return row.required_skill.name_enus, requiredSkillLevel
		return "", requiredSkillLevel

	def getName(self, row):
		return row.name_enus

ItemSet.initProxy(ItemSetProxy)
