Installing Ubuntu on VirtualBox
===============================

Introduction
------------

In this section, we will guide you through the process of installing Ubuntu on VirtualBox. VirtualBox is a powerful virtualization software that allows you to create and run virtual machines on your host operating system. Installing Ubuntu in a virtual machine enables you to practice the course material without affecting your main system.

Step 1: Downloading Ubuntu ISO Image
-----------------------------------

Before you begin, download the latest Ubuntu Desktop ISO image from the official website. Make sure to choose the appropriate version for your system, such as a 64-bit or 32-bit image. 

:download:`Ubuntu_22.04.2 <https://ubuntu.com/download/desktop/thank-you?version=22.04.2&architecture=amd64>`

Step 2: Creating a New Virtual Machine
-------------------------------------

1. Open VirtualBox and click on the "New" button to create a new virtual machine.
2. Give your virtual machine a name (e.g., "Ubuntu_ASE") and select "Linux" as the Type, and "Ubuntu (64-bit)" as the Version (or choose the appropriate version based on your ISO image).
3. Allocate memory to the virtual machine. We recommend at least 4GB for smooth performance, but you can adjust this based on your system's resources.
4. Choose "Create a virtual hard disk now" and click "Create."

Step 3: Installing Ubuntu on the Virtual Machine
-----------------------------------------------

1. In the VirtualBox Manager, select the newly created virtual machine and click on the "Start" button.
2. When prompted, browse and select the Ubuntu ISO image you downloaded earlier.
3. Follow the on-screen instructions to install Ubuntu on the virtual machine. You can choose the default options or customize the installation based on your preferences.

Step 4: Essential Post-Installation Setup
----------------------------------------

After Ubuntu is installed on the virtual machine, you may need to perform some post-installation setup:

1. Update Ubuntu: Open a terminal and run the following commands to update the system:

   .. code-block:: bash

      sudo apt update
      sudo apt upgrade

2. Install Guest Additions: In the VirtualBox menu, go to "Devices" -> "Insert Guest Additions CD Image." Then, open a terminal and run:

   .. code-block:: bash

      sudo apt install build-essential dkms
      sudo mount /dev/cdrom /media/cdrom
      cd /media/cdrom
      sudo ./autorun.sh

Step 5: Install gcc and gfortran libraries
--------------------------



.. code-block:: bash

   sudo apt install gcc gfortran

Conclusion
----------

Congratulations! You have successfully installed Ubuntu on VirtualBox. Your virtual machine is now ready to be used for the course. You can now proceed with the rest of the course content and practice your atomistic simulations with ease.

Remember to save your progress and take additional snapshots as you progress through the course to have checkpoints to revert to if needed.

Happy learning and experimenting with Python for Atomistic Simulation!
