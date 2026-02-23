"""
Fix Excel File - Remove Blank First Row
The Excel file has a blank first row, so headers are in row 2.
This script removes the blank row so headers are in row 1.
"""

import pandas as pd
import openpyxl
from openpyxl import load_workbook

print("="*60)
print("Fixing Excel File - Removing Blank First Row")
print("="*60)

# Load all CSV files (they have correct headers)
print("\nLoading CSV files...")
sdg_lookup = pd.read_csv('sdg_lookup.csv')
publications = pd.read_csv('Publications_cleaned.csv')
keywords = pd.read_csv('Keywords_cleaned.csv')
sdg_mappings = pd.read_csv('SDG_Mappings_cleaned.csv')

print(f"✓ Loaded all CSV files")
print(f"  Publications: {len(publications)} rows")
print(f"  Headers: {list(publications.columns)[:5]}...")

# Create new Excel file - headers will be in row 1 (no blank row)
print("\n" + "="*60)
print("Creating fixed Excel file (no blank rows)...")
print("="*60)

excel_filename = 'Power_BI_Combined_Data_Fixed.xlsx'

try:
    with pd.ExcelWriter(excel_filename, engine='openpyxl') as writer:
        # Write each dataframe with headers in row 1
        # index=False ensures no extra index column
        # header=True ensures headers are written
        
        sdg_lookup.to_excel(
            writer, 
            sheet_name='sdg_lookup', 
            index=False,  # Don't write row index
            header=True,  # Write column headers
            startrow=0    # Start at row 1 (no blank row)
        )
        print(f"✓ Created sheet: sdg_lookup")
        print(f"  Headers in row 1: {list(sdg_lookup.columns)}")
        
        publications.to_excel(
            writer, 
            sheet_name='Publications', 
            index=False,
            header=True,
            startrow=0
        )
        print(f"✓ Created sheet: Publications")
        print(f"  Headers in row 1: {list(publications.columns)[:5]}...")
        
        keywords.to_excel(
            writer, 
            sheet_name='Keywords', 
            index=False,
            header=True,
            startrow=0
        )
        print(f"✓ Created sheet: Keywords")
        print(f"  Headers in row 1: {list(keywords.columns)}")
        
        sdg_mappings.to_excel(
            writer, 
            sheet_name='SDG_Mappings', 
            index=False,
            header=True,
            startrow=0
        )
        print(f"✓ Created sheet: SDG_Mappings")
        print(f"  Headers in row 1: {list(sdg_mappings.columns)}")
    
    # Verify the file
    print("\n" + "="*60)
    print("Verifying file...")
    print("="*60)
    
    wb = load_workbook(excel_filename)
    sheet = wb['Publications']
    
    # Check row 1 (should be headers)
    row1 = [cell.value for cell in sheet[1]][:5]
    print(f"\nRow 1 (should be headers): {row1}")
    
    # Check row 2 (should be data)
    if len(list(sheet.rows)) > 1:
        row2 = [cell.value for cell in sheet[2]][:5]
        print(f"Row 2 (should be data): {row2}")
    
    print("\n✅ SUCCESS! File created with headers in row 1 (no blank row)")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

print("\n" + "="*60)
print("✅ FIXED FILE READY!")
print("="*60)
print(f"\nNew file: {excel_filename}")
print("\nNext steps:")
print("1. Delete the old dataset in Power BI Service")
print("2. Upload this new file: Power_BI_Combined_Data_Fixed.xlsx to OneDrive")
print("3. Create new dataset from this file")
print("4. Headers should now be recognized correctly in row 1!")
print("5. You should see 'article_uuid' instead of 'Column 1'")





