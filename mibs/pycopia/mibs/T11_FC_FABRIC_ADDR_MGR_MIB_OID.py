# python
# This file is generated by a program (mib2py). 

import T11_FC_FABRIC_ADDR_MGR_MIB

OIDMAP = {
'1.3.6.1.2.1.137': T11_FC_FABRIC_ADDR_MGR_MIB.t11FcFabricAddrMgrMIB,
'1.3.6.1.2.1.137.0': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamNotifications,
'1.3.6.1.2.1.137.1': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamMIBObjects,
'1.3.6.1.2.1.137.1.1': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamConfiguration,
'1.3.6.1.2.1.137.1.2': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamInfo,
'1.3.6.1.2.1.137.1.3': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamNotifyControl,
'1.3.6.1.2.1.137.2': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamMIBConformance,
'1.3.6.1.2.1.137.2.1': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamMIBCompliances,
'1.3.6.1.2.1.137.2.2': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamMIBGroups,
'1.3.6.1.2.1.137.1.2.3': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamMaxFcIdCacheSize,
'1.3.6.1.2.1.137.1.3.1': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamNotifyFabricIndex,
'1.3.6.1.2.1.137.1.1.1.1.1': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamFabricIndex,
'1.3.6.1.2.1.137.1.1.1.1.2': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamConfigDomainId,
'1.3.6.1.2.1.137.1.1.1.1.3': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamConfigDomainIdType,
'1.3.6.1.2.1.137.1.1.1.1.4': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamAutoReconfigure,
'1.3.6.1.2.1.137.1.1.1.1.5': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamContiguousAllocation,
'1.3.6.1.2.1.137.1.1.1.1.6': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamPriority,
'1.3.6.1.2.1.137.1.1.1.1.7': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamPrincipalSwitchWwn,
'1.3.6.1.2.1.137.1.1.1.1.8': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamLocalSwitchWwn,
'1.3.6.1.2.1.137.1.1.1.1.9': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamAssignedAreaIdList,
'1.3.6.1.2.1.137.1.1.1.1.10': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamGrantedFcIds,
'1.3.6.1.2.1.137.1.1.1.1.11': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamRecoveredFcIds,
'1.3.6.1.2.1.137.1.1.1.1.12': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamFreeFcIds,
'1.3.6.1.2.1.137.1.1.1.1.13': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamAssignedFcIds,
'1.3.6.1.2.1.137.1.1.1.1.14': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamAvailableFcIds,
'1.3.6.1.2.1.137.1.1.1.1.15': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamRunningPriority,
'1.3.6.1.2.1.137.1.1.1.1.16': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamPrincSwRunningPriority,
'1.3.6.1.2.1.137.1.1.1.1.17': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamState,
'1.3.6.1.2.1.137.1.1.1.1.18': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamLocalPrincipalSwitchSlctns,
'1.3.6.1.2.1.137.1.1.1.1.19': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamPrincipalSwitchSelections,
'1.3.6.1.2.1.137.1.1.1.1.20': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamBuildFabrics,
'1.3.6.1.2.1.137.1.1.1.1.21': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamFabricReconfigures,
'1.3.6.1.2.1.137.1.1.1.1.22': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamDomainId,
'1.3.6.1.2.1.137.1.1.1.1.23': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamSticky,
'1.3.6.1.2.1.137.1.1.1.1.24': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamRestart,
'1.3.6.1.2.1.137.1.1.1.1.25': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamRcFabricNotifyEnable,
'1.3.6.1.2.1.137.1.1.1.1.26': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamEnable,
'1.3.6.1.2.1.137.1.1.1.1.27': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamFabricName,
'1.3.6.1.2.1.137.1.1.2.1.1': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamIfRcfReject,
'1.3.6.1.2.1.137.1.1.2.1.2': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamIfRole,
'1.3.6.1.2.1.137.1.1.2.1.3': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamIfRowStatus,
'1.3.6.1.2.1.137.1.2.1.1.1': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamAreaAreaId,
'1.3.6.1.2.1.137.1.2.1.1.2': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamAreaAssignedPortIdList,
'1.3.6.1.2.1.137.1.2.2.1.1': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamDatabaseDomainId,
'1.3.6.1.2.1.137.1.2.2.1.2': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamDatabaseSwitchWwn,
'1.3.6.1.2.1.137.1.2.4.1.1': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamFcIdCacheWwn,
'1.3.6.1.2.1.137.1.2.4.1.2': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamFcIdCacheAreaIdPortId,
'1.3.6.1.2.1.137.1.2.4.1.3': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamFcIdCachePortIds,
'1.3.6.1.2.1.137.0.1': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamDomainIdNotAssignedNotify,
'1.3.6.1.2.1.137.0.2': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamNewPrincipalSwitchNotify,
'1.3.6.1.2.1.137.0.3': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamFabricChangeNotify,
'1.3.6.1.2.1.137.2.2.1': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamGroup,
'1.3.6.1.2.1.137.2.2.2': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamCommandGroup,
'1.3.6.1.2.1.137.2.2.3': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamDatabaseGroup,
'1.3.6.1.2.1.137.2.2.4': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamAreaGroup,
'1.3.6.1.2.1.137.2.2.5': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamCacheGroup,
'1.3.6.1.2.1.137.2.2.6': T11_FC_FABRIC_ADDR_MGR_MIB.t11FamNotificationGroup,
}
