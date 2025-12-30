# 🧱 HAND BLOCK BLAST - GAME XẾP GẠCH AI

**Hand Block Blast** là sự kết hợp độc đáo giữa dòng game xếp gạch trí tuệ kinh điển (kiểu *1010!*) và công nghệ **Thị giác máy tính (Computer Vision)** hiện đại.

Thay vì sử dụng chuột hay màn hình cảm ứng, người chơi sẽ tương tác trực tiếp với các khối gạch thông qua **Webcam**. Hệ thống AI sẽ biến ngón tay của bạn thành công cụ điều khiển chính xác, mang lại trải nghiệm tương tác "không chạm" đầy thú vị.

![Demo Banner]<img width="1094" height="763" alt="Screenshot 2025-12-30 152627" src="https://github.com/user-attachments/assets/6ffcbdd8-e44b-4b35-9420-c9d49e7b25c7" />

## ✨ Tính Năng Nổi Bật

* **Công nghệ AI Tracking:** Sử dụng MediaPipe để nhận diện khớp tay thời gian thực với độ trễ cực thấp.
* **Cơ chế "Thumb Control" (Điều khiển Ngón Cái):** Tính năng độc đáo giúp thả khối gạch chính xác tuyệt đối tại vị trí ngón cái, khắc phục điểm yếu khó căn chỉnh của các game hand-tracking thông thường.
* **Hệ thống Khóa Tay Thông Minh:** Tự động khóa mục tiêu vào bàn tay đầu tiên xuất hiện, giúp game không bị nhiễu khi có người khác đi qua khung hình.
* **Hệ thống Âm thanh Phản hồi:** Tích hợp âm thanh độ trễ thấp (Low-latency), tạo cảm giác thỏa mãn khi đặt gạch hoặc phá hàng (Hiệu ứng nổ).
* **Giao diện Dark Mode:** Thiết kế tối giản với hiệu ứng đổ bóng và phát sáng (Neon Glow).

## 🎮 Hướng Dẫn Chơi

### 1. Cách Điều Khiển (Gestures)

| Hành động | Cử chỉ tay | Mô tả |
| :--- | :--- | :--- |
| **Di chuyển chuột** | ☝️ **Ngón Trỏ** | Dùng đầu ngón trỏ như con trỏ chuột để lướt xem các khối gạch hoặc chọn Menu. |
| **Gắp khối gạch** | 👌 **Chụm tay (Pinch)** | Chạm đầu **Ngón Trỏ** và **Ngón Cái** lại với nhau. Giữ tư thế này để "nắm" lấy khối gạch. |
| **Kéo khối** | ✊ **Giữ Chụm** | Khi đang nắm khối, di chuyển tay để đưa khối gạch đến vị trí mong muốn trên bàn cờ. |
| **Thả / Đặt** | 🖐️ **Mở tay** | Tách hai ngón tay ra để thả khối xuống. |

> **💡 MẸO QUAN TRỌNG:**
> Game sử dụng cơ chế **"Thumb Control"**. Khi bạn thả tay, khối gạch sẽ rơi xuống đúng vị trí của **NGÓN CÁI**. Hãy nhìn vào ngón cái của bạn để căn ô cho chuẩn xác nhé!

### 2. Luật Chơi

1.  **Gắp & Thả:** Kéo các khối gạch từ khay chứa (bên phải) vào bàn cờ 8x8 (bên trái).
2.  **Ăn Điểm:** Lấp đầy một hàng ngang hoặc dọc để phá hủy chúng và ghi điểm (Hiệu ứng nổ 💥).
3.  **Combo:** Nếu bạn đặt một khối gạch mà phá hủy được nhiều hàng cùng lúc, bạn sẽ nhận được điểm thưởng Combo lớn.
4.  **Game Over:** Trò chơi kết thúc khi khay chứa vẫn còn khối gạch nhưng trên bàn cờ không còn chỗ trống nào phù hợp để đặt.

### 3. Lưu ý khi chơi

* **Ánh sáng:** Chơi ở nơi có ánh sáng tốt để Camera nhận diện tay rõ nét nhất.
* **Khoảng cách:** Ngồi cách Camera khoảng 0.5m - 1m để Camera nhìn thấy toàn bộ bàn tay.
* **Một tay:** Game chỉ nhận diện **một bàn tay** đầu tiên đưa lên. Nếu muốn đổi tay, hãy hạ tay cũ xuống và đưa tay mới lên.

## 📦 Cài Đặt & Chạy Game

### Yêu cầu hệ thống
* Python 3.x
* Webcam (Laptop hoặc rời)

### Các bước cài đặt

1.  **Tải mã nguồn (Clone):**
    ```bash
    git clone [https://github.com/VietHung207/Hand-Block-Blast.git](https://github.com/VietHung207/Hand-Block-Blast.git)
    cd Hand-Block-Blast
    ```

2.  **Cài đặt thư viện:**
    Mở Terminal và chạy lệnh sau:
    ```bash
    pip install opencv-python mediapipe pygame
    ```

3.  **Kiểm tra tài nguyên:**
    Đảm bảo các file sau nằm cùng thư mục với `main.py`:
    * `boom.wav`
    * `click.wav`
    * `logogame.ico`

4.  **Chạy game:**
    ```bash
    python main.py
    ```

## 🛠️ Cấu Trúc Dự Án

```text
Hand-Block-Blast/
├── game_backend.py     # Xử lý AI, Logic bàn cờ & Tính điểm
├── main.py             # Giao diện chính, Xử lý sự kiện & Âm thanh
├── boom.wav            # Âm thanh hiệu ứng
├── click.wav           # Âm thanh hiệu ứng
└── README.md           # Tài liệu hướng dẫn
```

## 👥 Đội Ngũ Phát Triển

| STT | Thành Viên | Vai Trò (Role) |
| :--: | :--- | :--- |
| 1 | **Nguyễn Việt Hùng** | Leader / Backend Dev |
| 2 | **Bùi Ngọc Phương Nam** | Backend Dev |
| 3 | **Đỗ Tiến Đạt** | Frontend Dev |
| 4 | **Phạm Tuấn Dương** | Frontend Dev & Tester |
| 5 | **Nguyễn Tuấn Huy** | Tester |






