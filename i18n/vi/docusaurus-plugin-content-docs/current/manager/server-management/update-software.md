---
title: "Làm cách nào để tôi cập nhật phần mềm máy chủ Outline?"
sidebar_label: "Làm cách nào để tôi cập nhật phần mềm máy chủ Outline?"
---

Máy chủ Outline sẽ tự động cập nhật các điểm cải tiến bảo mật mới nhất nhằm giúp bạn luôn sử dụng công nghệ mới nhất của Outline. Quá trình cập nhật tự động sử dụng [Watchtower](https://github.com/v2tec/watchtower). Đây là một thư viện nguồn mở, thường xuyên kiểm tra và cập nhật hình ảnh Docker chứa phần mềm Outline.

Ngoài ra, khi bạn cài đặt Outline bằng ứng dụng Quản lý Outline, chúng tôi sẽ thiết lập một dịch vụ chạy ngầm theo thời gian định trước để tự động nâng cấp phần mềm trên máy chủ bằng [Các bản nâng cấp không giám sát](https://wiki.debian.org/UnattendedUpgrades) (Ubuntu) và khởi động lại khi cần. Xin lưu ý rằng điều này không xảy ra trong Chế độ nâng cao nhằm mục đích duy trì cấu hình hiện có, dựa trên giả định là máy chủ lưu trữ đang được dùng cho các mục đích khác ngoài việc chạy Outline.
