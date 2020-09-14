from app import db
cols={
	'customer_id':['Customer ID','hidden'],
	'date_of_creation':['Date of Creation','date2'],
	'company_name':['Company Name','text'],
	'owner_name':['Owner Name','text'],
	'contact_no':['Contact No.','text'],
	'email_address':['Email Address','text'],
	'address':['Address','text'],
}
class Entry(db.Model):
	customer_id = db.Column(db.Integer, primary_key=True)
	date_of_creation=db.Column(db.Text, nullable=False)
	company_name=db.Column(db.Text, nullable=False)
	owner_name=db.Column(db.Text, nullable=False)
	contact_no=db.Column(db.Text, nullable=False)
	email_address=db.Column(db.Text, nullable=False)
	address=db.Column(db.Text, nullable=False)