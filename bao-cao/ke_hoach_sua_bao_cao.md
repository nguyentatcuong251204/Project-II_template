# Ke hoach sua bao cao theo file phan bien

Nguon doi chieu:
- File phan bien: `PhanBien_02_NguyenTatCuong.docx`
- Bao cao hien tai: `main.pdf`
- Ma nguon LaTeX: `main.tex`, `chapters/*.tex`, `Bibliography.bib`

Ngay lap ke hoach: 17/06/2026.

## 1. Tom tat ket luan doi chieu

Bao cao hien tai da sua duoc mot phan lon cac gop y trong file phan bien. Cac diem da thay da duoc xu ly gom:
- Da co chuong `KET LUAN` doc lap qua `chapters/conclusion.tex`.
- Da chuyen cach danh so hinh/bang ve dang theo chuong nhu `Hinh 5.1`, `Bang 5.1`, khong con dang `Hinh 5.2.1`.
- Da bo sung so do kien truc lai hai cap trong `chapters/chapter3.tex` bang hinh `images/pipeline.png`.
- Chuong 3 da co bang/phan mo ta tap hop, tham so, bien quyet dinh va don vi co ban cua mo hinh LP cap duoi.
- Chuong 3 da mo ta khong gian quan sat, khong gian hanh dong, anh xa action sang MW va ham thuong cua PPO.
- Chuong 3 da co doan danh gia do phuc tap tinh toan theo so lan goi LP.
- Chuong 5 da them don vi vao header cac bang chinh.
- Chuong 5 da giai thich mau thuan `180 bus` va `179 bus co phu tai`.
- Chuong 5 da khang dinh cac bang/hinh duoc tong hop tu cung mot lan thuc nghiem va chi dung cac phuong phap da chay lai.

Nhung viec con can lam tap trung vao phan dau bao cao, do tin cay so lieu/hinh anh, va chuan hoa tai lieu tham khao.

## 2. Viec can sua uu tien cao

### P1. Bo sung `Loi cam doan`

Gop y lien quan:
- File phan bien danh dau thieu `Loi cam doan` o front matter.

Tinh trang hien tai:
- `main.tex` co `Loi cam on`, `Tom tat`, muc luc, danh muc hinh/bang/ky hieu, nhung chua co `Loi cam doan`.

Ke hoach sua:
- Them mot trang `\chapter*{Loi cam doan}` sau `Loi cam on` hoac truoc `Loi cam on` theo mau Khoa neu co.
- Them vao muc luc bang `\addcontentsline{toc}{chapter}{Loi cam doan}`.
- Noi dung can khang dinh bao cao do sinh vien thuc hien, so lieu/ket qua trung thuc, nguon tham khao duoc trich dan day du.

File can sua:
- `main.tex`

Tieu chi xong:
- `main.pdf` co trang `LOI CAM DOAN`.
- Muc luc hien `Loi cam doan`.

### P2. Hoan thien Chuong 1: doi tuong, phuong phap, y nghia

Gop y lien quan:
- Chuong 1 moi co boi canh, muc tieu, pham vi; thieu `Doi tuong nghien cuu`, `Phuong phap nghien cuu`, `Y nghia khoa hoc va thuc tien`.

Tinh trang hien tai:
- `chapters/chapter1.tex` hien co 3 muc: `Boi canh`, `Muc tieu`, `Pham vi`.

Ke hoach sua:
- Them `\section{Doi tuong nghien cuu}`: neu ro bai toan GEP tren he thong WECC da tien xu ly, quyet dinh dau tu theo vung/cong nghe, va bai toan dieu do LP cap duoi.
- Them `\section{Phuong phap nghien cuu}`: tong hop mo hinh hoa toan hoc, LP cap duoi, BO-TPE, PPO, KKT-LP baseline, Monte Carlo.
- Them `\section{Y nghia khoa hoc va thuc tien}`: nhan manh khung lai BO/PPO + LP, kha nang danh gia danh doi chi phi - tin cay, va gioi han ung dung trong mo hinh xap xi.

File can sua:
- `chapters/chapter1.tex`

Tieu chi xong:
- Chuong 1 tra loi du boi canh, muc tieu, doi tuong, pham vi, phuong phap, y nghia.
- Khong lap y qua nhieu voi Chuong 2 va Chuong 3.

### P3. Ra soat nhat quan so lieu chu - bang trong Chuong 5

Gop y lien quan:
- File phan bien yeu cau kiem tra cac so nhu `45.5%`, `349.364 -> 125.336 GWh`, `2.995 ty USD` co khop bang goc hay khong.

Tinh trang hien tai:
- Cac so trong doan phan tich Chuong 5 co ve khop voi cac bang trong `chapters/chapter5.tex`, nhung file phan bien nhan manh can doi chieu voi ket qua goc, khong chi doi chieu OCR/PDF.

Ke hoach sua:
- Doi chieu tung con so trong doan van Chuong 5 voi bang ket qua/thuc nghiem goc.
- Lap bang kiem tra noi bo: so lieu trong bang LaTeX, so lieu trong cau phan tich, nguon file ket qua.
- Neu phat hien lech, sua ca bang va doan phan tich theo cung mot nguon.

File can sua:
- `chapters/chapter5.tex`
- Cac file ket qua goc neu co trong thu muc thuc nghiem/ma nguon ben ngoai bao cao.

Tieu chi xong:
- Khong con con so nao trong chu khac bang.
- Moi so quan trong co the truy ve mot nguon ket qua cu the.

### P4. Xuat lai cac hinh bi loi font/dau tieng Viet

Gop y lien quan:
- Hinh trong Chuong 5 bi loi dau tieng Viet theo file phan bien.

Tinh trang hien tai:
- Bao cao hien dung cac anh:
  - `images/results_chap5/chap5_penalty_comparison.png`
  - `images/results_chap5/chap5_convergence_summary.png`
  - `images/results_chap5/large_scale_eval/large_scale_penalty_comparison.png`
  - `images/results_chap5/large_scale_eval/large_scale_box_plots.png`
- Can mo/kiem tra anh goc de xac nhan con loi font hay khong.

Ke hoach sua:
- Mo tung anh PNG o Chuong 5, kiem tra nhan truc, tieu de, legend.
- Xuat lai hinh bang font ho tro tieng Viet, uu tien `DejaVu Sans`, `Arial`, hoac font Unicode san co.
- Neu co the, can nhac dung label tieng Anh ngan gon de tranh loi font trong matplotlib.

File can sua/thay:
- Cac PNG trong `images/results_chap5/`.
- Script ve hinh goc neu co.

Tieu chi xong:
- Khong con chu bi loi dau trong hinh.
- Chu trong hinh ro khi phong to PDF.

## 3. Viec can sua uu tien trung binh

### P5. Bo sung thong ke do lech chuan/khoang tin cay cho danh gia 800 kich ban

Gop y lien quan:
- Bang 800 kich ban nen kem `mean +/- std` hoac khoang tin cay.

Tinh trang hien tai:
- `chapters/chapter5.tex` muc `Danh gia quy mo lon tren 800 kich ban` moi trinh bay phan tram cai thien trung binh theo nhom, chua co std/CI.

Ke hoach sua:
- Tu du lieu 800 kich ban goc, tinh them do lech chuan theo tung nhom cho `Delta Penalty%` va `Delta Shed%`, hoac CI 95%.
- Neu bang hien tai qua rong, them mot bang phu rut gon hoac chuyen std/CI vao phan mo ta sau bang.
- Neu chua co du lieu goc trong thu muc bao cao, can lay tu pipeline thuc nghiem truoc khi viet so.

File can sua:
- `chapters/chapter5.tex`
- Script/tap tin ket qua goc neu co.

Tieu chi xong:
- Phan 800 kich ban co it nhat mot chi bao bien thien: `std`, `CI 95%`, hoac boxplot duoc giai thich ro.

### P6. Chuan hoa va ra soat tai lieu tham khao

Gop y lien quan:
- Kiem tra thu tu IEEE, doi chieu trich dan noi van voi danh muc, web co ngay truy cap.

Tinh trang hien tai:
- `biblatex` dang dung `style=ieee`, `sorting=none`.
- `Bibliography.bib` co nhieu muc `url` nhung chua thay `urldate`.

Ke hoach sua:
- Chay build va kiem tra warning `undefined citations`, `empty bibliography`, `missing fields`.
- Them `urldate = {2026-06-17}` cho cac muc web/arXiv/dataset co URL neu can theo yeu cau Khoa.
- Doi chieu moi `\cite{...}` trong cac file `.tex` voi key trong `Bibliography.bib`.
- Kiem tra danh muc cuoi PDF co dung thu tu xuat hien trong noi dung.

File can sua:
- `Bibliography.bib`
- Cac file `.tex` neu co key trich dan sai.

Tieu chi xong:
- Build khong bao citation bi thieu.
- Cac tai lieu online/dataset co URL va ngay truy cap neu mau yeu cau.

### P7. Lam ro tinh moi/dong gop trong Ket luan

Gop y lien quan:
- Ket luan nen neu ro tinh moi cua khung lai BO/PPO + LP cho GEP.

Tinh trang hien tai:
- `chapters/conclusion.tex` da co 3 ket luan chinh, nhung chua co doan rieng ve dong gop/tinh moi va chua tra loi truc tiep tung muc tieu o Chuong 1.

Ke hoach sua:
- Them mot doan mo dau hoac cuoi ket luan: dong gop chinh la khung danh gia lai hai cap, cap tren BO/PPO, cap duoi LP, so sanh voi KKT-LP, danh gia bang Monte Carlo/800 kich ban.
- Them cau noi ro cac ket qua da tra loi cac muc tieu nghien cuu trong Chuong 1.

File can sua:
- `chapters/conclusion.tex`

Tieu chi xong:
- Ket luan doc lap, khong chi tom tat Chuong 5.
- Co cau khang dinh dong gop va gioi han pham vi.

## 4. Viec can sua uu tien thap / kiem tra lai

### P8. Kiem tra trang nhan xet GVHD

Gop y lien quan:
- Trang nhan xet GVHD bi de trong, dac biet muc `Y thuc lam viec`.

Tinh trang hien tai:
- `main.tex` da co noi dung cho muc 1 va 2, nhung muc 3 van de trong cac dong `(a)`, `(b)`, `(c)`.

Ke hoach sua:
- Neu Khoa/GVHD yeu cau SV khong tu dien nhan xet, giu de trong va gui GVHD dien.
- Neu duoc phep dien goi y, bo sung noi dung ngan gon ve thai do lam viec, tinh chu dong, kha nang tiep thu gop y.

File can sua:
- `main.tex`

Tieu chi xong:
- Trang nhan xet khong con bi danh gia la bo trong bat thuong, hoac co ly do ro rang la cho GVHD dien.

### P9. Kiem tra lai so luong hinh

Gop y lien quan:
- Ban phan bien cho rang chi co 4 hinh, it cho mot DATN.

Tinh trang hien tai:
- Da co them so do pipeline va cac hinh Chuong 5. Can kiem tra danh muc hinh sau build de dem chinh xac.

Ke hoach sua:
- Chay build, xem `Danh muc hinh ve`.
- Neu van qua it, them hinh minh hoa Pareto chi phi - do tin cay hoac so do luong BO/PPO neu co du lieu.

File can sua:
- `chapters/chapter3.tex`
- `chapters/chapter5.tex`
- Thu muc `images/`

Tieu chi xong:
- Danh muc hinh co du so hinh phuc vu mo hinh va ket qua, khong chen hinh trang tri.

## 5. Thu tu thuc hien de toi uu cong sua

1. Sua cac muc khong phu thuoc du lieu: P1, P2, P7.
2. Kiem tra/build PDF lan 1 de dam bao muc luc, danh muc, so trang, cross-reference on dinh.
3. Xu ly cac muc phu thuoc ket qua goc: P3, P5.
4. Xuat lai hinh va thay PNG: P4.
5. Ra soat tai lieu tham khao: P6.
6. Quyet dinh trang nhan xet GVHD va so luong hinh: P8, P9.
7. Build lan cuoi bang quy trinh `xelatex -> biber -> xelatex -> xelatex`, sau do kiem tra `main.log` va doc lai `main.pdf`.

## 6. Checklist nghiem thu cuoi

- [ ] Co `Loi cam doan` trong PDF va muc luc.
- [ ] Chuong 1 co du doi tuong, phuong phap, y nghia.
- [ ] Ket luan doc lap va neu ro dong gop/tinh moi.
- [ ] Tat ca so lieu trong Chuong 5 khop giua bang, chu va nguon ket qua goc.
- [ ] Phan 800 kich ban co std/CI hoac ly giai bien thien tu boxplot.
- [ ] Hinh Chuong 5 khong loi font/dau tieng Viet.
- [ ] Tai lieu tham khao khong thieu key, dung thu tu IEEE, muc online/dataset co URL va ngay truy cap neu can.
- [ ] Trang nhan xet GVHD duoc dien hoac de trong dung quy trinh.
- [ ] Build cuoi khong co warning nghiem trong ve citation, reference, overfull hbox lon.
