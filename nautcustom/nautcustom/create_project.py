@frappe.whitelist()
def createProj(soNumb,soCust):
	frappe.msgprint("Hi")
	doc = frappe.new_doc({
		"doctype": "Project"
		"project_name": "Test" #soNumb + " " + soCust
		"status": "Open"
		"project_type": "External"
		})
	doc.insert()