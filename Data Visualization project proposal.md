# Data Visualization Project Proposal

## Background

My company need to purchase a datasource of Threat Intelligence(TI),there are many providers outside, and the quanlity of the datasources is unknow, so we need to do some prove of concept(POC) testing for these datasources before purchasing.

The form of datasources we currently purchase is API interface. Normally, we will request the TI API interface with ip addresses, which can be assumed to be a attack attampt address or the information of this address need to be acquired.

The purpose of the POC testing is to verify the accuracy and completness of the data returned by the API interface. So the testing requirements are following:

1. There will be 3 providers of TI datasources participate in the testing.
2. There will be 10,000 IPv4 addresses in total send to the each provider's API interface. The addresses are gathered from 5,000 IPv4 addresses which are baned by our firewall 