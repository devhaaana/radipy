<div align="center">

  [![radipy](../images/images/banner.svg)](#readme)

  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE "License")
  [![Release version](https://img.shields.io/github/release/devhaaana/radipy.svg?label=Download&style=for-the-badge)](#release-files "Release Files")
  [![Commits](https://img.shields.io/github/commit-activity/y/devhaaana/radipy.svg?label=commits&style=for-the-badge)](https://github.com/devhaaana/radipy/commits "Commit History")
  [![Last Commit](https://img.shields.io/github/last-commit/devhaaana/radipy.svg?label=&style=for-the-badge&display_timestamp=committer)](https://github.com/devhaaana/radipy/pulse/monthly "Last Commit")

</div>

<br />

<div align="center">

[ENGLISH](/README.md)  ·  [한국어](/documents/README-KR.md)  ·  [日本語](/documents/README-JP.md)

</div>

<br />

`radipy` は、日本のラジオサービス [radiko.jp](https://radiko.jp/) の放送を日本国外でストリーミングおよびダウンロードできる PyQt5 ベースのデスクトップアプリケーションです。

## インデックス

- [インデックス](#インデックス)
- [アーキテクチャ](#アーキテクチャ)
- [警告](#警告)
- [技術](#技術)
- [技術的詳細](#技術的詳細)
- [はじめに](#はじめに)
  - [インストール](#インストール)
  - [使用方法](#使用方法)
  - [リリースファイル](#リリースファイル)
  - [参考](#参考)

## アーキテクチャ

```
radipy
├─ LICENSE
├─ README.md
├─ data
│  ├─ auth
│  │  └─ auth_key.bin
│  └─ json
│     └─ area.json
├─ images
│  ├─ icons
│  │  ├─ dark
│  │  │  ├─ antenna-512-color.png
│  │  │  ├─ antenna-512.png
│  │  │  ├─ exit-512.png
│  │  │  ├─ menu-32.png
│  │  │  ├─ save-512-bg.png
│  │  │  ├─ save-512.png
│  │  │  ├─ search-32.png
│  │  │  └─ settings-32.png
│  │  ├─ light
│  │  │  ├─ antenna-512-color.png
│  │  │  ├─ antenna-512.png
│  │  │  ├─ exit-512.png
│  │  │  ├─ menu-32.png
│  │  │  ├─ save-512-bg.png
│  │  │  ├─ save-512.png
│  │  │  ├─ search-32.png
│  │  │  └─ settings-32.png
│  │  ├─ podcasts-32.png
│  │  └─ settings.png
│  └─ images
│     ├─ banner.svg
│     ├─ profile-circle.png
│     └─ radiko.png
├─ main.py
├─ radiko.py
├─ requirements.txt
├─ sample
│  ├─ base-ui-download.png
│  └─ base-ui-live.png
├─ style
│  ├─ dark_style.qss
│  ├─ light_style.qss
│  └─ style.qss
└─ ui_pyqt5.py
```

## 警告

**このプロジェクトを商業目的で使用しないでください。個人的な非商業的使用のみにご利用ください。**

## 技術

- `Python` : 3.12
- `PyQt`
- `FFmpeg`

## 技術的詳細

PC (HTML5) 版の radiko は、ユーザーの位置情報を IP アドレスで確認します。
しかし、Android 版の radiko は、ユーザー提供の GPS 情報でユーザーを認証します。IP アドレスを使用しません。

## はじめに

### インストール

- **ローカル**にインストールする方法:
  ```console
  $ git clone https://github.com/devhaaana/radipy.git
  $ cd radipy
  ```
- **Python** がシステムにインストールされていることを確認してください。次に、必要なパッケージを以下のコマンドでインストールします:
  ```console
  conda create -n radiko_env python=3.12
  conda activate radiko_env
  pip install -r requirements.txt
  ```

### 使用方法

```console
python main.py
```

![base-ui-live](../sample/base-ui-live.png)
![base-ui-download](../sample/base-ui-download.png)

### リリースファイル

| ファイル                                                                                    | 説明                                                        |
| :-------------------------------------------------------------------------------------- | :----------------------------------------------------------------- |
| [radipy-1.0.0.zip](https://github.com/devhaaana/radipy/archive/refs/tags/v1.0.0.zip)       | radipy v1.0.0 のソースコードを含む *ZIP* ファイル |
| [radipy-1.0.0.tar.gz](https://github.com/devhaaana/radipy/archive/refs/tags/v1.0.0.tar.gz) | radipy v1.0.0 のソースコードを含む *TAR.GZ* ファイル |

### 参考

- [rajiko](https://github.com/jackyzy823/rajiko)
- [radiko-downloader](https://github.com/devhaaana/radiko-downloader.git)

<br />

<div align="center">
  
  [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fdevhaaana%2Fradipy.git&count_bg=%23000000&title_bg=%23000000&icon=github.svg&icon_color=%23FFFFFF&title=GitHub&edge_flat=false)](https://hits.seeyoufarm.com)

</div>
