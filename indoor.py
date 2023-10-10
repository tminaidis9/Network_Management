#!/usr/bin/python

from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from mn_wifi.node import Station, OVSKernelAP
from mn_wifi.cli import CLI
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference
from subprocess import call


def MyNet():

    net = Mininet_wifi(topo=None,
                       build=False,
                       link=wmediumd,
                       wmediumd_mode=interference,
                       ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    info( '*** Add switches/APs\n')
    ap1 = net.addAccessPoint('ap1', cls=OVSKernelAP, ssid='ap1-ssid',
                             channel='1', mode='g', position='250.0,250.0,0')
    ap2 = net.addAccessPoint('ap2', cls=OVSKernelAP, ssid='ap2-ssid',
                             channel='1', mode='g', position='450.0,400.0,0')
    ap3 = net.addAccessPoint('ap3', cls=OVSKernelAP, ssid='ap3-ssid',
                             channel='1', mode='g', position='650,800.0,0')
    ap4 = net.addAccessPoint('ap4', cls=OVSKernelAP, ssid='ap4-ssid',
                             channel='1', mode='g', position='840.0,550.0,0')

    info( '*** Add hosts/stations\n')
    sta1 = net.addStation('sta1', ip='10.0.0.1',
                           position='300.0,75.0,0', range=25)
    sta2 = net.addStation('sta2', ip='10.0.0.2',
                           position='200.0,400.0,0', range=25)
    sta3 = net.addStation('sta3', ip='10.0.0.3',
                           position='345.0,400.0,0', range=25)
    sta4 = net.addStation('sta4', ip='10.0.0.4',
                           position='550.0,350.0,0', range=25)
    sta5 = net.addStation('sta5', ip='10.0.0.5',
                           position='600.0,380.0,0', range=25)
    sta6 = net.addStation('sta6', ip='10.0.0.6',
                           position='800.0,800.0,0', range=25)
    sta7 = net.addStation('sta7', ip='10.0.0.7',
                           position='799.0,297.0,0', range=25)


    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=3)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    net.plotGraph(max_x=1000, max_y=1000)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches/APs\n')
    net.get('ap1').start([])
    net.get('ap2').start([])
    net.get('ap3').start([])
    net.get('ap4').start([])

    info( '*** Post configure nodes\n')

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    MyNet()