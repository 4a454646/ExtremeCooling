# ExtremeCooling
A simple way to control (read: max out) your Lenovo Legion fans, via the command line. Targeted towards Linux users.

Based off the work of [Alberto Vicente from GitLab](https://gitlab.com/OdinTdh/extremecooling4linux). This removes all GUI elements and only necessitates one command: `./c.sh`.

## Installation Steps
1. Clone this directory.
2. Move both `c.sh` and `cooler.py` into a directory of your choice: I prefer `/home/<user>`.
3. Give execution permission to the shell script via `chmod +x c.sh`.
4. When you want to toggle extreme cooling, simply run the shell script, or run `cooler.py` as sudo.

(An easy way to do this is to keep things in your home directory: then, you can hotkey `Alt+F2` and type `./c.sh`.
