Câu hỏi : cấu hình --global được lưu ở đâu? Khác gì so với --local?
- File cấu hình --global được lưu tại thư mục Home (C:\Users\<Tên_User>\.gitconfig).

- Cấu hình này áp dụng cho tất cả repository của người dùng.

- Điểm khác biệt giữa --global và --local là phạm vi áp dụng, vị trí lưu trữ và độ ưu tiên.

- --local chỉ áp dụng cho repository hiện tại, được lưu trong file .git/config nằm trong thư mục .git của repo.

- Độ ưu tiên: --local > --global > --system.

Câu hỏi: Vì sao dùng git mv? release/lab01 có phải baseline? Vì sao không commit thẳng master dù làm một 
mình?

- Dùng git mv vì:

+ Di chuyển hoặc đổi tên file và đưa thay đổi vào staging area mà không cần chạy git add riêng.

+ Git có thể nhận diện lịch sử đổi tên dựa trên sự tương đồng nội dung file.

- release/lab01 đóng vai trò là một baseline, dùng làm cột mốc ổn định cho các bài lab tiếp theo.

- Không commit thẳng vào master để giữ nhánh chính luôn sạch sẽ và ổn định.

+ Cách ly lỗi và thử nghiệm an toàn trên branch riêng, sau khi kiểm tra thành công mới merge vào master.

+ Chia công việc thành các branch và commit riêng biệt để dễ quản lý, theo dõi và sửa lỗi.
