"""
Create Excel File for Power BI Service (Web)
This script combines all CSV files into a single Excel workbook with multiple sheets.
This solves the relationship limitations in Power BI Service web version.
"""

import pandas as pd
import os
from datetime import datetime

print("="*60)
print("Creating Excel File for Power BI Service")
print("="*60)

# Check if files exist
required_files = [
    'sdg_lookup.csv',
    'Publications_cleaned.csv',
    'Keywords_cleaned.csv',
    'SDG_Mappings_cleaned.csv'
]

print("\nChecking for required files...")
for file in required_files:
    if os.path.exists(file):
        print(f"✅ Found: {file}")
    else:
        print(f"❌ Missing: {file}")
        print("   Please run prepare_data_for_powerbi.py first!")

print("\n" + "="*60)
print("Loading data files...")
print("="*60)

# Load all CSV files
try:
    sdg_lookup = pd.read_csv('sdg_lookup.csv')
    print(f"✓ Loaded sdg_lookup: {len(sdg_lookup)} rows")
    
    publications = pd.read_csv('Publications_cleaned.csv')
    print(f"✓ Loaded Publications: {len(publications)} rows")
    
    keywords = pd.read_csv('Keywords_cleaned.csv')
    print(f"✓ Loaded Keywords: {len(keywords)} rows")
    
    sdg_mappings = pd.read_csv('SDG_Mappings_cleaned.csv')
    print(f"✓ Loaded SDG_Mappings: {len(sdg_mappings)} rows")
    
except Exception as e:
    print(f"❌ Error loading files: {e}")
    exit(1)

print("\n" + "="*60)
print("Creating Excel workbook...")
print("="*60)

# Create Excel file with multiple sheets
excel_filename = 'Power_BI_Combined_Data.xlsx'

try:
    with pd.ExcelWriter(excel_filename, engine='openpyxl') as writer:
        # Write each dataframe to a separate sheet
        sdg_lookup.to_excel(writer, sheet_name='sdg_lookup', index=False)
        print(f"✓ Created sheet: sdg_lookup ({len(sdg_lookup)} rows)")
        
        publications.to_excel(writer, sheet_name='Publications', index=False)
        print(f"✓ Created sheet: Publications ({len(publications)} rows)")
        
        keywords.to_excel(writer, sheet_name='Keywords', index=False)
        print(f"✓ Created sheet: Keywords ({len(keywords)} rows)")
        
        sdg_mappings.to_excel(writer, sheet_name='SDG_Mappings', index=False)
        print(f"✓ Created sheet: SDG_Mappings ({len(sdg_mappings)} rows)")
    
    print(f"\n✅ Successfully created: {excel_filename}")
    
except Exception as e:
    print(f"❌ Error creating Excel file: {e}")
    print("\nMake sure you have openpyxl installed:")
    print("  pip install openpyxl")
    exit(1)

# Verify file was created
if os.path.exists(excel_filename):
    file_size = os.path.getsize(excel_filename) / (1024 * 1024)  # MB
    print(f"\n📊 File Info:")
    print(f"   Filename: {excel_filename}")
    print(f"   Size: {file_size:.2f} MB")
    print(f"   Sheets: 4")
    
    print("\n" + "="*60)
    print("✅ READY FOR UPLOAD!")
    print("="*60)
    print(f"\nNext steps:")
    print(f"1. Upload '{excel_filename}' to OneDrive")
    print(f"2. In Power BI Service, create dataset from this Excel file")
    print(f"3. Power BI will recognize all 4 sheets")
    print(f"4. Create relationships between sheets in Model view")
    print(f"\nSee POWER_BI_WEB_ONEDRIVE_GUIDE.md for detailed instructions!")
    
else:
    print("❌ Excel file was not created successfully")





