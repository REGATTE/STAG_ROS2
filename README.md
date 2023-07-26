# STag ROS2: A ROS2 package for the Stable Fiducial Marker System

Based-on Source: [STag](https://github.com/bbenligiray/stag)

---

## Installation
### Install ROS2

This assumes you already have ROS2 installed on your device, else install either using the official [source](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html) or use [ansible ros2 installer](https://github.com/REGATTE/Ansible_ROS2).

## Install the repo

```sh
cd ~/ros2_ws/src/
git clone https://github.com/REGATTE/STAG_ROS2
colcon build
```
## Test

```sh
cd MarkerGenerator
python3 -m unittest test.py
```