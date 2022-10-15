#!/usr/bin/python
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
from mininet.link import TCLink

def myNetwork():
	net = Mininet( topo=None, build=False, ipBase='10.0.0.0/24', autoStaticArp=True, link = TCLink)
	info('*** Adding controller\n')
	c0 = net.addController('c0',controller=OVSController, port=6633)
	info('*** Add Switches\n')
	s9= net.addSwitch('s9')
	s10= net.addSwitch('s10')
	s11= net.addSwitch('s11')
	s12= net.addSwitch('s12')
	s13= net.addSwitch('s13')
	s14= net.addSwitch('s14')
	s15= net.addSwitch('s15')
	#s7= net.addSwitch('s7')
	info('*** Add hosts\n')
	h1 = net.addHost('h1', ip ='10.0.1.10') 
	h2 = net.addHost('h2', ip ='10.0.1.11')
	h3 = net.addHost('h3', ip ='10.0.1.12')
	h4 = net.addHost('h4', ip ='10.0.1.13')
	h5 = net.addHost('h5', ip ='10.0.2.10')
	h6 = net.addHost('h6', ip ='10.0.2.11')
	h7 = net.addHost('h7', ip ='10.0.2.12')
	h8 = net.addHost('h8', ip ='10.0.2.13')
	h9 = net.addHost('h9', ip ='10.0.1.1')
	h10 = net.addHost('h10', ip ='10.0.2.1')
	
	info('*** Add Links\n')
	net.addLink(h9, s9)
	net.addLink(h10, s9)
	net.addLink(h1, s11)
	net.addLink(h2, s11)
	net.addLink(h3, s12)
	net.addLink(h4, s12)
	net.addLink(h5, s14)
	net.addLink(h6, s14)
	net.addLink(h7, s15)
	net.addLink(h8, s15)
	#net.addLink(h5, s14)
#-------------------------------------------------------------------------------------
	net.addLink(s9, s10)
	net.addLink(s10, s11)
	net.addLink(s10, s12)
	net.addLink(s9, s13, bw = 20)
	net.addLink(s13, s14, bw = 20, delay = '5ms')
	net.addLink(s13, s15)
#------------------------------------------------------------------------------------

	info ('*** Starting Network\n')
	net.build()
	info('*** Starting Controller\n')
	for controller in net.controllers:
		controller.start()
	info('*** Starting Switches\n')
	net.get('s9').start([c0])
	net.get('s10').start([c0])
	net.get('s11').start([c0])
	net.get('s12').start([c0])
	net.get('s13').start([c0])
	net.get('s14').start([c0])
	net.get('s15').start([c0])

	info('*** Post configure switches and hosts\n')
	CLI(net)
	net.stop()
if __name__ == '__main__':
	setLogLevel('info')
	topo = myNetwork()
