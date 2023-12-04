# Auxiliary functions

import pandas as pd

def process_response(response, fail_msg, ret_format=None, attribute_ids=None):
    if response.status_code == 200:
        if response.text and response.text != '[]':  # Check if the response body is not empty
            try:
                data = response.json()
                if ret_format is None and attribute_ids is None:
                    if isinstance(data, list):
                        df = pd.DataFrame(data)
                        df = flatten_dict_columns(df)
                        df = flatten_dict_list_columns(df)
                        return df
                    if isinstance(data, dict): # in case of response dataframe with only 1 row to expand
                        df = pd.DataFrame({key: [value] for key, value in data.items()})
                        df = flatten_dict_columns(df)
                        df = flatten_dict_list_columns(df)
                        return df 
                else:
                    df = pd.DataFrame(data)
                    if ret_format == 'WIDE':
                        cols_to_group = df.columns[:-2]
                        df = df.pivot(index=cols_to_group, columns='clinicalAttributeId', values='value')              
                        df.reset_index(inplace=True)
                        # check if all attributes has been retrieved
                        miss_attr = [col for col in attribute_ids if col not in df.columns]
                        if miss_attr != []:
                            print("Attributes not present: " + ", ".join(map(str, miss_attr)))
                    elif ret_format == 'LONG':
                        miss_attr = [attr for attr in attribute_ids if attr not in set(df.clinicalAttributeId)]
                        if miss_attr != []:
                            print("Attributes not present: " + ", ".join(map(str, miss_attr)))
                    else: 
                        raise Exception("Error: ret_format must be 'LONG' or 'WIDE'")
                    return df
            except ValueError as e:
                print(f"Error decoding the JSON response: {e}")
        else:
            print("Response is empty. No data available.")
    else:
        error_message = f"{fail_msg} Status code: {response.status_code}"
    
        if response.text:
            error_message += f"\n Error messagge: {response.json()['message']}"
    
        raise Exception(error_message)

def flatten_dict_columns(df):
    def flatten_dict(d, parent_key=''):
        items = {}
        for key, value in d.items():
            new_key = parent_key + '_' + key if parent_key else key
            if isinstance(value, dict):
                items[new_key] = flatten_dict(value)
            else:
                items[new_key] = value
        return items

    new_data = []
    for _, row in df.iterrows():
        flattened_dict = {}
        for column, value in row.items():
            if isinstance(value, dict):
                flattened_dict.update(flatten_dict(value, column))
            else:
                flattened_dict[column] = value
        new_data.append(flattened_dict)

    new_df = pd.DataFrame(new_data)
    return new_df

def flatten_dict_list_columns(df):
    list_columns = []

    # Identify columns that contain lists of dict
    for column in df.columns:
        if df[column].apply(lambda x: isinstance(x, list) and all(isinstance(item, dict) for item in x)).all():
            list_columns.append(column)

    if not list_columns:
        return df

    new_data = []
    for _, row in df.iterrows():
        flattened_dicts = []
        for column in list_columns:
            list_of_dicts = row[column]
            for d in list_of_dicts:
                flattened_dict = {k: v for k, v in row.items() if k not in list_columns}
                flattened_dict.update(d)
                flattened_dicts.append(flattened_dict)
        if not flattened_dicts:
            flattened_dicts = [row.to_dict()]
        new_data.extend(flattened_dicts)

    new_df = pd.DataFrame(new_data)
    return new_df