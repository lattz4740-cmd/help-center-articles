---
title: Cách hoạt động của Outline
sidebar_label: Cách hoạt động của Outline
---

## Cài đặt máy chủ
 ​Mặc dù việc cài đặt Outline có vẻ đơn giản, nhưng thực ra có một tổ hợp phức tạp các bước diễn ra mà bạn không nhìn thấy để giúp cài đặt máy chủ của bạn. Mỗi khi cài đặt Outline, một tập lệnh cài đặt sẽ thực hiện các bước sau đây:

- Truy xuất và nhập phiên bản ổn định của hình ảnh Shadowbox bằng Docker. Ảnh này được lưu trữ tại địa chỉ [https://quay.io/](https://quay.io/) trên [Quay.io](https://quay.io/repository/outline/shadowbox?tab=tags). Ảnh này chứa máy chủ Outline và API Quản lý. Ứng dụng Quản lý máy chủ Outline sẽ sử dụng API này về sau để tạo và xoá khoá truy cập, chọn bật/tắt tính năng báo cáo chỉ số ẩn danh, v.v.
- [Watchtower](https://github.com/containrrr/watchtower) được cài đặt và định cấu hình để giúp kiểm tra nhằm tìm bản cập nhật hình ảnh mỗi giờ, qua đó giúp đảm bảo mọi máy chủ Outline đều chạy phiên bản mới nhất, được cải tiến bảo mật và sử dụng các tính năng mới nhất.
- Một máy chủ web dùng để truy cập vào API Quản lý sẽ được khởi động tại một cổng ngẫu nhiên trên một đường dẫn ngẫu nhiên, bí mật.
- [Chứng chỉ SSL tự ký](https://en.wikipedia.org/wiki/Self-signed_certificate) được tạo để có thể mã hoá hoạt động quản lý máy chủ Outline bằng giao thức TLS (Bảo mật tầng truyền tải), dù không có tên miền. Vân tay số duy nhất của chứng chỉ này cũng được tạo và lưu trữ trong ứng dụng Quản lý Outline để giúp ngăn chặn các cuộc tấn công MITM (Man in the Middle – Tấn công xen giữa).

Bạn không cần định cấu hình sau khi cài đặt Outline.

## Bảo mật máy chủ
 Outline là phần mềm nguồn mở, nghĩa là bất cứ ai cũng có thể xem mã nguồn và cải thiện nếu phát hiện ra lỗ hổng. Chúng tôi lưu trữ mã nguồn trên [GitHub](https://github.com/search?q=org%3AOutlineFoundation+outline&unscoped_q=outline).

 Ngoài ra, tất cả máy chủ Outline đã cài đặt đều sẽ cập nhật tự động mỗi khi có một phiên bản mới được phát hành, để đảm bảo rằng không có máy chủ Outline nào chạy phiên bản phần mềm cũ.

 Để quản lý khoá truy cập trên máy chủ, ứng dụng Quản lý Outline sẽ tương tác với một Dịch vụ quản lý trên máy chủ Outline. Dịch vụ quản lý này chạy tại một cổng ngẫu nhiên và sử dụng một đường dẫn bí mật, duy nhất. Bản thân Dịch vụ quản lý miễn nhiễm với hành vi dò lỗ hổng vì nó không đáp lại truy vấn trừ khi đường dẫn bí mật được xác định. Cuối cùng, mọi thông tin giao tiếp với Dịch vụ quản lý đều được mã hoá bằng một [chứng chỉ SSL tự ký](https://en.wikipedia.org/wiki/Self-signed_certificate).

 Ngoài ra, máy chủ Outline không lưu trữ nhật ký, nên kể cả khi bị xâm phạm, dữ liệu của người dùng cũng không bị lộ. Tìm hiểu thêm [tại đây](/about/security-and-privacy). Outline đã được [Radically Open Security](https://radicallyopensecurity.com/) và [Cure53](https://cure53.de/) kiểm tra vào năm 2018. Xem các báo cáo đó [tại đây](/about/security-and-privacy).

## Xử lý lưu lượng truy cập UDP
 Outline có thể vận hành dưới dạng một VPN toàn hệ thống, nghĩa là mọi lưu lượng truy cập UDP đều được truyền bằng kỹ thuật tạo đường hầm qua máy chủ Outline.

## Lưu lượng truy cập DNS
Outline thực hiện toàn bộ hoạt động tra cứu DNS qua máy chủ Outline và bảo vệ các lượt tra cứu này bằng cùng một phương thức mã hoá dùng trong tất cả hoạt động mạng khác. Các truy vấn DNS của bạn sẽ đi qua máy chủ Outline đến Dyn Internet Guide, OpenDNS, Cloudflare DNS hoặc Quad9 DNS. Outline không bao giờ ghi nhật ký các lượt tra cứu DNS của bạn.
