---
title: 개요
sidebar_label: 개요
---

Outline Manager에는 Google Cloud에서 실행되는 서버에서 Outline 서버를 자동으로 구성할 수 있는 기능이 포함되어 있습니다. 이 기능을 사용하기로 선택하면 Outline Manager에 Google 계정으로 로그인하라는 메시지가 표시됩니다. 로그인할 경우 Google Cloud 계정을 구성하기 위해 Outline Manager의 로컬 설치에 특정 [OAuth](https://developers.google.com/identity/protocols/oauth2) 권한이 부여됩니다.

이러한 권한을 제공하지 않으려면 Outline Manager의 고급 설정 안내에 따라 Google Cloud Platform에서 Outline을 실행하세요.

## 부여된 권한

자동 설정을 제공하려면 Outline Manager에서 Google 계정으로부터 다음 권한을 요구합니다.

## Google Cloud Platform

- Google Compute Engine 리소스 조회 및 관리
- Google Cloud 서비스 전체 데이터 조회 및 Google 계정 이메일 주소 확인

## 기본 계정 정보

- 기본 Google 계정 이메일 주소 확인
- Google에서 내 개인 정보를 나와 연결

## 추가 액세스

- Cloud Platform 프로젝트 관리
- Google Cloud Platform 결제 계정 조회 및 관리
- Google API 서비스 구성 관리

## 이러한 권한을 통해 Google은 다음과 같은 Outline 서버 관리를 위한 고급 기능을 지원할 수 있습니다.

- 정확한 결제 계정을 선택하도록 지원
- Outline 서버를 정리하기 위한 새 프로젝트 생성
- 사용 가능한 데이터 센터 나열
- Outline을 실행할 새 가상 머신 생성
- Outline으로 새 가상 머신 구성

## 권한 취소

[내 계정](https://myaccount.google.com/permissions)을 방문하여 Outline Manager용 Google Cloud Platform에 관한 액세스 권한을 취소할 수 있습니다. 액세스 권한을 취소하면 자동 설정으로 만든 모든 서버가 계속 실행되지만 Outline Manager에는 더 이상 표시되지 않습니다. 액세스 권한을 복원하려면 자동 설정 과정을 시작하여 Google Cloud Platform에 다시 연결하세요.

## Outline 프로젝트 조직

Google Cloud 자동 설정에서는 단일 [Google Cloud 프로젝트](https://cloud.google.com/resource-manager/docs/creating-managing-projects)를 사용하여 Outline 서버를 정리합니다. 프로젝트는 자동 설정을 처음 사용하는 동안 생성되며 ‘Outline-’ 뒤에 임의의 문자가 오는 추천 프로젝트 ID로 생성됩니다. 원하는 경우 생성 시 다른 프로젝트 ID를 선택할 수 있습니다. 프로젝트 이름은 ‘Outline 서버’로 지정됩니다.

## 결제 계정

Google Cloud 프로젝트에는 결제 정보를 정의하는 연결된 '결제 계정'이 필요합니다. Google Cloud 자동 설정을 처음 사용할 때 Outline 서버와 연결할 결제 계정을 제공하라는 메시지가 표시됩니다. 결제 계정에 문제가 있어 서버 실행이 중지되는 경우가 있습니다. 이 경우 [Google Cloud Console](https://console.cloud.google.com/getting-started)에 로그인하여 Outline과 연결된 Google Cloud 프로젝트(‘Outline 서버’라고 함)를 찾아 결제 설정을 업데이트해야 합니다.

## 서버 폐기

자동 설정을 사용하여 생성된 서버를 폐기하려는 경우 Outline Manager 내에서 가장 간편하게 폐기할 수 있습니다. 하지만 서버를 직접 폐기하려면 [Google Cloud Console](https://console.cloud.google.com/getting-started)에 로그인하여 초기 설정 중에 생성된 프로젝트(‘Outline 서버’라고 함)를 찾아 리소스를 삭제하거나 프로젝트를 종료할 수 있습니다.
