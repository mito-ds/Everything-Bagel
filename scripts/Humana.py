{"code": "from mitosheet.public.v3 import *\nimport pandas as pd\nimport numpy as np\n\n# Imported BOB1, BOB2 from /Users/aarondiamond-reivich/Desktop/MyPlanAdvocate-streamlit-app/TEST BOB Nov 9.xlsx\nsheet_df_dictonary = pd.read_excel(r'/Users/aarondiamond-reivich/Desktop/MyPlanAdvocate-streamlit-app/TEST BOB Nov 9.xlsx', engine='openpyxl', sheet_name=[\n    'BOB1',\n    'BOB2'\n], skiprows=0)\nBOB1 = sheet_df_dictonary['BOB1']\nBOB2 = sheet_df_dictonary['BOB2']\n\n# Merged BOB1 and BOB2 into df_merge\ntemp_df = BOB2.drop_duplicates(subset=['MBI']) # Remove duplicates so lookup merge only returns first match\ndf_merge = BOB1.merge(temp_df, left_on=['MBI'], right_on=['MBI'], how='left', suffixes=['_BOB1', '_BOB2'])\n\n# Reordered column NAME_BOB1\ndf_merge_columns = [col for col in df_merge.columns if col != 'NAME_BOB1']\ndf_merge_columns.insert(1, 'NAME_BOB1')\ndf_merge = df_merge[df_merge_columns]\n\n# Reordered column NAME_BOB2\ndf_merge_columns = [col for col in df_merge.columns if col != 'NAME_BOB2']\ndf_merge_columns.insert(2, 'NAME_BOB2')\ndf_merge = df_merge[df_merge_columns]\n\n# Reordered column PLAN_BOB2\ndf_merge_columns = [col for col in df_merge.columns if col != 'PLAN_BOB2']\ndf_merge_columns.insert(4, 'PLAN_BOB2')\ndf_merge = df_merge[df_merge_columns]\n\n# Reordered column APP SUBMITTED_BOB2\ndf_merge_columns = [col for col in df_merge.columns if col != 'APP SUBMITTED_BOB2']\ndf_merge_columns.insert(6, 'APP SUBMITTED_BOB2')\ndf_merge = df_merge[df_merge_columns]\n\n# Reordered column TERM DATE_BOB2\ndf_merge_columns = [col for col in df_merge.columns if col != 'TERM DATE_BOB2']\ndf_merge_columns.insert(8, 'TERM DATE_BOB2')\ndf_merge = df_merge[df_merge_columns]\n\n# Added column 'Name Check'\ndf_merge.insert(11, 'Name Check', CHECK(df_merge['NAME_BOB1'],df_merge['NAME_BOB2']))\n\n# Added column 'Plan Check'\ndf_merge.insert(12, 'Plan Check', CHECK(df_merge['PLAN_BOB1'],df_merge['PLAN_BOB2']))\n\n# Added column 'App Submitted Check'\ndf_merge.insert(13, 'App Submitted Check', CHECK(df_merge['APP SUBMITTED_BOB1'],df_merge['APP SUBMITTED_BOB2']))\n\n# Added column 'Term Check'\ndf_merge.insert(14, 'Term Check', CHECK(df_merge['TERM DATE_BOB1'],df_merge['TERM DATE_BOB2']))\n\n# Added column 'Status Check'\ndf_merge.insert(15, 'Status Check', CHECK(df_merge['STATUS_BOB1'],df_merge['STATUS_BOB2']))\n\n# Formatted dataframes. View these styling objects to see the formatted dataframe\ndf_merge_styler = df_merge.style\\\n    .apply(lambda series: np.where(series == False, 'color: #831100; background-color: #ffb5af', None), subset=['App Submitted Check', 'Term Check', 'Plan Check', 'Name Check', 'Status Check'])\n", "code_options": null, "fully_parameterized_function": "from mitosheet.public.v3 import *\nfrom __main__ import CHECK\nimport pandas as pd\nimport numpy as np\n\ndef function_ycqz(file_name_import_excel_0):\n    sheet_df_dictonary = pd.read_excel(file_name_import_excel_0, engine='openpyxl', sheet_name=[\n        'BOB1',\n        'BOB2'\n    ], skiprows=0)\n    BOB1 = sheet_df_dictonary['BOB1']\n    BOB2 = sheet_df_dictonary['BOB2']\n    \n    temp_df = BOB2.drop_duplicates(subset=['MBI']) # Remove duplicates so lookup merge only returns first match\n    df_merge = BOB1.merge(temp_df, left_on=['MBI'], right_on=['MBI'], how='left', suffixes=['_BOB1', '_BOB2'])\n    \n    df_merge_columns = [col for col in df_merge.columns if col != 'NAME_BOB1']\n    df_merge_columns.insert(1, 'NAME_BOB1')\n    df_merge = df_merge[df_merge_columns]\n    \n    df_merge_columns = [col for col in df_merge.columns if col != 'NAME_BOB2']\n    df_merge_columns.insert(2, 'NAME_BOB2')\n    df_merge = df_merge[df_merge_columns]\n    \n    df_merge_columns = [col for col in df_merge.columns if col != 'PLAN_BOB2']\n    df_merge_columns.insert(4, 'PLAN_BOB2')\n    df_merge = df_merge[df_merge_columns]\n    \n    df_merge_columns = [col for col in df_merge.columns if col != 'APP SUBMITTED_BOB2']\n    df_merge_columns.insert(6, 'APP SUBMITTED_BOB2')\n    df_merge = df_merge[df_merge_columns]\n    \n    df_merge_columns = [col for col in df_merge.columns if col != 'TERM DATE_BOB2']\n    df_merge_columns.insert(8, 'TERM DATE_BOB2')\n    df_merge = df_merge[df_merge_columns]\n    \n    df_merge.insert(11, 'Name Check', CHECK(df_merge['NAME_BOB1'],df_merge['NAME_BOB2']))\n    \n    df_merge.insert(12, 'Plan Check', CHECK(df_merge['PLAN_BOB1'],df_merge['PLAN_BOB2']))\n    \n    df_merge.insert(13, 'App Submitted Check', CHECK(df_merge['APP SUBMITTED_BOB1'],df_merge['APP SUBMITTED_BOB2']))\n    \n    df_merge.insert(14, 'Term Check', CHECK(df_merge['TERM DATE_BOB1'],df_merge['TERM DATE_BOB2']))\n    \n    df_merge.insert(15, 'Status Check', CHECK(df_merge['STATUS_BOB1'],df_merge['STATUS_BOB2']))\n    \n    df_merge_styler = df_merge.style\\\n    .apply(lambda series: np.where(series == False, 'color: #831100; background-color: #ffb5af', None), subset=['App Submitted Check', 'Term Check', 'Plan Check', 'Name Check', 'Status Check'])\n    \n    return BOB1, BOB2, df_merge\n", "param_metadata": [{"original_value": "/Users/aarondiamond-reivich/Desktop/MyPlanAdvocate-streamlit-app/TEST BOB Nov 9.xlsx", "type": "import", "subtype": "file_name_import_excel", "required": false, "name": "file_name_import_excel_0"}], "mito_analysis_version": 1}