import zipfile
import xml.etree.ElementTree as ET

docx_path = r'D:\do-an-tot-nghiep\bao-cao\Sinh Vien_ PhuLuc_HuongDanThucHienDATT_SV.docx'
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

with zipfile.ZipFile(docx_path, 'r') as z:
    with z.open('word/document.xml') as f:
        content = f.read().decode('utf-8')
    
    root = ET.fromstring(content)
    body = root.find('.//w:body', ns)
    paragraphs = body.findall('w:p', ns)
    
    for i, para in enumerate(paragraphs[130:185], start=130):
        pPr = para.find('w:pPr', ns)
        style = ''
        numPr = ''
        if pPr is not None:
            pStyle = pPr.find('w:pStyle', ns)
            if pStyle is not None:
                style = pStyle.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', '')
            np = pPr.find('w:numPr', ns)
            if np is not None:
                ilvl = np.find('w:ilvl', ns)
                if ilvl is not None:
                    numPr = 'ilvl=' + ilvl.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val')
        
        texts = []
        for run in para.findall('.//w:r', ns):
            t = run.find('w:t', ns)
            if t is not None and t.text:
                texts.append(t.text)
        
        text = ' '.join(texts).strip()
        
        sizes = set()
        for rPr in para.findall('.//w:rPr', ns):
            sz = rPr.find('w:sz', ns)
            if sz is not None:
                val = sz.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val')
                if val:
                    sizes.add(str(int(val)//2) + 'pt')
        
        if text:
            print(f'[{i:03d}] Style:{style:20} {numPr:10} Size:{str(list(sizes)):15} | {text[:90]}')
