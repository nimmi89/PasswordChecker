# Program to check password leaks

## Description

This program intends to find the number of times your password has been hacked without passing it over the Internet. The solution utilises partial  password sha-hash matching to find the right count.

## Requirements

Please find below the requirements to run this project:

- Python 3
- Modules - requests, hashlib

## Usage

1.Install modules using the command:
```
pip install hashlib
```
2.Run the [Python file](checkmypass.py) and pass it any text file containing all passwords to check:
```
python checkmypass.py <input text file>

```
3.The below example shows the expected output.
```

$ cat check_pass.txt
hhhhhhhhhhhhh6y8ookkjg
helloooooo
$ python checkmypass.py check_pass.txt
hhhhhhhhhhhhh6y8ookkjg was not found..Carry on!!!
helloooooo was found 76 times..You should probably change your password!!!
done
```

Check your password today itself, consider changing it if required and ensure security in your web activities!!! Keep learning!!!
