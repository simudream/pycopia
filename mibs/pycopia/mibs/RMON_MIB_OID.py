# python
# This file is generated by a program (mib2py). 

import RMON_MIB

OIDMAP = {
'1.3.6.1.2.1.16': RMON_MIB.rmon,
'1.3.6.1.2.1.16.0': RMON_MIB.rmonEventsV2,
'1.3.6.1.2.1.16.1': RMON_MIB.statistics,
'1.3.6.1.2.1.16.2': RMON_MIB.history,
'1.3.6.1.2.1.16.3': RMON_MIB.alarm,
'1.3.6.1.2.1.16.4': RMON_MIB.hosts,
'1.3.6.1.2.1.16.5': RMON_MIB.hostTopN,
'1.3.6.1.2.1.16.6': RMON_MIB.matrix,
'1.3.6.1.2.1.16.7': RMON_MIB.filter,
'1.3.6.1.2.1.16.8': RMON_MIB.capture,
'1.3.6.1.2.1.16.9': RMON_MIB.event,
'1.3.6.1.2.1.16.20': RMON_MIB.rmonConformance,
'1.3.6.1.2.1.16.20.8': RMON_MIB.rmonMibModule,
'1.3.6.1.2.1.16.20.9': RMON_MIB.rmonCompliances,
'1.3.6.1.2.1.16.20.10': RMON_MIB.rmonGroups,
'1.3.6.1.2.1.16.1.1.1.1': RMON_MIB.etherStatsIndex,
'1.3.6.1.2.1.16.1.1.1.2': RMON_MIB.etherStatsDataSource,
'1.3.6.1.2.1.16.1.1.1.3': RMON_MIB.etherStatsDropEvents,
'1.3.6.1.2.1.16.1.1.1.4': RMON_MIB.etherStatsOctets,
'1.3.6.1.2.1.16.1.1.1.5': RMON_MIB.etherStatsPkts,
'1.3.6.1.2.1.16.1.1.1.6': RMON_MIB.etherStatsBroadcastPkts,
'1.3.6.1.2.1.16.1.1.1.7': RMON_MIB.etherStatsMulticastPkts,
'1.3.6.1.2.1.16.1.1.1.8': RMON_MIB.etherStatsCRCAlignErrors,
'1.3.6.1.2.1.16.1.1.1.9': RMON_MIB.etherStatsUndersizePkts,
'1.3.6.1.2.1.16.1.1.1.10': RMON_MIB.etherStatsOversizePkts,
'1.3.6.1.2.1.16.1.1.1.11': RMON_MIB.etherStatsFragments,
'1.3.6.1.2.1.16.1.1.1.12': RMON_MIB.etherStatsJabbers,
'1.3.6.1.2.1.16.1.1.1.13': RMON_MIB.etherStatsCollisions,
'1.3.6.1.2.1.16.1.1.1.14': RMON_MIB.etherStatsPkts64Octets,
'1.3.6.1.2.1.16.1.1.1.15': RMON_MIB.etherStatsPkts65to127Octets,
'1.3.6.1.2.1.16.1.1.1.16': RMON_MIB.etherStatsPkts128to255Octets,
'1.3.6.1.2.1.16.1.1.1.17': RMON_MIB.etherStatsPkts256to511Octets,
'1.3.6.1.2.1.16.1.1.1.18': RMON_MIB.etherStatsPkts512to1023Octets,
'1.3.6.1.2.1.16.1.1.1.19': RMON_MIB.etherStatsPkts1024to1518Octets,
'1.3.6.1.2.1.16.1.1.1.20': RMON_MIB.etherStatsOwner,
'1.3.6.1.2.1.16.1.1.1.21': RMON_MIB.etherStatsStatus,
'1.3.6.1.2.1.16.2.1.1.1': RMON_MIB.historyControlIndex,
'1.3.6.1.2.1.16.2.1.1.2': RMON_MIB.historyControlDataSource,
'1.3.6.1.2.1.16.2.1.1.3': RMON_MIB.historyControlBucketsRequested,
'1.3.6.1.2.1.16.2.1.1.4': RMON_MIB.historyControlBucketsGranted,
'1.3.6.1.2.1.16.2.1.1.5': RMON_MIB.historyControlInterval,
'1.3.6.1.2.1.16.2.1.1.6': RMON_MIB.historyControlOwner,
'1.3.6.1.2.1.16.2.1.1.7': RMON_MIB.historyControlStatus,
'1.3.6.1.2.1.16.2.2.1.1': RMON_MIB.etherHistoryIndex,
'1.3.6.1.2.1.16.2.2.1.2': RMON_MIB.etherHistorySampleIndex,
'1.3.6.1.2.1.16.2.2.1.3': RMON_MIB.etherHistoryIntervalStart,
'1.3.6.1.2.1.16.2.2.1.4': RMON_MIB.etherHistoryDropEvents,
'1.3.6.1.2.1.16.2.2.1.5': RMON_MIB.etherHistoryOctets,
'1.3.6.1.2.1.16.2.2.1.6': RMON_MIB.etherHistoryPkts,
'1.3.6.1.2.1.16.2.2.1.7': RMON_MIB.etherHistoryBroadcastPkts,
'1.3.6.1.2.1.16.2.2.1.8': RMON_MIB.etherHistoryMulticastPkts,
'1.3.6.1.2.1.16.2.2.1.9': RMON_MIB.etherHistoryCRCAlignErrors,
'1.3.6.1.2.1.16.2.2.1.10': RMON_MIB.etherHistoryUndersizePkts,
'1.3.6.1.2.1.16.2.2.1.11': RMON_MIB.etherHistoryOversizePkts,
'1.3.6.1.2.1.16.2.2.1.12': RMON_MIB.etherHistoryFragments,
'1.3.6.1.2.1.16.2.2.1.13': RMON_MIB.etherHistoryJabbers,
'1.3.6.1.2.1.16.2.2.1.14': RMON_MIB.etherHistoryCollisions,
'1.3.6.1.2.1.16.2.2.1.15': RMON_MIB.etherHistoryUtilization,
'1.3.6.1.2.1.16.3.1.1.1': RMON_MIB.alarmIndex,
'1.3.6.1.2.1.16.3.1.1.2': RMON_MIB.alarmInterval,
'1.3.6.1.2.1.16.3.1.1.3': RMON_MIB.alarmVariable,
'1.3.6.1.2.1.16.3.1.1.4': RMON_MIB.alarmSampleType,
'1.3.6.1.2.1.16.3.1.1.5': RMON_MIB.alarmValue,
'1.3.6.1.2.1.16.3.1.1.6': RMON_MIB.alarmStartupAlarm,
'1.3.6.1.2.1.16.3.1.1.7': RMON_MIB.alarmRisingThreshold,
'1.3.6.1.2.1.16.3.1.1.8': RMON_MIB.alarmFallingThreshold,
'1.3.6.1.2.1.16.3.1.1.9': RMON_MIB.alarmRisingEventIndex,
'1.3.6.1.2.1.16.3.1.1.10': RMON_MIB.alarmFallingEventIndex,
'1.3.6.1.2.1.16.3.1.1.11': RMON_MIB.alarmOwner,
'1.3.6.1.2.1.16.3.1.1.12': RMON_MIB.alarmStatus,
'1.3.6.1.2.1.16.4.1.1.1': RMON_MIB.hostControlIndex,
'1.3.6.1.2.1.16.4.1.1.2': RMON_MIB.hostControlDataSource,
'1.3.6.1.2.1.16.4.1.1.3': RMON_MIB.hostControlTableSize,
'1.3.6.1.2.1.16.4.1.1.4': RMON_MIB.hostControlLastDeleteTime,
'1.3.6.1.2.1.16.4.1.1.5': RMON_MIB.hostControlOwner,
'1.3.6.1.2.1.16.4.1.1.6': RMON_MIB.hostControlStatus,
'1.3.6.1.2.1.16.4.2.1.1': RMON_MIB.hostAddress,
'1.3.6.1.2.1.16.4.2.1.2': RMON_MIB.hostCreationOrder,
'1.3.6.1.2.1.16.4.2.1.3': RMON_MIB.hostIndex,
'1.3.6.1.2.1.16.4.2.1.4': RMON_MIB.hostInPkts,
'1.3.6.1.2.1.16.4.2.1.5': RMON_MIB.hostOutPkts,
'1.3.6.1.2.1.16.4.2.1.6': RMON_MIB.hostInOctets,
'1.3.6.1.2.1.16.4.2.1.7': RMON_MIB.hostOutOctets,
'1.3.6.1.2.1.16.4.2.1.8': RMON_MIB.hostOutErrors,
'1.3.6.1.2.1.16.4.2.1.9': RMON_MIB.hostOutBroadcastPkts,
'1.3.6.1.2.1.16.4.2.1.10': RMON_MIB.hostOutMulticastPkts,
'1.3.6.1.2.1.16.4.3.1.1': RMON_MIB.hostTimeAddress,
'1.3.6.1.2.1.16.4.3.1.2': RMON_MIB.hostTimeCreationOrder,
'1.3.6.1.2.1.16.4.3.1.3': RMON_MIB.hostTimeIndex,
'1.3.6.1.2.1.16.4.3.1.4': RMON_MIB.hostTimeInPkts,
'1.3.6.1.2.1.16.4.3.1.5': RMON_MIB.hostTimeOutPkts,
'1.3.6.1.2.1.16.4.3.1.6': RMON_MIB.hostTimeInOctets,
'1.3.6.1.2.1.16.4.3.1.7': RMON_MIB.hostTimeOutOctets,
'1.3.6.1.2.1.16.4.3.1.8': RMON_MIB.hostTimeOutErrors,
'1.3.6.1.2.1.16.4.3.1.9': RMON_MIB.hostTimeOutBroadcastPkts,
'1.3.6.1.2.1.16.4.3.1.10': RMON_MIB.hostTimeOutMulticastPkts,
'1.3.6.1.2.1.16.5.1.1.1': RMON_MIB.hostTopNControlIndex,
'1.3.6.1.2.1.16.5.1.1.2': RMON_MIB.hostTopNHostIndex,
'1.3.6.1.2.1.16.5.1.1.3': RMON_MIB.hostTopNRateBase,
'1.3.6.1.2.1.16.5.1.1.4': RMON_MIB.hostTopNTimeRemaining,
'1.3.6.1.2.1.16.5.1.1.5': RMON_MIB.hostTopNDuration,
'1.3.6.1.2.1.16.5.1.1.6': RMON_MIB.hostTopNRequestedSize,
'1.3.6.1.2.1.16.5.1.1.7': RMON_MIB.hostTopNGrantedSize,
'1.3.6.1.2.1.16.5.1.1.8': RMON_MIB.hostTopNStartTime,
'1.3.6.1.2.1.16.5.1.1.9': RMON_MIB.hostTopNOwner,
'1.3.6.1.2.1.16.5.1.1.10': RMON_MIB.hostTopNStatus,
'1.3.6.1.2.1.16.5.2.1.1': RMON_MIB.hostTopNReport,
'1.3.6.1.2.1.16.5.2.1.2': RMON_MIB.hostTopNIndex,
'1.3.6.1.2.1.16.5.2.1.3': RMON_MIB.hostTopNAddress,
'1.3.6.1.2.1.16.5.2.1.4': RMON_MIB.hostTopNRate,
'1.3.6.1.2.1.16.6.1.1.1': RMON_MIB.matrixControlIndex,
'1.3.6.1.2.1.16.6.1.1.2': RMON_MIB.matrixControlDataSource,
'1.3.6.1.2.1.16.6.1.1.3': RMON_MIB.matrixControlTableSize,
'1.3.6.1.2.1.16.6.1.1.4': RMON_MIB.matrixControlLastDeleteTime,
'1.3.6.1.2.1.16.6.1.1.5': RMON_MIB.matrixControlOwner,
'1.3.6.1.2.1.16.6.1.1.6': RMON_MIB.matrixControlStatus,
'1.3.6.1.2.1.16.6.2.1.1': RMON_MIB.matrixSDSourceAddress,
'1.3.6.1.2.1.16.6.2.1.2': RMON_MIB.matrixSDDestAddress,
'1.3.6.1.2.1.16.6.2.1.3': RMON_MIB.matrixSDIndex,
'1.3.6.1.2.1.16.6.2.1.4': RMON_MIB.matrixSDPkts,
'1.3.6.1.2.1.16.6.2.1.5': RMON_MIB.matrixSDOctets,
'1.3.6.1.2.1.16.6.2.1.6': RMON_MIB.matrixSDErrors,
'1.3.6.1.2.1.16.6.3.1.1': RMON_MIB.matrixDSSourceAddress,
'1.3.6.1.2.1.16.6.3.1.2': RMON_MIB.matrixDSDestAddress,
'1.3.6.1.2.1.16.6.3.1.3': RMON_MIB.matrixDSIndex,
'1.3.6.1.2.1.16.6.3.1.4': RMON_MIB.matrixDSPkts,
'1.3.6.1.2.1.16.6.3.1.5': RMON_MIB.matrixDSOctets,
'1.3.6.1.2.1.16.6.3.1.6': RMON_MIB.matrixDSErrors,
'1.3.6.1.2.1.16.7.1.1.1': RMON_MIB.filterIndex,
'1.3.6.1.2.1.16.7.1.1.2': RMON_MIB.filterChannelIndex,
'1.3.6.1.2.1.16.7.1.1.3': RMON_MIB.filterPktDataOffset,
'1.3.6.1.2.1.16.7.1.1.4': RMON_MIB.filterPktData,
'1.3.6.1.2.1.16.7.1.1.5': RMON_MIB.filterPktDataMask,
'1.3.6.1.2.1.16.7.1.1.6': RMON_MIB.filterPktDataNotMask,
'1.3.6.1.2.1.16.7.1.1.7': RMON_MIB.filterPktStatus,
'1.3.6.1.2.1.16.7.1.1.8': RMON_MIB.filterPktStatusMask,
'1.3.6.1.2.1.16.7.1.1.9': RMON_MIB.filterPktStatusNotMask,
'1.3.6.1.2.1.16.7.1.1.10': RMON_MIB.filterOwner,
'1.3.6.1.2.1.16.7.1.1.11': RMON_MIB.filterStatus,
'1.3.6.1.2.1.16.7.2.1.1': RMON_MIB.channelIndex,
'1.3.6.1.2.1.16.7.2.1.2': RMON_MIB.channelIfIndex,
'1.3.6.1.2.1.16.7.2.1.3': RMON_MIB.channelAcceptType,
'1.3.6.1.2.1.16.7.2.1.4': RMON_MIB.channelDataControl,
'1.3.6.1.2.1.16.7.2.1.5': RMON_MIB.channelTurnOnEventIndex,
'1.3.6.1.2.1.16.7.2.1.6': RMON_MIB.channelTurnOffEventIndex,
'1.3.6.1.2.1.16.7.2.1.7': RMON_MIB.channelEventIndex,
'1.3.6.1.2.1.16.7.2.1.8': RMON_MIB.channelEventStatus,
'1.3.6.1.2.1.16.7.2.1.9': RMON_MIB.channelMatches,
'1.3.6.1.2.1.16.7.2.1.10': RMON_MIB.channelDescription,
'1.3.6.1.2.1.16.7.2.1.11': RMON_MIB.channelOwner,
'1.3.6.1.2.1.16.7.2.1.12': RMON_MIB.channelStatus,
'1.3.6.1.2.1.16.8.1.1.1': RMON_MIB.bufferControlIndex,
'1.3.6.1.2.1.16.8.1.1.2': RMON_MIB.bufferControlChannelIndex,
'1.3.6.1.2.1.16.8.1.1.3': RMON_MIB.bufferControlFullStatus,
'1.3.6.1.2.1.16.8.1.1.4': RMON_MIB.bufferControlFullAction,
'1.3.6.1.2.1.16.8.1.1.5': RMON_MIB.bufferControlCaptureSliceSize,
'1.3.6.1.2.1.16.8.1.1.6': RMON_MIB.bufferControlDownloadSliceSize,
'1.3.6.1.2.1.16.8.1.1.7': RMON_MIB.bufferControlDownloadOffset,
'1.3.6.1.2.1.16.8.1.1.8': RMON_MIB.bufferControlMaxOctetsRequested,
'1.3.6.1.2.1.16.8.1.1.9': RMON_MIB.bufferControlMaxOctetsGranted,
'1.3.6.1.2.1.16.8.1.1.10': RMON_MIB.bufferControlCapturedPackets,
'1.3.6.1.2.1.16.8.1.1.11': RMON_MIB.bufferControlTurnOnTime,
'1.3.6.1.2.1.16.8.1.1.12': RMON_MIB.bufferControlOwner,
'1.3.6.1.2.1.16.8.1.1.13': RMON_MIB.bufferControlStatus,
'1.3.6.1.2.1.16.8.2.1.1': RMON_MIB.captureBufferControlIndex,
'1.3.6.1.2.1.16.8.2.1.2': RMON_MIB.captureBufferIndex,
'1.3.6.1.2.1.16.8.2.1.3': RMON_MIB.captureBufferPacketID,
'1.3.6.1.2.1.16.8.2.1.4': RMON_MIB.captureBufferPacketData,
'1.3.6.1.2.1.16.8.2.1.5': RMON_MIB.captureBufferPacketLength,
'1.3.6.1.2.1.16.8.2.1.6': RMON_MIB.captureBufferPacketTime,
'1.3.6.1.2.1.16.8.2.1.7': RMON_MIB.captureBufferPacketStatus,
'1.3.6.1.2.1.16.9.1.1.1': RMON_MIB.eventIndex,
'1.3.6.1.2.1.16.9.1.1.2': RMON_MIB.eventDescription,
'1.3.6.1.2.1.16.9.1.1.3': RMON_MIB.eventType,
'1.3.6.1.2.1.16.9.1.1.4': RMON_MIB.eventCommunity,
'1.3.6.1.2.1.16.9.1.1.5': RMON_MIB.eventLastTimeSent,
'1.3.6.1.2.1.16.9.1.1.6': RMON_MIB.eventOwner,
'1.3.6.1.2.1.16.9.1.1.7': RMON_MIB.eventStatus,
'1.3.6.1.2.1.16.9.2.1.1': RMON_MIB.logEventIndex,
'1.3.6.1.2.1.16.9.2.1.2': RMON_MIB.logIndex,
'1.3.6.1.2.1.16.9.2.1.3': RMON_MIB.logTime,
'1.3.6.1.2.1.16.9.2.1.4': RMON_MIB.logDescription,
'1.3.6.1.2.1.16.0.1': RMON_MIB.risingAlarm,
'1.3.6.1.2.1.16.0.2': RMON_MIB.fallingAlarm,
'1.3.6.1.2.1.16.20.10.1': RMON_MIB.rmonEtherStatsGroup,
'1.3.6.1.2.1.16.20.10.2': RMON_MIB.rmonHistoryControlGroup,
'1.3.6.1.2.1.16.20.10.3': RMON_MIB.rmonEthernetHistoryGroup,
'1.3.6.1.2.1.16.20.10.4': RMON_MIB.rmonAlarmGroup,
'1.3.6.1.2.1.16.20.10.5': RMON_MIB.rmonHostGroup,
'1.3.6.1.2.1.16.20.10.6': RMON_MIB.rmonHostTopNGroup,
'1.3.6.1.2.1.16.20.10.7': RMON_MIB.rmonMatrixGroup,
'1.3.6.1.2.1.16.20.10.8': RMON_MIB.rmonFilterGroup,
'1.3.6.1.2.1.16.20.10.9': RMON_MIB.rmonPacketCaptureGroup,
'1.3.6.1.2.1.16.20.10.10': RMON_MIB.rmonEventGroup,
'1.3.6.1.2.1.16.20.10.11': RMON_MIB.rmonNotificationGroup,
}
