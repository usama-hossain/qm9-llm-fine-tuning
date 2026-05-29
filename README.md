# QM9 Dataset Split

Our project uses the QM9 dataset (yairschiff/qm9). Our dataset is split into train, validation, and test sets.

## Dataset Information

The dataset is stored in Parquet format. The features include:

- **num_atoms**: Number of atoms (int64)
- **atomic_symbols**: List of atomic symbols (string)
- **pos**: 3D positions (list of float64)
- **charges**: Atomic charges (list of float64)
- **harmonic_oscillator_frequencies**: Vibrational frequencies (list of float64)
- **smiles**: SMILES string
- **inchi**: InChI string
- **A, B, C**: Rotational constants (float64)
- **mu**: Dipole moment (float64)
- **alpha**: Isotropic polarizability (float64)
- **homo**: Highest occupied molecular orbital energy (float64)
- **lumo**: Lowest unoccupied molecular orbital energy (float64)
- **gap**: HOMO-LUMO gap (float64)
- **r2**: Electronic spatial extent (float64)
- **zpve**: Zero-point vibrational energy (float64)
- **u0**: Internal energy at 0K (float64)
- **u**: Internal energy at 298.15K (float64)
- **h**: Enthalpy at 298.15K (float64)
- **g**: Free energy at 298.15K (float64)
- **cv**: Heat capacity at 298.15K (float64)
- **canonical_smiles**: Canonical SMILES (string)
- **logP**: Octanol-water partition coefficient (float64)
- **qed**: Quantitative Estimate of Drug-likeness (float64)
- **np_score**: Natural product-likeness score (float64)
- **sa_score**: Synthetic accessibility score (float64)
- **ring_count**: Number of rings (int64)
- **R3-R9**: Ring counts by size (int64)
- **single_bond, double_bond, triple_bond, aromatic_bond**: Bond counts (int64)

## Splits

The dataset was split using `download_data.py`:
- **Train**: 80% (107,109 examples)
- **Validation**: 10% (13,388)
- **Test**: 10% (13,388)

## Usage

To load the dataset, use the `datasets` library:

```python
from datasets import load_from_disk

train_data = load_from_disk("./qm9_split_train")
val_data = load_from_disk("./qm9_split_val")
test_data = load_from_disk("./qm9_split_test")
```
