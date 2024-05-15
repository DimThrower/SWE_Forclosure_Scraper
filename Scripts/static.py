class PropertyHeaders:
    address = "Address"
    city = "City"
    zip_code = "Zip Code"
    year_built = "Yr Built"
    original_owner_1_first_name = "Original Owner  1 First Name"
    original_owner_1_last_name = "Original Owner  1 Last Name"
    original_owner_2_first_name = "Original Owner  2 First Name"
    original_owner_2_last_name = "Original Owner  2 Last Name"
    tax_account_id_number = "Tax Account ID Nbr"
    property_value = "Property Value"
    loan_origination_date = "Loan Orig Date"
    legal_description = "Legal Description"
    key_map = "Key Map"
    current_owner = "Current Owner"
    link_to_deed_of_trust = "Link to Deed of Trust"
    estimated_loan_balance = "Est Loan Balance"
    loan_type = "Loan Type"
    mortgagee = "Mortgagee"
    bedrooms = "Bdrms"
    trustee_reference_number = "Trustee Reference Nbr"
    estimated_bid_previous_posts = "Est Bid/Previous Posts"
    title_report = "Title Report"
    loan_term = "Loan Term"
    trustee_view_notice = "Trustee / View Notice"
    square_footage = "Sq Ftg"
    sale_hours_record_posted = "Sale Hrs/Record Posted"
    original_loan_amount = "Original Loan Amount"
    estimated_equity = "Estimated Equity"
    estimated_margin = "Estimated Margin"

class PropertyDetails:
    def __init__(self):
        self.address = None
        self.city = None
        self.zip_code = None
        self.year_built = None
        self.original_owner_1_first_name = None
        self.original_owner_1_last_name = None
        self.original_owner_2_first_name = None
        self.original_owner_2_last_name = None
        self.tax_account_id_number =None
        self.property_value = None
        self.loan_origination_date = None
        self.legal_description = None
        self.key_map = None
        self.current_owner = None
        self.link_to_deed_of_trust = None
        self.estimated_loan_balance = None
        self.loan_type = None
        self.mortgagee = None
        self.bedrooms = None
        self.trustee_reference_number = None
        self.estimated_bid_previous_posts = None
        self.title_report = None
        self.loan_term = None
        self.trustee_view_notice = None
        self.square_footage = None
        self.sale_hours_record_posted = None
        self.original_loan_amount = None
        self.estimated_equity = None
        self.estimated_margin = None

    def print_attributes(self):
        for attr, value in self.__dict__.items():
            print(f"{attr} = {value}")

    def are_address_and_city_filled(self):
        if self.address is not None and self.city is not None:
            return True
        else:
            return False