# 🧱 HAND BLOCK BLAST - GAME XẾP GẠCH AI

Một tựa game trí tuệ hiện đại lấy cảm hứng từ *1010!*, điều khiển hoàn toàn bằng cử chỉ tay thông qua Webcam. Dự án sử dụng Python kết hợp với các công nghệ Thị giác máy tính (Computer Vision) tiên tiến để mang lại trải nghiệm tương tác không chạm.

![Demo Banner]([https://via.placeholder.com/800x400?text=Hand+Block+Blast+Gameplay](https://drive.google.com/file/d/18txx_4Vy4j8wMhzWxK1nT6F0hi99QXCY/view?usp=drive_link))

## ✨ Tính Năng Nổi Bật

* **Công nghệ AI Tracking:** Sử dụng MediaPipe để nhận diện khớp tay thời gian thực với độ trễ cực thấp.
* **Cơ chế "Thumb Control" (Điều khiển Ngón Cái):** Tính năng độc đáo giúp thả khối gạch chính xác tuyệt đối tại vị trí ngón cái, khắc phục điểm yếu khó căn chỉnh của các game hand-tracking thông thường.
* **Hệ thống Khóa Tay Thông Minh:** Tự động khóa mục tiêu vào bàn tay đầu tiên xuất hiện, giúp game không bị nhiễu khi có người khác đi qua khung hình.
* **Hệ thống Âm thanh Phản hồi:** Tích hợp âm thanh độ trễ thấp (Low-latency), tạo cảm giác thỏa mãn khi đặt gạch hoặc phá hàng (Hiệu ứng nổ).
* **Giao diện Dark Mode:** Thiết kế tối giản với hiệu ứng đổ bóng và phát sáng (Neon Glow).

## 🎮 Hướng Dẫn Chơi

### Cách Điều Khiển

| Hành động | Cử chỉ tay | Mô tả |
| :--- | :--- | :--- |
| **Di chuyển chuột** | ☝️ **Ngón Trỏ** | Di chuyển ngón trỏ để lướt qua các khối gạch hoặc chọn Menu. |
| **Gắp khối gạch** | 👌 **Chụm tay (Pinch)** | Chạm đầu **Ngón Trỏ** và **Ngón Cái** lại với nhau để "gắp" khối lên. |
| **Kéo khối** | ✊ **Giữ Chụm** | Giữ nguyên tư thế chụm tay để kéo khối gạch đi khắp màn hình. |
| **Thả / Đặt** | 🖐️ **Mở tay** | Tách hai ngón tay ra để thả khối xuống. **Mẹo:** Khối gạch sẽ rơi ngay tại vị trí **Ngón Cái**. |

### Luật Chơi

1.  **Gắp & Thả:** Kéo các khối gạch từ khay chứa (bên phải) vào bàn cờ 8x8 (bên trái).
2.  **Ăn Điểm:** Lấp đầy một hàng ngang hoặc dọc để phá hủy chúng và ghi điểm.
3.  **Combo:** Phá hủy nhiều hàng cùng lúc để tạo ra tiếng nổ lớn và nhận điểm thưởng.
4.  **Game Over:** Trò chơi kết thúc khi không còn chỗ trống trên bàn cờ để đặt các khối gạch hiện có.

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

👥 Tác Giả
Dự án được phát triển bởi:

VietHung207 (Nguyễn Việt Hùng)

Bùi Ngọc Phương Nam

Đỗ Tiến Đạt

Phạm Tuấn Dương

Nguyễn Tuấn Huy

