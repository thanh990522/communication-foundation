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
homework/data/S01.json  Câu hỏi + đáp án homework
homework/audio/S01/     Audio bài nghe của homework
tools/lesson-builder/   Công cụ soạn & build lại từng bài (không phải trang web)
tools/homework-builder/ Công cụ soạn homework + tạo audio
```

## Homework

- Học viên làm homework trực tiếp trên web, không cần đăng nhập, không gửi bài.
- Bấm *Nộp bài* → chấm tự động, hiện đáp án đúng; dưới 80% phải làm lại.
- Điểm cao nhất được lưu trên trình duyệt của học viên và hiện trên thẻ bài học ở trang chủ.

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
