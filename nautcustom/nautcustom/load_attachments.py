
from __future__ import unicode_literals

import frappe
from frappe import _, throw
from frappe.utils import flt
from frappe.utils.file_manager import save_url
import json


@frappe.whitelist()
def attach_all_docs(document, method=None):
	"""This function attaches drawings to the purchase order based on the items being ordered"""
	document = json.loads(document)

	current_attachments = []
	for file_url in frappe.db.sql("""select file_url from `tabFile` where attached_to_doctype = %(doctype)s and attached_to_name = %(docname)s""", {'doctype': document["doctype"], 'docname': document["name"]}, as_dict=True ):
		current_attachments.append(file_url.file_url)
	count = 0
	for item_doc in document["items"]:
		item = [item_doc["item_name"]]

		attachments = []
		for file_url in frappe.db.sql("""select file_url from `tabFile` where attached_to_doctype = %(doctype)s and attached_to_name = %(docname)s""", {'doctype': ["Item"], 'docname': item}, as_dict=True ):
			attachments.append(file_url.file_url)

		for attach in attachments:
			if not attach in current_attachments:
				count = count + 1
				save_url(attach, document["doctype"], document["name"], "Home/Attachments")
	frappe.msgprint("Attached {0} files".format(count))
