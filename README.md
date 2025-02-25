<div align="center">

  [![radipy](./images/images/banner.svg)](#readme)

  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE "License")
  [![Commits](https://img.shields.io/github/commit-activity/y/devhaaana/radipy.svg?label=commits&style=for-the-badge)](https://github.com/devhaaana/radipy/commits "Commit History")
  [![Last Commit](https://img.shields.io/github/last-commit/devhaaana/radipy.svg?label=&style=for-the-badge&display_timestamp=committer)](https://github.com/devhaaana/radipy/pulse/monthly "Last Commit")

</div>

`radipy` can record the [radiko.jp](https://radiko.jp/) programs outside of Japan.

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

## Warning
**Please do not use this project for commercial use. Only for your personal, non-commercial use.**

## Technologies
- `Python` : 3.12
- `PyQt`
- `FFmpeg`

# Technical Details
The authentication of PC(html5) version radkio validates user's location via IP address.
However, the android version of radkio validates user provided by GPS information, not via user's IP address.

# Getting Started
## Installation
- You can install it **locally:**
  ```console
  $ git clone https://github.com/devhaaana/radipy.git
  $ cd radipy
  ```

- Make sure you have **Python** installed on your system. Then, install the **required packages** by running the following command:
  ```console
  conda create -n radiko_env python=3.12
  conda activate radiko_env
  pip install -r requirements.txt
  ```

## Usage
```console
python main.py
```

![base-ui-live](./sample/base-ui-live.png)
![base-ui-download](./sample/base-ui-download.png)

## Reference
- [rajiko](https://github.com/jackyzy823/rajiko)
- [radiko-downloader](https://github.com/devhaaana/radiko-downloader.git)
