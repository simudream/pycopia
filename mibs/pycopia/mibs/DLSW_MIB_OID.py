# python
# This file is generated by a program (mib2py). 

import DLSW_MIB

OIDMAP = {
'0.0': DLSW_MIB.null,
'1.3.6.1.2.1.46': DLSW_MIB.dlsw,
'1.3.6.1.2.1.46.1': DLSW_MIB.dlswMIB,
'1.3.6.1.2.1.46.1.0': DLSW_MIB.dlswTraps,
'1.3.6.1.2.1.46.1.1': DLSW_MIB.dlswNode,
'1.3.6.1.2.1.46.1.1.10': DLSW_MIB.dlswTrapControl,
'1.3.6.1.2.1.46.1.2': DLSW_MIB.dlswTConn,
'1.3.6.1.2.1.46.1.2.1': DLSW_MIB.dlswTConnStat,
'1.3.6.1.2.1.46.1.2.4': DLSW_MIB.dlswTConnSpecific,
'1.3.6.1.2.1.46.1.2.4.1': DLSW_MIB.dlswTConnTcp,
'1.3.6.1.2.1.46.1.3': DLSW_MIB.dlswInterface,
'1.3.6.1.2.1.46.1.4': DLSW_MIB.dlswDirectory,
'1.3.6.1.2.1.46.1.4.1': DLSW_MIB.dlswDirStat,
'1.3.6.1.2.1.46.1.4.2': DLSW_MIB.dlswDirCache,
'1.3.6.1.2.1.46.1.4.3': DLSW_MIB.dlswDirLocate,
'1.3.6.1.2.1.46.1.5': DLSW_MIB.dlswCircuit,
'1.3.6.1.2.1.46.1.5.1': DLSW_MIB.dlswCircuitStat,
'1.3.6.1.2.1.46.1.6': DLSW_MIB.dlswSdlc,
'1.3.6.1.2.1.46.2': DLSW_MIB.dlswDomains,
'1.3.6.1.2.1.46.2.1': DLSW_MIB.dlswTCPDomain,
'1.3.6.1.2.1.46.3': DLSW_MIB.dlswConformance,
'1.3.6.1.2.1.46.3.1': DLSW_MIB.dlswCompliances,
'1.3.6.1.2.1.46.3.2': DLSW_MIB.dlswGroups,
'1.3.6.1.2.1.46.1.1.1': DLSW_MIB.dlswNodeVersion,
'1.3.6.1.2.1.46.1.1.2': DLSW_MIB.dlswNodeVendorID,
'1.3.6.1.2.1.46.1.1.3': DLSW_MIB.dlswNodeVersionString,
'1.3.6.1.2.1.46.1.1.4': DLSW_MIB.dlswNodeStdPacingSupport,
'1.3.6.1.2.1.46.1.1.5': DLSW_MIB.dlswNodeStatus,
'1.3.6.1.2.1.46.1.1.6': DLSW_MIB.dlswNodeUpTime,
'1.3.6.1.2.1.46.1.1.7': DLSW_MIB.dlswNodeVirtualSegmentLFSize,
'1.3.6.1.2.1.46.1.1.8': DLSW_MIB.dlswNodeResourceNBExclusivity,
'1.3.6.1.2.1.46.1.1.9': DLSW_MIB.dlswNodeResourceMacExclusivity,
'1.3.6.1.2.1.46.1.1.10.1': DLSW_MIB.dlswTrapCntlTConnPartnerReject,
'1.3.6.1.2.1.46.1.1.10.2': DLSW_MIB.dlswTrapCntlTConnProtViolation,
'1.3.6.1.2.1.46.1.1.10.3': DLSW_MIB.dlswTrapCntlTConn,
'1.3.6.1.2.1.46.1.1.10.4': DLSW_MIB.dlswTrapCntlCircuit,
'1.3.6.1.2.1.46.1.2.1.1': DLSW_MIB.dlswTConnStatActiveConnections,
'1.3.6.1.2.1.46.1.2.1.2': DLSW_MIB.dlswTConnStatCloseIdles,
'1.3.6.1.2.1.46.1.2.1.3': DLSW_MIB.dlswTConnStatCloseBusys,
'1.3.6.1.2.1.46.1.4.1.1': DLSW_MIB.dlswDirMacEntries,
'1.3.6.1.2.1.46.1.4.1.2': DLSW_MIB.dlswDirMacCacheHits,
'1.3.6.1.2.1.46.1.4.1.3': DLSW_MIB.dlswDirMacCacheMisses,
'1.3.6.1.2.1.46.1.4.1.4': DLSW_MIB.dlswDirMacCacheNextIndex,
'1.3.6.1.2.1.46.1.4.1.5': DLSW_MIB.dlswDirNBEntries,
'1.3.6.1.2.1.46.1.4.1.6': DLSW_MIB.dlswDirNBCacheHits,
'1.3.6.1.2.1.46.1.4.1.7': DLSW_MIB.dlswDirNBCacheMisses,
'1.3.6.1.2.1.46.1.4.1.8': DLSW_MIB.dlswDirNBCacheNextIndex,
'1.3.6.1.2.1.46.1.5.1.1': DLSW_MIB.dlswCircuitStatActives,
'1.3.6.1.2.1.46.1.5.1.2': DLSW_MIB.dlswCircuitStatCreates,
'1.3.6.1.2.1.46.1.6.1': DLSW_MIB.dlswSdlcLsEntries,
'1.3.6.1.2.1.46.1.2.2.1.1': DLSW_MIB.dlswTConnConfigIndex,
'1.3.6.1.2.1.46.1.2.2.1.2': DLSW_MIB.dlswTConnConfigTDomain,
'1.3.6.1.2.1.46.1.2.2.1.3': DLSW_MIB.dlswTConnConfigLocalTAddr,
'1.3.6.1.2.1.46.1.2.2.1.4': DLSW_MIB.dlswTConnConfigRemoteTAddr,
'1.3.6.1.2.1.46.1.2.2.1.5': DLSW_MIB.dlswTConnConfigLastModifyTime,
'1.3.6.1.2.1.46.1.2.2.1.6': DLSW_MIB.dlswTConnConfigEntryType,
'1.3.6.1.2.1.46.1.2.2.1.7': DLSW_MIB.dlswTConnConfigGroupDefinition,
'1.3.6.1.2.1.46.1.2.2.1.8': DLSW_MIB.dlswTConnConfigSetupType,
'1.3.6.1.2.1.46.1.2.2.1.9': DLSW_MIB.dlswTConnConfigSapList,
'1.3.6.1.2.1.46.1.2.2.1.10': DLSW_MIB.dlswTConnConfigAdvertiseMacNB,
'1.3.6.1.2.1.46.1.2.2.1.11': DLSW_MIB.dlswTConnConfigInitCirRecvWndw,
'1.3.6.1.2.1.46.1.2.2.1.12': DLSW_MIB.dlswTConnConfigOpens,
'1.3.6.1.2.1.46.1.2.2.1.13': DLSW_MIB.dlswTConnConfigRowStatus,
'1.3.6.1.2.1.46.1.2.3.1.1': DLSW_MIB.dlswTConnOperTDomain,
'1.3.6.1.2.1.46.1.2.3.1.2': DLSW_MIB.dlswTConnOperLocalTAddr,
'1.3.6.1.2.1.46.1.2.3.1.3': DLSW_MIB.dlswTConnOperRemoteTAddr,
'1.3.6.1.2.1.46.1.2.3.1.4': DLSW_MIB.dlswTConnOperEntryTime,
'1.3.6.1.2.1.46.1.2.3.1.5': DLSW_MIB.dlswTConnOperConnectTime,
'1.3.6.1.2.1.46.1.2.3.1.6': DLSW_MIB.dlswTConnOperState,
'1.3.6.1.2.1.46.1.2.3.1.7': DLSW_MIB.dlswTConnOperConfigIndex,
'1.3.6.1.2.1.46.1.2.3.1.8': DLSW_MIB.dlswTConnOperFlowCntlMode,
'1.3.6.1.2.1.46.1.2.3.1.9': DLSW_MIB.dlswTConnOperPartnerVersion,
'1.3.6.1.2.1.46.1.2.3.1.10': DLSW_MIB.dlswTConnOperPartnerVendorID,
'1.3.6.1.2.1.46.1.2.3.1.11': DLSW_MIB.dlswTConnOperPartnerVersionStr,
'1.3.6.1.2.1.46.1.2.3.1.12': DLSW_MIB.dlswTConnOperPartnerInitPacingWndw,
'1.3.6.1.2.1.46.1.2.3.1.13': DLSW_MIB.dlswTConnOperPartnerSapList,
'1.3.6.1.2.1.46.1.2.3.1.14': DLSW_MIB.dlswTConnOperPartnerNBExcl,
'1.3.6.1.2.1.46.1.2.3.1.15': DLSW_MIB.dlswTConnOperPartnerMacExcl,
'1.3.6.1.2.1.46.1.2.3.1.16': DLSW_MIB.dlswTConnOperPartnerNBInfo,
'1.3.6.1.2.1.46.1.2.3.1.17': DLSW_MIB.dlswTConnOperPartnerMacInfo,
'1.3.6.1.2.1.46.1.2.3.1.18': DLSW_MIB.dlswTConnOperDiscTime,
'1.3.6.1.2.1.46.1.2.3.1.19': DLSW_MIB.dlswTConnOperDiscReason,
'1.3.6.1.2.1.46.1.2.3.1.20': DLSW_MIB.dlswTConnOperDiscActiveCir,
'1.3.6.1.2.1.46.1.2.3.1.21': DLSW_MIB.dlswTConnOperInDataPkts,
'1.3.6.1.2.1.46.1.2.3.1.22': DLSW_MIB.dlswTConnOperOutDataPkts,
'1.3.6.1.2.1.46.1.2.3.1.23': DLSW_MIB.dlswTConnOperInDataOctets,
'1.3.6.1.2.1.46.1.2.3.1.24': DLSW_MIB.dlswTConnOperOutDataOctets,
'1.3.6.1.2.1.46.1.2.3.1.25': DLSW_MIB.dlswTConnOperInCntlPkts,
'1.3.6.1.2.1.46.1.2.3.1.26': DLSW_MIB.dlswTConnOperOutCntlPkts,
'1.3.6.1.2.1.46.1.2.3.1.27': DLSW_MIB.dlswTConnOperCURexSents,
'1.3.6.1.2.1.46.1.2.3.1.28': DLSW_MIB.dlswTConnOperICRexRcvds,
'1.3.6.1.2.1.46.1.2.3.1.29': DLSW_MIB.dlswTConnOperCURexRcvds,
'1.3.6.1.2.1.46.1.2.3.1.30': DLSW_MIB.dlswTConnOperICRexSents,
'1.3.6.1.2.1.46.1.2.3.1.31': DLSW_MIB.dlswTConnOperNQexSents,
'1.3.6.1.2.1.46.1.2.3.1.32': DLSW_MIB.dlswTConnOperNRexRcvds,
'1.3.6.1.2.1.46.1.2.3.1.33': DLSW_MIB.dlswTConnOperNQexRcvds,
'1.3.6.1.2.1.46.1.2.3.1.34': DLSW_MIB.dlswTConnOperNRexSents,
'1.3.6.1.2.1.46.1.2.3.1.35': DLSW_MIB.dlswTConnOperCirCreates,
'1.3.6.1.2.1.46.1.2.3.1.36': DLSW_MIB.dlswTConnOperCircuits,
'1.3.6.1.2.1.46.1.2.4.1.1.1.1': DLSW_MIB.dlswTConnTcpConfigKeepAliveInt,
'1.3.6.1.2.1.46.1.2.4.1.1.1.2': DLSW_MIB.dlswTConnTcpConfigTcpConnections,
'1.3.6.1.2.1.46.1.2.4.1.1.1.3': DLSW_MIB.dlswTConnTcpConfigMaxSegmentSize,
'1.3.6.1.2.1.46.1.2.4.1.2.1.1': DLSW_MIB.dlswTConnTcpOperKeepAliveInt,
'1.3.6.1.2.1.46.1.2.4.1.2.1.2': DLSW_MIB.dlswTConnTcpOperPrefTcpConnections,
'1.3.6.1.2.1.46.1.2.4.1.2.1.3': DLSW_MIB.dlswTConnTcpOperTcpConnections,
'1.3.6.1.2.1.46.1.3.1.1.1': DLSW_MIB.dlswIfRowStatus,
'1.3.6.1.2.1.46.1.3.1.1.2': DLSW_MIB.dlswIfVirtualSegment,
'1.3.6.1.2.1.46.1.3.1.1.3': DLSW_MIB.dlswIfSapList,
'1.3.6.1.2.1.46.1.4.2.1.1.1': DLSW_MIB.dlswDirMacIndex,
'1.3.6.1.2.1.46.1.4.2.1.1.2': DLSW_MIB.dlswDirMacMac,
'1.3.6.1.2.1.46.1.4.2.1.1.3': DLSW_MIB.dlswDirMacMask,
'1.3.6.1.2.1.46.1.4.2.1.1.4': DLSW_MIB.dlswDirMacEntryType,
'1.3.6.1.2.1.46.1.4.2.1.1.5': DLSW_MIB.dlswDirMacLocationType,
'1.3.6.1.2.1.46.1.4.2.1.1.6': DLSW_MIB.dlswDirMacLocation,
'1.3.6.1.2.1.46.1.4.2.1.1.7': DLSW_MIB.dlswDirMacStatus,
'1.3.6.1.2.1.46.1.4.2.1.1.8': DLSW_MIB.dlswDirMacLFSize,
'1.3.6.1.2.1.46.1.4.2.1.1.9': DLSW_MIB.dlswDirMacRowStatus,
'1.3.6.1.2.1.46.1.4.2.2.1.1': DLSW_MIB.dlswDirNBIndex,
'1.3.6.1.2.1.46.1.4.2.2.1.2': DLSW_MIB.dlswDirNBName,
'1.3.6.1.2.1.46.1.4.2.2.1.3': DLSW_MIB.dlswDirNBNameType,
'1.3.6.1.2.1.46.1.4.2.2.1.4': DLSW_MIB.dlswDirNBEntryType,
'1.3.6.1.2.1.46.1.4.2.2.1.5': DLSW_MIB.dlswDirNBLocationType,
'1.3.6.1.2.1.46.1.4.2.2.1.6': DLSW_MIB.dlswDirNBLocation,
'1.3.6.1.2.1.46.1.4.2.2.1.7': DLSW_MIB.dlswDirNBStatus,
'1.3.6.1.2.1.46.1.4.2.2.1.8': DLSW_MIB.dlswDirNBLFSize,
'1.3.6.1.2.1.46.1.4.2.2.1.9': DLSW_MIB.dlswDirNBRowStatus,
'1.3.6.1.2.1.46.1.4.3.1.1.1': DLSW_MIB.dlswDirLocateMacMac,
'1.3.6.1.2.1.46.1.4.3.1.1.2': DLSW_MIB.dlswDirLocateMacMatch,
'1.3.6.1.2.1.46.1.4.3.1.1.3': DLSW_MIB.dlswDirLocateMacLocation,
'1.3.6.1.2.1.46.1.4.3.2.1.1': DLSW_MIB.dlswDirLocateNBName,
'1.3.6.1.2.1.46.1.4.3.2.1.2': DLSW_MIB.dlswDirLocateNBMatch,
'1.3.6.1.2.1.46.1.4.3.2.1.3': DLSW_MIB.dlswDirLocateNBLocation,
'1.3.6.1.2.1.46.1.5.2.1.1': DLSW_MIB.dlswCircuitS1Mac,
'1.3.6.1.2.1.46.1.5.2.1.2': DLSW_MIB.dlswCircuitS1Sap,
'1.3.6.1.2.1.46.1.5.2.1.3': DLSW_MIB.dlswCircuitS1IfIndex,
'1.3.6.1.2.1.46.1.5.2.1.4': DLSW_MIB.dlswCircuitS1DlcType,
'1.3.6.1.2.1.46.1.5.2.1.5': DLSW_MIB.dlswCircuitS1RouteInfo,
'1.3.6.1.2.1.46.1.5.2.1.6': DLSW_MIB.dlswCircuitS1CircuitId,
'1.3.6.1.2.1.46.1.5.2.1.7': DLSW_MIB.dlswCircuitS1Dlc,
'1.3.6.1.2.1.46.1.5.2.1.8': DLSW_MIB.dlswCircuitS2Mac,
'1.3.6.1.2.1.46.1.5.2.1.9': DLSW_MIB.dlswCircuitS2Sap,
'1.3.6.1.2.1.46.1.5.2.1.10': DLSW_MIB.dlswCircuitS2Location,
'1.3.6.1.2.1.46.1.5.2.1.11': DLSW_MIB.dlswCircuitS2TDomain,
'1.3.6.1.2.1.46.1.5.2.1.12': DLSW_MIB.dlswCircuitS2TAddress,
'1.3.6.1.2.1.46.1.5.2.1.13': DLSW_MIB.dlswCircuitS2CircuitId,
'1.3.6.1.2.1.46.1.5.2.1.14': DLSW_MIB.dlswCircuitOrigin,
'1.3.6.1.2.1.46.1.5.2.1.15': DLSW_MIB.dlswCircuitEntryTime,
'1.3.6.1.2.1.46.1.5.2.1.16': DLSW_MIB.dlswCircuitStateTime,
'1.3.6.1.2.1.46.1.5.2.1.17': DLSW_MIB.dlswCircuitState,
'1.3.6.1.2.1.46.1.5.2.1.18': DLSW_MIB.dlswCircuitPriority,
'1.3.6.1.2.1.46.1.5.2.1.19': DLSW_MIB.dlswCircuitFCSendGrantedUnits,
'1.3.6.1.2.1.46.1.5.2.1.20': DLSW_MIB.dlswCircuitFCSendCurrentWndw,
'1.3.6.1.2.1.46.1.5.2.1.21': DLSW_MIB.dlswCircuitFCRecvGrantedUnits,
'1.3.6.1.2.1.46.1.5.2.1.22': DLSW_MIB.dlswCircuitFCRecvCurrentWndw,
'1.3.6.1.2.1.46.1.5.2.1.23': DLSW_MIB.dlswCircuitFCLargestRecvGranted,
'1.3.6.1.2.1.46.1.5.2.1.24': DLSW_MIB.dlswCircuitFCLargestSendGranted,
'1.3.6.1.2.1.46.1.5.2.1.25': DLSW_MIB.dlswCircuitFCHalveWndwSents,
'1.3.6.1.2.1.46.1.5.2.1.26': DLSW_MIB.dlswCircuitFCResetOpSents,
'1.3.6.1.2.1.46.1.5.2.1.27': DLSW_MIB.dlswCircuitFCHalveWndwRcvds,
'1.3.6.1.2.1.46.1.5.2.1.28': DLSW_MIB.dlswCircuitFCResetOpRcvds,
'1.3.6.1.2.1.46.1.5.2.1.29': DLSW_MIB.dlswCircuitDiscReasonLocal,
'1.3.6.1.2.1.46.1.5.2.1.30': DLSW_MIB.dlswCircuitDiscReasonRemote,
'1.3.6.1.2.1.46.1.5.2.1.31': DLSW_MIB.dlswCircuitDiscReasonRemoteData,
'1.3.6.1.2.1.46.1.6.2.1.1': DLSW_MIB.dlswSdlcLsLocalMac,
'1.3.6.1.2.1.46.1.6.2.1.2': DLSW_MIB.dlswSdlcLsLocalSap,
'1.3.6.1.2.1.46.1.6.2.1.3': DLSW_MIB.dlswSdlcLsLocalIdBlock,
'1.3.6.1.2.1.46.1.6.2.1.4': DLSW_MIB.dlswSdlcLsLocalIdNum,
'1.3.6.1.2.1.46.1.6.2.1.5': DLSW_MIB.dlswSdlcLsRemoteMac,
'1.3.6.1.2.1.46.1.6.2.1.6': DLSW_MIB.dlswSdlcLsRemoteSap,
'1.3.6.1.2.1.46.1.6.2.1.7': DLSW_MIB.dlswSdlcLsRowStatus,
'1.3.6.1.2.1.46.1.0.1': DLSW_MIB.dlswTrapTConnPartnerReject,
'1.3.6.1.2.1.46.1.0.2': DLSW_MIB.dlswTrapTConnProtViolation,
'1.3.6.1.2.1.46.1.0.3': DLSW_MIB.dlswTrapTConnUp,
'1.3.6.1.2.1.46.1.0.4': DLSW_MIB.dlswTrapTConnDown,
'1.3.6.1.2.1.46.1.0.5': DLSW_MIB.dlswTrapCircuitUp,
'1.3.6.1.2.1.46.1.0.6': DLSW_MIB.dlswTrapCircuitDown,
'1.3.6.1.2.1.46.3.2.1': DLSW_MIB.dlswNodeGroup,
'1.3.6.1.2.1.46.3.2.2': DLSW_MIB.dlswNodeNBGroup,
'1.3.6.1.2.1.46.3.2.3': DLSW_MIB.dlswTConnStatGroup,
'1.3.6.1.2.1.46.3.2.4': DLSW_MIB.dlswTConnConfigGroup,
'1.3.6.1.2.1.46.3.2.5': DLSW_MIB.dlswTConnOperGroup,
'1.3.6.1.2.1.46.3.2.6': DLSW_MIB.dlswTConnNBGroup,
'1.3.6.1.2.1.46.3.2.7': DLSW_MIB.dlswTConnTcpConfigGroup,
'1.3.6.1.2.1.46.3.2.8': DLSW_MIB.dlswTConnTcpOperGroup,
'1.3.6.1.2.1.46.3.2.9': DLSW_MIB.dlswInterfaceGroup,
'1.3.6.1.2.1.46.3.2.10': DLSW_MIB.dlswDirGroup,
'1.3.6.1.2.1.46.3.2.11': DLSW_MIB.dlswDirNBGroup,
'1.3.6.1.2.1.46.3.2.12': DLSW_MIB.dlswDirLocateGroup,
'1.3.6.1.2.1.46.3.2.13': DLSW_MIB.dlswDirLocateNBGroup,
'1.3.6.1.2.1.46.3.2.14': DLSW_MIB.dlswCircuitStatGroup,
'1.3.6.1.2.1.46.3.2.15': DLSW_MIB.dlswCircuitGroup,
'1.3.6.1.2.1.46.3.2.16': DLSW_MIB.dlswSdlcGroup,
'1.3.6.1.2.1.46.3.2.17': DLSW_MIB.dlswNotificationGroup,
}
