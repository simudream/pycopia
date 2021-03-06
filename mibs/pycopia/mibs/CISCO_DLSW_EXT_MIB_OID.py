# python
# This file is generated by a program (mib2py). 

import CISCO_DLSW_EXT_MIB

OIDMAP = {
'1.3.6.1.4.1.9.9.74': CISCO_DLSW_EXT_MIB.ciscoDlswExtMIB,
'1.3.6.1.4.1.9.9.74.1': CISCO_DLSW_EXT_MIB.ciscoDlswExtMIBObjects,
'1.3.6.1.4.1.9.9.74.1.1': CISCO_DLSW_EXT_MIB.cdeDomains,
'1.3.6.1.4.1.9.9.74.1.1.1': CISCO_DLSW_EXT_MIB.cdeFSTDomain,
'1.3.6.1.4.1.9.9.74.1.1.2': CISCO_DLSW_EXT_MIB.cdeDirectHdlcDomain,
'1.3.6.1.4.1.9.9.74.1.1.3': CISCO_DLSW_EXT_MIB.cdeDirectFrameRelayDomain,
'1.3.6.1.4.1.9.9.74.1.1.4': CISCO_DLSW_EXT_MIB.cdeLlc2Domain,
'1.3.6.1.4.1.9.9.74.1.2': CISCO_DLSW_EXT_MIB.cdeNode,
'1.3.6.1.4.1.9.9.74.1.3': CISCO_DLSW_EXT_MIB.cdeTConn,
'1.3.6.1.4.1.9.9.74.1.3.3': CISCO_DLSW_EXT_MIB.cdeTConnSpecific,
'1.3.6.1.4.1.9.9.74.1.3.3.1': CISCO_DLSW_EXT_MIB.cdeTConnTcp,
'1.3.6.1.4.1.9.9.74.1.3.3.2': CISCO_DLSW_EXT_MIB.cdeTConnDirect,
'1.3.6.1.4.1.9.9.74.1.4': CISCO_DLSW_EXT_MIB.cdeInterface,
'1.3.6.1.4.1.9.9.74.1.5': CISCO_DLSW_EXT_MIB.cdeCircuit,
'1.3.6.1.4.1.9.9.74.1.6': CISCO_DLSW_EXT_MIB.cdeFast,
'1.3.6.1.4.1.9.9.74.1.7': CISCO_DLSW_EXT_MIB.cdeTrapControl,
'1.3.6.1.4.1.9.9.74.2': CISCO_DLSW_EXT_MIB.cdeTrapsPrefix,
'1.3.6.1.4.1.9.9.74.2.0': CISCO_DLSW_EXT_MIB.cdeTraps,
'1.3.6.1.4.1.9.9.74.3': CISCO_DLSW_EXT_MIB.cdeMIBConformance,
'1.3.6.1.4.1.9.9.74.3.1': CISCO_DLSW_EXT_MIB.cdeMIBCompliances,
'1.3.6.1.4.1.9.9.74.3.2': CISCO_DLSW_EXT_MIB.cdeMIBGroups,
'1.3.6.1.4.1.9.9.74.1.2.1': CISCO_DLSW_EXT_MIB.cdeNodeTAddr,
'1.3.6.1.4.1.9.9.74.1.2.2': CISCO_DLSW_EXT_MIB.cdeNodeGroup,
'1.3.6.1.4.1.9.9.74.1.2.3': CISCO_DLSW_EXT_MIB.cdeNodeBorder,
'1.3.6.1.4.1.9.9.74.1.2.4': CISCO_DLSW_EXT_MIB.cdeNodeCost,
'1.3.6.1.4.1.9.9.74.1.2.5': CISCO_DLSW_EXT_MIB.cdeNodeKeepaliveInterval,
'1.3.6.1.4.1.9.9.74.1.2.6': CISCO_DLSW_EXT_MIB.cdeNodePassiveConnect,
'1.3.6.1.4.1.9.9.74.1.2.7': CISCO_DLSW_EXT_MIB.cdeNodeBiuSegment,
'1.3.6.1.4.1.9.9.74.1.2.8': CISCO_DLSW_EXT_MIB.cdeNodeInitPacingWindow,
'1.3.6.1.4.1.9.9.74.1.2.9': CISCO_DLSW_EXT_MIB.cdeNodeMaxPacingWindow,
'1.3.6.1.4.1.9.9.74.1.2.10': CISCO_DLSW_EXT_MIB.cdeNodePromiscuous,
'1.3.6.1.4.1.9.9.74.1.2.11': CISCO_DLSW_EXT_MIB.cdeNodePromPeerDefaultsCost,
'1.3.6.1.4.1.9.9.74.1.2.12': CISCO_DLSW_EXT_MIB.cdeNodePromPeerDefaultsDestMac,
'1.3.6.1.4.1.9.9.74.1.2.13': CISCO_DLSW_EXT_MIB.cdeNodePromPeerDefaultsKeepaliveInterval,
'1.3.6.1.4.1.9.9.74.1.2.14': CISCO_DLSW_EXT_MIB.cdeNodePromPeerDefaultsLFSize,
'1.3.6.1.4.1.9.9.74.1.2.15': CISCO_DLSW_EXT_MIB.cdeNodePromPeerDefaultsTCPQueueMax,
'1.3.6.1.4.1.9.9.74.1.2.16': CISCO_DLSW_EXT_MIB.cdeNodePeerOnDemandDefaultsCost,
'1.3.6.1.4.1.9.9.74.1.2.17': CISCO_DLSW_EXT_MIB.cdeNodePeerOnDemandDefaultsFst,
'1.3.6.1.4.1.9.9.74.1.2.18': CISCO_DLSW_EXT_MIB.cdeNodePeerOnDemandDefaultsInactivityInterval,
'1.3.6.1.4.1.9.9.74.1.2.19': CISCO_DLSW_EXT_MIB.cdeNodePeerOnDemandDefaultsKeepaliveInterval,
'1.3.6.1.4.1.9.9.74.1.2.20': CISCO_DLSW_EXT_MIB.cdeNodePeerOnDemandDefaultsLFSize,
'1.3.6.1.4.1.9.9.74.1.2.21': CISCO_DLSW_EXT_MIB.cdeNodePeerOnDemandDefaultsPriority,
'1.3.6.1.4.1.9.9.74.1.2.22': CISCO_DLSW_EXT_MIB.cdeNodePeerOnDemandDefaultsTCPQueueMax,
'1.3.6.1.4.1.9.9.74.1.7.1': CISCO_DLSW_EXT_MIB.cdeTrapCntlTConn,
'1.3.6.1.4.1.9.9.74.1.7.2': CISCO_DLSW_EXT_MIB.cdeTrapCntlCircuit,
'1.3.6.1.4.1.9.9.74.1.3.1.1.1': CISCO_DLSW_EXT_MIB.cdeTConnConfigTDomainType,
'1.3.6.1.4.1.9.9.74.1.3.1.1.2': CISCO_DLSW_EXT_MIB.cdeTConnConfigLocalAck,
'1.3.6.1.4.1.9.9.74.1.3.1.1.3': CISCO_DLSW_EXT_MIB.cdeTConnConfigCost,
'1.3.6.1.4.1.9.9.74.1.3.1.1.4': CISCO_DLSW_EXT_MIB.cdeTConnConfigLFSize,
'1.3.6.1.4.1.9.9.74.1.3.1.1.5': CISCO_DLSW_EXT_MIB.cdeTConnConfigKeepaliveInterval,
'1.3.6.1.4.1.9.9.74.1.3.1.1.6': CISCO_DLSW_EXT_MIB.cdeTConnConfigBackup,
'1.3.6.1.4.1.9.9.74.1.3.1.1.7': CISCO_DLSW_EXT_MIB.cdeTConnConfigBackupTAddr,
'1.3.6.1.4.1.9.9.74.1.3.1.1.8': CISCO_DLSW_EXT_MIB.cdeTConnConfigBackupLinger,
'1.3.6.1.4.1.9.9.74.1.3.1.1.9': CISCO_DLSW_EXT_MIB.cdeTConnConfigBackupLingerInterval,
'1.3.6.1.4.1.9.9.74.1.3.1.1.10': CISCO_DLSW_EXT_MIB.cdeTConnConfigPriority,
'1.3.6.1.4.1.9.9.74.1.3.1.1.11': CISCO_DLSW_EXT_MIB.cdeTConnConfigDestMac,
'1.3.6.1.4.1.9.9.74.1.3.1.1.12': CISCO_DLSW_EXT_MIB.cdeTConnConfigDynamic,
'1.3.6.1.4.1.9.9.74.1.3.1.1.13': CISCO_DLSW_EXT_MIB.cdeTConnConfigDynamicNoLlc,
'1.3.6.1.4.1.9.9.74.1.3.1.1.14': CISCO_DLSW_EXT_MIB.cdeTConnConfigDynamicInactivityInterval,
'1.3.6.1.4.1.9.9.74.1.3.2.1.1': CISCO_DLSW_EXT_MIB.cdeTConnOperPartnerCost,
'1.3.6.1.4.1.9.9.74.1.3.2.1.2': CISCO_DLSW_EXT_MIB.cdeTConnOperPartnerPriority,
'1.3.6.1.4.1.9.9.74.1.3.2.1.3': CISCO_DLSW_EXT_MIB.cdeTConnOperPartnerBorderPeer,
'1.3.6.1.4.1.9.9.74.1.3.2.1.4': CISCO_DLSW_EXT_MIB.cdeTConnOperPartnerGroupNum,
'1.3.6.1.4.1.9.9.74.1.3.2.1.5': CISCO_DLSW_EXT_MIB.cdeTConnOperTDomainType,
'1.3.6.1.4.1.9.9.74.1.3.3.1.1.1.1': CISCO_DLSW_EXT_MIB.cdeTConnTcpConfigQueueMax,
'1.3.6.1.4.1.9.9.74.1.3.3.2.1.1.1': CISCO_DLSW_EXT_MIB.cdeTConnDirectConfigIfIndex,
'1.3.6.1.4.1.9.9.74.1.3.3.2.1.1.2': CISCO_DLSW_EXT_MIB.cdeTConnDirectConfigMediaEncap,
'1.3.6.1.4.1.9.9.74.1.3.3.2.1.1.3': CISCO_DLSW_EXT_MIB.cdeTConnDirectConfigFrameRelayDlci,
'1.3.6.1.4.1.9.9.74.1.4.1.1.1': CISCO_DLSW_EXT_MIB.cdeIfType,
'1.3.6.1.4.1.9.9.74.1.5.1.1.1': CISCO_DLSW_EXT_MIB.cdeCircuitS1Name,
'1.3.6.1.4.1.9.9.74.1.5.1.1.2': CISCO_DLSW_EXT_MIB.cdeCircuitS2Name,
'1.3.6.1.4.1.9.9.74.1.5.1.1.3': CISCO_DLSW_EXT_MIB.cdeCircuitS1IdBlock,
'1.3.6.1.4.1.9.9.74.1.5.1.1.4': CISCO_DLSW_EXT_MIB.cdeCircuitS1IdNum,
'1.3.6.1.4.1.9.9.74.1.6.1.1.1': CISCO_DLSW_EXT_MIB.cdeFastS1Mac,
'1.3.6.1.4.1.9.9.74.1.6.1.1.2': CISCO_DLSW_EXT_MIB.cdeFastS1Sap,
'1.3.6.1.4.1.9.9.74.1.6.1.1.3': CISCO_DLSW_EXT_MIB.cdeFastS2Mac,
'1.3.6.1.4.1.9.9.74.1.6.1.1.4': CISCO_DLSW_EXT_MIB.cdeFastS2Sap,
'1.3.6.1.4.1.9.9.74.1.6.1.1.5': CISCO_DLSW_EXT_MIB.cdeFastS1IfIndex,
'1.3.6.1.4.1.9.9.74.1.6.1.1.6': CISCO_DLSW_EXT_MIB.cdeFastS1RouteInfo,
'1.3.6.1.4.1.9.9.74.1.6.1.1.7': CISCO_DLSW_EXT_MIB.cdeFastS1CacheId,
'1.3.6.1.4.1.9.9.74.1.6.1.1.8': CISCO_DLSW_EXT_MIB.cdeFastS2TDomain,
'1.3.6.1.4.1.9.9.74.1.6.1.1.9': CISCO_DLSW_EXT_MIB.cdeFastS2TAddress,
'1.3.6.1.4.1.9.9.74.1.6.1.1.10': CISCO_DLSW_EXT_MIB.cdeFastS2CacheId,
'1.3.6.1.4.1.9.9.74.1.6.1.1.11': CISCO_DLSW_EXT_MIB.cdeFastOrigin,
'1.3.6.1.4.1.9.9.74.1.6.1.1.12': CISCO_DLSW_EXT_MIB.cdeFastTimeToLive,
'1.3.6.1.4.1.9.9.74.2.0.1': CISCO_DLSW_EXT_MIB.cdeTrapTConnUpDown,
'1.3.6.1.4.1.9.9.74.2.0.2': CISCO_DLSW_EXT_MIB.cdeTrapCircuitUpDown,
'1.3.6.1.4.1.9.9.74.3.2.1': CISCO_DLSW_EXT_MIB.cdeMIBNodeGroup,
'1.3.6.1.4.1.9.9.74.3.2.2': CISCO_DLSW_EXT_MIB.cdeMIBTConnConfigGroup,
'1.3.6.1.4.1.9.9.74.3.2.3': CISCO_DLSW_EXT_MIB.cdeMIBTConnOperGroup,
'1.3.6.1.4.1.9.9.74.3.2.4': CISCO_DLSW_EXT_MIB.cdeMIBTConnTcpConfigGroup,
'1.3.6.1.4.1.9.9.74.3.2.5': CISCO_DLSW_EXT_MIB.cdeMIBTConnDirectConfigGroup,
'1.3.6.1.4.1.9.9.74.3.2.6': CISCO_DLSW_EXT_MIB.cdeMIBInterfaceGroup,
'1.3.6.1.4.1.9.9.74.3.2.7': CISCO_DLSW_EXT_MIB.cdeMIBCircuitGroup,
'1.3.6.1.4.1.9.9.74.3.2.8': CISCO_DLSW_EXT_MIB.cdeMIBFastGroup,
'1.3.6.1.4.1.9.9.74.3.2.9': CISCO_DLSW_EXT_MIB.cdeTrapControlGroup,
}
