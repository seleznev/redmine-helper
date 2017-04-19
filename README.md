# redmine-helper

Usage:

```
$ ./redmine-helper --help
usage: redmine-helper [-h] [--version] [-d DOMAIN] -k KEY [-t TEMPLATE]
                      {list-projects}

positional arguments:
  {list-projects}

optional arguments:
  -h, --help            show this help message and exit
  --version             print program version
  -d DOMAIN, --domain DOMAIN
                        Redmine domain
  -k KEY, --key KEY     Redmine API key
  -t TEMPLATE, --template TEMPLATE
                        path to output template
```

Example:

```
$ ./redmine-helper list-projects -d example.com -k REDMINE_API_KEY -t templates/list-projects.j2 
# Redmine projects

* Project1
* Project2
* Project3
```
