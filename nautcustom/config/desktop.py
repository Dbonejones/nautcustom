# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Nautcustom",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Nautcustom")
		},
				{
			"module_name": "Drawings Portal",
			"color": "#4256f4",
			"icon": "fa fa-pencil-square-o",
			"type": "module",
			"label": _("Drawings Portal")
		},
				{
			"module_name": "Legal Documents",
			"color": "#6b6353",
			"icon": "fa fa-gavel",
			"type": "module",
			"label": _("Legal Documents")
		},
	]
