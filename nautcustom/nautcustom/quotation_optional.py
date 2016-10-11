from __future__ import unicode_literals
import frappe

def second_totals(doc, method):
  total = 0.0
  for data in doc.optional_items:
    data.amount = data.qty * data.rate
    total += data.amount
  doc.optional_total = total