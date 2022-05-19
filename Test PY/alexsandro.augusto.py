# #### Shooju Test ####
print(f"\nShooju Test: Alexsandro Augusto Ignácio\n")

# Imports of Libraries

import pandas as pd
import requests
import os
from zipfile import ZipFile
import time
import json

# Constant Variables 
URL =  'https://www.jodidata.org/_resources/files/downloads/gas-data/jodi_gas_csv_beta.zip'
PATH = 'C://Users//alexsandro.ignacio//Downloads' # Where is alexsandro.ignacio change for your user.
TARGET = 'jodi_gas_csv_beta.zip'
NAME_FILE = 'jodi_gas_beta.csv'
NAME_FILE_JSON = 'jodi_gas_beta.json'
ENCOD = 'latin-1'
PATH_FILE = os.path.join(PATH, TARGET)
PATH_FILE_JSON = os.path.join(PATH, NAME_FILE_JSON)
MARK = 60

# Functions
def verify_dirictory(PATH, TARGET):
    # Checking if the file exists
    for dirpath, dirnames, filenames in os.walk(os.path.abspath(PATH)):
        for file in filenames:
            # print(dirpath)
            # print(dirnames)
            if file == TARGET:
                path_file = os.path.join(dirpath, file)
                try:
                    os.remove(path_file)
                    print(f'- File Removed -\n')
                    
                except OSError as e:
                    print(f"Error:{ e.strerror}\n")
            #  print(file)    

# Program
verify_dirictory(PATH, TARGET)        

print(f"## Starting Count Time Download ##\n")
start = time.time()

# Request URL
os.getcwd()
os.chdir(PATH)

reqst = requests.get(URL,  allow_redirects=True)
print(f"Status: {reqst.status_code}")

# Writing File
open(TARGET, 'wb').write(reqst.content)

end = time.time()
print(f"## Time: {round((end - start), 2)} ##")

############# Reading Zip File #############

# Reading data
with ZipFile(PATH_FILE) as file_zip:
    with file_zip.open(NAME_FILE) as file:
        _df = pd.read_csv(file, sep=',', encoding=ENCOD)


print(f"\n")
print(f"#" * MARK)
print(f"\nShape: {_df.shape}\n")
print(f"\n{_df}\n")
print(f"#" * MARK)
print(f"\n")

dict_country = {'AD':'Andorra','AE':'Emirados Árabes Unidos','AF':'Afeganistão','AG':'Antígua e Barbuda','AI':'Anguilla','AL':'Albânia','AM':'Armênia','AN':'Antilhas Holandesas','AO':'Angola','AP':'Organização Regional de Propriedade Industrial Africana','AQ':'Antartica','AR':'Argentina','AS':'Samoa Americana','AT':'Áustria','AU':'Austrália','AW':'Aruba','AZ':'Azerbaidjão','BA':'Bósnia e Herzegóvina','BB':'Barbados','BD':'Bangladesh','BE':'Bélgica','BF':'Burkina Faso','BG':'Bulgária','BH':'Bareine','BI':'Burundi','BJ':'Benin','BM':'Bermudas','BN':'Brunei Darussalam','BO':'Bolívia','BR':'Brasil','BS':'Bahamas','BT':'Butão','BV':'Ilha Bouvet','BW':'Botswana','BX':'Benelux','BY':'Belarus','BZ':'Belize','CA':'Canadá','CC':'Ilhas Cocos','CD':'República Dem. Do Congo','CF':'República Centro Africana','CG':'Congo','CH':'Suíça','CI':'Costa do Marfim','CK':'Ilhas Cook','CL':'Chile','CM':'Camarões','CN':'China','CO':'Colômbia','CR':'Costa Rica','CU':'Cuba','CV':'Cabo Verde','CX':'Ilha Natal','CY':'Chipre','CZ':'República Tcheca','DE':'Alemanha','DJ':'Djibuti','DK':'Dinamarca','DM':'Dominica','DO':'República Dominicana','DZ':'Argélia','EC':'Equador','EE':'Estônia','EG':'Egito','EH':'Saara Ocidental','EM':'Escritório para Harmonização no Mercado Interno','ER':'Eritréia','ES':'Espanha','ET':'Etiópia','FI':'Finlândia','FJ':'Fiji','FK':'Ilhas Malvinas','FM':'Micronésia','FO':'Ilhas Faroe','FR':'França','GA':'Gabão','GB':'Reino Unido','GD':'Granada','GE':'Geórgia','GG':'Ilhas do Canal','GH':'Gana','GI':'Gibraltar','GL':'Groenlândia','GM':'Gambia','GN':'Guine','GP':'Guadalupe','GQ':'Guine Equatorial','GR':'Grécia','GS':'Geórgia do Sul e Ilhas Sandwich do Sul','GT':'Guatemala','GU':'Guam','GW':'Guiné Bissau','GY':'Guiana','HK':'Hong-Kong','HM':'Ilhas Heard e McDonald','HN':'Honduras','HR':'Croácia','HT':'Haiti','HU':'Hungria','ID':'Indonésia','ID':'Indonésia','IE':'Irlanda','IE':'Irlanda','IL':'Israel','IL':'Israel','IM':'Ilha do Homem','IN':'India','IO':'Territ.Britan.Oceano Índico','IQ':'Iraque','IQ':'Iraque','IR':'Irã','IR':'Irã','IS':'Islândia','IS':'Islândia','IT':'Itália','JE':'Jersey','JM':'Jamaica','JO':'Jordânia','JP':'Japão','KE':'Quênia','KG':'Quirguistão','KH':'Camboja','KI':'Kiribati','KM':'Comores','KN':'São Cristovão e Nevis','KP':'República Pop. Dem. da Coreia','KR':'República da Coréia','KW':'Kuwait','KY':'Ilhas Cayman','KZ':'Cazaquistão','LA':'Laos','LB':'Líbano','LC':'Santa Lúcia','LI':'Liechtenstein','LK':'Sri Lanka','LR':'Libéria','LS':'Lesoto','LT':'Lituânia','LU':'Luxemburgo','LV':'Letônia','LY':'Líbia','MA':'Marrocos','MC':'Mônaco','MD':'República da Moldova','ME':'Montenegro','MG':'Madagascar','MH':'Ilhas Marshall','MK':'República da Macedonia','ML':'Mali','MM':'Mianmá','MN':'Mongólia','MO':'Macau','MP':'Ilhas Marianas do Norte','MQ':'Martinica','MR':'Mauritânia','MS':'Mont Serrat','MT':'Malta','MU':'Maurício','MV':'Maldivas','MW':'Malawi','MX':'México','MY':'Malásia','MZ':'Moçambique','NA':'Namíbia','NC':'Nova Caledônia','NE':'Níger','NF':'Ilha Norfalk','NG':'Nigéria','NI':'Nicarágua','NL':'Holanda','NO':'Noruega','NP':'Nepal','NR':'Nauru','NZ':'Nova Zelândia','OA':'Organização Africana de Propriedade Intelectual (OAPI)','OM':'Omã','PA':'Panamá','PE':'Peru','PF':'Polinésia Francesa','PG':'Papua Nova Guiné','PH':'Filipinas','PK':'Paquistão','PL':'Polônia','PM':'Saint Pierre e Miquelon','PN':'Pitcairn','PR':'Porto Rico','PS':'Território Ocupado Palestino','PT':'Portugal','PW':'Palau','PY':'Paraguai','QA':'Catar','RE':'Reunião','RO':'Romênia','RS':'Sérvia','RU':'Federação Russa','RW':'Ruanda','SA':'Arábia Saudita','SB':'Ilhas Salomão','SC':'Seychelles','SD':'Sudão','SE':'Suécia','SG':'Singapura','SH':'Santa Helena','SI':'Eslovenia','SJ':'Svalbard e Jan Mayen','SK':'Eslováquia','SL':'Serra Leoa','SM':'São Marino','SN':'Senegal','SO':'Somália','SR':'Suriname','ST':'São Tomé e Príncipe','SV':'El Salvador','SY':'Síria','SZ':'Suazilândia','TC':'Ilhas Turks e Caicos','TD':'Chade','TF':'Terras Austrais Francesas','TG':'Togo','TH':'Tailândia','TJ':'Tadjiquistão','TK':'Tokelau','TL':'Timor-Leste','TM':'Turcomenistão','TN':'Tunísia','TO':'Tonga','TR':'Turquia','TT':'Trinidad e Tobago','TV':'Tuvalu','TW':'Taiwan','TZ':'República Unida da Tanzânia','UA':'Ucrânia','UG':'Uganda','UM':'Ilhas Menores','US':'Estados Unidos da América','UY':'Uruguai','UZ':'Uzbequistão','VA':'Vaticano','VC':'São Vicente e Granadinas','VE':'Venezuela','VG':'Ilhas Virgens (Britânicas)','VI':'Ilhas Virgens (U.S.)','VN':'Vietnã','VU':'Vanuatu','WF':'Ilhas Wallis e Futura','WO':'Organização Mundial de Propriedade Intelectual – OMPI (WIPO)','WS':'Samoa Ocidental','YE':'Iêmen','YU':'Yugoslávia','ZA':'Africa do Sul','ZM':'Zâmbia','ZR':'Zaire','ZW':'Zimbábue'}

_obj  = []

print(f"\n## Starting Count Time creating json ##\n")
start = time.time()
for index, row in _df.iterrows():
    # print(index, row["TIME_PERIOD"],row["OBS_VALUE"])
    # obj_dict["series_id"] = index
    # obj_dict["points"] = [row["TIME_PERIOD"],row["OBS_VALUE"]]
    # obj_dict["fields"] = {"country":dict_country[row['REF_AREA']], "concept":"Gas World Database", "units":row['UNIT_MEASURE'], "source":"JODI" }
    _obj.append({   
    "series_id":index,
    "points":[row["TIME_PERIOD"],row["OBS_VALUE"]],
    "fields":{
      "country":dict_country[row['REF_AREA']],
      "concept":"Gas World Database",
      "units":row['UNIT_MEASURE'],
      "source":"JODI"
    }})

print(f"\n")
print(f"#" * MARK)
print(f"\n{_obj}\n")
print(f"#" * MARK)
print(f"\n")

verify_dirictory(PATH, NAME_FILE_JSON)

with open (PATH_FILE_JSON, 'w', encoding=ENCOD) as file:
    json.dump(_obj, file, indent=2, ensure_ascii=False)

print(f'- File Created -\n')

end = time.time()
print(f"## Time for creating json: {round((end - start), 2)} ##\n")

