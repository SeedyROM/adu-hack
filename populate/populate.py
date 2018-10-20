import openpyxl
import django
from accounts.models import User, ContractorInformation 
from connections.models import Service
wb = openpyxl.load_workbook('adu_profs.xlsx')
ws = wb.active

des_ser = Service.objects.get_or_create(name='Design',description='Able to design living spaces.')
bui_ser = Service.objects.get_or_create(name='Build',description='Able to build structures.')
oth_ser = Service.objects.get_or_create(name='Other',description='Other')

for row in ws.iter_rows():
	name, design, build, other, url = [c.value for c in row]
	
	if design:
		des_ser.
	

