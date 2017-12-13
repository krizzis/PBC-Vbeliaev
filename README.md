# PBC-Vbeliaev #  

Project for Python Boot Camp (SoftServe, Dec 2017)
Author: Beliaev Viacheslav

## Table of contents ##
* **[Day 1](#day-1)**
  * [Vagrant file](#1-vagrant-file)
  * [Fibonacci sequence](#2-fibonacci-sequence)
  * [Numbers pairs](#3-numbers-pairs)
* **[Day 2](#day-2)**
  * [Prepare virtual environment](#1-prepare-virtual-environment)
  * [Simple unit tests](#2-simple-unit-tests)
  * [Install Java on VM](#3-install-java-on-vm)
* **[Day 3](#day-3)**
  * [Structuring project](#1-structuring-project)
  * [Use parametrize](#2-use-parametrize)
  * [Configure markers](#3-configure-markers)
  * [Use CLI config for your tow programs](#4-use-cli-config-for-you-tow-programs)
  * [Decorator](#5-decorator)
* **[Day 4](#day-4)**
  * [Fix issues](#fix-issues)
* **[Day 5](#day-5)**
  * [Automate Selenium Grid installation](#1-automate-selenium-grid-installation)
* **[Day 6](#day-6)**
  * [Update project structure](#1-update-project-structure)
  * [Update vagrant](#2-update-vagrant)
  * [Create tests](#3-create-tests)
* **[Day 7](#day-7)**
  * [Install firefox and geckodriver on VM](#1-install-firefox-and-geckodriver-on-vm)
  * [Update Selenium grid run](#2-update-selenium-grid-run)
  * [Test a grid config](#3-test-a-grid-config)

## DAY 1 ##

### **1. Vagrant file** ###

*Deploy VM with Vagrant, configure IP address and name*

Run `vagrant init`

Open the Vagrantfile and change the contents to the following:

```
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.provider "virtualbox" do |vb|
  vb.name = "Vbeliaev"
  end
end
```

Then run `vagrant up`
Finally you can connect to your VM with ssh: `ssh vagrant@192.168.33.10` (login/pass is 'vagant')


[File](https://github.com/krizzis/PBC-Vbeliaev/blob/master/Vagrantfile)


### **2. Fibonacci sequence** ###
*Function which prints desired count of fibonacci numbers.*  
You can run the script `Fibonacci.py`  

* **number (int):** (Mandatory) Number The required number of sequence members.  
E.g. `Fibonacci.py 15` will print 15 first members of Fibonacci sequence


* **-h:** Print help


### **3. Numbers pairs** ###
*Function which prints pairs of numbers which sum is specified for a given collection of numbers*
You can run the script `Numbers_pairs.py`

* **-n (--numbers):** (Mandatory) List of numbers to check.  
* **-s (--summ):** (Optional) Sum of pairs to check. Default value = 10
* **-a (--all):** (Optional) Flag to find all possible pairs. Only unique pairs by default

E.g. `Numbers_pairs.py 1 5 8 9 10 -74 5 6 4 4` will print (\[1, 9],\[5, 5], \[6,4])  
while `Numbers_pairs.py 1 5 8 9 10 -74 5 6 4 4 --all` will print (\[1, 9],\[5, 5], \[6,4], \[6,4])

* **-h:** Print help

## DAY 2 ##

### **1. Prepare virtual environment** ###
*Prepare the virtual environment for your project.*

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **2. Simple unit tests** ###
*Write unit tests for your code (2 modules) from Day 1 HW. For each module with code please create a module with the unit tests. Don't forget about requirements.txt.*

- Both `Fibonacci.py` and `Numbers_pair.py` have been refactored.
- Modules `test_fib.py` and `test_pair.py` have been added. Modules contain unit tests for `Fibonacci.py` and `Numbers_pair.py` respectively
- File `Requirements.txt` with needed dependencies for **pytest** has been added  

### **3. Install Java on VM:** ###
*Update Vagrantfile for installing of Java on VM*  

Open Vagrantfile and add following section:
```
config.vm.provision "shell", inline: <<-SHELL
     apt-get -y -q update
     apt-get -y -q upgrade
     apt-get -y -q install software-properties-common htop
     add-apt-repository ppa:webupd8team/java
     apt-get -y -q update
     echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections
     apt-get -y -q install oracle-java8-installer
     update-java-alternatives -s java-8-oracle
SHELL
```

Run VM and check Java has been installed `java -version`  

## DAY 3 ##

### **1. Structuring project** ###

Current project's structure rebuild into:
```
├── README.md               <- This file. Contains all information need to know to work with this code
├── my_app                  <- Main package for code
├── requirements.txt        <- Contains all required dependencies
└── tests                   <- Main package for unit tests
```

### **2. Use parametrize** ###
Both `test_fib.py` and `test_pairs.py` have been refactored. Similar tests have been replaced with parametrized tests.
E.g.:

```
@pytest.mark.parametrize("test_input,expected", [
    (1, [0]),
    (2, [0, 1]),
    (3, [0, 1, 1]),
    (7, [0, 1, 1, 2, 3, 5, 8]),
])
def test_positive(test_input, expected):
    assert fib(test_input) == expected
```

### **3. Configure markers** ###

One dummy test has been added to `test_fib.py` to demonstrate `skip` markers:

```
@pytest.mark.skip
def test_some_todo_test():
    pass

```

### **4. Use CLI config for your tow programs** ###

Module `app.py` has been added to the root. You can run module from console to call either `Fibonacci.py` or `Numbers_pairs.py` using their arguments.
You can find more detail in section Day 1:  [Fibonacci](#2-fibonacci-sequence) and [Numbers pairs](#3-numbers-pairs)

Also Module `app2.py` has been added for `docopt` version of implementation.

`Docopt` is a command-line interface description language. For more details about library you can find on its website: [docopt.org](http://docopt.org/) or
check project's git: [Docopt](https://github.com/docopt/docopt)

### **5. Decorator** ###
Module `Decorator` have been added. Contains decorator to print function name and arguments each run. Example of output:
`pairs([1, 9, 1], all_pairs=True)`

## DAY 4 ##

### **Fix issues:** ###
  
```
- All modules have been renamed to be satisfy to naming conversion
- Mark parametrizing  have been added to all tests
- number_pairs.py have been updated to needed signature. Related test have been updated also
```

## DAY 5 ##

### **1. Automate Selenium Grid installation** ###

Library `paramiko` has been added to the project:

```
Paramiko is a Python (2.7, 3.4+) implementation of the SSHv2 protocol [1], providing both client and server functionality.
While it leverages a Python C extension for low level cryptography (Cryptography), Paramiko itself is a pure Python interface around SSH networking concepts.
```
[Paramiko web-site](http://www.paramiko.org/) [Paramiko git](https://github.com/paramiko/paramiko/)

### **2. Use pytest fixtures** ###

Module `conftest.py` contains now fixture to set-up Selenium grid on the virtual machine before tests.
It also kills all the Selenium processes after all tests execution

## DAY 6 ##

### **1. Update project structure** ###

Structure of project have been updated to match example and following requirements:

* a name of your main package is pbc
* a name of package with unit tests is tests

Currently structure of the project is:

```
D:.
│   .gitignore
│   app.py
│   README.md
│   requirements.txt
│   Vagrantfile
│
├───pbc
│   │   func_decorators.py
│   │   __init__.py
│   │
│   ├───sel_grid
│   │       conftest.py
│   │       connections.py
│   │       sel_grid.py
│   │       test_sel_grid.py
│   │       __init__.py
│   │
│   └───tools
│           fibonacci.py
│           numbers_pairs.py
│           __init__.py
│
└───tests
    │   __init__.py
    │
    └───tools
            test_fib.py
            test_pairs.py
            __init__.py
```

### **2. Update vagrant** ###

Vagrant file have been updated with:
`config.vm.define "github krizzis"`

### **3. Create tests** ###

New modules in project:

 * `conftest.py` contains fixture `ssh_client` for creating ssh connection with VM and destroying it after the tests
 * `connections.py` contains implementation of Ssh client using paramiko
 * `sel_grid.py` contains classes related to creating and configuring of the Selenium Grid
 * `test_sel_grid.py` contains tests on creating and configuring Selenium Grid functionality.

## DAY 7 ##

### **1. Install firefox and geckodriver on VM** ###

Following script has been added to Vagrant file:

```
add-apt-repository ppa:mozillateam/firefox-next
apt-get -y install firefox
wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz
tar -xvzf geckodriver*
mv geckodriver /usr/local/sbin
```

### **2. Update Selenium grid run** ###

Command to download Selenium Grid node configuration file has been added:

```
wget -O sg-node.json https://gist.github.com/extsoft/aed4cb6e0b1ae3cd1d38cafffdd79310/raw/
```

Also appropriate changes have been made to use this file during starting a node:

```
java -jar selenium-server-standalone-3.8.0.jar -role node  -nodeConfig sg-node.json >> log.txt 2>&1 &
```

Method `is_downloaded` from `Grid` have been updated. `target_file` has been added as parameter. Now method can check different files by filename

Class `StartGrid` has been updated accordingly

### **3. Test a grid config** ###