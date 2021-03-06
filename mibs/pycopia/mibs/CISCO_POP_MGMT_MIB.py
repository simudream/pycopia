# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, IpAddress, Integer32, Gauge32, Counter32, TimeTicks
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_SMI import ciscoExperiment
from SNMPv2_TC import DisplayString, TimeStamp
from IF_MIB import InterfaceIndexOrZero

class CISCO_POP_MGMT_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-POP-MGMT-MIB'
	conformance = 2
	name = 'CISCO-POP-MGMT-MIB'
	language = 2
	description = 'Added objects:\ncpmDS1DS0UsageTable\ncpmActiveDS0sHighWaterMark\ncpmSW56CfgBChannelsInUse'

# nodes
class ciscoPopMgmtMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19])
	name = 'ciscoPopMgmtMIB'

class ciscoPopMgmtMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1])
	name = 'ciscoPopMgmtMIBObjects'

class cpmDS0Usage(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1])
	name = 'cpmDS0Usage'

class cpmCallFailure(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 2])
	name = 'cpmCallFailure'

class cpmActiveCallSummary(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3])
	name = 'cpmActiveCallSummary'

class cpmCallHistorySummary(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4])
	name = 'cpmCallHistorySummary'

class ciscoPopMgmtMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 3])
	name = 'ciscoPopMgmtMIBConformance'

class ciscoPopMgmtMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 1])
	name = 'ciscoPopMgmtMIBCompliances'

class ciscoPopMgmtMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 2])
	name = 'ciscoPopMgmtMIBGroups'


# macros
# types 
# scalars 
class cpmISDNCfgBChanInUseForAnalog(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class cpmISDNCfgBChannelsInUse(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class cpmActiveDS0s(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class cpmPPPCalls(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class cpmV120Calls(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class cpmV110Calls(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class cpmActiveDS0sHighWaterMark(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cpmSW56CfgBChannelsInUse(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class cpmISDNCallsRejected(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 2, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cpmModemCallsRejected(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 2, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cpmISDNCallsClearedAbnormally(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 2, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cpmModemCallsClearedAbnormally(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 2, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cpmISDNNoResource(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 2, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cpmModemNoResource(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 2, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cpmCallHistorySummaryTableMaxLength(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cpmCallHistorySummaryRetainTimer(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'minutes'


# columns
class cpmDS1SlotIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cpmDS1PortIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cpmChannelIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cpmConfiguredType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unknown'), Enum(2, 'isdn'), Enum(3, 'ct1'), Enum(4, 'ce1')]


class cpmDS0CallType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'idle'), Enum(2, 'unknown'), Enum(3, 'analog'), Enum(4, 'digital'), Enum(5, 'v110'), Enum(6, 'v120')]


class cpmL2Encapsulation(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'idle'), Enum(2, 'unknown'), Enum(3, 'ppp'), Enum(4, 'slip'), Enum(5, 'arap'), Enum(6, 'hdlc'), Enum(7, 'exec')]


class cpmCallCount(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cpmTimeInUse(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class cpmInOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cpmOutOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cpmInPackets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cpmOutPackets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cpmAssociatedInterface(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 13])
	syntaxobject = InterfaceIndexOrZero


class cpmDS1UsageSlotIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cpmDS1UsagePortIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cpmDS1ActiveDS0s(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class cpmDS1ActiveDS0sHighWaterMark(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cpmActiveCallStartTimeIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class cpmActiveCallSummaryIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cpmActiveUserID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class cpmActiveUserIpAddr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class cpmActiveCallType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unknown'), Enum(2, 'analog'), Enum(3, 'digital'), Enum(4, 'v110'), Enum(5, 'v120')]


class cpmActiveModemSlot(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cpmActiveModemPort(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cpmActiveCallDuration(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class cpmActiveEntrySlot(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cpmActiveEntryPort(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cpmActiveEntryChannel(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cpmActiveRemotePhoneNumber(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class cpmActiveLocalPhoneNumber(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class cpmActiveTTYNumber(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cpmCallDisconnectTimeIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class cpmCallStartTimeIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class cpmCallHistorySummaryIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cpmUserID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class cpmUserIpAddr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class cpmCallType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unknown'), Enum(2, 'analog'), Enum(3, 'digital'), Enum(4, 'v110'), Enum(5, 'v120')]


class cpmModemSlot(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cpmModemPort(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cpmCallDuration(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class cpmEntrySlot(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cpmEntryPort(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cpmEntryChannel(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cpmRemotePhoneNumber(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class cpmLocalPhoneNumber(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class cpmTTYNumber(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# rows 
class cpmDS0UsageEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([cpmDS1SlotIndex, cpmDS1PortIndex, cpmChannelIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1])
	access = 2
	columns = {'cpmDS1SlotIndex': cpmDS1SlotIndex, 'cpmDS1PortIndex': cpmDS1PortIndex, 'cpmChannelIndex': cpmChannelIndex, 'cpmConfiguredType': cpmConfiguredType, 'cpmDS0CallType': cpmDS0CallType, 'cpmL2Encapsulation': cpmL2Encapsulation, 'cpmCallCount': cpmCallCount, 'cpmTimeInUse': cpmTimeInUse, 'cpmInOctets': cpmInOctets, 'cpmOutOctets': cpmOutOctets, 'cpmInPackets': cpmInPackets, 'cpmOutPackets': cpmOutPackets, 'cpmAssociatedInterface': cpmAssociatedInterface}


class cpmDS1DS0UsageEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([cpmDS1UsageSlotIndex, cpmDS1UsagePortIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1])
	access = 2
	columns = {'cpmDS1UsageSlotIndex': cpmDS1UsageSlotIndex, 'cpmDS1UsagePortIndex': cpmDS1UsagePortIndex, 'cpmDS1ActiveDS0s': cpmDS1ActiveDS0s, 'cpmDS1ActiveDS0sHighWaterMark': cpmDS1ActiveDS0sHighWaterMark}


class cpmActiveCallSummaryEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([cpmActiveCallStartTimeIndex, cpmActiveCallSummaryIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1])
	access = 2
	columns = {'cpmActiveCallStartTimeIndex': cpmActiveCallStartTimeIndex, 'cpmActiveCallSummaryIndex': cpmActiveCallSummaryIndex, 'cpmActiveUserID': cpmActiveUserID, 'cpmActiveUserIpAddr': cpmActiveUserIpAddr, 'cpmActiveCallType': cpmActiveCallType, 'cpmActiveModemSlot': cpmActiveModemSlot, 'cpmActiveModemPort': cpmActiveModemPort, 'cpmActiveCallDuration': cpmActiveCallDuration, 'cpmActiveEntrySlot': cpmActiveEntrySlot, 'cpmActiveEntryPort': cpmActiveEntryPort, 'cpmActiveEntryChannel': cpmActiveEntryChannel, 'cpmActiveRemotePhoneNumber': cpmActiveRemotePhoneNumber, 'cpmActiveLocalPhoneNumber': cpmActiveLocalPhoneNumber, 'cpmActiveTTYNumber': cpmActiveTTYNumber}


class cpmCallHistorySummaryEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([cpmCallDisconnectTimeIndex, cpmCallStartTimeIndex, cpmCallHistorySummaryIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1])
	access = 2
	columns = {'cpmCallDisconnectTimeIndex': cpmCallDisconnectTimeIndex, 'cpmCallStartTimeIndex': cpmCallStartTimeIndex, 'cpmCallHistorySummaryIndex': cpmCallHistorySummaryIndex, 'cpmUserID': cpmUserID, 'cpmUserIpAddr': cpmUserIpAddr, 'cpmCallType': cpmCallType, 'cpmModemSlot': cpmModemSlot, 'cpmModemPort': cpmModemPort, 'cpmCallDuration': cpmCallDuration, 'cpmEntrySlot': cpmEntrySlot, 'cpmEntryPort': cpmEntryPort, 'cpmEntryChannel': cpmEntryChannel, 'cpmRemotePhoneNumber': cpmRemotePhoneNumber, 'cpmLocalPhoneNumber': cpmLocalPhoneNumber, 'cpmTTYNumber': cpmTTYNumber}


# notifications (traps) 
# groups 
class cpmCallFailureGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 2, 2])
	group = [cpmISDNCallsRejected, cpmModemCallsRejected, cpmISDNCallsClearedAbnormally, cpmModemCallsClearedAbnormally, cpmISDNNoResource, cpmModemNoResource]

class cpmActiveCallSummaryGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 2, 3])
	group = [cpmActiveUserID, cpmActiveCallType, cpmActiveUserIpAddr, cpmActiveModemSlot, cpmActiveModemPort, cpmActiveCallDuration, cpmActiveEntrySlot, cpmActiveEntryPort, cpmActiveEntryChannel, cpmActiveRemotePhoneNumber, cpmActiveLocalPhoneNumber, cpmActiveTTYNumber]

class cpmCallHistorySummaryGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 2, 4])
	group = [cpmCallHistorySummaryTableMaxLength, cpmCallHistorySummaryRetainTimer, cpmUserID, cpmUserIpAddr, cpmCallType, cpmModemSlot, cpmModemPort, cpmCallDuration, cpmEntrySlot, cpmEntryPort, cpmEntryChannel, cpmRemotePhoneNumber, cpmLocalPhoneNumber, cpmTTYNumber]

class cpmDS0UsageGroupRev1(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 2, 5])
	group = [cpmConfiguredType, cpmDS0CallType, cpmL2Encapsulation, cpmCallCount, cpmTimeInUse, cpmInOctets, cpmOutOctets, cpmInPackets, cpmOutPackets, cpmAssociatedInterface, cpmISDNCfgBChanInUseForAnalog, cpmISDNCfgBChannelsInUse, cpmActiveDS0s, cpmPPPCalls, cpmV120Calls, cpmV110Calls, cpmActiveDS0sHighWaterMark, cpmDS1ActiveDS0s, cpmDS1ActiveDS0sHighWaterMark, cpmSW56CfgBChannelsInUse]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
