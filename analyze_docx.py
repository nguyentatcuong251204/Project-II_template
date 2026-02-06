import zipfile
import xml.etree.ElementTree as ET
import os

docx_path = 'Do_an_template.docx'

def analyze_docx(path):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return

    try:
        with zipfile.ZipFile(path, 'r') as z:
            # Analyze document.xml for page margins
            if 'word/document.xml' in z.namelist():
                xml_content = z.read('word/document.xml')
                root = ET.fromstring(xml_content)
                
                namespaces = {
                    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
                }
                
                # Find sectPr (Section Properties)
                # It can be direct child of body or inside p/pPr
                body = root.find('w:body', namespaces)
                if body is not None:
                    sectPr = body.find('w:sectPr', namespaces)
                    if sectPr is not None:
                         pgMar = sectPr.find('w:pgMar', namespaces)
                         if pgMar is not None:
                             print("Page Margins:")
                             for attr in pgMar.attrib:
                                 # 1440 twips = 1 inch = 2.54 cm
                                 # 1 cm = 567 twips
                                 val = int(pgMar.attrib[attr])
                                 cm_val = val / 567.0
                                 print(f"  {attr}: {val} twips (~{cm_val:.2f} cm)")
                    else:
                        print("No direct sectPr found in body.")
            
            # Analyze font size/styles from styles.xml
            if 'word/styles.xml' in z.namelist():
                xml_content = z.read('word/styles.xml')
                root = ET.fromstring(xml_content)
                namespaces = {
                    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
                }
                
                print("\nStyles Analysis (Normal/Default):")
                # Look for 'Normal' style
                for style in root.findall('w:style', namespaces):
                    style_id = style.get(f"{{{namespaces['w']}}}styleId")
                    if style_id == 'Normal':
                        rPr = style.find('w:rPr', namespaces)
                        if rPr is not None:
                            sz = rPr.find('w:sz', namespaces)
                            if sz is not None:
                                # value is in half-points. 24 = 12pt
                                val = int(sz.get(f"{{{namespaces['w']}}}val"))
                                print(f"  Normal Font Size: {val} half-points ({val/2} pt)")
                            else:
                                print(f"  Normal Font Size: Default (usually 11 or 12pt)")
                            
                            rFonts = rPr.find('w:rFonts', namespaces)
                            if rFonts is not None:
                                ascii_font = rFonts.get(f"{{{namespaces['w']}}}ascii")
                                print(f"  Normal Font: {ascii_font}")
                        else:
                            print("  Normal style has no explicit run properties.")

    except Exception as e:
        print(f"Error reading docx: {e}")

if __name__ == "__main__":
    analyze_docx(docx_path)
