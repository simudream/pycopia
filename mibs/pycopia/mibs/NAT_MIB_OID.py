# python
# This file is generated by a program (mib2py). 

import NAT_MIB

OIDMAP = {
'1.3.6.1.2.1.123': NAT_MIB.natMIB,
'1.3.6.1.2.1.123.0': NAT_MIB.natMIBNotifications,
'1.3.6.1.2.1.123.1': NAT_MIB.natMIBObjects,
'1.3.6.1.2.1.123.1.1': NAT_MIB.natDefTimeouts,
'1.3.6.1.2.1.123.1.2': NAT_MIB.natNotifCtrl,
'1.3.6.1.2.1.123.2': NAT_MIB.natMIBConformance,
'1.3.6.1.2.1.123.2.1': NAT_MIB.natMIBGroups,
'1.3.6.1.2.1.123.2.2': NAT_MIB.natMIBCompliances,
'1.3.6.1.2.1.123.1.1.1': NAT_MIB.natBindDefIdleTimeout,
'1.3.6.1.2.1.123.1.1.2': NAT_MIB.natUdpDefIdleTimeout,
'1.3.6.1.2.1.123.1.1.3': NAT_MIB.natIcmpDefIdleTimeout,
'1.3.6.1.2.1.123.1.1.4': NAT_MIB.natOtherDefIdleTimeout,
'1.3.6.1.2.1.123.1.1.5': NAT_MIB.natTcpDefIdleTimeout,
'1.3.6.1.2.1.123.1.1.6': NAT_MIB.natTcpDefNegTimeout,
'1.3.6.1.2.1.123.1.2.1': NAT_MIB.natNotifThrottlingInterval,
'1.3.6.1.2.1.123.1.5': NAT_MIB.natAddrBindNumberOfEntries,
'1.3.6.1.2.1.123.1.7': NAT_MIB.natAddrPortBindNumberOfEntries,
'1.3.6.1.2.1.123.1.3.1.1': NAT_MIB.natInterfaceRealm,
'1.3.6.1.2.1.123.1.3.1.2': NAT_MIB.natInterfaceServiceType,
'1.3.6.1.2.1.123.1.3.1.3': NAT_MIB.natInterfaceInTranslates,
'1.3.6.1.2.1.123.1.3.1.4': NAT_MIB.natInterfaceOutTranslates,
'1.3.6.1.2.1.123.1.3.1.5': NAT_MIB.natInterfaceDiscards,
'1.3.6.1.2.1.123.1.3.1.6': NAT_MIB.natInterfaceStorageType,
'1.3.6.1.2.1.123.1.3.1.7': NAT_MIB.natInterfaceRowStatus,
'1.3.6.1.2.1.123.1.4.1.1': NAT_MIB.natAddrMapIndex,
'1.3.6.1.2.1.123.1.4.1.2': NAT_MIB.natAddrMapName,
'1.3.6.1.2.1.123.1.4.1.3': NAT_MIB.natAddrMapEntryType,
'1.3.6.1.2.1.123.1.4.1.4': NAT_MIB.natAddrMapTranslationEntity,
'1.3.6.1.2.1.123.1.4.1.5': NAT_MIB.natAddrMapLocalAddrType,
'1.3.6.1.2.1.123.1.4.1.6': NAT_MIB.natAddrMapLocalAddrFrom,
'1.3.6.1.2.1.123.1.4.1.7': NAT_MIB.natAddrMapLocalAddrTo,
'1.3.6.1.2.1.123.1.4.1.8': NAT_MIB.natAddrMapLocalPortFrom,
'1.3.6.1.2.1.123.1.4.1.9': NAT_MIB.natAddrMapLocalPortTo,
'1.3.6.1.2.1.123.1.4.1.10': NAT_MIB.natAddrMapGlobalAddrType,
'1.3.6.1.2.1.123.1.4.1.11': NAT_MIB.natAddrMapGlobalAddrFrom,
'1.3.6.1.2.1.123.1.4.1.12': NAT_MIB.natAddrMapGlobalAddrTo,
'1.3.6.1.2.1.123.1.4.1.13': NAT_MIB.natAddrMapGlobalPortFrom,
'1.3.6.1.2.1.123.1.4.1.14': NAT_MIB.natAddrMapGlobalPortTo,
'1.3.6.1.2.1.123.1.4.1.15': NAT_MIB.natAddrMapProtocol,
'1.3.6.1.2.1.123.1.4.1.16': NAT_MIB.natAddrMapInTranslates,
'1.3.6.1.2.1.123.1.4.1.17': NAT_MIB.natAddrMapOutTranslates,
'1.3.6.1.2.1.123.1.4.1.18': NAT_MIB.natAddrMapDiscards,
'1.3.6.1.2.1.123.1.4.1.19': NAT_MIB.natAddrMapAddrUsed,
'1.3.6.1.2.1.123.1.4.1.20': NAT_MIB.natAddrMapStorageType,
'1.3.6.1.2.1.123.1.4.1.21': NAT_MIB.natAddrMapRowStatus,
'1.3.6.1.2.1.123.1.6.1.1': NAT_MIB.natAddrBindLocalAddrType,
'1.3.6.1.2.1.123.1.6.1.2': NAT_MIB.natAddrBindLocalAddr,
'1.3.6.1.2.1.123.1.6.1.3': NAT_MIB.natAddrBindGlobalAddrType,
'1.3.6.1.2.1.123.1.6.1.4': NAT_MIB.natAddrBindGlobalAddr,
'1.3.6.1.2.1.123.1.6.1.5': NAT_MIB.natAddrBindId,
'1.3.6.1.2.1.123.1.6.1.6': NAT_MIB.natAddrBindTranslationEntity,
'1.3.6.1.2.1.123.1.6.1.7': NAT_MIB.natAddrBindType,
'1.3.6.1.2.1.123.1.6.1.8': NAT_MIB.natAddrBindMapIndex,
'1.3.6.1.2.1.123.1.6.1.9': NAT_MIB.natAddrBindSessions,
'1.3.6.1.2.1.123.1.6.1.10': NAT_MIB.natAddrBindMaxIdleTime,
'1.3.6.1.2.1.123.1.6.1.11': NAT_MIB.natAddrBindCurrentIdleTime,
'1.3.6.1.2.1.123.1.6.1.12': NAT_MIB.natAddrBindInTranslates,
'1.3.6.1.2.1.123.1.6.1.13': NAT_MIB.natAddrBindOutTranslates,
'1.3.6.1.2.1.123.1.8.1.1': NAT_MIB.natAddrPortBindLocalAddrType,
'1.3.6.1.2.1.123.1.8.1.2': NAT_MIB.natAddrPortBindLocalAddr,
'1.3.6.1.2.1.123.1.8.1.3': NAT_MIB.natAddrPortBindLocalPort,
'1.3.6.1.2.1.123.1.8.1.4': NAT_MIB.natAddrPortBindProtocol,
'1.3.6.1.2.1.123.1.8.1.5': NAT_MIB.natAddrPortBindGlobalAddrType,
'1.3.6.1.2.1.123.1.8.1.6': NAT_MIB.natAddrPortBindGlobalAddr,
'1.3.6.1.2.1.123.1.8.1.7': NAT_MIB.natAddrPortBindGlobalPort,
'1.3.6.1.2.1.123.1.8.1.8': NAT_MIB.natAddrPortBindId,
'1.3.6.1.2.1.123.1.8.1.9': NAT_MIB.natAddrPortBindTranslationEntity,
'1.3.6.1.2.1.123.1.8.1.10': NAT_MIB.natAddrPortBindType,
'1.3.6.1.2.1.123.1.8.1.11': NAT_MIB.natAddrPortBindMapIndex,
'1.3.6.1.2.1.123.1.8.1.12': NAT_MIB.natAddrPortBindSessions,
'1.3.6.1.2.1.123.1.8.1.13': NAT_MIB.natAddrPortBindMaxIdleTime,
'1.3.6.1.2.1.123.1.8.1.14': NAT_MIB.natAddrPortBindCurrentIdleTime,
'1.3.6.1.2.1.123.1.8.1.15': NAT_MIB.natAddrPortBindInTranslates,
'1.3.6.1.2.1.123.1.8.1.16': NAT_MIB.natAddrPortBindOutTranslates,
'1.3.6.1.2.1.123.1.9.1.1': NAT_MIB.natSessionIndex,
'1.3.6.1.2.1.123.1.9.1.2': NAT_MIB.natSessionPrivateSrcEPBindId,
'1.3.6.1.2.1.123.1.9.1.3': NAT_MIB.natSessionPrivateSrcEPBindMode,
'1.3.6.1.2.1.123.1.9.1.4': NAT_MIB.natSessionPrivateDstEPBindId,
'1.3.6.1.2.1.123.1.9.1.5': NAT_MIB.natSessionPrivateDstEPBindMode,
'1.3.6.1.2.1.123.1.9.1.6': NAT_MIB.natSessionDirection,
'1.3.6.1.2.1.123.1.9.1.7': NAT_MIB.natSessionUpTime,
'1.3.6.1.2.1.123.1.9.1.8': NAT_MIB.natSessionAddrMapIndex,
'1.3.6.1.2.1.123.1.9.1.9': NAT_MIB.natSessionProtocolType,
'1.3.6.1.2.1.123.1.9.1.10': NAT_MIB.natSessionPrivateAddrType,
'1.3.6.1.2.1.123.1.9.1.11': NAT_MIB.natSessionPrivateSrcAddr,
'1.3.6.1.2.1.123.1.9.1.12': NAT_MIB.natSessionPrivateSrcPort,
'1.3.6.1.2.1.123.1.9.1.13': NAT_MIB.natSessionPrivateDstAddr,
'1.3.6.1.2.1.123.1.9.1.14': NAT_MIB.natSessionPrivateDstPort,
'1.3.6.1.2.1.123.1.9.1.15': NAT_MIB.natSessionPublicAddrType,
'1.3.6.1.2.1.123.1.9.1.16': NAT_MIB.natSessionPublicSrcAddr,
'1.3.6.1.2.1.123.1.9.1.17': NAT_MIB.natSessionPublicSrcPort,
'1.3.6.1.2.1.123.1.9.1.18': NAT_MIB.natSessionPublicDstAddr,
'1.3.6.1.2.1.123.1.9.1.19': NAT_MIB.natSessionPublicDstPort,
'1.3.6.1.2.1.123.1.9.1.20': NAT_MIB.natSessionMaxIdleTime,
'1.3.6.1.2.1.123.1.9.1.21': NAT_MIB.natSessionCurrentIdleTime,
'1.3.6.1.2.1.123.1.9.1.22': NAT_MIB.natSessionInTranslates,
'1.3.6.1.2.1.123.1.9.1.23': NAT_MIB.natSessionOutTranslates,
'1.3.6.1.2.1.123.1.10.1.1': NAT_MIB.natProtocol,
'1.3.6.1.2.1.123.1.10.1.2': NAT_MIB.natProtocolInTranslates,
'1.3.6.1.2.1.123.1.10.1.3': NAT_MIB.natProtocolOutTranslates,
'1.3.6.1.2.1.123.1.10.1.4': NAT_MIB.natProtocolDiscards,
'1.3.6.1.2.1.123.0.1': NAT_MIB.natPacketDiscard,
'1.3.6.1.2.1.123.2.1.1': NAT_MIB.natConfigGroup,
'1.3.6.1.2.1.123.2.1.2': NAT_MIB.natTranslationGroup,
'1.3.6.1.2.1.123.2.1.3': NAT_MIB.natStatsInterfaceGroup,
'1.3.6.1.2.1.123.2.1.4': NAT_MIB.natStatsProtocolGroup,
'1.3.6.1.2.1.123.2.1.5': NAT_MIB.natStatsAddrMapGroup,
'1.3.6.1.2.1.123.2.1.6': NAT_MIB.natMIBNotificationGroup,
}
