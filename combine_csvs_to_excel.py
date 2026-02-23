"""
Combine CSV Files into One Excel File with Multiple Sheets
This creates an Excel file that Power BI can easily import
"""

import pandas as pd
import openpyxl

print("="*60)
print("Combining CSV Files into Excel for Power BI")
print("="*60)

# Load CSV files
print("\n1. Loading CSV files...")

try:
    matches = pd.read_csv('Collab_Matches_For_PowerBI.csv')
    print(f"✓ Loaded Collab_Matches_For_PowerBI.csv ({len(matches)} rows)")
except FileNotFoundError:
    print("⚠ Collab_Matches_For_PowerBI.csv not found")
    matches = None

try:
    researchers = pd.read_csv('Researcher_Profiles_For_PowerBI.csv')
    print(f"✓ Loaded Researcher_Profiles_For_PowerBI.csv ({len(researchers)} rows)")
except FileNotFoundError:
    print("⚠ Researcher_Profiles_For_PowerBI.csv not found")
    researchers = None

try:
    network = pd.read_csv('network_graph_data.csv')
    print(f"✓ Loaded network_graph_data.csv ({len(network)} rows)")
except FileNotFoundError:
    print("⚠ network_graph_data.csv not found (optional)")
    network = None

try:
    best_matches = pd.read_csv('best_faculty_match.csv')
    print(f"✓ Loaded best_faculty_match.csv ({len(best_matches)} rows)")
except FileNotFoundError:
    print("⚠ best_faculty_match.csv not found (optional)")
    best_matches = None

# Create Excel file with multiple sheets
print("\n2. Creating Excel file with multiple sheets...")

excel_file = 'Collab_Hub_Data.xlsx'

with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
    if matches is not None:
        matches.to_excel(writer, sheet_name='Matches', index=False)
        print(f"✓ Created 'Matches' sheet ({len(matches)} rows)")
    
    if researchers is not None:
        researchers.to_excel(writer, sheet_name='Researchers', index=False)
        print(f"✓ Created 'Researchers' sheet ({len(researchers)} rows)")
    
    if network is not None:
        network.to_excel(writer, sheet_name='Network', index=False)
        print(f"✓ Created 'Network' sheet ({len(network)} rows)")
    
    if best_matches is not None:
        best_matches.to_excel(writer, sheet_name='Best_Matches', index=False)
        print(f"✓ Created 'Best_Matches' sheet ({len(best_matches)} rows)")

print(f"\n✓ Saved: {excel_file}")
print(f"  - File ready for Power BI upload!")
print(f"  - All sheets are in one file")

print("\n" + "="*60)
print("NEXT STEPS:")
print("="*60)
print("1. Upload Collab_Hub_Data.xlsx to Power BI Service")
print("2. Power BI will automatically create a dataset with all sheets")
print("3. Create relationships between sheets (if needed)")
print("4. Build your visualizations!")
print("="*60)



