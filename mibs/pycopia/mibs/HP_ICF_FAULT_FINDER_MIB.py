# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import Integer32, MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP, NOTIFICATION_GROUP
from SNMPv2_TC import TimeStamp, TEXTUAL_CONVENTION
from ENTITY_MIB import PhysicalIndex
from HP_ICF_OID import hpicfObjectModules, hpicfCommon, hpicfCommonTrapsPrefix

class HP_ICF_FAULT_FINDER_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/HP-ICF-FAULT-FINDER-MIB'
	conformance = 5
	name = 'HP-ICF-FAULT-FINDER-MIB'
	language = 2
	description = 'This MIB module contains object definitions for\nmanaging the Fault Finder feature in web-capable\nHP devices.'

# nodes
class hpicfFaultFinderMib(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12])
	name = 'hpicfFaultFinderMib'

class hpicfFaultFinderConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1])
	name = 'hpicfFaultFinderConformance'

class hpicfFaultFinderCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 1])
	name = 'hpicfFaultFinderCompliances'

class hpicfFaultFinderGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2])
	name = 'hpicfFaultFinderGroups'

class hpicfFaultFinder(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7])
	name = 'hpicfFaultFinder'


# macros
# types 

class HpicfFaultType(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'badDriver'), Enum(2, 'badXcvr'), Enum(3, 'badCable'), Enum(4, 'tooLongCable'), Enum(5, 'overBandwidth'), Enum(6, 'bcastStorm'), Enum(7, 'partition'), Enum(8, 'misconfiguredSQE'), Enum(9, 'polarityReversal'), Enum(10, 'networkLoop'), Enum(11, 'lossOfLink'), Enum(12, 'portSecurityViolation'), Enum(13, 'backupLinkTransition'), Enum(14, 'meshingFault'), Enum(15, 'fanFault'), Enum(16, 'rpsFault'), Enum(17, 'stuck10MbFault'), Enum(18, 'lossOfStackMember'), Enum(19, 'hotSwapReboot')]


class HpicfFaultTolerance(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 255))


class HpicfFaultAction(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'none'), Enum(2, 'warn'), Enum(3, 'warnAndDisable'), Enum(4, 'warnAndSpeedReduce'), Enum(5, 'warnAndSpeedReduceAndDisable')]


class HpicfUrlString(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 255))

# scalars 
class hpicfFfFaultInfoURL(ScalarObject):
	access = 3
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 3])
	syntaxobject = HpicfUrlString


# columns
class hpicfFfControlIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1, 1])
	syntaxobject = HpicfFaultType


class hpicfFfAction(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1, 2])
	syntaxobject = HpicfFaultAction


class hpicfFfWarnTolerance(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1, 3])
	syntaxobject = HpicfFaultTolerance


class hpicfFfDisablePortTolerance(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1, 4])
	syntaxobject = HpicfFaultTolerance


class hpicfFfSpeedReduceTolerance(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1, 5])
	syntaxobject = HpicfFaultTolerance


class hpicfFfLogIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpicfFfLogCreateTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class hpicfFfLogPhysEntity(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 3])
	syntaxobject = PhysicalIndex


class hpicfFfLogFaultType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 4])
	syntaxobject = HpicfFaultType


class hpicfFfLogAction(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 5])
	syntaxobject = HpicfFaultAction


class hpicfFfLogSeverity(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'informational'), Enum(2, 'medium'), Enum(3, 'critical')]


class hpicfFfLogStatus(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'new'), Enum(2, 'active'), Enum(3, 'old')]


# rows 
class hpicfFfControlEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([hpicfFfControlIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1])
	access = 2
	columns = {'hpicfFfControlIndex': hpicfFfControlIndex, 'hpicfFfAction': hpicfFfAction, 'hpicfFfWarnTolerance': hpicfFfWarnTolerance, 'hpicfFfDisablePortTolerance': hpicfFfDisablePortTolerance, 'hpicfFfSpeedReduceTolerance': hpicfFfSpeedReduceTolerance}


class hpicfFfLogEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([hpicfFfLogIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1])
	access = 2
	columns = {'hpicfFfLogIndex': hpicfFfLogIndex, 'hpicfFfLogCreateTime': hpicfFfLogCreateTime, 'hpicfFfLogPhysEntity': hpicfFfLogPhysEntity, 'hpicfFfLogFaultType': hpicfFfLogFaultType, 'hpicfFfLogAction': hpicfFfLogAction, 'hpicfFfLogSeverity': hpicfFfLogSeverity, 'hpicfFfLogStatus': hpicfFfLogStatus}


# notifications (traps) 
class hpicfFaultFinderTrap(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 1, 0, 5])

# groups 
class hpicfFaultConfigGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 1])
	group = [hpicfFfAction, hpicfFfWarnTolerance, hpicfFfDisablePortTolerance]

class hpicfFaultLogGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 2])
	group = [hpicfFfLogCreateTime, hpicfFfLogPhysEntity, hpicfFfLogFaultType, hpicfFfLogAction, hpicfFfLogSeverity, hpicfFfLogStatus, hpicfFfFaultInfoURL]

class hpicfFaultNotifyGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 3])
	group = [hpicfFaultFinderTrap]

class hpicfFaultConfig2Group(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 4])
	group = [hpicfFfAction, hpicfFfWarnTolerance, hpicfFfDisablePortTolerance, hpicfFfSpeedReduceTolerance]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
