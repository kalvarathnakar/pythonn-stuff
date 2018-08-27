import pandas as pd


object_detection_dict ={"TropicanaApple":4,'Cap':19,"TropicanaOrange":4}
output_data={}
for key,value in object_detection_dict.items():
	try:
		output_data[key].append(value)
	except Exception as e:
		output_data[key]=[value]
print output_data


# Create a Pandas dataframe from some data.
df = pd.DataFrame(output_data)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1',index=0)

# Close the Pandas Excel writer and output the Excel file.
writer.save()