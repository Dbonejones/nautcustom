# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate, flt

def execute(filters=None):
	if not filters:
		filters = {}

	columns = get_columns()
	data = get_data(filters)
	
	return columns, data


def get_columns():
	return [
		_("Employee") + ":Link/Employee:120",
		_("Name") + ":Data:200",
		_("Date") + ":Date:100",
		_("Status") + ":Data:70",
		_("Hours") + ":Float:50",
		_("Holiday") + ":Data:200"
	]

	
def get_data(filters):
	
	holiday_filter = {"holiday_date": (">=", filters.from_date),
				"holiday_date": ("<=", filters.to_date)}
				
	if filters.holiday_list:
		holiday_filter["parent"] = filters.year
		
	holidays = frappe.get_all("Holiday", fields=["holiday_date"],
				filters=holiday_filter)
				
	holidays_list = []
	
	for holiday in holidays:
		holidays_list.append(holiday.holiday_date)

	return holidays_list[2]
	
	datalist = frappe.db.sql(""" select `employee`, `employee_name`,
		`attendance_date`, `status`, `hours`
		from `tabAttendance`
		where `attendance_date` >= %(from_date)s and `attendance_date` <= %(to_date)s and `employee` = %(employee_name)s
		order by `attendance_date` asc
		""", filters, as_list=1)
	#return datalist
