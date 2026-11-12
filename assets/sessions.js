/* =============================================================
   DANH SÁCH BÀI HỌC — chỉ cần sửa file này khi mở bài mới
   Mở một bài: đổi status từ 'soon' thành 'live' và thêm url, zip
   ============================================================= */
window.PHASES = [
  {n:1, name:'Nén A1 & kích hoạt', weeks:[1,3], focus:'Alphabet/IPA, lexical chunks, routines, transactions, repair phrases', product:'9 voice notes + 3 simulations'},
  {n:2, name:'A2 Expansion I', weeks:[4,6], focus:'Past, future, health, advice', product:'Story + plan + health simulation'},
  {n:3, name:'A2 Expansion II', weeks:[7,9], focus:'Travel, experiences, comparison, description', product:'Travel problem + life interview'},
  {n:4, name:'Integration & Fluency', weeks:[10,12], focus:'Opinions, complaints, work, presentation', product:'A2 portfolio + action plan'}
];
window.SESSIONS = [
 {
  "id": "S01",
  "week": 1,
  "title": "Alphabet & Spelling Out Loud",
  "goal": "Đọc đúng tên 26 chữ cái theo 7 nhóm âm; nghe và đánh vần tên, email; hỏi lại khi chưa nghe rõ.",
  "status": "live",
  "url": "lessons/S01/",
  "zip": "lessons/S01/S01_Audio_MP3.zip",
  "offline": "lessons/S01/S01_offline.html",
  "hw": "homework/?s=S01"
 },
 {
  "id": "S02",
  "week": 1,
  "title": "Routines, Habits & Real Schedules",
  "goal": "Mô tả lịch ngày thường và hỏi sâu về thói quen của người khác.",
  "status": "live",
  "url": "lessons/S02/",
  "zip": "lessons/S02/S02_Audio_MP3.zip",
  "offline": "lessons/S02/S02_offline.html",
  "hw": "homework/?s=S02"
 },
 {
  "id": "S03",
  "week": 1,
  "title": "People, Homes & Neighbourhoods",
  "goal": "Mô tả một người và nơi sống, đồng thời giải thích điều mình thích hoặc không thích.",
  "status": "live",
  "url": "lessons/S03/",
  "zip": "lessons/S03/S03_Audio_MP3.zip",
  "offline": "lessons/S03/S03_offline.html",
  "hw": "homework/?s=S03"
 },
 {
  "id": "S04",
  "week": 2,
  "title": "Time, Appointments & Arrangements",
  "goal": "Sắp xếp, xác nhận và đổi lịch hẹn một cách lịch sự.",
  "status": "closed",
  "url": "lessons/S04/",
  "zip": "lessons/S04/S04_Audio_MP3.zip",
  "offline": "lessons/S04/S04_offline.html",
  "hw": "homework/?s=S04"
 },
 {
  "id": "S05",
  "week": 2,
  "title": "Directions & Getting Around Town",
  "goal": "Hỏi, hiểu và đưa chỉ đường nhiều bước dựa trên mốc địa điểm.",
  "status": "soon"
 },
 {
  "id": "S06",
  "week": 2,
  "title": "Food, Shopping Lists & Quantities",
  "goal": "Lập danh sách mua sắm, hỏi số lượng và xử lý trường hợp thiếu hàng.",
  "status": "soon"
 },
 {
  "id": "S07",
  "week": 3,
  "title": "Eating Out: From Menu to Bill",
  "goal": "Đặt món, hỏi gợi ý, nêu yêu cầu ăn uống và thanh toán.",
  "status": "soon"
 },
 {
  "id": "S08",
  "week": 3,
  "title": "Shopping, Sizes, Returns & Refunds",
  "goal": "Tìm sản phẩm phù hợp, thử đồ và yêu cầu đổi hoặc hoàn tiền.",
  "status": "soon"
 },
 {
  "id": "S09",
  "week": 3,
  "title": "Everyday Services & Polite Requests",
  "goal": "Yêu cầu dịch vụ, giải thích vấn đề và xác nhận giải pháp.",
  "status": "soon"
 },
 {
  "id": "S10",
  "week": 4,
  "title": "Past Events: What Happened?",
  "goal": "Kể về cuối tuần hoặc một sự kiện đã hoàn thành với thời gian rõ ràng.",
  "status": "soon"
 },
 {
  "id": "S11",
  "week": 4,
  "title": "Past Questions & Storytelling",
  "goal": "Hỏi chi tiết và kể một sự việc theo trình tự có mở đầu, diễn biến và kết thúc.",
  "status": "soon"
 },
 {
  "id": "S12",
  "week": 4,
  "title": "Checkpoint 1: Everyday Life Simulation",
  "goal": "Tích hợp nội dung Buổi 1–11 trong ba tình huống và tự sửa khi bị gián đoạn giao tiếp.",
  "status": "soon"
 },
 {
  "id": "S13",
  "week": 5,
  "title": "Plans, Goals & Intentions",
  "goal": "Trình bày kế hoạch 3–12 tháng và giải thích lý do, bước thực hiện.",
  "status": "soon"
 },
 {
  "id": "S14",
  "week": 5,
  "title": "Invitations & Social Arrangements",
  "goal": "Mời, nhận lời, từ chối và sắp xếp lại một hoạt động xã hội.",
  "status": "soon"
 },
 {
  "id": "S15",
  "week": 5,
  "title": "Predictions, Decisions & Offers",
  "goal": "Đưa ra dự đoán, quyết định tức thời, lời hứa và đề nghị giúp đỡ.",
  "status": "soon"
 },
 {
  "id": "S16",
  "week": 6,
  "title": "Symptoms & Describing Health Problems",
  "goal": "Mô tả triệu chứng, mức độ, thời gian và ảnh hưởng đến sinh hoạt.",
  "status": "soon"
 },
 {
  "id": "S17",
  "week": 6,
  "title": "Advice, Rules & Obligation",
  "goal": "Đưa lời khuyên và phân biệt điều bắt buộc, bị cấm hoặc không cần thiết.",
  "status": "soon"
 },
 {
  "id": "S18",
  "week": 6,
  "title": "At the Clinic & Pharmacy",
  "goal": "Đặt lịch, hiểu hướng dẫn dùng thuốc và hỏi lại thông tin quan trọng.",
  "status": "soon"
 },
 {
  "id": "S19",
  "week": 7,
  "title": "Public Transport & Tickets",
  "goal": "Hỏi tuyến đường, mua vé, đổi chuyến và xác nhận thông tin khởi hành.",
  "status": "soon"
 },
 {
  "id": "S20",
  "week": 7,
  "title": "Hotels & Travel Services",
  "goal": "Nhận phòng, hỏi tiện ích, đưa yêu cầu và báo vấn đề tại khách sạn.",
  "status": "soon"
 },
 {
  "id": "S21",
  "week": 7,
  "title": "Checkpoint 2: Travel Problems",
  "goal": "Xử lý chậm chuyến, thất lạc đồ hoặc dịch vụ không đúng và thương lượng giải pháp.",
  "status": "soon"
 },
 {
  "id": "S22",
  "week": 8,
  "title": "Life Experiences: Have You Ever…?",
  "goal": "Hỏi và trả lời về trải nghiệm, sau đó hỏi thêm chi tiết quá khứ.",
  "status": "soon"
 },
 {
  "id": "S23",
  "week": 8,
  "title": "Recent Events & Unfinished Time",
  "goal": "Nói về việc vừa xảy ra, đã hoàn thành hoặc chưa hoàn thành và nêu thời gian khi cần.",
  "status": "soon"
 },
 {
  "id": "S24",
  "week": 8,
  "title": "Life Milestones & Personal Interviews",
  "goal": "Mô tả hành trình cá nhân bằng trải nghiệm tổng quát và các sự kiện có thời gian cụ thể.",
  "status": "soon"
 },
 {
  "id": "S25",
  "week": 9,
  "title": "Comparing Everyday Options",
  "goal": "So sánh hai hoặc ba lựa chọn và đưa ra quyết định dựa trên tiêu chí thực tế.",
  "status": "soon"
 },
 {
  "id": "S26",
  "week": 9,
  "title": "Recommendations & Best Choices",
  "goal": "Đưa đề xuất về địa điểm, món ăn hoặc hoạt động và giải thích vì sao đáng trải nghiệm.",
  "status": "soon"
 },
 {
  "id": "S27",
  "week": 9,
  "title": "Describing Places with Useful Detail",
  "goal": "Mô tả người, vật và nơi chốn bằng mệnh đề quan hệ đơn giản.",
  "status": "soon"
 },
 {
  "id": "S28",
  "week": 10,
  "title": "Opinions, Reasons & Examples",
  "goal": "Đưa ý kiến rõ ràng với ít nhất hai lý do và một ví dụ.",
  "status": "soon"
 },
 {
  "id": "S29",
  "week": 10,
  "title": "Agreeing, Disagreeing & Keeping Discussion Going",
  "goal": "Đồng ý hoặc không đồng ý lịch sự, phản hồi ý kiến và đặt câu hỏi mở rộng.",
  "status": "soon"
 },
 {
  "id": "S30",
  "week": 10,
  "title": "Checkpoint 3: Complaints & Problem Solving",
  "goal": "Đưa phàn nàn lịch sự, giải thích tác động và thương lượng giải pháp chấp nhận được.",
  "status": "soon"
 },
 {
  "id": "S31",
  "week": 11,
  "title": "Skills, Strengths & Development",
  "goal": "Mô tả khả năng hiện tại, khả năng quá khứ và kỹ năng đang phát triển.",
  "status": "soon"
 },
 {
  "id": "S32",
  "week": 11,
  "title": "Work, Study, Rules & Responsibilities",
  "goal": "Giải thích nhiệm vụ, quy định, quyền lựa chọn và xin phép trong môi trường học tập/công việc.",
  "status": "soon"
 },
 {
  "id": "S33",
  "week": 11,
  "title": "Phone Calls, Messages & Workplace Small Talk",
  "goal": "Thực hiện cuộc gọi cơ bản, để lại lời nhắn và duy trì small talk trước công việc chính.",
  "status": "soon"
 },
 {
  "id": "S34",
  "week": 12,
  "title": "Personal Story & Short Presentation",
  "goal": "Thực hiện bài nói 2–3 phút có mở bài, trình tự rõ, điểm nhấn và kết luận.",
  "status": "soon"
 },
 {
  "id": "S35",
  "week": 12,
  "title": "Integrated Real-life Rotation",
  "goal": "Chuyển linh hoạt giữa sáu tình huống đời thực và duy trì giao tiếp khi thiếu từ.",
  "status": "soon"
 },
 {
  "id": "S36",
  "week": 12,
  "title": "Final A2 Performance Assessment",
  "goal": "Chứng minh năng lực A2 qua phỏng vấn, tình huống chức năng, kể chuyện và tương tác tự do.",
  "status": "soon"
 }
];
