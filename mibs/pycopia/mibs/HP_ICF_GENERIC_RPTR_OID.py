# python
# This file is generated by a program (mib2py). 

import HP_ICF_GENERIC_RPTR

OIDMAP = {
'1.3.6.1.4.1.11.2.14.2.10': HP_ICF_GENERIC_RPTR.hubSecurity,
'1.3.6.1.4.1.11.2.14.10.2.8': HP_ICF_GENERIC_RPTR.hpicfGenRptrMib,
'1.3.6.1.4.1.11.2.14.10.2.8.1': HP_ICF_GENERIC_RPTR.hpicfGenRptrConformance,
'1.3.6.1.4.1.11.2.14.10.2.8.1.1': HP_ICF_GENERIC_RPTR.hpicfGenRptrCompliances,
'1.3.6.1.4.1.11.2.14.10.2.8.1.2': HP_ICF_GENERIC_RPTR.hpicfGenRptrGroups,
'1.3.6.1.4.1.11.2.14.11.4.1': HP_ICF_GENERIC_RPTR.hpGRpBasic,
'1.3.6.1.4.1.11.2.14.11.4.1.1': HP_ICF_GENERIC_RPTR.hpGRpBasicGlobal,
'1.3.6.1.4.1.11.2.14.11.4.2': HP_ICF_GENERIC_RPTR.hpicfGRpBackupLinks,
'1.3.6.1.4.1.11.2.14.11.4.3': HP_ICF_GENERIC_RPTR.hpGRpPortMapping,
'1.3.6.1.4.1.11.2.14.11.4.4': HP_ICF_GENERIC_RPTR.hpGRpLoadBalancing,
'1.3.6.1.4.1.11.2.14.11.4.5': HP_ICF_GENERIC_RPTR.hpicfGRpSwitchConfig,
'1.3.6.1.4.1.11.2.14.11.4.6': HP_ICF_GENERIC_RPTR.hpicfGRpBridge,
'1.3.6.1.4.1.11.2.14.11.4.1.1.1': HP_ICF_GENERIC_RPTR.hpGRpSelfHealEnable,
'1.3.6.1.4.1.11.2.14.11.4.2.1': HP_ICF_GENERIC_RPTR.hpicfBackupLinkNextIndex,
'1.3.6.1.4.1.11.2.14.11.4.4.1': HP_ICF_GENERIC_RPTR.hpGRpPortMapAutoConfigEnable,
'1.3.6.1.4.1.11.2.14.11.4.4.2': HP_ICF_GENERIC_RPTR.hpGRpLoadBalanceNow,
'1.3.6.1.4.1.11.2.14.11.4.4.3': HP_ICF_GENERIC_RPTR.hpGRpLastLoadBalanceTime,
'1.3.6.1.4.1.11.2.14.11.4.5.3': HP_ICF_GENERIC_RPTR.hpicfGRpCurrentPrimarySwitch,
'1.3.6.1.4.1.11.2.14.11.4.5.4': HP_ICF_GENERIC_RPTR.hpicfGRpDesiredPrimarySwitch,
'1.3.6.1.4.1.11.2.14.11.4.6.1': HP_ICF_GENERIC_RPTR.hpGRpBridgeAdminStatus,
'1.3.6.1.4.1.11.2.14.2.10.1.1.1': HP_ICF_GENERIC_RPTR.hubSecPtGroupIndex,
'1.3.6.1.4.1.11.2.14.2.10.1.1.2': HP_ICF_GENERIC_RPTR.hubSecPtPortIndex,
'1.3.6.1.4.1.11.2.14.2.10.1.1.3': HP_ICF_GENERIC_RPTR.hubSecPtSecurityAddress,
'1.3.6.1.4.1.11.2.14.2.10.1.1.4': HP_ICF_GENERIC_RPTR.hubSecPtAuthorizedAddress,
'1.3.6.1.4.1.11.2.14.2.10.1.1.5': HP_ICF_GENERIC_RPTR.hubSecPtPreventEavesdrop,
'1.3.6.1.4.1.11.2.14.2.10.1.1.6': HP_ICF_GENERIC_RPTR.hubSecPtAlarmEnable,
'1.3.6.1.4.1.11.2.14.2.10.1.1.7': HP_ICF_GENERIC_RPTR.hubSecPtIntrusionFlag,
'1.3.6.1.4.1.11.2.14.2.10.2.1.1': HP_ICF_GENERIC_RPTR.hubIntruderIndex,
'1.3.6.1.4.1.11.2.14.2.10.2.1.2': HP_ICF_GENERIC_RPTR.hubIntruderGroup,
'1.3.6.1.4.1.11.2.14.2.10.2.1.3': HP_ICF_GENERIC_RPTR.hubIntruderPort,
'1.3.6.1.4.1.11.2.14.2.10.2.1.4': HP_ICF_GENERIC_RPTR.hubIntruderAddress,
'1.3.6.1.4.1.11.2.14.2.10.2.1.5': HP_ICF_GENERIC_RPTR.hubIntruderTime,
'1.3.6.1.4.1.11.2.14.2.10.2.1.6': HP_ICF_GENERIC_RPTR.hubIntruderType,
'1.3.6.1.4.1.11.2.14.2.10.2.1.7': HP_ICF_GENERIC_RPTR.hubIntruderTrainingViolation,
'1.3.6.1.4.1.11.2.14.2.10.3.1.1': HP_ICF_GENERIC_RPTR.hpSecPtGroupIndex,
'1.3.6.1.4.1.11.2.14.2.10.3.1.2': HP_ICF_GENERIC_RPTR.hpSecPtPortIndex,
'1.3.6.1.4.1.11.2.14.2.10.3.1.3': HP_ICF_GENERIC_RPTR.hpSecPtAddressLimit,
'1.3.6.1.4.1.11.2.14.2.10.3.1.4': HP_ICF_GENERIC_RPTR.hpSecPtLearnMode,
'1.3.6.1.4.1.11.2.14.2.10.3.1.5': HP_ICF_GENERIC_RPTR.hpSecPtPreventEavesdrop,
'1.3.6.1.4.1.11.2.14.2.10.3.1.6': HP_ICF_GENERIC_RPTR.hpSecPtAlarmEnable,
'1.3.6.1.4.1.11.2.14.2.10.3.1.7': HP_ICF_GENERIC_RPTR.hpSecPtIntrusionFlag,
'1.3.6.1.4.1.11.2.14.2.10.4.1.1': HP_ICF_GENERIC_RPTR.hpSecCfgAddrGroupIndex,
'1.3.6.1.4.1.11.2.14.2.10.4.1.2': HP_ICF_GENERIC_RPTR.hpSecCfgAddrPortIndex,
'1.3.6.1.4.1.11.2.14.2.10.4.1.3': HP_ICF_GENERIC_RPTR.hpSecCfgAddress,
'1.3.6.1.4.1.11.2.14.2.10.4.1.4': HP_ICF_GENERIC_RPTR.hpSecCfgStatus,
'1.3.6.1.4.1.11.2.14.2.10.5.1.1': HP_ICF_GENERIC_RPTR.hpSecAuthAddrGroupIndex,
'1.3.6.1.4.1.11.2.14.2.10.5.1.2': HP_ICF_GENERIC_RPTR.hpSecAuthAddrPortIndex,
'1.3.6.1.4.1.11.2.14.2.10.5.1.3': HP_ICF_GENERIC_RPTR.hpSecAuthAddress,
'1.3.6.1.4.1.11.2.14.11.4.1.1.2.1.1': HP_ICF_GENERIC_RPTR.hpGRpRepeaterIndex,
'1.3.6.1.4.1.11.2.14.11.4.1.1.2.1.2': HP_ICF_GENERIC_RPTR.hpGRpRepeaterIfIndex,
'1.3.6.1.4.1.11.2.14.11.4.1.1.2.1.3': HP_ICF_GENERIC_RPTR.hpGRpRepeaterName,
'1.3.6.1.4.1.11.2.14.11.4.1.1.2.1.4': HP_ICF_GENERIC_RPTR.hpGRpRepeaterVlanIndex,
'1.3.6.1.4.1.11.2.14.11.4.2.2.1.1': HP_ICF_GENERIC_RPTR.hpicfBackupLinkIndex,
'1.3.6.1.4.1.11.2.14.11.4.2.2.1.2': HP_ICF_GENERIC_RPTR.hpicfBackupLinkPrimaryGroup,
'1.3.6.1.4.1.11.2.14.11.4.2.2.1.3': HP_ICF_GENERIC_RPTR.hpicfBackupLinkPrimaryPort,
'1.3.6.1.4.1.11.2.14.11.4.2.2.1.4': HP_ICF_GENERIC_RPTR.hpicfBackupLinkBackupGroup,
'1.3.6.1.4.1.11.2.14.11.4.2.2.1.5': HP_ICF_GENERIC_RPTR.hpicfBackupLinkBackupPort,
'1.3.6.1.4.1.11.2.14.11.4.2.2.1.6': HP_ICF_GENERIC_RPTR.hpicfBackupLinkAddress,
'1.3.6.1.4.1.11.2.14.11.4.2.2.1.7': HP_ICF_GENERIC_RPTR.hpicfBackupLinkTestTime,
'1.3.6.1.4.1.11.2.14.11.4.2.2.1.8': HP_ICF_GENERIC_RPTR.hpicfBackupLinkConsecFailures,
'1.3.6.1.4.1.11.2.14.11.4.2.2.1.9': HP_ICF_GENERIC_RPTR.hpicfBackupLinkState,
'1.3.6.1.4.1.11.2.14.11.4.2.2.1.10': HP_ICF_GENERIC_RPTR.hpicfBackupLinkFailEventIndex,
'1.3.6.1.4.1.11.2.14.11.4.2.2.1.11': HP_ICF_GENERIC_RPTR.hpicfBackupLinkStatus,
'1.3.6.1.4.1.11.2.14.11.4.3.1.1.1': HP_ICF_GENERIC_RPTR.hpGRpPMSegmentIndex,
'1.3.6.1.4.1.11.2.14.11.4.3.1.1.3': HP_ICF_GENERIC_RPTR.hpGRpPMCurrentRptrIndex,
'1.3.6.1.4.1.11.2.14.11.4.3.2.1.1': HP_ICF_GENERIC_RPTR.hpGRpPMSegAllowedRptrIndex,
'1.3.6.1.4.1.11.2.14.11.4.3.3.1.1': HP_ICF_GENERIC_RPTR.hpGRpPMPortGroupIndex,
'1.3.6.1.4.1.11.2.14.11.4.3.3.1.2': HP_ICF_GENERIC_RPTR.hpGRpPMPortIndex,
'1.3.6.1.4.1.11.2.14.11.4.3.3.1.3': HP_ICF_GENERIC_RPTR.hpGRpPMPortEntPhysicalIndex,
'1.3.6.1.4.1.11.2.14.11.4.3.3.1.4': HP_ICF_GENERIC_RPTR.hpGRpPMPortCurrentRptrIndex,
'1.3.6.1.4.1.11.2.14.11.4.3.4.1.1': HP_ICF_GENERIC_RPTR.hpGRpPMPortAllowedRptrIndex,
'1.3.6.1.4.1.11.2.14.11.4.5.1.1.1': HP_ICF_GENERIC_RPTR.hpicfGRpSwitchIndex,
'1.3.6.1.4.1.11.2.14.11.4.5.1.1.2': HP_ICF_GENERIC_RPTR.hpicfGRpSwitchType,
'1.3.6.1.4.1.11.2.14.11.4.5.1.1.3': HP_ICF_GENERIC_RPTR.hpicfGRpSwitchEntPhysicalIndex,
'1.3.6.1.4.1.11.2.14.11.4.5.1.1.4': HP_ICF_GENERIC_RPTR.hpicfGRpSwitchLinkCount,
'1.3.6.1.4.1.11.2.14.11.4.5.1.1.5': HP_ICF_GENERIC_RPTR.hpicfGRpSwitchStatus,
'1.3.6.1.4.1.11.2.14.11.4.5.2.1.1': HP_ICF_GENERIC_RPTR.hpicfGRpSwitchLinkIndex,
'1.3.6.1.4.1.11.2.14.11.4.5.2.1.2': HP_ICF_GENERIC_RPTR.hpicfGRpSwitchLinkRptrGroup,
'1.3.6.1.4.1.11.2.14.11.4.5.2.1.3': HP_ICF_GENERIC_RPTR.hpicfGRpSwitchLinkRptrPort,
'1.3.6.1.4.1.11.2.14.11.4.5.2.1.4': HP_ICF_GENERIC_RPTR.hpicfGRpSwitchLinkState,
'1.3.6.1.4.1.11.2.14.12.4.0.1': HP_ICF_GENERIC_RPTR.hpicfIntrusionTrap,
'1.3.6.1.4.1.11.2.14.12.4.0.2': HP_ICF_GENERIC_RPTR.hpicfBackupLinkTrap,
'1.3.6.1.4.1.11.2.14.10.2.8.1.2.1': HP_ICF_GENERIC_RPTR.hpicfHubSecurityGroup,
'1.3.6.1.4.1.11.2.14.10.2.8.1.2.2': HP_ICF_GENERIC_RPTR.hpicfGenRptrBasicGroup,
'1.3.6.1.4.1.11.2.14.10.2.8.1.2.3': HP_ICF_GENERIC_RPTR.hpicfGenRptrSecPtGroup,
'1.3.6.1.4.1.11.2.14.10.2.8.1.2.4': HP_ICF_GENERIC_RPTR.hpicfGenRptrInfoGroup,
'1.3.6.1.4.1.11.2.14.10.2.8.1.2.5': HP_ICF_GENERIC_RPTR.hpicfGenRptrBkpLinkGroup,
'1.3.6.1.4.1.11.2.14.10.2.8.1.2.6': HP_ICF_GENERIC_RPTR.hpicfGenRptrPortMappingGroup,
'1.3.6.1.4.1.11.2.14.10.2.8.1.2.7': HP_ICF_GENERIC_RPTR.hpicfGenRptrLoadBalanceGroup,
'1.3.6.1.4.1.11.2.14.10.2.8.1.2.8': HP_ICF_GENERIC_RPTR.hpicfGenRptrSwitchConfigGroup,
'1.3.6.1.4.1.11.2.14.10.2.8.1.2.9': HP_ICF_GENERIC_RPTR.hpicfGenRptrSecNotifyGroup,
'1.3.6.1.4.1.11.2.14.10.2.8.1.2.10': HP_ICF_GENERIC_RPTR.hpicfGenRptrBkpLinkNotifyGroup,
'1.3.6.1.4.1.11.2.14.10.2.8.1.2.11': HP_ICF_GENERIC_RPTR.hpicfSecPtGroup,
'1.3.6.1.4.1.11.2.14.10.2.8.1.2.12': HP_ICF_GENERIC_RPTR.hpicfGenRptrBridgeGroup,
'1.3.6.1.4.1.11.2.14.10.2.8.1.2.13': HP_ICF_GENERIC_RPTR.hpicfSecPtGroup2,
}
