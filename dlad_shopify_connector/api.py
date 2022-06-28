import frappe
from dlad_shopify_connector.constants import (
	SETTING_DOCTYPE,
	API_VERSION
)
from shopify.session import Session
from shopify.resources import (Product, InventoryItem, InventoryLevel)

def temp_shopify_session(func):
	"""Any function that needs to access shopify api needs this decorator. The decorator starts a temp session that's destroyed when function returns."""

	def wrapper(*args, **kwargs):

		# no auth in testing
		if frappe.flags.in_test:
			return func(*args, **kwargs)

		setting = frappe.get_doc(SETTING_DOCTYPE)
		if setting.is_enabled():
			auth_details = (setting.shopify_url, API_VERSION, setting.get_password("password"))
			with Session.temp(*auth_details):
				return func(*args, **kwargs)

	return wrapper

@frappe.whitelist(allow_guest=True)
@temp_shopify_session
def ping(cmd, name):
	item = Product.find(4164377903167)
	item_dict = item.to_dict()

	varient = item.variants[0]
	varient.title = '50g Loose Leaf / Tin update'
	inv_item = InventoryItem.find(varient.inventory_item_id)
	print('>>>>>>>>>>>>>>>>>>>>>>>>>>', inv_item)
	InventoryLevel.set(18705023039, varient.inventory_item_id, 9)
	inv_item.save()
	# item.save()

	return inv_item.to_dict()