<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

# Server setup automation with Python

## Build with

* [![Python][Python-image]][Python-url]

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* The first time you have to have Python installed on your computer. If you don't have Python installed, you can install Python [**here**](https://www.python.org/downloads/)
* Ensure that the target operating system you intend to automate uses [**Ubuntu**](https://ubuntu.com/)
* If you require the Ubuntu operating system, you can install it by following the installation process provided [**here**](https://ubuntu.com/download)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Installation and Usage

1. Clone this repository

   ```sh
    git clone https://github.com/titan2903/cakeplabs-technical-test.git
   ```

2. Go to the directory of the cloned repository
  
3. Copy the file `.env.example` to a file named `.env`

   ```sh
    cp .env.example .env
   ```

4. Edit the values in the `.env` file according to the hostname or IP address, username and password that you have

5. Install python-dotenv

   ```sh
    pip install python-dotenv
   ```

6. Implemented a script to eliminate the need for password entry when executing sudo on the destination server you want to automate. Refer to the instructions [**here**](https://www.cyberciti.biz/faq/linux-unix-running-sudo-command-without-a-password/) for adding the script.

7. Run this repository on your local machine

   ```sh
    python3 main.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[Python-url]: https://nextjs.org/
[Python-image]: https://img.shields.io/badge/python-FFFFF0?style=for-the-badge&logo=python&logoColor=blue
