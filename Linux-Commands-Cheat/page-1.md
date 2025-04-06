# 🚀 Linux Commands Cheat Sheet

> A futuristic, clean, and developer-friendly list of essential Linux commands.

---

## 📁 Directory Commands

| 🧠 Command | 🔍 Description |
|-----------|----------------|
| `cd` | Navigate through files and directories |
| `cd ..` | Move one directory up |
| `cd -` | Move to your previous directory |
| `pwd` | Show current working directory |
| `mkdir [directory]` | Create a new directory |
| `rmdir` | Delete a directory |
| `scp [file.txt] [user@host:/path]` | Securely copy a file to a server |
| `rsync -a /source/ /destination/` | Sync contents between directories |

---

## 💾 Disk Usage Commands

| 💽 Command | 🧠 Description |
|-----------|----------------|
| `df` | Display disk space usage |
| `du` | Show space used by files/directories |
| `du -ah` | Show all files/folders with size |
| `du -sh` | Show total size of current folder |
| `fdisk -l` | View disk partitions |
| `findmnt` | Show mounted filesystems |

---

## 📄 File Commands

| 📦 Command | 📘 Description |
|-----------|----------------|
| `ls` | List directory contents |
| `ls -a` | Show hidden files |
| `ls -al` | Show detailed list view |
| `cat [file]` | Show contents of a file |
| `cat > [file]` | Create a new file |
| `diff file1 file2` | Compare contents of two files |
| `cat file1 file2 > file3` | Combine files into a new one |
| `cat file | tr a-z A-Z > output.txt` | Convert text to UPPERCASE |
| `tar cf archive.tar [file]` | Create a `.tar` archive |
| `tar czf archive.tar.gz [folder]` | Create a gzip archive |
| `tar xf archive.tar` | Extract `.tar` archive |
| `gzip [file]` | Compress file with `.gz` |
| `chmod [options] [file]` | Change permissions |
| `chown [user]:[group] [file]` | Change ownership |
| `rm [file]` | Delete a file |

---

## 🌌 Tips

```bash
# Combine commands using &&
mkdir project && cd project

# Use man to get help with any command
man rsync

# View human-readable sizes
du -sh *
