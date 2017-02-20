
Vagrant.configure("2") do |config|
  config.vm.define "master", primary: true do |master|
    master.vm.box = "ubuntu-VAGRANTSLASH-trusty64"
    master.vm.hostname = 'master'
    master.vm.box_url = "https://github.com/sepetrov/trusty64/releases/download/v0.0.5/trusty64.box"

    master.vm.network :private_network, ip: "192.168.56.101"


    master.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 512]
      v.customize ["modifyvm", :id, "--name", "master"]
    end
  end
  config.vm.define "minion1" do |minion1|
    minion1.vm.box = "ubuntu-VAGRANTSLASH-trusty64"
    minion1.vm.hostname = 'minion1'
    minion1.vm.box_url = "https://github.com/sepetrov/trusty64/releases/download/v0.0.5/trusty64.box"

    minion1.vm.network :private_network, ip: "192.168.56.102"


    minion1.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 512]
      v.customize ["modifyvm", :id, "--name", "minion1"]
    end
  end

  config.vm.define "minion2" do |minion2|
    minion2.vm.box = "ubuntu-VAGRANTSLASH-trusty64"
    minion2.vm.hostname = 'minion2'
    minion2.vm.box_url = "https://github.com/sepetrov/trusty64/releases/download/v0.0.5/trusty64.box"

    minion2.vm.network :private_network, ip: "192.168.56.103"

    minion2.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 512]
      v.customize ["modifyvm", :id, "--name", "minion2"]
    end
  end
  config.vm.define "minion3" do |minion3|
    minion3.vm.box = "ubuntu-VAGRANTSLASH-trusty64"
    minion3.vm.hostname = 'minion3'
    minion3.vm.box_url = "https://github.com/sepetrov/trusty64/releases/download/v0.0.5/trusty64.box"

    minion3.vm.network :private_network, ip: "192.168.56.104"

    minion3.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 512]
      v.customize ["modifyvm", :id, "--name", "minion3"]
    end
  end
end


