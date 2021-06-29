
<p align="center">
    <a href="https://github.com/badges/shields/graphs/contributors" alt="Contributors">
        <img src="https://img.shields.io/github/contributors/badges/shields" /></a>
    <a href="#backers" alt="Backers on Open Collective">
        <img src="https://img.shields.io/opencollective/backers/shields" /></a>
    <a href="#sponsors" alt="Sponsors on Open Collective">
        <img src="https://img.shields.io/opencollective/sponsors/shields" /></a>
    <a href="https://github.com/badges/shields/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/badges/shields" /></a>
    <a href="https://circleci.com/gh/badges/shields/tree/master">
        <img src="https://img.shields.io/circleci/project/github/badges/shields/master" alt="build status"></a>
    <a href="https://circleci.com/gh/badges/daily-tests">
        <img src="https://img.shields.io/circleci/project/github/badges/daily-tests?label=service%20tests"
            alt="service-test status"></a>
    <a href="https://coveralls.io/github/badges/shields">
        <img src="https://img.shields.io/coveralls/github/badges/shields"
            alt="coverage"></a>
    <a href="https://lgtm.com/projects/g/badges/shields/alerts/">
        <img src="https://img.shields.io/lgtm/alerts/g/badges/shields"
            alt="Total alerts"/></a>
    <a href="https://discord.gg/HjJCwm5">
        <img src="https://img.shields.io/discord/308323056592486420?logo=discord"
            alt="chat on Discord"></a>
    <a href="https://twitter.com/intent/follow?screen_name=shields_io">
        <img src="https://img.shields.io/twitter/follow/shields_io?style=social&logo=twitter"
            alt="follow on Twitter"></a>
</p>

<p align="center">
  <a href="#">
    <img src="https://github.com/tamimdalwai/Docker-Web-App/blob/main/images/docker-engine.png" alt="Logo" width="80" height="80">
  </a>


  <h3 align="center">DOCKER WEBAPP</h3>

  <p align="center" font-weight="bold">
    "Build, Ship and Run Any App, Anywhere"
    <br />
    <br />
    <a href="https://github.com/">View Demo</a>
    ·
    <a href="https://github.com/tamimdalwai/Docker-Web-App/issues">Report Bug</a>
    ·
    <a href="https://github.com/tamimdalwai/Docker-Web-App/issues">Request Feature</a>
  </p>

</p>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
     <li><a href="#usage">TODO</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



## About The Project

<img src="https://github.com/tamimdalwai/Docker-Web-App/blob/main/images/screenshot.png" alt="Logo" width="" height="">

​		Docker is great containerization tool which provides user "Platfrom as a Service" (PaaS).A Docker WebApp is a lightweight  WebApp that includes feature to execute docker commands remotely from browser.This project focuses on UI/UX and easeness to admin user to perform docker tasks. Dynamic webinterface of this project makes it more attractive.

### Built With

* [Apache Web Server](https://httpd.apache.org/)
* [Docker](https://www.docker.com/)
* [Ajax](https://www.w3schools.com/xml/ajax_intro.asp)
* [HTML](https://www.w3schools.com/html/)
* [CSS](https://www.w3schools.com/css/default.asp)
* [JavaScript](https://www.w3schools.com/js/default.asp)

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Docker need to be installed on the remote linux server.

1. Docker
   * Docker command to install on Red Hat linux, CentOS, Fedora. 
     > `yum  install docker-ce`
2. Apache Web Server
   * Apache Webserver need to installed in the remoted linux server.
     > `yum install httpd`

### Installation

1. Clone the repo in the linux workspace

```sh
git clone https://github.com/tamimdalwai/Docker-Web-App
```

2. Copy the html,css files in the /var/www/html folder

```sh
cp -r ./www/html/* /var/www/html
```

3. Copy the cgi-bin files in the /var/www/cgi-bin

```js
cp -r ./www/cgi-bin/* /var/www/cgi-bin/
```

4. Start the apache daemon and docker daemon
```sh
#systemctl start httpd
#systemctl start docker
```
5. Check ip address where apache server is running and type the ip address in the address of browser...All Done!!!!!!!

## Usage

By using docker web app we can -

* remotely control docker containers
* as it is deployed on top of apache server, it can be accessed from anywhere.
* provides easeness to use and great ui experience.

## #TODO

Yet this project has not fully completed yet, we can further enhance this web app by adding following features:
* Get interactive Terminal of launched containers in web browser.
* Create form to launch containers for non-it guys with inputs as follows:
  - Select Image
  - Select no. of containers
  - Launch button
* Create form to Remove containers for non-it guys with inputs as follows:
  * Select Containers from list
  * Remove
* Create form to create custom docker images.
* Form/Button to push the images to [docker hub](https://hub.docker.com/) repository.


## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## Contact

Tamim Dalwai - tamimdalwai@gmail.com

Project Link: [Click Here...](https://github.com/tamimdalwai/Docker-Web-App)

