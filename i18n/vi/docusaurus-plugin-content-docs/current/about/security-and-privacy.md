---
title: Tính bảo mật và quyền riêng tư khi sử dụng Outline
sidebar_label: Tính bảo mật và quyền riêng tư khi sử dụng Outline
---

Tính bảo mật và quyền riêng tư khi sử dụng Outline

## Cách Outline bảo vệ thông tin giao tiếp của bạn trên mạng

Lưu lượng truy cập vào Internet dễ bị theo dõi nhất khi đi qua mạng địa phương hoặc quốc gia.

Outline giúp giữ bí mật cho thông tin giao tiếp bằng cách mã hoá lưu lượng truy cập Internet của bạn khi thông tin di chuyển trong mạng quốc gia và duy trì mã hoá cho đến khi những thông tin này đến máy chủ Outline. Khi Outine mã hoá lưu lượng truy cập, những người quan sát trên mạng không thể điều tra các trang web mà bạn truy cập hoặc thông tin bạn truyền đi.

Outline cũng có thể giúp bạn khôi phục quyền sử dụng những công cụ giao tiếp bảo mật hai đầu mà bạn có thể không truy cập được tại quốc gia của bạn trong các trường hợp khác.

## Tiêu chuẩn mã hoá

Outline mã hoá thông tin giao tiếp giữa thiết bị của bạn và máy chủ Outline bằng thuật toán mật mã AEAD 256-bit Chacha2020 IETF Poly 1305. Thuật toán mật mã AEAD giúp đảm bảo tính bí mật, toàn vẹn và xác thực, đồng thời đạt hiệu suất rất cao trên phần cứng hiện đại.

## Kiểm nghiệm bảo mật

Vào năm 2018, Outline đã được Radically Open Security và Cure53 kiểm nghiệm. Đây là hai tổ chức đánh giá khả năng bảo mật kỹ thuật số độc lập, đánh giá phần mềm theo các tiêu chuẩn bảo mật mới nhất. Radically Open Security đã kiểm nghiệm Outline một lần nữa vào năm 2022 và Cure53 đã kiểm nghiệm Outline SDK vào năm 2024. Bạn có thể đọc các báo cáo liên quan dưới đây:

- [Báo cáo kiểm tra thâm nhập của Radically Open Security (tháng 3 năm 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report.pdf)
- [Báo cáo của Cure53 về việc kiểm nghiệm và kiểm tra thâm nhập Outline của Jigsaw (tháng 12 năm 2018)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report.pdf)
- [Báo cáo kiểm tra thâm nhập của Radically Open Security (tháng 12 năm 2022)](https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report-2022.pdf)
- [Báo cáo kiểm tra thâm nhập của Cure53 đối với SDK của Outline VPN thuộc Jigsaw (tháng 1 năm 2024)](https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report-SDK-2024.pdf)

## Chỉ số và nhật ký ẩn danh

Outline chỉ theo dõi băng thông đã dùng dưới dạng "số byte đã truyền" đối với mỗi khoá truy cập. Thông tin này cho phép quản trị viên máy chủ điều chỉnh gói thuê bao băng thông với các nhà cung cấp máy chủ đám mây khi cần, nhưng không cho phép họ xem thông tin thực tế được truyền qua máy chủ Outline.

Tìm hiểu thêm về hoạt động [thu thập dữ liệu và thông tin](/about/data-collection) của Outline.

---

## Câu hỏi thường gặp về tính bảo mật và quyền riêng tư

## Outline có thể giúp tôi ẩn danh trên mạng không?

Không, Outline không phải là một công cụ giúp ẩn danh. Outline bảo vệ quyền riêng tư của bạn khỏi những kẻ theo dõi tiềm ẩn trên mạng.

Outline không ẩn danh bạn hoàn toàn trên các trang web mà bạn truy cập, vì những trang web này vẫn có thể nhận dạng bạn khi bạn đăng nhập hoặc đôi khi thông qua một số kỹ thuật như vân tay số trên trình duyệt. Đối với ứng dụng dành cho thiết bị di động, hầu hết điện thoại thông minh hiện đại đều có các API cho phép các ứng dụng đã cài đặt thu thập thông tin vị trí độc lập với proxy của bạn vì các API này có thể dựa trên GPS đã nhúng.

Nói chung, VPN cung cấp các biện pháp bảo vệ quan trọng, đặc biệt là trước việc bị theo dõi trên Internet, nhưng luôn có rủi ro khi vận hành trên mạng. Kể cả khi bạn dùng VPN, nếu một nhà cung cấp dịch vụ mạng đã biết danh tính của bạn và có thể quan sát lưu lượng truy cập mạng của bạn, thì họ có thể xác định địa chỉ IP máy chủ Outline của bạn. Thông tin này có thể được dùng để chặn bạn truy cập vào máy chủ Outline hoặc để tìm hiểu thói quen sử dụng của bạn, chẳng như thời gian bạn thường lên mạng và có thể là vị trí tương đối của bạn.

## Người ta có thể biết khi tôi đang sử dụng Outline hay không?

Có thể. Các nền tảng và dịch vụ bạn truy cập rất có khả năng sẽ biết được rằng bạn đang kết nối từ một máy chủ đám mây. Đôi khi, họ có thể suy luận được rằng bạn đang sử dụng một VPN, nhưng họ sẽ không thể xem nội dung lưu lượng truy cập Internet của bạn.

## Outline có bảo vệ tôi khỏi tất cả các mối đe doạ về an ninh mạng có thể xảy ra không?

Không. Không một công cụ bảo mật nào có thể bảo vệ bạn trước tất cả mối đe dọa về an ninh mạng có thể xảy ra. Outline giúp bạn truy cập vào thế giới Internet rộng lớn và tăng cường khả năng bảo vệ quyền riêng tư bằng cách mã hoá lưu lượng truy cập, nhưng bạn nên thực hiện các biện pháp phòng ngừa bổ sung để bảo vệ bản thân khỏi các hình thức tấn công khác, chẳng hạn như phần mềm độc hại và tấn công giả mạo.

Để củng cố khả năng bảo vệ trên mạng, bạn nên làm việc với một chuyên gia về an ninh mạng trong tổ chức của bạn. Ngoài ra, bạn có thể xem hướng dẫn phù hợp với bạn do các chuyên gia bảo mật hàng đầu trên [Security Planner](https://securityplanner.org/) đưa ra. Security Planner là một trang web được xây dựng nhằm cung cấp hướng dẫn rõ ràng về cách lựa chọn các công cụ an ninh mạng phù hợp cho những vấn đề bạn lo ngại.

Bạn cũng có thể tìm hiểu về các sản phẩm khác của [Jigsaw](https://jigsaw.google.com/) về an ninh mạng, như [Intra](https://getintra.org/), [Project Shield](https://g.co/shield) và [Cảnh báo mật khẩu](https://chrome.google.com/webstore/detail/password-alert/noondiphcddnnabmjcihcjfbhfklnnep?).

## Việc sử dụng VPN có hợp pháp không?

Vui lòng tìm hiểu luật pháp và quy định tại địa phương của bạn, cũng như Điều khoản dịch vụ của nhà cung cấp dịch vụ đám mây mà bạn dự định sử dụng trước khi vận hành Outline hoặc dùng ứng dụng này.
