# PBC-Vbeliaev #  

Project for Python Boot Camp (SoftServe, Dec 2017)

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


[File](https://github.com/krizzis/PBC-Vbeliaev/blob/master/Day1/Vagrantfile)


### **2. Fibonacci sequence** ###
*Function which prints desired count of fibonacci numbers.*  
You can run the script [Fibonacci.py](https://github.com/krizzis/PBC-Vbeliaev/blob/master/Day1/Fibonacci.py) with the following parameters:  

* **number (int):** (Mandatory) Number The required number of sequence members.  
E.g. `Fibonacci.py 15` will print 15 first members of Fibonacci sequence


* **-h:** Print help


### **3. Numbers pairs** ###
*Function which prints pairs of numbers which sum is specified for a given collection of numbers*
You can run the script [Numbers_pairs.py](https://github.com/krizzis/PBC-Vbeliaev/blob/master/Day1/Numbers_pairs.py) with the following parameters:

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

### **5. Decorator** ###
Module `Decorator` have been added. Contains decorator to print function name and arguments each run. Example of output:
`pairs([1, 9, 1], all_pairs=True)`

## DAY 4 ##

Todo


