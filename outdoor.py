#!/usr/bin/python

from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from mn_wifi.node import Station, OVSKernelAP
from mn_wifi.cli import CLI
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference
from subprocess import call


def myNet():

    net = Mininet_wifi(topo=None,
                       build=False,
                       link=wmediumd,
                       wmediumd_mode=interference,
                       ipBase='10.0.0.0/8')

    info( '--- Add controllers, APs---\n' )
    ap1 = net.addAccessPoint('ap1', cls=OVSKernelAP, ssid='ap1-ssid',
                             channel='1', mode='g', position='120.0,150.0,0', range=180)
    ap2 = net.addAccessPoint('ap2', cls=OVSKernelAP, ssid='ap2-ssid',
                             channel='1', mode='g', position='160.0,800.0,0', range=350)
    ap3 = net.addAccessPoint('ap3', cls=OVSKernelAP, ssid='ap3-ssid',
                             channel='1', mode='g', position='350.0,100.0,0', range=0)
    ap4 = net.addAccessPoint('ap4', cls=OVSKernelAP, ssid='ap4-ssid',
                             channel='1', mode='g', position='400.0,330.0,0', range=185)
    ap5 = net.addAccessPoint('ap5', cls=OVSKernelAP, ssid='ap5-ssid',
                             channel='1', mode='g', position='560.0,665.0,0', range=180)
    ap6 = net.addAccessPoint('ap6', cls=OVSKernelAP, ssid='ap6-ssid',
                             channel='1', mode='g', position='620.0,300.0,0', range=250)
    ap7 = net.addAccessPoint('ap7', cls=OVSKernelAP, ssid='ap7-ssid',
                             channel='1', mode='g', position='840.0,620.0,0', range=230)

    info( '--- Add hosts/stations ---\n')
    sta1 = net.addStation('sta1', ip='10.0.0.1',
                           position='126.0,598.0,0', range=25)
    sta2 = net.addStation('sta2', ip='10.0.0.2',
                           position='400.0,400.0,0', range=25)
    sta3 = net.addStation('sta3', ip='10.0.0.3',
                           position='258.0,500.0,0', range=25)
    sta4 = net.addStation('sta4', ip='10.0.0.4',
                           position='422.0,54.0,0', range=25)
    sta5 = net.addStation('sta5', ip='10.0.0.5',
                           position='466.0,149.0,0', range=25)
    sta6 = net.addStation('sta6', ip='10.0.0.6',
                           position='299.0,12.0,0', range=25)
    sta7 = net.addStation('sta7', ip='10.0.0.7',
                           position='587.0,478.0,0', range=25)
    sta8 = net.addStation('sta8', ip='10.0.0.8',
                           position='770.0,600.0,0', range=25)
    sta9 = net.addStation('sta9', ip='10.0.0.9',
                           position='789.0,220.0,0', range=25)
    sta10 = net.addStation('sta10', ip='10.0.0.10',
                           position='50.0,110.0,0', range=25)

    info("--- Configuring Propagation Model ---\n")
    net.setPropagationModel(model="logDistance", exp=3)

    info("--- Configuring wifi nodes ---\n")
    net.configureWifiNodes()
    net.plotGraph(max_x=1100, max_y=1100)

    info( '--- Starting network ---\n')
    net.build()
    info( '--- Starting controllers ---\n')
    for controller in net.controllers:
        controller.start()

    info( '--- Starting switches/APs ---\n')
    net.get('ap1').start([])
    net.get('ap2').start([])
    net.get('ap3').start([])
    net.get('ap4').start([])
    net.get('ap5').start([])
    net.get('ap6').start([])
    net.get('ap7').start([])

    info( '--- Post configure nodes ---\n')
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    myNet()
