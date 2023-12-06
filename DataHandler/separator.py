from rdkit import Chem
from rdkit.Chem import AllChem

# Replace 'your_file.sdf' with the path to your SDF file
sdf_file_path = 'PubChem_compound_smiles_substructure_O=C1CCN1_records.sdf'
supplier = Chem.SDMolSupplier(sdf_file_path)

for idx, mol in enumerate(supplier):
    if mol is not None:
        # Create a new SDF writer for each molecule
        writer = Chem.SDWriter(f'results/sdfs/ziad/molecule_{idx+1}.sdf')
        writer.write(mol)      
        writer.close()
