## Linux Commands Cheat Sheet (Page 2)

### File Commands

| Command | Description |
|--------|-------------|
| rm -r [directory_name] | remove a directory recursively |
| rm -rf [directory_name] | remove a directory recursively without requiring confirmation |
| wc | print the number of words, lines, and bytes in a file |
| cp | copy files from the current directory to a different directory |
| cp [file_name1] [file_name2] | copy the contents of the first file to the second file |
| wget | download files from the internet |
| cp -r [directory_name1] [directory_name2] | recursively copy the contents of the first directory into the second directory |
| mv | move or rename files |
| mv [file_name1] [file_name2] | rename file_name1 to file_name2 |
| ln -s /path/to/[file_name] [link_name] | create a symbolic link to a file |
| touch [file_name] | create a new file |
| more [file_name] | show the contents of a file |
| head [file_name] | show the first 10 lines of a file |
| tail [file_name] | show the last 10 lines of a file |
| gpg -c [file_name] | encrypt a file |
| gpg [file_name.gpg] | decrypt a file |

### System & Process Commands

| Command | Description |
|--------|-------------|
| sudo | perform tasks that need administrative or root permissions |
| locate | search for a file or directory |
| find | to locate files within a directory |
| jobs | display current jobs |
| kill | terminate an unresponsive program |
| history | review the commands you entered before |
| uname | print information about your Linux system |
| man | show manual instructions of Linux commands |
| zip | compress files into a zip archive |
| unzip | extract zipped files from a zip archive |
| top | monitor system resource usage |
| ps | show a snapshot of active processes |
| echo | move data into a file |
| hostname | know the name of your host/network |
| ping | check connectivity to a server |

### Network

| Command | Description |
|--------|-------------|
| ip addr show | show IP addresses and network interfaces |
| ifconfig | show IP addresses of all network interfaces |
| netstat -pnltu | show active ports |
| netstat -nutlp | show more information about a domain |
| whois [domain] | show more information about a domain |
| dig [domain] | show DNS information about a domain |
| host [domain] | do an IP lookup for a domain |