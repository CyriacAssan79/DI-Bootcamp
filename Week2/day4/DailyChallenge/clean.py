import nbformat

input_file = "dailychallenge.ipynb"
output_file = "dailychallenge.ipynb"

# Charger le notebook
with open(input_file, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Supprimer les métadonnées widgets invalides
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

# Nettoyer aussi les cellules
for cell in nb.cells:
    if "widgets" in cell.get("metadata", {}):
        del cell["metadata"]["widgets"]

# Sauvegarder le notebook corrigé
with open(output_file, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("Notebook corrigé :", output_file)