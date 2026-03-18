---
title: Thiết lập tự động Google Cloud
sidebar_label: Thiết lập tự động Google Cloud
---

## Tổng quan

Ứng dụng Quản lý Outline có một tính năng cho phép bạn tự động định cấu hình Máy chủ Outline trên máy chủ chạy trên Google Cloud. Nếu bạn chọn sử dụng tính năng này, thì ứng dụng Quản lý Outline sẽ yêu cầu bạn đăng nhập bằng Tài khoản Google. Tài khoản này sẽ cấp một số quyền[OAuth](https://developers.google.com/identity/protocols/oauth2) để cài đặt ứng dụng Quản lý Outline trên thiết bị nhằm mục đích định cấu hình Tài khoản Google Cloud.

 Nếu không muốn cấp những quyền này, bạn có thể làm theo các hướng dẫn thiết lập nâng cao trong ứng dụng Quản lý Outline để chạy Outline trên Google Cloud Platform.

## Quyền đã được cấp

Để cung cấp chế độ thiết lập tự động, ứng dụng Quản lý Outline yêu cầu các quyền sau đây trong Tài khoản Google của bạn.

## Google Cloud Platform

- Xem và quản lý tài nguyên của bạn trên Google Compute Engine
- Xem dữ liệu của bạn trong các dịch vụ của Google Cloud và xem địa chỉ email của Tài khoản Google của bạn

## Thông tin cơ bản về tài khoản

- Xem địa chỉ email trong Tài khoản Google chính của bạn
- Liên kết bạn với những thông tin cá nhân của bạn trên Google

## Quyền truy cập bổ sung

- Quản lý các dự án của bạn trên Cloud Platform
- Xem và quản lý tài khoản thanh toán Google Cloud Platform của bạn
- Quản lý cấu hình dịch vụ API của Google

Các quyền này cho phép chúng tôi hỗ trợ chức năng nâng cao để quản lý máy chủ Outline của bạn, bao gồm:

- Cho phép bạn chọn đúng tài khoản thanh toán
- Tạo một dự án mới để sắp xếp các máy chủ Outline của bạn
- Liệt kê các trung tâm dữ liệu có sẵn
- Tạo máy ảo mới để chạy Outline
- Định cấu hình máy ảo mới bằng Outline

## Thu hồi quyền

Bạn có thể thu hồi quyền truy cập vào Google Cloud Platform đối với ứng dụng Quản lý Outline bằng cách truy cập vào phần[Tài khoản của tôi](https://myaccount.google.com/permissions). Nếu bạn thu hồi quyền truy cập, mọi máy chủ bạn đã tạo bằng tính năng thiết lập tự động sẽ vẫn chạy nhưng không còn xuất hiện trong ứng dụng Quản lý Outline nữa. Để khôi phục quyền truy cập vào các ứng dụng đó, bạn chỉ cần kết nối lại với Google Cloud Platform bằng cách bắt đầu quy trình thiết lập tự động.

## Sắp xếp dự án Outline

Tính năng thiết lập tự động của Google Cloud sử dụng một[dự án Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects) duy nhất để sắp xếp các máy chủ Outline của bạn. Dự án này được tạo trong lần đầu tiên thiết lập tự động, với một mã dự án đề xuất bắt đầu bằng “Outline-” rồi đến một chuỗi ký tự ngẫu nhiên. Bạn có thể chọn một mã dự án khác khi tạo, nếu muốn. Dự án này sẽ có tên là "Máy chủ Outline".

## Tài khoản thanh toán

Các dự án Google Cloud yêu cầu bạn phải liên kết với một "tài khoản thanh toán" để xác định thông tin thanh toán. Khi mới sử dụng tính năng thiết lập tự động trên Google Cloud, bạn sẽ được yêu cầu cung cấp một tài khoản thanh toán để liên kết với máy chủ Outline của bạn. Đôi khi, máy chủ sẽ ngừng chạy vì xảy ra sự cố với tài khoản thanh toán. Trong trường hợp này, bạn nên đăng nhập vào[Google Cloud Console](https://console.cloud.google.com/getting-started), tìm dự án Google Cloud liên kết với Outline (có tên là “Máy chủ Outline”) rồi cập nhật các chế độ cài đặt thanh toán.

## Huỷ bỏ máy chủ

Nếu bạn muốn huỷ bỏ các máy chủ đã tạo bằng chế độ thiết lập tự động, thì cách dễ nhất là làm việc này trong ứng dụng Quản lý Outline. Tuy nhiên, nếu muốn tự hủy bỏ các máy chủ, bạn có thể đăng nhập vào[Google Cloud Console](https://console.cloud.google.com/getting-started), tìm dự án được tạo trong quá trình thiết lập ban đầu (có tên là “Máy chủ Outline”) rồi xóa các tài nguyên ở đó hoặc tắt dự án đó.
