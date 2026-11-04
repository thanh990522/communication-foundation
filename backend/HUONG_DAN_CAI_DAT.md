# Hướng dẫn bật hệ thống Homework (làm 1 lần, khoảng 5 phút)

Hệ thống lưu bài nộp và tiến độ học viên trong **Google Sheet của thầy**; voice note lưu trong **Google Drive của thầy**.

## Bước 1 — Tạo Google Sheet
1. Mở https://sheets.new (đăng nhập Gmail của thầy).
2. Đặt tên: `GIAO TIEP FOUNDATION - Homework`.

## Bước 2 — Dán mã
1. Trong Sheet: **Tiện ích mở rộng (Extensions) → Apps Script**.
2. Xoá hết nội dung có sẵn trong `Code.gs`, dán toàn bộ nội dung file [`backend/Code.gs`](Code.gs).
3. Bấm 💾 **Lưu**.

## Bước 3 — Cấp quyền
1. Ở thanh trên cùng, chọn hàm **`setup`** → bấm **▶ Chạy (Run)**.
2. Google hỏi quyền → **Xem xét quyền** → chọn tài khoản → **Nâng cao (Advanced)** → **Đi tới … (không an toàn)** → **Cho phép**.
   (Cảnh báo này xuất hiện vì đây là mã của thầy, chưa qua Google duyệt — bình thường.)
3. Quay lại Sheet: sẽ có 3 tab mới **Students**, **Submissions**, **Homework**.

## Bước 4 — Triển khai Web App
1. **Triển khai (Deploy) → Tùy chọn triển khai mới (New deployment)**.
2. Bấm ⚙️ cạnh "Chọn loại" → **Ứng dụng web (Web app)**.
3. **Thực thi dưới dạng (Execute as):** *Tôi (Me)* · **Ai có quyền truy cập (Who has access):** *Bất kỳ ai (Anyone)*.
4. Bấm **Triển khai** → sao chép **URL ứng dụng web** (dạng `https://script.google.com/macros/s/…/exec`).
5. Gửi URL đó cho Claude (hoặc tự dán vào `assets/config.js`).

## Sử dụng hằng ngày
- **Chấm bài:** tab **Submissions** — mỗi lần nộp là 1 dòng. Thầy điền cột **Teacher score** (VD `9/10`), **Teacher feedback**, và đổi **Status** thành `Đã chấm`. Học viên thấy ngay trong mục *Tiến độ của tôi*.
- **Nghe voice note:** cột **Voice notes** có link file trong Drive (thư mục *GIAO TIEP FOUNDATION - Voice notes*).
- **Tự thêm câu hỏi:** tab **Homework**, mỗi dòng 1 câu:
  | Cột | Ý nghĩa |
  |---|---|
  | Session | `S01`, `S02`… |
  | QID | mã câu, không trùng (VD `T1`). Trùng mã câu có sẵn → thay thế câu đó |
  | Section | tên phần (VD `G. Thêm của thầy`) |
  | Type | `mcq` (chọn đáp án) · `gap` (điền từ, prompt có `____`) · `listen_mcq` / `listen_type` (cần Audio URL) · `writing` |
  | Prompt | đề bài |
  | Options | các lựa chọn, cách nhau bằng ` \| ` |
  | Answer | đáp án đúng; nhiều đáp án chấp nhận cách nhau bằng ` \| ` |
  | Audio URL | link MP3 (tuỳ chọn) |
  | Points | điểm |
  | Active | `yes` để hiện, `no` để ẩn |
- **Sửa mã sau này:** dán mã mới → **Triển khai → Quản lý triển khai → ✏️ → Phiên bản mới → Triển khai** (URL giữ nguyên).
