# ABOUT
**For linux and mac users, not for windows :P**

**acabot** is a **command line interface** that provides a unified interface for using WebKiosk with a single configuration file. You can use acadbot from within your favorite terminal to meet all your WebKiosk needs.

Sneak Peak...
<p align="center">
  <img src="/asciinema/acadbot.svg?sanitize=true" alt="acadbot in work"/>
</p>


# DEPENDENCIES
To install the **dependencies** for acadbot, run the following command.

    $ pip3 install -r requirements.txt

# INSTALLATION
To install **acadbot** on your system, just run the following commands **one by one**.

    $ cd <navigate to the location where you want to install acadbot>
    $ git clone https://github.com/boddah31/acadbot
    $ cd acadbot
    # Installs acadbot from the given path.
    $ pip3 install -e .


**[WARNING] Don't delete the acadbot directory, after installation.**

# USING acadbot
If your're running acadbot for the very first time, you will need to configure it first using:

    $ acadbot config --user <roll number here>
    $ acadbot config --passwd<enter>
    # It will display a prompt, asking for your password.

After you're done with the configuration part, you're ready to use it as in the asciinema above(the **gif** image).


# AUTHORS
* Rishabh Mehta <eternal.blizzard23@gmail.com>
* Devesh Kashmiri <kashmiridevesh@gmail.com> 

If you have any issues or queries regarding acadbot, please don't
hesitate to email the **@authors**.

# LICENSE [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This code falls under the MIT license which permits the reuse of the proprietary software provided that all copies of the licensed software include a copy of the MIT License terms and the copyright notice.