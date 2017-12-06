# PBC-Vbeliaev #  

Project for Python Boot Camp (SoftServe, Dec 2017)

## Table of contents ##
* ### **Day 1:**  ###
  * [Vagrant file](#vagrant-file)
  * [Fibonacci sequence](#fibonacci-sequence)
  * [Numbers pairs](#numbers-pairs)
* ### **Day 2:** ###
  * [Prepare virtual environment](#prepare-virtual-environment)
  * [Simple unit tests](simple-unit-tests)
  * [Install Java on VM](install-java-on-vm)
* ### **Day 3:** ###

## [Day 1](https://github.com/krizzis/PBC-Vbeliaev/tree/master/Day1) ##
  
### **Vagrant file** ###

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


### **Fibonacci sequence** ###
*Function which prints desired count of fibonacci numbers.*  
You can run the script [Fibonacci.py](https://github.com/krizzis/PBC-Vbeliaev/blob/master/Day1/Fibonacci.py) with the following parameters:  

* **number (int):** (Mandatory) Number The required number of sequence members.  
E.g. `Fibonacci.py 15` will print 15 first members of Fibonacci sequence


* **-h:** Print help


### **Numbers pairs** ###
*Function which prints pairs of numbers which sum is specified for a given collection of numbers*
You can run the script [Numbers_pairs.py](https://github.com/krizzis/PBC-Vbeliaev/blob/master/Day1/Numbers_pairs.py) with the following parameters:

* **-n (--numbers):** (Mandatory) List of numbers to check.  
* **-s (--summ):** (Optional) Sum of pairs to check. Default value = 10
* **-a (--all):** (Optional) Flag to find all possible pairs. Only unique pairs by default

E.g. `Numbers_pairs.py 1 5 8 9 10 -74 5 6 4 4` will print (\[1, 9],\[5, 5], \[6,4])  
while `Numbers_pairs.py 1 5 8 9 10 -74 5 6 4 4 --all` will print (\[1, 9],\[5, 5], \[6,4], \[6,4])

* **-h:** Print help

## [Day 2](https://github.com/krizzis/PBC-Vbeliaev/tree/master/Day2) ## 

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

DAY 3

#
