# dahua-brute
Bruteforce dahua login page

## Setup
- Create python virtual environment and install deps
```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install requests
```
> For NixOS just do `nix-shell`

# Usage
- Add or modify `password-list.txt` according to your usage
- Add target ip addresses in `hosts.txt`

Now just run 
```bash
$ python dahua-brute.py
```
