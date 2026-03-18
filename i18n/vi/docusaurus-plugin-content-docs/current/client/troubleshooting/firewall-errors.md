---
title: Lỗi tường lửa
sidebar_label: Lỗi tường lửa
---

Có ba loại sự cố tường lửa mà bạn có thể gặp phải:

## Bạn có thể bị tường lửa mạng chặn.

Nếu bạn cố cài đặt Outline khi đang kết nối với một mạng đã kích hoạt tường lửa, chẳng hạn như ở trường học hoặc nơi làm việc, hãy thử cài đặt khi kết nối với một mạng khác.

Nếu cách này không hiệu quả, vui lòng liên hệ với quản trị viên mạng để được phép kết nối giữa mạng đã kích hoạt tường lửa với máy chủ Outline. Bạn sẽ cần phải biết địa chỉ IP của máy chủ Outline và các cổng mà Outline đang chạy (thông tin này có ở phần cuối cùng trong tập lệnh cài đặt).

**Bạn có thể bị tường lửa thiết bị chặn**.

Nếu trên thiết bị có phần mềm chặn kết nối đầu ra trên các cổng không chuẩn hoặc phần mềm không được nhận dạng (ví dụ: ZoneAlarm của CheckPoint), vui lòng tham khảo tài liệu của thiết bị hoặc phần mềm tương ứng để tìm hiểu cách tạo trường hợp ngoại lệ cho Outline.

## Bạn có thể bị tường lửa máy chủ chặn.

Nhà cung cấp dịch vụ đám mây bạn đã chọn có thể yêu cầu bạn tạo thủ công trường hợp ngoại lệ cho tường lửa máy chủ để mở các cổng mà Outline đang chạy. Sau khi chạy tập lệnh cài đặt, bạn sẽ thấy hai cổng được chọn ngẫu nhiên mà Outline đang chạy trong máy chủ. Bạn chỉ cần mở hai cổng này là đủ.

 Để tạo trường hợp ngoại lệ cho tường lửa máy chủ, bạn nên xem tài liệu về 'ufw' và 'iptables':

- UFW: [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW)
- Iptables: [https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)
