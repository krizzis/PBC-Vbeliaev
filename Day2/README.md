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