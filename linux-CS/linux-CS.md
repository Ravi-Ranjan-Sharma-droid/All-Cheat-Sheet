# 🐧 Linux Command Cheat Sheet for Developers

A comprehensive guide to essential Linux commands for efficient development workflows. 💻🚀

---

## 📂 File and Directory Management

| Command                           | Description                                        |
|-----------------------------------|----------------------------------------------------|
| `ls`                              | List files in the current directory                |
| `ls -l`                           | Detailed list with permissions, sizes, and dates   |
| `ls -a`                           | Show all files, including hidden ones              |
| `pwd`                             | Print the current working directory                |
| `cd [directory]`                  | Change to specified directory                      |
| `cd ..`                           | Move up one directory level                        |
| `mkdir [directory]`               | Create a new directory                             |
| `mkdir -p [dir1/dir2/dir3]`       | Create nested directories                          |
| `rmdir [directory]`               | Remove an empty directory                          |
| `rm [file]`                       | Remove a file                                      |
| `rm -r [directory]`               | Remove a directory and its contents recursively    |
| `cp [source] [destination]`       | Copy files or directories                          |
| `mv [source] [destination]`       | Move or rename files or directories                |
| `find [path] -name [pattern]`     | Search for files matching a pattern                |
| `tree`                            | Display directories and files in a tree-like format|

---

## 📝 File Viewing and Editing

| Command                           | Description                                        |
|-----------------------------------|----------------------------------------------------|
| `cat [file]`                      | Display the content of a file                      |
| `less [file]`                     | View file content one screen at a time             |
| `head [file]`                     | Display the first 10 lines of a file               |
| `tail [file]`                     | Display the last 10 lines of a file                |
| `nano [file]`                     | Open file in the Nano text editor                  |
| `vim [file]`                      | Open file in the Vim text editor                   |
| `echo "text" > [file]`            | Write text to a file (overwrite)                   |
| `echo "text" >> [file]`           | Append text to a file                              |
| `touch [file]`                    | Create a new empty file or update timestamp        |

---

## 🔍 File Permissions and Ownership

| Command                           | Description                                        |
|-----------------------------------|----------------------------------------------------|
| `chmod [permissions] [file]`      | Change file permissions                            |
| `chown [owner]:[group] [file]`    | Change file owner and group                        |
| `ls -l`                           | View file permissions and ownership                |
| `umask [permissions]`             | Set default permissions for new files              |

---

## 🔧 Process Management

| Command                           | Description                                        |
|-----------------------------------|----------------------------------------------------|
| `ps`                              | Display active processes                           |
| `top`                             | Show real-time active processes                    |
| `htop`                            | Interactive process viewer (if installed)          |
| `kill [PID]`                      | Terminate a process by its Process ID              |
| `killall [process_name]`          | Terminate all processes with the given name        |
| `bg`                              | Resume a suspended process in the background       |
| `fg`                              | Resume a process in the foreground                 |
| `jobs`                            | List current background jobs                       |
| `nohup [command] &`               | Run a command immune to hangups, in background     |

---

## 🌐 Networking

| Command                           | Description                                        |
|-----------------------------------|----------------------------------------------------|
| `ping [host]`                     | Send ICMP echo requests to test connectivity       |
| `curl [url]`                      | Transfer data from or to a server                  |
| `wget [url]`                      | Download files from the internet                   |
| `netstat -tuln`                   | Show listening ports and services                  |
| `ss -tuln`                        | Display socket statistics                          |
| `scp [user@host]:[file] [dest]`   | Securely copy files between hosts                  |
| `rsync -av [source] [dest]`       | Synchronize files between locations                |

---

## 🗃️ Archiving and Compression

| Command                                | Description                                       |
|----------------------------------------|---------------------------------------------------|
| `tar -cvf [archive.tar] [files]`       | Create a tar archive                              |
| `tar -xvf [archive.tar]`               | Extract a tar archive                             |
| `tar -czvf [archive.tar.gz] [files]`   | Create a compressed tar archive using gzip        |
| `tar -xzvf [archive.tar.gz]`           | Extract a compressed tar archive                  |
| `zip [archive.zip] [files]`            | Create a zip archive                              |
| `unzip [archive.zip]`                  | Extract a zip archive                             |

---

## 🛡️ User Management

| Command                           | Description                                        |
|-----------------------------------|----------------------------------------------------|
| `whoami`                          | Display the current logged-in user                 |
| `sudo [command]`                  | Execute a command as the superuser                 |
| `su [user]`                       | Switch to another user                             |
| `adduser [user]`                  | Add a new user                                     |
| `passwd [user]`                   | Change user password                               |
| `who`                             | Show who is logged in                              |
| `groups [user]`                   | Display groups a user belongs to                   |

---

## 🛠️ Disk Usage and Management

| Command                           | Description                                        |
|-----------------------------------|----------------------------------------------------|
| `df -h`                           | Display disk space usage in human-readable format  |
| `du -sh [directory]`              | Show disk usage of a directory                     |
| `mount [device] [dir]`            | Mount a filesystem                                 |
| `umount [device]`                 | Unmount a filesystem                               |
| `fsck [device]`                   | Check and repair a filesystem                      |

---

## 📈 System Monitoring and Performance

| Command                           | Description                                        |
|-----------------------------------|----------------------------------------------------|
| `uptime`                          | Show how long the system has been running          |
| `free -h`                         | Display memory usage                               |
| `vmstat`                          | Report system performance metrics                  |
| `iostat`                          | Report CPU and I/O statistics                      |
| `sar`                             | Collect, report, or save system activity           |

---

## 🧹 Package Management

**For Debian/Ubuntu-based systems:**

| Command                           | Description                                        |
|-----------------------------------|----------------------------------------------------|
| `apt-get update`                  | Update package lists                               |
| `apt-get upgrade`                 | Upgrade all packages                               |
| `apt-get install [package]`       | Install a new package                              |
| `apt-get remove [package]`        | Remove a package                                   |
| `apt-get autoremove`              | Remove unnecessary packages                        |
