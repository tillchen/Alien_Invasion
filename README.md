<!-- PROJECT SHIELDS -->
[![Build Status][build-shield]]()
[![Contributors][contributors-shield]]()
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<p align="center">
    <a href="https://github.com/tillchen/Alien_Invasion"><img src="images/ship.bmp" alt="Logo" width="80" height="80"></a>
    <h3 align="center">Alien Invasion!</h3>
    <p align="center">
        A fun python game built using pygame.<br>
        <a href="https://github.com/tillchen/Alien_Invasion"><strong>Explore the docs »</strong></a><br><br>
    <a href="https://github.com/tillchen/Alien_Invasion/issues">Report Bug</a>
    </p>
</p>

<!-- TABLE OF CONTENTS -->
# Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->
# About The Project

![gif](images/demo.gif)

This is a fun python game. While building this game myself, I learned:

* how to handle large projects;
* code refactoring.

Plus, it strenthened my coding skills in Python and my love for programming :grin:

## Built With

* [Pygame](https://www.pygame.org/)

<!-- GETTING STARTED -->
# Getting Started

## Prerequisites

* [Python3](https://www.python.org/downloads/)
* Pygame

    ```sh
    python3 -m pip install --user pygame
    ```

* If --user doesn't work (for example on macOS,) try this instead:

    ```sh
    python3 -m pip install pygame
    ```

## Installation

1. Clone the repository

    ```sh
    git clone https://github.com/tillchen/Alien_Invasion.git
    ```

<!-- USAGE EXAMPLES -->
# Usage

1. Go to the directory and run the game

    ```sh
    python3 alien_invasion.py
    ```

2. Click **Play** to start.
3. Press **<-** and **->** to control the positions of the ship.
4. Press **space** key to fire a bullet and kill an alien. Try to kill all aliens in the window.
5. Press **q** or **esc** to quit the game.
6. Only **3 bullets** are allowed to be present in the same window. So try to be as accurate as possible.
7. For every game, you have **3 ships**. If an anlien hits your ship or hits the bottom, you'll lose a ship. And the game'll restart at the same level. You'll lose the game if all 3 ships are gone.
8. As the level goes up, the speed of the game and the point you get for each killed alien also goes up.
9. Enjoy the game and beat your own or your friends' high score :sunglasses:

<!-- CONTRIBUTING -->
# Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
# License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
# Contact

Tianyao (Till) Chen - tillchen417@gmail.com

Personal website: https://tillchen.com

<!-- ACKNOWLEDGEMENTS -->
# Acknowledgements

* [Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming](https://www.amazon.com/Python-Crash-Course-2nd-Edition/dp/1593279280/ref=sr_1_1?keywords=python+crash+course&qid=1558808134&s=gateway&sr=8-1)

<!-- MARKDOWN LINKS & IMAGES -->
[build-shield]: https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat-square
[contributors-shield]: https://img.shields.io/badge/contributors-1-orange.svg?style=flat-square
[license-shield]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
[license-url]: https://choosealicense.com/licenses/mit
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/tillchen/
