import json

from rdkit import Chem
from rdkit.Chem import AllChem


################################# Config #############################
######################################################################

def extract_molecule_info(sdf_file):
    suppl = Chem.SDMolSupplier(sdf_file)
    molecule_info_list = []

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
            molecule_info_list.append(molecule_info)

    return molecule_info_list


def group_similar_samples(samples):
    similarity_dict = {}
    non_iterated_dict = {}

    for sample in samples:
        inchi = sample['Ligand InChI']
        if inchi not in similarity_dict:
            similarity_dict[inchi] = [sample]
            non_iterated_dict[inchi] = sample
        else:
            similar_samples = similarity_dict[inchi]
            similar_samples.append(sample)
    
    return similarity_dict, non_iterated_dict

if __name__ == "__main__":
    json_file_path = 'molecule_info.json'
    with open(json_file_path, 'r') as json_file:
        samples = json.load(json_file)
    # # Group similar samples based on InChI Key
    grouped_samples = group_similar_samples(samples)[1]
    # print(len(grouped_samples),len(samples))
    # print(samples[1])#['Ligand InChI'])
    # print(samples[16])#['Ligand InChI'])
    print(len(list(grouped_samples)))
