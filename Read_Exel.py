import pandas as pd

def read_recipe_file(md_recipe):
	xls = pd.ExcelFile(md_recipe)
	data = pd.read_excel(xls, 'RECIPE', keep_default_na=False, converters={'RECIPE':str, 'Categories':str, current_location:str})

	for idx in data.index:
		if data['RECIPE'][idx] == '':
			break
		else:
			if data[current_location][idx] == '-':
				pass
			else:
				next_loc_list.update({data['RECIPE'][idx]: [data['Categories'][idx], data[current_location][idx]]})

	print('****************************')
	print('***** List of NEXT_LOC *****')
	print('****************************')
	##print(next_loc_list)
	for i in next_loc_list:
		print('RECIPE : {} | Categories : {} | NEXT_LOC : {}'.format(i, next_loc_list[i][0], next_loc_list[i][1]))
	print()

	data = pd.read_excel(xls, 'MD_REJECT_REASON', keep_default_na=False, converters={'RECIPE':str, 'Categories':str, equip_id:str})
	for idx in data.index:
		if data['RECIPE'][idx] == '':
			break
		else:
			if data[equip_id][idx] == '-':
				pass
			else:
				md_reject_reason_list.update({data['RECIPE'][idx]: [data['Categories'][idx], data[equip_id][idx].split(',\n')]})

	print('************************************')
	print('***** List of MD_REJECT_REASON *****')
	print('************************************')
	##print(md_reject_reason_list)
	for i in md_reject_reason_list:
		print('RECIPE : {} | Categories : {} | MD_REJECT_REASON : {}'.format(i, md_reject_reason_list[i][0], md_reject_reason_list[i][1]))
	print()

	data = pd.read_excel(xls, 'MD_STATUS', keep_default_na=False, converters={'GROUP':str, 'CATEGORIES':str, 'MD_STATUS':str})
	for idx in data.index:
		if data['MD_STATUS'][idx] == '':
			break
		else:
			if data['GROUP'][idx] == ('FA Hold'):
				fa_hold_list.update({data['MD_STATUS'][idx]: data['CATEGORIES'][idx]})
			elif data['GROUP'][idx] == ('Non Prodcution'):
				non_production_list.update({data['MD_STATUS'][idx]: data['CATEGORIES'][idx]})
			else:
				pass

	print('************************************')
	print('********* List of FA Hold **********')
	print('************************************')
	##print(fa_hold_list)
	for i in fa_hold_list:
		print('MD_STATUS : {} | {}'.format(i, fa_hold_list[i]))
	print()


	print('************************************')
	print('****** List of Non Production ******')
	print('************************************')
	##print(non_production_list)
	for i in non_production_list:
		print('MD_STATUS : {} | {}'.format(i, non_production_list[i]))
	print()

equip_id = 'DIAG_APP'
current_location = 'ASRS'		# to get NEXT_LOC as ASRS
next_loc_list = {}
md_reject_reason_list = {}
fa_hold_list = {}
non_production_list = {}

md_recipe = 'MiniDeckRecipe.xlsx'
read_recipe_file(md_recipe)