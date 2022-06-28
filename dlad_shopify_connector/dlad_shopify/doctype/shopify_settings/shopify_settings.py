# Copyright (c) 2022, DLAD Software Solutions and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class ShopifySettings(Document):
	
	def is_enabled(self) -> bool:
		return bool(self.enable_shopify)
