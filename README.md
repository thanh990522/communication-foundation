# Tiếng Anh Giao Tiếp Foundation

Website bài giảng cho khóa **Tiếng Anh Giao Tiếp A1 → A2** (12 tuần · 36 buổi · 90 phút/buổi), giảng viên **Mr. Hà Chí Thanh**.

## Cấu trúc

```
index.html              Trang chủ: 36 buổi theo 4 giai đoạn / 12 tuần
assets/sessions.js      Danh sách bài học + trạng thái (sửa file này khi mở bài mới)
lessons/S01/            Bài 01 (slide trình chiếu)
  index.html            Trang bài học
  audio/                Từng file MP3 (phát trực tiếp + tải về)
  S01_Audio_MP3.zip     Toàn bộ audio của bài
homework/index.html     Trang làm homework (homework/?s=S01)
homework/data/S01.json  Câu hỏi homework (đáp án tự chấm lưu dạng mã băm SHA-256)
homework/audio/S01/     Audio bài nghe của homework
assets/student.js       Đăng nhập học viên (tên + email) & gọi backend
assets/config.js        URL Web App Google Apps Script
backend/Code.gs         Backend: Google Sheet lưu bài nộp, tiến độ; Drive lưu voice note
backend/HUONG_DAN_CAI_DAT.md  Hướng dẫn bật hệ thống homework
tools/lesson-builder/   Công cụ soạn & build lại từng bài (không phải trang web)
tools/homework-builder/ Công cụ soạn homework + tạo audio
```

## Homework & tiến độ cá nhân

- Học viên đăng nhập bằng **tên + email** (lưu trên trình duyệt), làm homework và nộp trực tiếp trên web.
- Phần trắc nghiệm / điền từ / nghe-viết tự chấm ngay; phần viết và voice note gửi về Google Sheet để thầy chấm.
- Mục **Tiến độ của tôi** trên trang chủ: số bài đã nộp, điểm tự chấm, điểm & nhận xét của thầy, bài nên làm tiếp.
- Thầy có thể tự thêm câu hỏi trong tab **Homework** của Google Sheet (xem `backend/HUONG_DAN_CAI_DAT.md`).

## Mở một bài mới

1. Build bài vào `lessons/Sxx/` (xem `tools/lesson-builder/S01/build.sh` làm mẫu).
2. Trong `assets/sessions.js`, đổi `status: "soon"` thành `"live"` và thêm `url`, `zip`, `offline`, `hw`.
3. Commit & push lên `main` — GitHub Pages tự cập nhật sau khoảng 1–2 phút.

## Quy ước thiết kế bài học

- Slide 16:9 kín màn hình, theme xanh dương – vàng trên nền trắng, không thanh điều khiển.
- Chuyển slide: phím ← → (hoặc bút trình chiếu), `F` toàn màn hình, `Esc` dừng audio.
- Flow: Warm-up → Input → Controlled practice → Speaking → Fluency → Wrap-up; ưu tiên thời lượng nói.
- Audio: giọng neural Anh–Anh (Microsoft Sonia / Ryan / Libby qua `edge-tts`); mỗi audio có ▶ phát và ⬇ tải MP3.
- Không có ghi chú giáo viên hay phụ lục trong slide.
