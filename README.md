[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]


<br />
<div align="center">
<h3 align="center">PS3 HFW Server</h3>
  <p align="center">
    Download and install Hybrid Firmware (HFW) Without PC.
    <br />
    <br />
    <a href="https://replit.com/@frxx/ps3-hfw-server-node">Run live (HFW 4.89)</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a proxy server to trick the console that there is a new version of the firmware, and it downloads and installs it, doing the opposite of what is commonly done when a new version comes out and you want to log in to PSN with an older version.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
* Node.js v16.x
* Firmware desired to install, see [PS3Xploit](https://ps3xploit.com)

### Installation

1. Clone the repo
   ```git clone https://github.com/xfrcc/ps3-hfw-server.git```
2. Paste the Firmware File in the firmware folder
3. in proyect folder, run ```npm install``` to install dependencies
3. Start server
   ```node .```
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

In the PS3 Follow the next steps
* Go to Network Settings>Internet connection settings and select the same setting as follow
* Settings Method: Custom
* Connection Method: Wired or Wireless
* IP Address Setting: Automatic
* DHCP Host Name: Do Not Set
* DNS Setting: Automatic
* MTU: Automatic
* Proxy Server: Use
* In Proxy Server Address, if you're running locally you write the ip where the proxy server is running and port is 80 by default, if you're using the repl live write the one provided there
* Now continue and UPnP enable, save Settings but DO NOT test connection (it wont work)
* Go to system update, a fake 9.99 one will appear, just install as normal
* Optional, go to the web browser to start instantly the PS3Xploit's HEN Installer
* Don't forget to disable the proxy after in your PS3
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [PS3Xploit Team](https://ps3xploit.com)
* [PS3-custom-fwversion-proxy](https://github.com/Mte90/PS3-custom-fwversion-proxy)
* [PS3-Proxy-Server-for-Android](https://github.com/DADi590/PS3-Proxy-Server-for-Android)
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/xfrcc/ps3-hfw-server.svg?style=for-the-badge
[contributors-url]: https://github.com/xfrcc/ps3-hfw-server/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/xfrcc/ps3-hfw-server.svg?style=for-the-badge
[forks-url]: https://github.com/xfrcc/ps3-hfw-server/network/members
[stars-shield]: https://img.shields.io/github/stars/xfrcc/ps3-hfw-server.svg?style=for-the-badge
[stars-url]: https://github.com/xfrcc/ps3-hfw-server/stargazers
[issues-shield]: https://img.shields.io/github/issues/xfrcc/ps3-hfw-server.svg?style=for-the-badge
[issues-url]: https://github.com/xfrcc/ps3-hfw-server/issues
