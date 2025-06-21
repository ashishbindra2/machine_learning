# 

## Os

### 1. Not a variant of UNIX.

```
a) AIX
b) Linux --- True
c) HP-UX
d) BSD-os
```



The term **"variant of Unix"** refers to different operating systems that are based on or inspired by the original **Unix** operating system. These variants can be broadly categorized into two types:

---

## 🧱 1. **Unix-certified (official) variants**
These are operating systems that comply with the **Single UNIX Specification** by The Open Group and are officially branded as UNIX®.

Examples:
| OS Name       | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| **AIX**       | IBM’s Unix, used in enterprise environments                                  |
| **HP-UX**     | Hewlett-Packard’s Unix, often used on HP servers                            |
| **Solaris**   | Originally by Sun Microsystems (now Oracle Solaris)                         |
| **UnixWare**  | Developed by SCO (later acquired by Xinuos)                                 |
| **IRIX**      | SGI’s version of Unix, used in high-performance graphics workstations       |

---

## 🧪 2. **Unix-like (non-certified) variants**
These are not certified by The Open Group but are heavily based on Unix principles, often open-source.

### 🔹 **BSD Family (Berkeley Software Distribution):**
- **FreeBSD** – Known for performance and network stack stability
- **OpenBSD** – Security-focused
- **NetBSD** – Portability-focused
- **DragonFly BSD** – Designed for performance and scalability

### 🔹 **Linux Distributions (Unix-like but not derived from original Unix):**
- **Ubuntu, Debian, Fedora, CentOS, Arch Linux** – Built on the Linux kernel but inspired by Unix
- **Android** – Based on the Linux kernel (thus Unix-like)

### 🔹 **macOS (formerly OS X):**
- **Darwin** (the core of macOS) is a Unix-based OS derived from BSD with Mach microkernel elements.
- macOS is officially **Unix 03** certified.

---

## 🧭 Summary Table

| Category         | Examples                      | Certification     |
|------------------|-------------------------------|-------------------|
| Official Unix    | AIX, HP-UX, Solaris           | Certified UNIX®   |
| BSD Variants     | FreeBSD, OpenBSD, NetBSD      | Not certified     |
| Linux Distros    | Ubuntu, Fedora, Arch, etc.    | Not certified     |
| macOS            | Darwin/macOS                  | Certified UNIX®   |

---

### 🧠 What is a **Kernel**?

The **kernel** is the **core component of an operating system**. It acts as a bridge between applications and the hardware, managing system resources like:

* **CPU scheduling**
* **Memory management**
* **Device I/O**
* **Process management**
* **File systems**

---

### 🔍 Types of Kernels

| Kernel Type     | Description                                                   | Example OS                     |
| --------------- | ------------------------------------------------------------- | ------------------------------ |
| **Monolithic**  | All core services run in a single space (fast, but complex)   | Linux, BSD                     |
| **Microkernel** | Minimal core; most services (e.g., drivers) run in user space | Minix, QNX, GNU Hurd           |
| **Hybrid**      | Combines monolithic and microkernel traits                    | Windows NT, macOS (XNU kernel) |
| **Exokernel**   | Minimal abstraction; gives apps more direct hardware access   | Research OS only               |
| **Nanokernel**  | Extremely small kernel, even less than microkernel            | Very niche/embedded systems    |

---

### 🛠 Key Components of a Kernel

1. **Process Manager** – Handles process creation, scheduling, and termination.
2. **Memory Manager** – Manages RAM allocation and paging.
3. **Device Drivers** – Interface with hardware devices.
4. **File System Manager** – Manages file operations and access.
5. **System Calls Interface** – Entry point for user programs to request services.

---

### 🐧 Examples of Unix or Unix-like Kernels

| Kernel Name    | Used In                  | Type        |
| -------------- | ------------------------ | ----------- |
| **Linux**      | Linux distributions      | Monolithic  |
| **XNU**        | macOS, iOS               | Hybrid      |
| **System V**   | Original AT\&T Unix      | Monolithic  |
| **BSD Kernel** | FreeBSD, OpenBSD, NetBSD | Monolithic  |
| **Mach**       | NeXTSTEP, GNU Hurd       | Microkernel |

---

If you're interested, I can show **kernel architecture diagrams** or explain **how a kernel boots** step-by-step. Would you like that?

### drrectory used in linux contain user informations


In Linux, **user information is primarily stored** in the following **files and directories**:

---

### 📁 **1. `/etc/passwd`**
- Stores basic user account information.
- Each line represents a user in this format:
  ```
  username:x:UID:GID:comment:home_directory:shell
  ```
- Example:
  ```
  john:x:1001:1001:John Doe:/home/john:/bin/bash
  ```

---

### 📁 **2. `/etc/shadow`**
- Stores **encrypted passwords** and password-related info.
- Only readable by root (more secure than `/etc/passwd`).
- Format includes: password hash, last change, expiry, etc.

---

### 📁 **3. `/etc/group`**
- Defines user **group memberships**.
- Format: `group_name:x:GID:user1,user2,...`

---

### 📁 **4. `/home/`**
- Each user typically has a personal directory:
  ```
  /home/john/
  /home/alice/
  ```
- Contains their files, configurations, downloads, etc.

---

### 📁 **5. `/var/mail/`**
- Contains **user mailbox files** (if mail is configured).
  ```
  /var/mail/john
  ```

---

### 🧠 Bonus: User Info Commands

- `whoami` → Shows your current username
- `id` → Shows UID, GID, and groups
- `getent passwd john` → Full details of user `john`
- `cat /etc/passwd` → See all users

---

Here is a list of **important Linux directories** (from the root `/`) and their **purpose**:

---

### 📂 **Linux Directory Structure Overview**

| Directory    | Purpose                                                                     |
| ------------ | --------------------------------------------------------------------------- |
| `/`          | **Root directory** – top of the directory tree                              |
| `/bin`       | Essential **user binaries** (e.g., `ls`, `cp`, `bash`) for all users        |
| `/sbin`      | System **administration binaries** (e.g., `reboot`, `ifconfig`)             |
| `/boot`      | Bootloader files (e.g., `vmlinuz`, `initrd`)                                |
| `/dev`       | Device files (e.g., `/dev/sda`, `/dev/null`)                                |
| `/etc`       | System-wide **configuration files**                                         |
| `/home`      | Home directories of normal users (e.g., `/home/john`)                       |
| `/lib`       | Essential shared **libraries** for binaries in `/bin` and `/sbin`           |
| `/lib64`     | Libraries for 64-bit systems                                                |
| `/media`     | Mount point for **removable media** (USBs, CDs)                             |
| `/mnt`       | Temporary mount point for filesystems                                       |
| `/opt`       | Optional software packages (usually third-party)                            |
| `/proc`      | Virtual **filesystem with process and system info** (e.g., `/proc/cpuinfo`) |
| `/root`      | Home directory of the **root user**                                         |
| `/run`       | Temporary runtime data since boot                                           |
| `/srv`       | Data for **services** (e.g., FTP, web servers)                              |
| `/sys`       | Virtual filesystem for **hardware and device info**                         |
| `/tmp`       | Temporary files (cleared on reboot)                                         |
| `/usr`       | Secondary hierarchy: user programs, libraries, docs                         |
| `/usr/bin`   | Most user-level **program binaries**                                        |
| `/usr/sbin`  | Non-essential system binaries (admin tools)                                 |
| `/usr/lib`   | Libraries for `/usr/bin` and `/usr/sbin`                                    |
| `/usr/local` | Locally installed software (custom programs)                                |
| `/var`       | Variable data like logs, mail, databases                                    |
| `/var/log`   | Log files (e.g., `syslog`, `auth.log`)                                      |
| `/var/tmp`   | Persistent temporary files                                                  |

---

### 🧭 Visual Structure (Tree)

```
/
├── bin/
├── boot/
├── dev/
├── etc/
├── home/
│   ├── user1/
│   └── user2/
├── lib/
├── media/
├── mnt/
├── opt/
├── proc/
├── root/
├── run/
├── sbin/
├── srv/
├── sys/
├── tmp/
├── usr/
│   ├── bin/
│   ├── lib/
│   └── local/
└── var/
```

---
In Linux, **directory permissions** determine who can access or modify files **within** that directory. The permission model uses:

* **r** → Read (list files)
* **w** → Write (create/delete/rename files)
* **x** → Execute (enter the directory)

---

### 📁 Common Default Directory Permissions

| Directory    | Owner  | Group  | Others  | Typical Mode       | Description                                           |
| ------------ | ------ | ------ | ------- | ------------------ | ----------------------------------------------------- |
| `/`          | `root` | `root` | `x`     | `755` (drwxr-xr-x) | Everyone can access root directory                    |
| `/home`      | `root` | `root` | `x`     | `755`              | Users can access their own `/home/username`           |
| `/home/user` | `user` | `user` | none    | `700` or `750`     | Only the user (or group) can access their home dir    |
| `/tmp`       | `root` | `root` | `rwx+t` | `1777`             | Writable by all, but users can't delete others' files |
| `/etc`       | `root` | `root` | `r-x`   | `755`              | Readable config files, only root can write            |
| `/var/log`   | `root` | `root` | none    | `750` or `700`     | Logs accessible to root and maybe system users        |
| `/usr`       | `root` | `root` | `r-x`   | `755`              | Readable system files, no write access for users      |
| `/dev`       | `root` | `root` | varies  | `755`              | Special device files, permission per device           |
| `/proc`      | `root` | `root` | varies  | `555` or `r-x`     | Virtual files, mostly readable                        |

---

### 🛠 Example: Checking Directory Permissions

Run this in your terminal:

```bash
ls -ld /etc /home /tmp /var/log
```

Example output:

```
drwxr-xr-x  123 root root 4096 Jun 20 09:00 /etc
drwxr-xr-x   10 root root 4096 Jun 20 09:00 /home
drwxrwxrwt   15 root root 4096 Jun 20 09:00 /tmp
```

---

### 🔒 Special Permissions

* **Sticky bit (`t`)**: Used in `/tmp` to prevent users from deleting others' files.
* **Setuid (`s`)**: Runs a program with the permission of the file owner.
* **Setgid (`s`)**: Files created inherit the group of the directory.

---

### 🧪 Change Directory Permissions

```bash
chmod 755 /mydir        # rwx for owner, rx for group and others
chmod 700 /mydir        # only owner can access
chmod 1777 /mydir       # world-writable with sticky bit (like /tmp)
```

---

Would you like a cheat sheet or script to audit permissions across your system?
### 🧠 What Does "Execute" (x) Mean in Linux Permissions?

In Linux, the **`execute` permission (`x`)** has **different meanings** depending on whether it's applied to a **file** or a **directory**:

---

### 📄 **1. Execute on a File**

* It means the file **can be run as a program or script**.
* Applies to:

  * Binary executables (`/bin/ls`)
  * Shell scripts (`my_script.sh`)

#### 🔧 Example:

```bash
chmod +x my_script.sh
./my_script.sh  # This will now run
```

Without `x`, you'll get:

```bash
bash: ./my_script.sh: Permission denied
```

---

### 📁 **2. Execute on a Directory**

* **Allows you to "enter" (cd into)** the directory.
* Needed to **access files or subdirectories** by name (but not list them unless you also have `r`).

#### 🔧 Example:

```bash
ls /mydir    # Fails if no 'r'
cd /mydir    # Fails if no 'x'
```

| Permission | Meaning for Directories                   |
| ---------- | ----------------------------------------- |
| `r`        | Can **list** directory contents (`ls`)    |
| `w`        | Can **create/delete/rename** files inside |
| `x`        | Can **cd into**, and **access** by name   |

---

### 🔍 Example Breakdown

```bash
drwxr-x--x  2 user1 users 4096 Jun 21 10:00 mydir
```

* `d` = directory
* `rwx` = owner can read, write, and enter
* `r-x` = group can read and enter
* `--x` = others can only enter (but not list)

---

### 🧪 Test It Yourself

```bash
mkdir testdir
touch testdir/secret.txt
chmod 111 testdir     # x only

cd testdir            # ✅ works
ls                    # ❌ Permission denied
cat secret.txt        # ✅ works if you know filename
```

---

Let me know if you'd like a **diagram** or **real-world scenarios** of how `x` permission is used in security setups.


### ⌨️ **What does `Ctrl + D` do in Linux/Unix?**

`Ctrl + D` is a **keyboard shortcut** with different behavior depending on **context**, but in general:

---

### 🧠 **It sends an EOF (End Of File)** signal to the terminal or input stream.

---

### 💻 In the Terminal Shell (like Bash, Zsh):

| Situation                | What Happens                                 |
| ------------------------ | -------------------------------------------- |
| **At empty prompt**      | Closes the terminal or logs out of the shell |
| **In middle of command** | Acts as EOF, ending input to that command    |

#### 🧪 Example:

```bash
cat > myfile.txt
hello
world
[Press Ctrl + D]
```

* Ends the `cat` input and saves the file.
* Without `Ctrl + D`, the shell keeps waiting for more input.

---

### 📝 In Programming / Input to Scripts:

* Used to **end input** when reading from standard input (stdin).
* Often used with commands like `cat`, `python`, or while reading data interactively.

---

### ❌ NOT a "Delete" Shortcut

* It **does NOT mean "delete"** like `Backspace` or `Del` keys.
* `Ctrl + D` stands for **EOF**, not **Erase**.

---

### 🔄 Summary

| Context               | `Ctrl + D` Action                 |
| --------------------- | --------------------------------- |
| Bash Shell            | Logout / Exit                     |
| `cat`, `python`, etc. | Send EOF to end input             |
| SSH Session           | Ends session (if at shell prompt) |
| Input redirection     | Ends manual input from keyboard   |

---

Would you like a full cheat sheet of other Linux terminal shortcuts (`Ctrl + C`, `Ctrl + Z`, etc.)?


In Linux and programming, **regular expressions (regex)** are patterns used to **match text**. There are **different types (or flavors)** of regular expressions, mainly based on the tool or programming language being used.

---

## 🔍 **Types of Regular Expressions**

### 1. **Basic Regular Expressions (BRE)**

Used by traditional tools like `grep`, `sed`, and `ed`.

#### 🧩 Features:

* Limited metacharacters (some need backslashes)
* Simpler syntax

#### 🧪 Examples:

| Pattern   | Meaning                                |
| --------- | -------------------------------------- |
| `.`       | Any single character                   |
| `*`       | Zero or more of the previous character |
| `[abc]`   | Any one of a, b, or c                  |
| `\{n,m\}` | Repeat previous item n to m times      |
| `\(` `\)` | Grouping (must be escaped)             |
| `\|`      | OR operator (must be escaped)          |

---

### 2. **Extended Regular Expressions (ERE)**

Used by tools like `egrep` or `grep -E`.

#### 🧩 Features:

* More readable: no need to escape grouping or alternation
* Includes `+`, `?`, `|`, `()` without backslashes

#### 🧪 Examples:

| Pattern | Meaning              |                  |
| ------- | -------------------- | ---------------- |
| `a+`    | One or more 'a's     |                  |
| `a?`    | Zero or one 'a'      |                  |
| \`a     | b\`                  | Match 'a' or 'b' |
| `(abc)` | Group 'abc' together |                  |

---

### 3. **Perl-Compatible Regular Expressions (PCRE)**

Used in tools like `perl`, `grep -P`, and most modern programming languages.

#### 🧩 Features:

* Most powerful and flexible
* Support for lookaheads, backreferences, conditionals, Unicode, etc.

#### 🧪 Examples:

| Pattern    | Meaning                                 |
| ---------- | --------------------------------------- |
| `(?=abc)`  | Positive lookahead (followed by 'abc')  |
| `(?<=abc)` | Positive lookbehind (preceded by 'abc') |
| `\d{2,4}`  | Match 2 to 4 digits                     |
| `\bword\b` | Word boundary match for 'word'          |

---

## 🧪 Summary Table

| Type     | Tools/Use                    | Syntax Complexity | Escaping Needed        |   |
| -------- | ---------------------------- | ----------------- | ---------------------- | - |
| **BRE**  | `grep`, `sed`, `awk`         | Simple            | Yes                    |   |
| **ERE**  | `egrep`, `grep -E`           | Moderate          | No (for (), +,         | ) |
| **PCRE** | `perl`, `grep -P`, languages | Advanced          | Minimal, rich features |   |

---

### Bonus: Programming Languages with Regex Support

| Language   | Regex Flavor                 |
| ---------- | ---------------------------- |
| Python     | PCRE-like via `re`           |
| JavaScript | JavaScript RegEx             |
| Java       | Java RegEx (similar to PCRE) |
| Ruby       | PCRE-like                    |

---

Would you like a **cheat sheet of common regex patterns** (email, phone, URL, etc.) or how to test regex in Linux?

### copy data without overwriting existing files
Here’s a complete list of useful `cp` (copy) command options in Linux, with clear explanations and examples. This cheat sheet covers **copying files, directories, preventing overwrites, preserving metadata**, and more.

---

## 📦 **`cp` Command Overview**

```bash
cp [OPTIONS] source destination
```

---

## 🧰 **Most Common `cp` Options**

| Option                                 | Meaning                                                          | Example                            |
| -------------------------------------- | ---------------------------------------------------------------- | ---------------------------------- |
| `-r` or `-R`                           | Copy directories **recursively**                                 | `cp -r dir1/ dir2/`                |
| `-f`                                   | **Force overwrite** (even if file is write-protected)            | `cp -f a.txt b.txt`                |
| `-i`                                   | **Interactive** – Ask before overwriting                         | `cp -i a.txt b.txt`                |
| `-n`                                   | **No overwrite** – Skip existing files                           | `cp -n a.txt b.txt`                |
| `-u`                                   | Copy **only if source is newer** than destination                | `cp -u a.txt b.txt`                |
| `-v`                                   | **Verbose** – Show files being copied                            | `cp -v a.txt b.txt`                |
| `-a`                                   | **Archive** – Preserve everything (same as `-dr --preserve=all`) | `cp -a dir1/ dir2/`                |
| `-p`                                   | Preserve **timestamp, mode, ownership**                          | `cp -p a.txt b.txt`                |
| `--preserve=mode,ownership,timestamps` | Fine control over what to preserve                               | `cp --preserve=all a.txt b.txt`    |
| `--parents`                            | Preserve full **path structure** when copying                    | `cp --parents dir1/file.txt dir2/` |
| `--no-clobber`                         | Same as `-n` (don't overwrite)                                   | `cp --no-clobber a.txt b.txt`      |
| `--backup`                             | Create backup of existing files                                  | `cp --backup=numbered a.txt b.txt` |

---

## 🧪 **Example Use Cases**

### 1. 🔁 Copy a Directory (Recursive)

```bash
cp -r myfolder/ /backup/myfolder/
```

### 2. 🔒 Copy Without Overwriting

```bash
cp -n file.txt /backup/
```

### 3. 🗃️ Preserve Metadata

```bash
cp -p file.txt /backup/
```

### 4. 📦 Full Archive Copy (best for backup)

```bash
cp -a myfolder/ /backup/myfolder/
```

### 5. 👀 Show Copy Progress (Verbose)

```bash
cp -rv myfolder/ /backup/
```

### 6. 🧠 Smart Update: Only Copy If Newer

```bash
cp -u file.txt /backup/
```

---

## ⚠️ Note

* Always be careful when copying **over existing files** — use `-i` or `-n` to prevent accidental data loss.
* For **large or complex copies**, consider using `rsync`.

---

Would you like a **bash script** that uses `cp` to safely back up files or sync directories with logs?

To **copy data without overwriting existing files**, you can use the `cp` command with the **`-n` (no-clobber)** option in Linux.

---

### ✅ **Basic Command**

```bash
cp -n source_file target_file
```

This will **copy only if `target_file` doesn't exist**.

---

### 📁 **Copying a Directory Without Overwriting Files**

```bash
cp -rn source_dir/ target_dir/
```

* `-r`: recursive (for directories)
* `-n`: do not overwrite existing files

---

### 🧪 Example

```bash
mkdir source target
echo "hello" > source/file1.txt
echo "world" > target/file1.txt

cp -n source/file1.txt target/   # ❌ file1.txt is NOT overwritten
```

---

### 💡 Alternative Using `rsync` (More Powerful)

```bash
rsync -av --ignore-existing source_dir/ target_dir/
```

* `-a`: archive mode (preserves timestamps, permissions, etc.)
* `-v`: verbose
* `--ignore-existing`: skip files that already exist in the target

---

### 🧭 Summary

| Tool    | Command Example                          | Description                         |
| ------- | ---------------------------------------- | ----------------------------------- |
| `cp`    | `cp -n file1 dest/`                      | Simple copy, no overwrite           |
| `cp`    | `cp -rn src/ dest/`                      | Recursive copy, skip existing       |
| `rsync` | `rsync -av --ignore-existing src/ dest/` | Faster & safer for large operations |

---

Let me know if you want a script to copy only new/modified files or handle duplicates smartly.

### 🧠 **`vi` Editor Modes Explained (Cheat Sheet)**

The `vi` (or `vim`) editor has **three main modes**, and understanding them is crucial for editing files efficiently.

---

## 🔀 1. **Normal Mode (Command Mode)**

* Default mode when you open `vi`.
* Used for navigation and issuing commands (e.g., delete, copy, paste).

🔧 **Common Commands:**

| Command         | Action                            |
| --------------- | --------------------------------- |
| `h` `j` `k` `l` | Move cursor left, down, up, right |
| `x`             | Delete character under cursor     |
| `dd`            | Delete (cut) a line               |
| `yy`            | Copy a line (yank)                |
| `p`             | Paste                             |
| `u`             | Undo                              |
| `/word`         | Search for "word"                 |
| `:`             | Enter command-line mode           |

✅ **Enter Normal Mode**:
Press `Esc` from any other mode.

---

## ✏️ 2. **Insert Mode**

* Allows you to **edit or insert text** like in a regular text editor.

🔧 **To Enter Insert Mode:**

| Command | Meaning              |
| ------- | -------------------- |
| `i`     | Insert before cursor |
| `I`     | Insert at line start |
| `a`     | Append after cursor  |
| `A`     | Append at line end   |
| `o`     | Open new line below  |
| `O`     | Open new line above  |

✅ **Exit Insert Mode**:
Press `Esc`

---

## 💻 3. **Command-Line Mode (Colon Mode)**

* Used for saving, quitting, and advanced commands.

🔧 **Common Commands (start with `:`):**

| Command     | Description                   |
| ----------- | ----------------------------- |
| `:w`        | Save (write)                  |
| `:q`        | Quit                          |
| `:wq`       | Save and quit                 |
| `:q!`       | Quit **without saving**       |
| `:x`        | Save and quit (same as `:wq`) |
| `:set nu`   | Show line numbers             |
| `:set nonu` | Hide line numbers             |

✅ **Enter this mode**:
From **Normal Mode**, press `:`.

---

## 🧭 Mode Navigation Summary

| From \ To    | Normal Mode | Insert Mode         | Command Mode    |
| ------------ | ----------- | ------------------- | --------------- |
| Normal       | —           | `i`, `a`, `o`, etc. | `:`             |
| Insert       | `Esc`       | —                   | `Esc`, then `:` |
| Command-Line | Press `Esc` | `Esc`, then `:`     | —               |

---

Would you like a downloadable **vi/vim cheat sheet PDF** or a guide to customize `.vimrc`?

### 🧠 What is the **Default Field Delimiter** in Linux Commands?

In many Unix/Linux commands that work with **text files**, the **default field delimiter** (also called a separator) is typically:

```
(default) ⏩ **Whitespace** (spaces or tabs)
```

---

## 🔍 Common Commands and Their Default Field Delimiters

| Command         | Default Field Delimiter      | Notes                                                           |
| --------------- | ---------------------------- | --------------------------------------------------------------- |
| `cut`           | **TAB (`\t`)**               | You can override with `-d` (e.g., `-d ':'`)                     |
| `awk`           | **Whitespace (spaces/tabs)** | Fields accessed via `$1`, `$2`, etc. You can change using `-F`  |
| `sort`          | **Entire line**              | Can specify fields with `-k` and delimiter with `-t`            |
| `uniq`          | **Entire line**              | Doesn't split by fields unless you use `cut` or `awk` before it |
| `tr`            | Character-by-character       | No concept of fields — operates on characters                   |
| `paste`         | **TAB (`\t`)**               | Can change with `-d`                                            |
| `join`          | **Space or TAB**             | Can change with `-t`                                            |
| `IFS` (in bash) | **Whitespace**               | Internal Field Separator (used in shell scripting)              |

---

### 🧪 Examples

#### 1. `cut`

```bash
echo "apple banana cherry" | cut -f2    # Won't work unless separated by TAB
```

```bash
echo "apple:banana:cherry" | cut -d':' -f2
# Output: banana
```

#### 2. `awk`

```bash
echo "apple banana cherry" | awk '{print $2}'
# Output: banana

echo "apple:banana:cherry" | awk -F':' '{print $2}'
# Output: banana
```

#### 3. `sort`

```bash
sort -t':' -k2 file.txt
# Sort by 2nd field using ':' as delimiter
```

---

### 📌 Bash Script Tip: Change Field Delimiter

```bash
IFS=:
read a b c <<< "apple:banana:cherry"
echo "$b"   # Output: banana
```

---

Would you like a script that detects the delimiter in a file automatically or handles CSV/TSV files safely?

### 🧠 How to **Read Input in `awk`**

In `awk`, input is **read automatically line by line** from a file or standard input (stdin). You **don’t need to manually call a function to read input** — `awk` handles it for you.

---

## ✅ Basic Structure

```bash
awk '{ print $0 }' file.txt
```

* `awk` reads **each line** of the file.
* `$0` = the **entire line**
* `$1`, `$2`, etc. = individual **fields/columns**

---

## 🧪 Example: Read Input from User via Pipe

```bash
echo "John 25" | awk '{ print "Name:", $1, "| Age:", $2 }'
# Output: Name: John | Age: 25
```

---

## 📥 Reading from `stdin` (Manual input)

```bash
awk '{ print "You entered:", $0 }'
```

Then type something and press **Enter**:

```text
hello world
# Output: You entered: hello world
```

🔚 Press **Ctrl + D** to send EOF and end input.

---

## 🧩 Using `awk` with `read` (in shell, not inside awk)

```bash
read line
echo "$line" | awk '{ print $1, $2 }'
```

> `read` is a **shell command**, not part of `awk`. It reads into a variable which is then piped to `awk`.

---

## 📘 Multi-Line Input Example

```bash
awk '{ print "Line:", NR, "->", $0 }'
```

Run it, then paste or type multiple lines. It will:

* Automatically read each line
* Print line number (`NR`) and content

---

## 🔄 Custom Input Field Separator

You can change how `awk` splits fields using `-F`:

```bash
echo "apple,banana,grape" | awk -F',' '{ print $2 }'
# Output: banana
```

---

### 🧭 Summary

| Concept         | In `awk`                             |
| --------------- | ------------------------------------ |
| Read Line       | Automatic (`awk` reads line by line) |
| Read Field      | Use `$1`, `$2`, ...                  |
| All Input Line  | `$0`                                 |
| Line Number     | `NR`                                 |
| Field Separator | `-F` option                          |
| End Input       | **Ctrl + D**                         |

---

Would you like a **real-world awk example** like CSV parsing, summing columns, or conditional filtering?

### ✅ **Command to Get the PID of the Current Shell**

To get the **Process ID (PID)** of your **current shell**, use:

```bash
echo $$
```

---

### 📌 Explanation:

* `$$` is a **special shell variable** that stores the **PID of the currently running shell**.

---

### 🧪 Example:

```bash
$ echo $$
31847
```

That means your current shell (e.g., Bash) is running as PID **31847**.

---

### 🔍 Bonus: Related PID Commands

| Command      | Description                                |                               |
| ------------ | ------------------------------------------ | ----------------------------- |
| `echo $$`    | PID of current shell                       |                               |
| `ps`         | List all running processes                 |                               |
| `ps -p $$`   | Details of the current shell process       |                               |
| `echo $PPID` | PID of **parent process** (e.g., terminal) |                               |
| \`ps -ef     | grep bash\`                                | Find all bash shell processes |

---

Would you like a script that logs and tracks shell PIDs for user sessions?

It looks like you're asking **"cron is a?"** (possibly a typo of "corn"). So let’s clarify both meanings:

---

### 🌽 If you meant **"corn"**:

> **Corn** is a **grain/plant** (botanically called *maize*) used for food, livestock feed, and biofuel.

---

### 🕒 If you meant **"cron"**, here’s the real answer:

### 🧠 **`cron` is a Linux/Unix time-based job scheduler.**

It’s a **daemon** that runs in the background and executes tasks (called **cron jobs**) **at specified times or intervals**.

---

### ✅ Key Features of `cron`:

| Feature     | Description                            |
| ----------- | -------------------------------------- |
| Scheduler   | Automates command/script execution     |
| Syntax      | Uses crontab file (`crontab -e`)       |
| Granularity | Runs jobs **by minute/hour/day/month** |
| Daemon      | Background service (`crond`)           |

---

### 🧾 Example `cron` Job

```cron
0 5 * * * /home/user/backup.sh
```

Runs `backup.sh` every day at 5:00 AM.

**Cron fields:**

```
* * * * *  command
│ │ │ │ │
│ │ │ │ └─── Day of week (0-6, Sun-Sat)
│ │ │ └───── Month (1-12)
│ │ └─────── Day of month (1-31)
│ └───────── Hour (0-23)
└─────────── Minute (0-59)
```

---

### 📦 Command Summary

| Command                 | Use                               |
| ----------------------- | --------------------------------- |
| `crontab -e`            | Edit the current user's cron jobs |
| `crontab -l`            | List the current user's cron jobs |
| `crontab -r`            | Remove all cron jobs              |
| `systemctl status cron` | Check cron daemon status          |

---

Let me know if you want a **cron expression generator**, validator, or examples for specific use cases like backups, logs, or reminders.
