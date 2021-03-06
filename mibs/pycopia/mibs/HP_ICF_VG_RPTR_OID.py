# python
# This file is generated by a program (mib2py). 

import HP_ICF_VG_RPTR

OIDMAP = {
'1.3.6.1.4.1.11.2.14.10.2.11': HP_ICF_VG_RPTR.hpicfVgRptrMib,
'1.3.6.1.4.1.11.2.14.10.2.11.1': HP_ICF_VG_RPTR.hpicfVgRptrConformance,
'1.3.6.1.4.1.11.2.14.10.2.11.1.1': HP_ICF_VG_RPTR.hpicfVgRptrCompliances,
'1.3.6.1.4.1.11.2.14.10.2.11.1.2': HP_ICF_VG_RPTR.hpicfVgRptrGroups,
'1.3.6.1.4.1.11.2.14.11.3.1': HP_ICF_VG_RPTR.hpVgBasic,
'1.3.6.1.4.1.11.2.14.11.3.1.1': HP_ICF_VG_RPTR.hpVgBasicGlobal,
'1.3.6.1.4.1.11.2.14.11.3.1.2': HP_ICF_VG_RPTR.hpVgBasicGroup,
'1.3.6.1.4.1.11.2.14.11.3.1.3': HP_ICF_VG_RPTR.hpVgBasicPort,
'1.3.6.1.4.1.11.2.14.11.3.2': HP_ICF_VG_RPTR.hpVgMonitor,
'1.3.6.1.4.1.11.2.14.11.3.2.1': HP_ICF_VG_RPTR.hpVgMonitorGlobal,
'1.3.6.1.4.1.11.2.14.11.3.2.1.1': HP_ICF_VG_RPTR.hpVgMonCounters,
'1.3.6.1.4.1.11.2.14.11.3.2.2': HP_ICF_VG_RPTR.hpVgMonitorGroup,
'1.3.6.1.4.1.11.2.14.11.3.2.3': HP_ICF_VG_RPTR.hpVgMonitorPort,
'1.3.6.1.4.1.11.2.14.11.3.1.1.1': HP_ICF_VG_RPTR.hpVgEntityName,
'1.3.6.1.4.1.11.2.14.11.3.1.1.2': HP_ICF_VG_RPTR.hpVgRedundantUpLinksFlag,
'1.3.6.1.4.1.11.2.14.11.3.1.1.4': HP_ICF_VG_RPTR.hpVgNullAddrTraining,
'1.3.6.1.4.1.11.2.14.11.3.2.1.1.1': HP_ICF_VG_RPTR.hpVgMonGlbReadableFrames,
'1.3.6.1.4.1.11.2.14.11.3.2.1.1.2': HP_ICF_VG_RPTR.hpVgMonGlbReadableOctets,
'1.3.6.1.4.1.11.2.14.11.3.2.1.1.3': HP_ICF_VG_RPTR.hpVgMonGlbUnreadableOctets,
'1.3.6.1.4.1.11.2.14.11.3.2.1.1.4': HP_ICF_VG_RPTR.hpVgMonGlbHighPriorityFrames,
'1.3.6.1.4.1.11.2.14.11.3.2.1.1.5': HP_ICF_VG_RPTR.hpVgMonGlbHighPriorityOctets,
'1.3.6.1.4.1.11.2.14.11.3.2.1.1.6': HP_ICF_VG_RPTR.hpVgMonGlbBroadcastFrames,
'1.3.6.1.4.1.11.2.14.11.3.2.1.1.7': HP_ICF_VG_RPTR.hpVgMonGlbMulticastFrames,
'1.3.6.1.4.1.11.2.14.11.3.2.1.1.8': HP_ICF_VG_RPTR.hpVgMonGlbIPMFrames,
'1.3.6.1.4.1.11.2.14.11.3.2.1.1.9': HP_ICF_VG_RPTR.hpVgMonGlbDataErrorFrames,
'1.3.6.1.4.1.11.2.14.11.3.2.1.1.10': HP_ICF_VG_RPTR.hpVgMonGlbPriorityPromotions,
'1.3.6.1.4.1.11.2.14.11.3.2.1.1.11': HP_ICF_VG_RPTR.hpVgMonGlbHCReadableOctets,
'1.3.6.1.4.1.11.2.14.11.3.2.1.1.12': HP_ICF_VG_RPTR.hpVgMonGlbHCUnreadableOctets,
'1.3.6.1.4.1.11.2.14.11.3.2.1.1.13': HP_ICF_VG_RPTR.hpVgMonGlbHCHighPriorityOctets,
'1.3.6.1.4.1.11.2.14.11.3.2.1.1.14': HP_ICF_VG_RPTR.hpVgMonGlbHCNormPriorityOctets,
'1.3.6.1.4.1.11.2.14.11.3.2.1.1.15': HP_ICF_VG_RPTR.hpVgMonGlbNormPriorityFrames,
'1.3.6.1.4.1.11.2.14.11.3.2.1.1.16': HP_ICF_VG_RPTR.hpVgMonGlbNormPriorityOctets,
'1.3.6.1.4.1.11.2.14.11.3.2.1.1.17': HP_ICF_VG_RPTR.hpVgMonGlbNullAddressedFrames,
'1.3.6.1.4.1.11.2.14.11.3.2.1.1.18': HP_ICF_VG_RPTR.hpVgMonGlbOversizeFrames,
'1.3.6.1.4.1.11.2.14.11.3.2.1.1.19': HP_ICF_VG_RPTR.hpVgMonGlbTransitionToTrainings,
'1.3.6.1.4.1.11.2.14.11.3.1.1.3.1.1': HP_ICF_VG_RPTR.hpVgXcvrGroupIndex,
'1.3.6.1.4.1.11.2.14.11.3.1.1.3.1.2': HP_ICF_VG_RPTR.hpVgXcvrIndex,
'1.3.6.1.4.1.11.2.14.11.3.1.1.3.1.3': HP_ICF_VG_RPTR.hpVgXcvrType,
'1.3.6.1.4.1.11.2.14.11.3.1.1.3.1.4': HP_ICF_VG_RPTR.hpVgXcvrAssociatedPort,
'1.3.6.1.4.1.11.2.14.11.3.1.1.3.1.5': HP_ICF_VG_RPTR.hpVgXcvrState,
'1.3.6.1.4.1.11.2.14.11.3.1.1.3.1.6': HP_ICF_VG_RPTR.hpVgXcvrAbandonments,
'1.3.6.1.4.1.11.2.14.11.3.1.1.3.1.7': HP_ICF_VG_RPTR.hpVgXcvrIsMovable,
'1.3.6.1.4.1.11.2.14.11.3.1.2.1.1.1': HP_ICF_VG_RPTR.hpVgGrpGroupIndex,
'1.3.6.1.4.1.11.2.14.11.3.1.2.1.1.2': HP_ICF_VG_RPTR.hpVgGrpPortsAdminStatus,
'1.3.6.1.4.1.11.2.14.11.3.1.2.1.1.3': HP_ICF_VG_RPTR.hpVgGrpPortsTrained,
'1.3.6.1.4.1.11.2.14.11.3.1.2.1.1.4': HP_ICF_VG_RPTR.hpVgGrpPortsInTraining,
'1.3.6.1.4.1.11.2.14.11.3.1.2.1.1.5': HP_ICF_VG_RPTR.hpVgGrpPortsCascaded,
'1.3.6.1.4.1.11.2.14.11.3.1.2.1.1.6': HP_ICF_VG_RPTR.hpVgGrpPortsPromiscuous,
'1.3.6.1.4.1.11.2.14.11.3.1.3.1.1.1': HP_ICF_VG_RPTR.hpVgPortGroupIndex,
'1.3.6.1.4.1.11.2.14.11.3.1.3.1.1.2': HP_ICF_VG_RPTR.hpVgPortIndex,
'1.3.6.1.4.1.11.2.14.11.3.1.3.1.1.3': HP_ICF_VG_RPTR.hpVgPortPolarityReversed,
'1.3.6.1.4.1.11.2.14.11.3.1.3.1.1.4': HP_ICF_VG_RPTR.hpVgPortWireSkewError,
'1.3.6.1.4.1.11.2.14.11.3.1.3.1.1.5': HP_ICF_VG_RPTR.hpVgPortAssociatedXcvrIndex,
'1.3.6.1.4.1.11.2.14.11.3.1.3.1.1.6': HP_ICF_VG_RPTR.hpVgPortNumAssociatedXcvrs,
'1.3.6.1.4.1.11.2.14.12.3.0.1': HP_ICF_VG_RPTR.hpVgRedundantUplinkTrap,
'1.3.6.1.4.1.11.2.14.12.3.0.2': HP_ICF_VG_RPTR.hpVgLossOfActiveTrap,
'1.3.6.1.4.1.11.2.14.10.2.11.1.2.2': HP_ICF_VG_RPTR.hpicfVgRptrBasicGroup,
'1.3.6.1.4.1.11.2.14.10.2.11.1.2.4': HP_ICF_VG_RPTR.hpicfVgRptrMonitorGroup,
'1.3.6.1.4.1.11.2.14.10.2.11.1.2.5': HP_ICF_VG_RPTR.hpicfVgRptrXcvrGroup,
'1.3.6.1.4.1.11.2.14.10.2.11.1.2.6': HP_ICF_VG_RPTR.hpicfVgRptrRedundantUplinkGroup,
'1.3.6.1.4.1.11.2.14.10.2.11.1.2.7': HP_ICF_VG_RPTR.hpicfVgRptrBasicTraps,
'1.3.6.1.4.1.11.2.14.10.2.11.1.2.8': HP_ICF_VG_RPTR.hpicfVgRptrRedundantUplinkTraps,
}
