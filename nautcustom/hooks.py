# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "nautcustom"
app_title = "Nautcustom"
app_publisher = "Nautican"
app_description = "Customizations to ERPNext for Nautican"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "devon@nautican.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/nautcustom/css/nautcustom.css"
# app_include_js = "/assets/nautcustom/js/nautcustom.js"

# include js, css files in header of web template
# web_include_css = "/assets/nautcustom/css/nautcustom.css"
# web_include_js = "/assets/nautcustom/js/nautcustom.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "nautcustom.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "nautcustom.install.before_install"
# after_install = "nautcustom.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "nautcustom.notifications.get_notification_config"

# Fixtures
# --------
fixtures = ["Custom Field", "Custom Script"]

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"nautcustom.tasks.all"
# 	],
# 	"daily": [
# 		"nautcustom.tasks.daily"
# 	],
# 	"hourly": [
# 		"nautcustom.tasks.hourly"
# 	],
# 	"weekly": [
# 		"nautcustom.tasks.weekly"
# 	]
# 	"monthly": [
# 		"nautcustom.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "nautcustom.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "nautcustom.event.get_events"
# }
