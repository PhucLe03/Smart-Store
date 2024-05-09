# Backend và IoT
## Chuẩn bị
- Database:
  - Sử dụng MySQL (có thể host bằng [XAMPP](https://www.apachefriends.org/download.html))
  - Sau khi host MySQL server, tạo database tên `test` (nếu chưa có) và chạy lệnh trong file [smartstore.sql](smartstore.sql) để tạo các bảng dữ liệu.

- Thư viện python: cài đặt python và cài các thư viện đã liệt kê trong file `requirements.txt`
```c
$ pip install -r requirements.txt
```

## Các bước để host Backend

- Lệnh để host Backend
  ```c
  $ uvicorn app:be_app --host <hostIP> --port <portID> --reload
  ```
  Với `<hostIP>` là địa chỉ IP của máy đang host, `<portID>` là port ta chọn để host
- Đối với Linux: Nếu có lỗi xảy ra, hãy thử kiểm tra xem port có process nào chiếm hay không (ở đây thử kiểm tra port 8080)
  ```c
  $ lsof -i :<port>
  ```
  Với `<port>` là port đang kiểm tra

## Các bước kiểm tra IoT để nhận diện khuôn mặt

- Ở đây sử dụng thiết bị là Raspberry Pi 4 cùng với Raspberry Camera
- Đảm bảo rằng Backend (host theo hướng dẫn ở trên) đang chạy ổn định
- Chạy lệnh với format sau:
  ```
  $ python3 iot.py <email>
  ```
  Với `<email>` là địa chỉ email của người dùng lưu trong database
