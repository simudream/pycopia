# python
# This file is generated by a program (mib2py). 

import DIFFSERV_MIB

OIDMAP = {
'1.3.6.1.2.1.97': DIFFSERV_MIB.diffServMib,
'1.3.6.1.2.1.97.1': DIFFSERV_MIB.diffServMIBObjects,
'1.3.6.1.2.1.97.1.1': DIFFSERV_MIB.diffServDataPath,
'1.3.6.1.2.1.97.1.2': DIFFSERV_MIB.diffServClassifier,
'1.3.6.1.2.1.97.1.3': DIFFSERV_MIB.diffServMeter,
'1.3.6.1.2.1.97.1.4': DIFFSERV_MIB.diffServTBParam,
'1.3.6.1.2.1.97.1.5': DIFFSERV_MIB.diffServAction,
'1.3.6.1.2.1.97.1.6': DIFFSERV_MIB.diffServAlgDrop,
'1.3.6.1.2.1.97.1.7': DIFFSERV_MIB.diffServQueue,
'1.3.6.1.2.1.97.1.8': DIFFSERV_MIB.diffServScheduler,
'1.3.6.1.2.1.97.2': DIFFSERV_MIB.diffServMIBConformance,
'1.3.6.1.2.1.97.2.1': DIFFSERV_MIB.diffServMIBCompliances,
'1.3.6.1.2.1.97.2.2': DIFFSERV_MIB.diffServMIBGroups,
'1.3.6.1.2.1.97.3': DIFFSERV_MIB.diffServMIBAdmin,
'1.3.6.1.2.1.97.3.1': DIFFSERV_MIB.diffServTBMeters,
'1.3.6.1.2.1.97.3.1.1': DIFFSERV_MIB.diffServTBParamSimpleTokenBucket,
'1.3.6.1.2.1.97.3.1.2': DIFFSERV_MIB.diffServTBParamAvgRate,
'1.3.6.1.2.1.97.3.1.3': DIFFSERV_MIB.diffServTBParamSrTCMBlind,
'1.3.6.1.2.1.97.3.1.4': DIFFSERV_MIB.diffServTBParamSrTCMAware,
'1.3.6.1.2.1.97.3.1.5': DIFFSERV_MIB.diffServTBParamTrTCMBlind,
'1.3.6.1.2.1.97.3.1.6': DIFFSERV_MIB.diffServTBParamTrTCMAware,
'1.3.6.1.2.1.97.3.1.7': DIFFSERV_MIB.diffServTBParamTswTCM,
'1.3.6.1.2.1.97.3.2': DIFFSERV_MIB.diffServSchedulers,
'1.3.6.1.2.1.97.3.2.1': DIFFSERV_MIB.diffServSchedulerPriority,
'1.3.6.1.2.1.97.3.2.2': DIFFSERV_MIB.diffServSchedulerWRR,
'1.3.6.1.2.1.97.3.2.3': DIFFSERV_MIB.diffServSchedulerWFQ,
'1.3.6.1.2.1.97.1.2.1': DIFFSERV_MIB.diffServClfrNextFree,
'1.3.6.1.2.1.97.1.2.3': DIFFSERV_MIB.diffServClfrElementNextFree,
'1.3.6.1.2.1.97.1.2.5': DIFFSERV_MIB.diffServMultiFieldClfrNextFree,
'1.3.6.1.2.1.97.1.3.1': DIFFSERV_MIB.diffServMeterNextFree,
'1.3.6.1.2.1.97.1.4.1': DIFFSERV_MIB.diffServTBParamNextFree,
'1.3.6.1.2.1.97.1.5.1': DIFFSERV_MIB.diffServActionNextFree,
'1.3.6.1.2.1.97.1.5.4': DIFFSERV_MIB.diffServCountActNextFree,
'1.3.6.1.2.1.97.1.6.1': DIFFSERV_MIB.diffServAlgDropNextFree,
'1.3.6.1.2.1.97.1.6.3': DIFFSERV_MIB.diffServRandomDropNextFree,
'1.3.6.1.2.1.97.1.7.1': DIFFSERV_MIB.diffServQNextFree,
'1.3.6.1.2.1.97.1.8.1': DIFFSERV_MIB.diffServSchedulerNextFree,
'1.3.6.1.2.1.97.1.8.3': DIFFSERV_MIB.diffServMinRateNextFree,
'1.3.6.1.2.1.97.1.8.5': DIFFSERV_MIB.diffServMaxRateNextFree,
'1.3.6.1.2.1.97.1.1.1.1.1': DIFFSERV_MIB.diffServDataPathIfDirection,
'1.3.6.1.2.1.97.1.1.1.1.2': DIFFSERV_MIB.diffServDataPathStart,
'1.3.6.1.2.1.97.1.1.1.1.3': DIFFSERV_MIB.diffServDataPathStorage,
'1.3.6.1.2.1.97.1.1.1.1.4': DIFFSERV_MIB.diffServDataPathStatus,
'1.3.6.1.2.1.97.1.2.2.1.1': DIFFSERV_MIB.diffServClfrId,
'1.3.6.1.2.1.97.1.2.2.1.2': DIFFSERV_MIB.diffServClfrStorage,
'1.3.6.1.2.1.97.1.2.2.1.3': DIFFSERV_MIB.diffServClfrStatus,
'1.3.6.1.2.1.97.1.2.4.1.1': DIFFSERV_MIB.diffServClfrElementId,
'1.3.6.1.2.1.97.1.2.4.1.2': DIFFSERV_MIB.diffServClfrElementPrecedence,
'1.3.6.1.2.1.97.1.2.4.1.3': DIFFSERV_MIB.diffServClfrElementNext,
'1.3.6.1.2.1.97.1.2.4.1.4': DIFFSERV_MIB.diffServClfrElementSpecific,
'1.3.6.1.2.1.97.1.2.4.1.5': DIFFSERV_MIB.diffServClfrElementStorage,
'1.3.6.1.2.1.97.1.2.4.1.6': DIFFSERV_MIB.diffServClfrElementStatus,
'1.3.6.1.2.1.97.1.2.6.1.1': DIFFSERV_MIB.diffServMultiFieldClfrId,
'1.3.6.1.2.1.97.1.2.6.1.2': DIFFSERV_MIB.diffServMultiFieldClfrAddrType,
'1.3.6.1.2.1.97.1.2.6.1.3': DIFFSERV_MIB.diffServMultiFieldClfrDstAddr,
'1.3.6.1.2.1.97.1.2.6.1.4': DIFFSERV_MIB.diffServMultiFieldClfrDstPrefixLength,
'1.3.6.1.2.1.97.1.2.6.1.5': DIFFSERV_MIB.diffServMultiFieldClfrSrcAddr,
'1.3.6.1.2.1.97.1.2.6.1.6': DIFFSERV_MIB.diffServMultiFieldClfrSrcPrefixLength,
'1.3.6.1.2.1.97.1.2.6.1.7': DIFFSERV_MIB.diffServMultiFieldClfrDscp,
'1.3.6.1.2.1.97.1.2.6.1.8': DIFFSERV_MIB.diffServMultiFieldClfrFlowId,
'1.3.6.1.2.1.97.1.2.6.1.9': DIFFSERV_MIB.diffServMultiFieldClfrProtocol,
'1.3.6.1.2.1.97.1.2.6.1.10': DIFFSERV_MIB.diffServMultiFieldClfrDstL4PortMin,
'1.3.6.1.2.1.97.1.2.6.1.11': DIFFSERV_MIB.diffServMultiFieldClfrDstL4PortMax,
'1.3.6.1.2.1.97.1.2.6.1.12': DIFFSERV_MIB.diffServMultiFieldClfrSrcL4PortMin,
'1.3.6.1.2.1.97.1.2.6.1.13': DIFFSERV_MIB.diffServMultiFieldClfrSrcL4PortMax,
'1.3.6.1.2.1.97.1.2.6.1.14': DIFFSERV_MIB.diffServMultiFieldClfrStorage,
'1.3.6.1.2.1.97.1.2.6.1.15': DIFFSERV_MIB.diffServMultiFieldClfrStatus,
'1.3.6.1.2.1.97.1.3.2.1.1': DIFFSERV_MIB.diffServMeterId,
'1.3.6.1.2.1.97.1.3.2.1.2': DIFFSERV_MIB.diffServMeterSucceedNext,
'1.3.6.1.2.1.97.1.3.2.1.3': DIFFSERV_MIB.diffServMeterFailNext,
'1.3.6.1.2.1.97.1.3.2.1.4': DIFFSERV_MIB.diffServMeterSpecific,
'1.3.6.1.2.1.97.1.3.2.1.5': DIFFSERV_MIB.diffServMeterStorage,
'1.3.6.1.2.1.97.1.3.2.1.6': DIFFSERV_MIB.diffServMeterStatus,
'1.3.6.1.2.1.97.1.4.2.1.1': DIFFSERV_MIB.diffServTBParamId,
'1.3.6.1.2.1.97.1.4.2.1.2': DIFFSERV_MIB.diffServTBParamType,
'1.3.6.1.2.1.97.1.4.2.1.3': DIFFSERV_MIB.diffServTBParamRate,
'1.3.6.1.2.1.97.1.4.2.1.4': DIFFSERV_MIB.diffServTBParamBurstSize,
'1.3.6.1.2.1.97.1.4.2.1.5': DIFFSERV_MIB.diffServTBParamInterval,
'1.3.6.1.2.1.97.1.4.2.1.6': DIFFSERV_MIB.diffServTBParamStorage,
'1.3.6.1.2.1.97.1.4.2.1.7': DIFFSERV_MIB.diffServTBParamStatus,
'1.3.6.1.2.1.97.1.5.2.1.1': DIFFSERV_MIB.diffServActionId,
'1.3.6.1.2.1.97.1.5.2.1.2': DIFFSERV_MIB.diffServActionInterface,
'1.3.6.1.2.1.97.1.5.2.1.3': DIFFSERV_MIB.diffServActionNext,
'1.3.6.1.2.1.97.1.5.2.1.4': DIFFSERV_MIB.diffServActionSpecific,
'1.3.6.1.2.1.97.1.5.2.1.5': DIFFSERV_MIB.diffServActionStorage,
'1.3.6.1.2.1.97.1.5.2.1.6': DIFFSERV_MIB.diffServActionStatus,
'1.3.6.1.2.1.97.1.5.3.1.1': DIFFSERV_MIB.diffServDscpMarkActDscp,
'1.3.6.1.2.1.97.1.5.5.1.1': DIFFSERV_MIB.diffServCountActId,
'1.3.6.1.2.1.97.1.5.5.1.2': DIFFSERV_MIB.diffServCountActOctets,
'1.3.6.1.2.1.97.1.5.5.1.3': DIFFSERV_MIB.diffServCountActPkts,
'1.3.6.1.2.1.97.1.5.5.1.4': DIFFSERV_MIB.diffServCountActStorage,
'1.3.6.1.2.1.97.1.5.5.1.5': DIFFSERV_MIB.diffServCountActStatus,
'1.3.6.1.2.1.97.1.6.2.1.1': DIFFSERV_MIB.diffServAlgDropId,
'1.3.6.1.2.1.97.1.6.2.1.2': DIFFSERV_MIB.diffServAlgDropType,
'1.3.6.1.2.1.97.1.6.2.1.3': DIFFSERV_MIB.diffServAlgDropNext,
'1.3.6.1.2.1.97.1.6.2.1.4': DIFFSERV_MIB.diffServAlgDropQMeasure,
'1.3.6.1.2.1.97.1.6.2.1.5': DIFFSERV_MIB.diffServAlgDropQThreshold,
'1.3.6.1.2.1.97.1.6.2.1.6': DIFFSERV_MIB.diffServAlgDropSpecific,
'1.3.6.1.2.1.97.1.6.2.1.7': DIFFSERV_MIB.diffServAlgDropOctets,
'1.3.6.1.2.1.97.1.6.2.1.8': DIFFSERV_MIB.diffServAlgDropPkts,
'1.3.6.1.2.1.97.1.6.2.1.9': DIFFSERV_MIB.diffServAlgRandomDropOctets,
'1.3.6.1.2.1.97.1.6.2.1.10': DIFFSERV_MIB.diffServAlgRandomDropPkts,
'1.3.6.1.2.1.97.1.6.2.1.11': DIFFSERV_MIB.diffServAlgDropStorage,
'1.3.6.1.2.1.97.1.6.2.1.12': DIFFSERV_MIB.diffServAlgDropStatus,
'1.3.6.1.2.1.97.1.6.4.1.1': DIFFSERV_MIB.diffServRandomDropId,
'1.3.6.1.2.1.97.1.6.4.1.2': DIFFSERV_MIB.diffServRandomDropMinThreshBytes,
'1.3.6.1.2.1.97.1.6.4.1.3': DIFFSERV_MIB.diffServRandomDropMinThreshPkts,
'1.3.6.1.2.1.97.1.6.4.1.4': DIFFSERV_MIB.diffServRandomDropMaxThreshBytes,
'1.3.6.1.2.1.97.1.6.4.1.5': DIFFSERV_MIB.diffServRandomDropMaxThreshPkts,
'1.3.6.1.2.1.97.1.6.4.1.6': DIFFSERV_MIB.diffServRandomDropProbMax,
'1.3.6.1.2.1.97.1.6.4.1.7': DIFFSERV_MIB.diffServRandomDropWeight,
'1.3.6.1.2.1.97.1.6.4.1.8': DIFFSERV_MIB.diffServRandomDropSamplingRate,
'1.3.6.1.2.1.97.1.6.4.1.9': DIFFSERV_MIB.diffServRandomDropStorage,
'1.3.6.1.2.1.97.1.6.4.1.10': DIFFSERV_MIB.diffServRandomDropStatus,
'1.3.6.1.2.1.97.1.7.2.1.1': DIFFSERV_MIB.diffServQId,
'1.3.6.1.2.1.97.1.7.2.1.2': DIFFSERV_MIB.diffServQNext,
'1.3.6.1.2.1.97.1.7.2.1.3': DIFFSERV_MIB.diffServQMinRate,
'1.3.6.1.2.1.97.1.7.2.1.4': DIFFSERV_MIB.diffServQMaxRate,
'1.3.6.1.2.1.97.1.7.2.1.5': DIFFSERV_MIB.diffServQStorage,
'1.3.6.1.2.1.97.1.7.2.1.6': DIFFSERV_MIB.diffServQStatus,
'1.3.6.1.2.1.97.1.8.2.1.1': DIFFSERV_MIB.diffServSchedulerId,
'1.3.6.1.2.1.97.1.8.2.1.2': DIFFSERV_MIB.diffServSchedulerNext,
'1.3.6.1.2.1.97.1.8.2.1.3': DIFFSERV_MIB.diffServSchedulerMethod,
'1.3.6.1.2.1.97.1.8.2.1.4': DIFFSERV_MIB.diffServSchedulerMinRate,
'1.3.6.1.2.1.97.1.8.2.1.5': DIFFSERV_MIB.diffServSchedulerMaxRate,
'1.3.6.1.2.1.97.1.8.2.1.6': DIFFSERV_MIB.diffServSchedulerStorage,
'1.3.6.1.2.1.97.1.8.2.1.7': DIFFSERV_MIB.diffServSchedulerStatus,
'1.3.6.1.2.1.97.1.8.4.1.1': DIFFSERV_MIB.diffServMinRateId,
'1.3.6.1.2.1.97.1.8.4.1.2': DIFFSERV_MIB.diffServMinRatePriority,
'1.3.6.1.2.1.97.1.8.4.1.3': DIFFSERV_MIB.diffServMinRateAbsolute,
'1.3.6.1.2.1.97.1.8.4.1.4': DIFFSERV_MIB.diffServMinRateRelative,
'1.3.6.1.2.1.97.1.8.4.1.5': DIFFSERV_MIB.diffServMinRateStorage,
'1.3.6.1.2.1.97.1.8.4.1.6': DIFFSERV_MIB.diffServMinRateStatus,
'1.3.6.1.2.1.97.1.8.6.1.1': DIFFSERV_MIB.diffServMaxRateId,
'1.3.6.1.2.1.97.1.8.6.1.2': DIFFSERV_MIB.diffServMaxRateLevel,
'1.3.6.1.2.1.97.1.8.6.1.3': DIFFSERV_MIB.diffServMaxRateAbsolute,
'1.3.6.1.2.1.97.1.8.6.1.4': DIFFSERV_MIB.diffServMaxRateRelative,
'1.3.6.1.2.1.97.1.8.6.1.5': DIFFSERV_MIB.diffServMaxRateThreshold,
'1.3.6.1.2.1.97.1.8.6.1.6': DIFFSERV_MIB.diffServMaxRateStorage,
'1.3.6.1.2.1.97.1.8.6.1.7': DIFFSERV_MIB.diffServMaxRateStatus,
'1.3.6.1.2.1.97.2.2.1': DIFFSERV_MIB.diffServMIBDataPathGroup,
'1.3.6.1.2.1.97.2.2.2': DIFFSERV_MIB.diffServMIBClfrGroup,
'1.3.6.1.2.1.97.2.2.3': DIFFSERV_MIB.diffServMIBClfrElementGroup,
'1.3.6.1.2.1.97.2.2.4': DIFFSERV_MIB.diffServMIBMultiFieldClfrGroup,
'1.3.6.1.2.1.97.2.2.5': DIFFSERV_MIB.diffServMIBMeterGroup,
'1.3.6.1.2.1.97.2.2.6': DIFFSERV_MIB.diffServMIBTBParamGroup,
'1.3.6.1.2.1.97.2.2.7': DIFFSERV_MIB.diffServMIBActionGroup,
'1.3.6.1.2.1.97.2.2.8': DIFFSERV_MIB.diffServMIBDscpMarkActGroup,
'1.3.6.1.2.1.97.2.2.9': DIFFSERV_MIB.diffServMIBCounterGroup,
'1.3.6.1.2.1.97.2.2.10': DIFFSERV_MIB.diffServMIBAlgDropGroup,
'1.3.6.1.2.1.97.2.2.11': DIFFSERV_MIB.diffServMIBRandomDropGroup,
'1.3.6.1.2.1.97.2.2.12': DIFFSERV_MIB.diffServMIBQGroup,
'1.3.6.1.2.1.97.2.2.13': DIFFSERV_MIB.diffServMIBSchedulerGroup,
'1.3.6.1.2.1.97.2.2.14': DIFFSERV_MIB.diffServMIBMinRateGroup,
'1.3.6.1.2.1.97.2.2.15': DIFFSERV_MIB.diffServMIBMaxRateGroup,
}
