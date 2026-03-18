---
title: Thuật ngữ
sidebar_label: Thuật ngữ
---

**VPN là gì?**

 Mạng riêng ảo (VPN) là kết nối riêng tư giữa (các) thiết bị của bạn và một máy chủ lưu trữ. Khi dùng VPN, lưu lượng truy cập của bạn sẽ được ẩn khỏi nhà cung cấp dịch vụ Internet. Bạn có thể dùng VPN trong những trường hợp sau:

- Bảo vệ dữ liệu khi dùng mạng Wi-Fi công cộng
- Giữ bí mật dữ liệu duyệt web khỏi nhà cung cấp dịch vụ Internet và các cơ quan chính phủ
- Truy cập vào nội dung không bị kiểm duyệt của nhiều nguồn trên khắp thế giới

**Outline khác với các VPN truyền thống ở điểm nào?**

 Nhà cung cấp dịch vụ Internet có thể dễ dàng phát hiện và chặn các VPN truyền thống bằng cách nhận dạng những giao thức bảo mật phổ biến và/hoặc dấu hiệu về lưu lượng truy cập. Outline có khả năng chống chọi cao hơn vì ứng dụng này được xây dựng bằng một giao thức được thiết kế để khó bị phát hiện và do đó khó bị chặn hơn. Outline có khả năng vượt qua các hình thức kiểm duyệt phức tạp như chặn dựa trên mạng hoặc chặn IP.

**Máy chủ Outline là gì?**

 Máy chủ Outline chạy VPN mà những người dùng được cho phép sẽ có thể kết nối. Nếu đang tạo một mạng mới, thì bạn có thể sử dụng máy chủ bảo mật của riêng mình làm máy chủ Outline (nếu có) hoặc bạn có thể sử dụng một nhà cung cấp dịch vụ đám mây, chẳng hạn như:

- DigitalOcean
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)

Bạn có thể thiết lập máy chủ trong ứng dụng Quản lý Outline.

## Người quản lý dịch vụ là ai? {#servicemanager}
 Người quản lý dịch vụ là người chịu trách nhiệm thiết lập máy chủ Outline và chia sẻ khoá truy cập với người dùng. Người này thường chịu trách nhiệm về chi phí sử dụng máy chủ. 

## Khoá truy cập là gì? {#accesskey}
 Khoá truy cập dùng để truy cập vào một máy chủ Outline hiện có và kết nối với VPN. [Người quản lý dịch vụ](#servicemanager) sẽ cung cấp cho bạn một khoá truy cập hoặc bạn có thể tự[thiết lập một máy chủ Outline](/manager/server-setup/setup-server). Dưới đây là một ví dụ về khoá truy cập (đây chỉ là khoá mẫu nên sẽ không hoạt động): 

 ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1eXhUQ3MzemVEMTk=@XXX.XXX.4.1:39485/?outline=1

**Ứng dụng Quản lý Outline là gì?**

 Quản lý Outline là một ứng dụng máy tính cho phép người quản lý dịch vụ thiết lập một máy chủ Outline, tạo [khoá truy cập](#accesskey) và thiết lập hạn mức dữ liệu được sử dụng cho từng khoá. Bạn có thể tải phiên bản mới nhất của ứng dụng Quản lý Outline[tại đây](https://getoutline.org/get-started/#step-3) hoặc[tại đây](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

**Ứng dụng Outline là gì?**

 Outline là một ứng dụng dành cho máy tính và thiết bị di động, cho phép bạn kết nối với một máy chủ Outline và truy cập vào VPN bằng khoá truy cập. Bạn có thể tải phiên bản mới nhất của ứng dụng Outline[tại đây](https://getoutline.org/get-started/#step-3) hoặc[tại đây](https://www.reddit.com/r/outlinevpn/wiki/index/download_links/).

**Hạn mức dữ liệu là gì?**

 Ứng dụng Quản lý Outline cho phép người quản lý dịch vụ đặt hạn mức dữ liệu kéo dài trong 30 ngày cho khoá truy cập để tránh việc sử dụng quá mức và giúp duy trì chi phí trong phạm vi dự đoán. Người quản lý dịch vụ có thể đặt một hạn mức mặc định áp dụng cho mọi khoá và cũng có thể đặt hạn mức riêng cho một khoá bất kỳ để thay thế hạn mức mặc định. Sau khi được thiết lập, hạn mức dữ liệu sẽ có hiệu lực ngay lập tức và được thực thi mỗi giờ.

Nếu người quản lý dịch vụ chọn chia sẻ các chỉ số với Jigsaw, họ cần phải đọc[chính sách về việc thu thập dữ liệu](/about/data-collection) để nắm cụ thể cách hoạt động sử dụng hạn mức dữ liệu sẽ được báo cáo.
