// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.query_reports["Attendance for pay period"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"reqd": 1,
			"default": frappe.datetime.nowdate()
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"reqd": 1,
			"default": frappe.datetime.month_end()
		},
		{
			"fieldname":"employee_name",
			"label": __("Employee Name"),
			"fieldtype": "Link",
			"options": "Employee"
		},
		{
			"fieldname":"holiday_list",
			"label": __("Holiday List"),
			"fieldtype": "Link",
			"options": "Holiday List"
		},
		{
			"fieldname":"year",
			"label": __("Year"),
			"fieldtype": "Link",
			"options": "Holiday List"
		}
	]
}