---
title: Cài đặt ứng dụng Outline trên Linux
sidebar_label: Cài đặt ứng dụng Outline trên Linux
---

Kể từ phiên bản 1.15 của ứng dụng Outline, tất cả các phiên bản trong tương lai sẽ được phát hành dưới dạng gói Debian cho hệ điều hành Linux. Hãy xem [các yêu cầu tối thiểu về hệ thống](/client/getting-started/system-requirements) của chúng tôi để biết thêm thông tin về những hệ điều hành mà chúng tôi hỗ trợ.

## Cài đặt ứng dụng Outline cho các bản phân phối Linux dựa trên Debian (Nên dùng)

Chạy các lệnh sau:

1. Cài đặt khoá kho lưu trữ của Outline và thêm kho lưu trữ.
   ```
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
2. Cập nhật danh sách gói apt và cài đặt phiên bản mới nhất của ứng dụng Outline.
   ```
   sudo apt update
   sudo apt install outline-client
   ```

Để kiểm tra hoặc cài đặt các bản cập nhật trong tương lai, hãy chạy lại các lệnh trong Bước 2. Xin lưu ý rằng tính năng tự động cập nhật trong ứng dụng bị tắt đối với ứng dụng Outline trên Linux, bắt đầu từ phiên bản 1.15.

Để gỡ cài đặt ứng dụng Outline, hãy chạy lệnh sau:

```
sudo apt purge outline-client
```

## Lựa chọn thay thế

1. Tải gói ứng dụng Outline mới nhất cho Debian xuống từ [https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb](https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb)
2. Chạy các lệnh sau trong dòng lệnh để cài đặt gói
   ```
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   sudo apt install ./outline-client.deb
   ```
3. Kiểm tra bản cập nhật theo cách thủ công, vì tính năng tự động cập nhật trong ứng dụng bị tắt đối với ứng dụng Outline trên Linux, bắt đầu từ phiên bản 1.15.
4. Để gỡ cài đặt ứng dụng Outline, hãy chạy lệnh sau trong dòng lệnh:
   ```
   sudo apt purge outline-client
   ```
