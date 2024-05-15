import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

from Scripts import settings, html_actions, static, csv_actions, misc

url = "file:///C:/Users/Admin/Desktop/galvprefore2-6-24.htm"
def main(url, csv_file_name):

    csv_path = os.path.join(settings.csv_folder_path,f'{csv_file_name}.csv')

    chromeDriverPath = settings.chromeDrivePath

    options = Options()

    # Keep the browser from showing by making it headless
    options.add_argument("--headless")

    # Saves on GPU process since images aren't rendered
    options.add_argument("--disable-gpu")

    # Initalize broser instance
    browser = webdriver.Chrome(executable_path=chromeDriverPath, options=options)

    browser.get(url)

    ph = static.PropertyHeaders()

    pd = static.PropertyDetails()

    city = None
    
    # Creating a list of header values
    headers = [value for key, value in static.PropertyHeaders.__dict__.items() if not key.startswith("__")]

    soup = BeautifulSoup(browser.page_source, 'html.parser')

    all_property_tbls = soup.find_all("table")

    # property_tbl = soup.find(id="myTable_0")
    for property_tbl in all_property_tbls:
        
        if 'id' in property_tbl.attrs:
            if "myTable_" in property_tbl.get('id'): 
            
                table_rows = property_tbl.find_all('tr')

                table_row_1 = table_rows[0]
                table_row_2 = table_rows[1]
                table_row_3 = table_rows[2]
                table_row_4 = table_rows[3]

                table_row_1_cells = table_row_1.find_all('td')
                table_row_2_cells = table_row_2.find_all('td')
                table_row_3_cells = table_row_3.find_all('td')
                table_row_4_cells = table_row_4.find_all('td')

                # Gather Data from first row
                address_and_zip = html_actions.innerHTML_Drill(table_row_1_cells[0].find('a'))
                # Split the string from the right
                if address_and_zip:
                    if misc.ends_with_five_or_more_numbers(address_and_zip):

                        parts = address_and_zip.rsplit(' ', 1)  # Split once from the right
                        if len(parts) > 1:
                            pd.address = parts[0]
                            pd.zip_code = parts[1]
                        else:
                            continue
                    else:
                        pd.address = address_and_zip
                        
                pd.year_built = html_actions.innerHTML_Drill(table_row_1_cells[1])

                # Splitting the names
                original_owner_str = html_actions.innerHTML_Drill(table_row_1_cells[2])
                transformed_names = misc.transform_names_no_middle_initials(original_owner_str)
                pd.original_owner_1_first_name, pd.original_owner_1_last_name, pd.original_owner_2_first_name, pd.original_owner_2_last_name = misc.split_names(transformed_names)
                
                pd.tax_account_id_number = html_actions.innerHTML_Drill(table_row_1_cells[3])
                pd.property_value = html_actions.innerHTML_Drill(table_row_1_cells[4])
                pd.loan_origination_date= html_actions.innerHTML_Drill(table_row_1_cells[5])

                # Gather Data from first row
                pd.legal_description = html_actions.innerHTML_Drill(table_row_2_cells[0])
                pd.key_map = html_actions.innerHTML_Drill(table_row_2_cells[1])
                pd.current_owner = html_actions.innerHTML_Drill(table_row_2_cells[2])
                pd.link_to_deed_of_trust = html_actions.innerHTML_Drill(table_row_2_cells[3])
                pd.estimated_loan_balance = html_actions.innerHTML_Drill(table_row_2_cells[4])
                pd.loan_type = html_actions.innerHTML_Drill(table_row_2_cells[5])

                # Gather Data from first row
                pd.mortgagee = html_actions.innerHTML_Drill(table_row_3_cells[0])
                pd.bedrooms = html_actions.innerHTML_Drill(table_row_3_cells[1])
                pd.trustee_reference_number = html_actions.innerHTML_Drill(table_row_3_cells[2])
                pd.estimated_bid_previous_posts = html_actions.innerHTML_Drill(table_row_3_cells[3])
                pd.title_report = html_actions.innerHTML_Drill(table_row_3_cells[4])
                pd.loan_term = html_actions.innerHTML_Drill(table_row_3_cells[5])

                # Gather Data from first row
                pd.trustee_view_notice = table_row_4_cells[1].find('a')['href']
                pd.square_footage = html_actions.innerHTML_Drill(table_row_4_cells[2])
                pd.sale_hours_record_posted = html_actions.innerHTML_Drill(table_row_4_cells[3])
                pd.original_loan_amount = html_actions.innerHTML_Drill(table_row_4_cells[4])
                pd.estimated_equity = html_actions.innerHTML_Drill(table_row_4_cells[5])
                pd.estimated_margin = html_actions.innerHTML_Drill(table_row_4_cells[6])
            
        else:
            tr = property_tbl.find("tr")
            if tr:
                # print(f"TR --*---*-- {tr}")
                if 'bgcolor' in tr.attrs:
                    if "#CCFFFF" in tr.get('bgcolor'):
                        city_element = tr.find()
                        # print(f"City Element --*---*-- {city_element}")

                        city_string = html_actions.innerHTML_Drill(city_element)

                        # print(f"City String --*---*-- {city_string}")
                        # Take the "&nbsp" off
                        city = city_string.rsplit(';', 1)[0]

        if city:
            pd.city = city

        if pd.are_address_and_city_filled():
            data_row = {
                ph.address: pd.address,
                ph.city: pd.city,
                ph.zip_code: pd.zip_code,
                ph.year_built: pd.year_built,
                ph.original_owner_1_first_name: pd.original_owner_1_first_name, 
                ph.original_owner_1_last_name: pd.original_owner_1_last_name, 
                ph.original_owner_2_first_name: pd.original_owner_2_first_name, 
                ph.original_owner_2_last_name: pd.original_owner_2_last_name,
                ph.tax_account_id_number: pd.tax_account_id_number,
                ph.property_value: pd.property_value,
                ph.loan_origination_date: pd.loan_origination_date,
                ph.legal_description: pd.legal_description,
                ph.key_map: pd.key_map,
                ph.current_owner: pd.current_owner,
                ph.link_to_deed_of_trust: pd.link_to_deed_of_trust,
                ph.estimated_loan_balance: pd.estimated_loan_balance,
                ph.loan_type: pd.loan_type,
                ph.mortgagee: pd.mortgagee,
                ph.bedrooms: pd.bedrooms,
                ph.trustee_reference_number: pd.trustee_reference_number,
                ph.estimated_bid_previous_posts: pd.estimated_bid_previous_posts,
                ph.title_report: pd.title_report,
                ph.loan_term: pd.loan_term,
                ph.trustee_view_notice: pd.trustee_view_notice,
                ph.square_footage: pd.square_footage,
                ph.sale_hours_record_posted: pd.sale_hours_record_posted,
                ph.original_loan_amount: pd.original_loan_amount,
                ph.estimated_equity: pd.estimated_equity,
                ph.estimated_margin: pd.estimated_margin,
            }

            csv_actions.csv_writer(csv_path=csv_path, headers=headers, data_row=data_row)

            # Create a new instance to start again
            pd = static.PropertyDetails()

    if os.path.exists(csv_path):
        print(f"Success: File created! -- {csv_path}")
    else:
        print(f"Failed: File not created! -- {csv_path}")

    return(csv_path)