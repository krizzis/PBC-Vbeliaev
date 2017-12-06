# PBC-Vbeliaev #  

## Table of contents ##
* ### **Day 1:**  ###
  * [Vagrant file](#vagrant-file)
  * [Fibonacci sequence](#fibonacci-sequence)
  * [Numbers pairs](#numbers-pairs)
* ### **Day 2:** ##
  * [Prepare virtual environment](#prepare-virtual-environment)
  * [Simple unit tests](simple-unit-tests)
  * [Install Java on VM](install-java-on-vm)

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

### **Prepare virtual environment** ###

### **Simple unit tests** ###

### **3. Install Java on VM:** ###
