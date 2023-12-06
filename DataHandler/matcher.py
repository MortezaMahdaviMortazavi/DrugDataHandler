import json
import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem


################################# Config #############################
######################################################################

def extract_molecule_info(sdf_file):
    suppl = Chem.SDMolSupplier(sdf_file)
    molecule_info_list = []
    ichis = []
    for mol in suppl:
        if mol is not None:
            molecule_info = {
                'Ligand Name': mol.GetProp('BindingDB Ligand Name'),
                'Reactant_set_id': mol.GetProp('BindingDB Reactant_set_id'),
                'Ligand InChI': mol.GetProp('Ligand InChI'),
                'Ligand InChI Key': mol.GetProp('Ligand InChI Key'),
                'MonomerID': mol.GetProp('BindingDB MonomerID'),
                'Target Name': mol.GetProp('Target Name'),
                'UniProt Primary ID': mol.GetProp('UniProt (SwissProt) Primary ID of Target Chain'),
            }
            ichis.append(mol.GetProp('Ligand InChI'))
            molecule_info_list.append(molecule_info)

    return molecule_info_list,ichis


def group_similar_samples(samples):
    similarity_dict = {}
    output = {}
    deleted_dict = {}
    checkout_list = []
    idx = 1
    for sample in samples:
        # inchi = sample['Ligand InChI']
        inchi = sample
        if inchi not in checkout_list:
            checkout_list.append(inchi)
            output[inchi] = {'Molecule_Number':idx,'similar_to':[]}
        else:
            deleted_dict[idx] = inchi
            output[inchi]['similar_to'].append(idx)
        idx+=1


    return output,deleted_dict

def write_to_json(data,json_file,indent):
    with open(json_file,'w') as _file_:
        json.dump(data,_file_,indent=indent)
 
def read_json_data(json_file):
    with open(json_file,'r') as f:
        return json.load(f)

def write_sentence_to_file(sentence, file_path):
    with open(file_path, "a") as file:
        file.write(sentence)  # Add a newline after each sentence

pd.read_excel('Antibiotics.xlsx')

# main = read_json_data('restructured_data.json')
# delete = read_json_data('deleted_restructured_data.json')
# print(len(main),len(delete),len(delete)+len(main))

json_file_path = 'restructured_data.json'

rec = read_json_data(json_file_path)
ichis = []
for item in rec:
    ichis.append(item['InChI'])
    write_sentence_to_file(item['InChI'],'rec.txt')



# for item in main:
#     write_sentence_to_file(item['InChI'],'main.txt')
# path = 'All_Ligands.txt'
# sdf_path = 'All_Ligands_BindingDB.sdf'
# ichis = extract_molecule_info(sdf_path)[1]
# output_json = 'molecule_non_iterated.json'
# output_txt = 'molecule_non_iterated.txt'
# with open(path,'r') as f:
#     samples = f.readlines()
# samples.extend(ichis)
# print(len(samples))
# restructured_data = []
# output, deleted_dict = group_similar_samples(samples)

# for molecule_inchi, properties in output.items():
#     if molecule_inchi not in ichis:
#         molecule_info = {
#             "Molecule_Number": properties["Molecule_Number"],
#             "InChI": molecule_inchi,
#             "similar_to": properties["similar_to"]
#         }
#         restructured_data.append(molecule_info)

# with open('restructured_data.json', 'w') as json_file:
    # json.dump(restructured_data, json_file, indent=2)

# restructured_data = []
# # # Loop through the original data and restructure it
# for molecule_number, inchi in deleted_dict.items():
#     molecule_info = {
#         "Molecule_Number": int(molecule_number),
#         "InChI": inchi,
#     }
#     restructured_data.append(molecule_info)

# with open('deleted_restructured_data.json', 'w') as json_file:
#     json.dump(restructured_data, json_file, indent=1)

# with open(json_file_path, 'r') as json_file:
#     sampless = json.load(json_file)

# with open('deleted_restructured_data.json', 'r') as json_file:
#     samplesss = json.load(json_file)

# print(len(samples),len(sampless),len(samplesss),len(samplesss)-len(sampless))

# # Save non-similar dictionary to JSON
# with open('first_results/output.json', 'w') as json_file:
#     json.dump(output, json_file)

# # Save deleted dictionary to JSON
# with open('first_results/deleted_dict.json', 'w') as json_file:
#     json.dump(deleted_dict, json_file)

# # Save non-similar dictionary to TXT
# with open('first_results/output.txt', 'w') as txt_file:
#     for idx, inchi in output.items():
#         txt_file.write(f"Index: {idx}, InChI: {inchi}\n")

# # Save deleted dictionary to TXT
# with open('first_results/deleted_dict.txt', 'w') as txt_file:
#     for idx, inchi in deleted_dict.items():
#         txt_file.write(f"Index: {idx}, InChI: {inchi}\n")