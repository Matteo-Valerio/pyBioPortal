# Auxiliary functions

import pandas as pd

def process_response(response, ret_format, attribute_ids):
    if response.text and response.text != '[]':  # Check if the response body is not empty
        try:
            data = response.json()
            df = pd.DataFrame(data)
            if ret_format == 'WIDE':
                cols_to_group = df.columns[:-2]
                df = df.pivot(index=cols_to_group, columns='clinicalAttributeId', values='value')              
                df.reset_index(inplace=True)
                # check if all attributes has been retrieved
                miss_attr = [col for col in attribute_ids if col not in df.columns]
                if miss_attr != []:
                    print("Attributes not present: " + ", ".join(map(str, miss_attr)))
            else:
                miss_attr = [attr for attr in attribute_ids if attr not in set(df.clinicalAttributeId)]
                if miss_attr != []:
                    print("Attributes not present: " + ", ".join(map(str, miss_attr)))
            return df
        except ValueError as e:
            print(f"Error decoding the JSON response: {e}")
    else:
        print("Response is empty. No data available.")

def check_response(response, fail_msg):
    if response.status_code == 200:
        if response.text and response.text != '[]':  # Check if the response body is not empty
            try:
                data = response.json()
                return pd.DataFrame(data)
            except ValueError as e:
                print(f"Error decoding the JSON response: {e}")
        else:
            print("Response is empty. No data available.")
    else:
        error_message = f"{fail_msg} Status code: {response.status_code}"
    
        if response.text:
            error_message += f"\n Error messagge: {response.json()['message']}"
    
        raise Exception(error_message)
        #raise Exception(f"{fail_msg} Status code: {response.status_code}")