# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP, NOTIFICATION_GROUP
from SNMPv2_MIB import sysUpTime
from SNMP_FRAMEWORK_MIB import SnmpAdminString
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Integer32, Unsigned32, NOTIFICATION_TYPE, Counter32, Gauge32, mib_2, zeroDotZero
from SNMP_TARGET_MIB import SnmpTagValue
from SNMPv2_TC import TEXTUAL_CONVENTION, RowStatus, TruthValue

class DISMAN_EVENT_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/DISMAN-EVENT-MIB'
	conformance = 5
	name = 'DISMAN-EVENT-MIB'
	language = 2
	description = 'The MIB module for defining event triggers and actions\nfor network management purposes.'

# nodes
class sysUpTimeInstance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 3, 0])
	name = 'sysUpTimeInstance'

class dismanEventMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88])
	name = 'dismanEventMIB'

class dismanEventMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1])
	name = 'dismanEventMIBObjects'

class mteResource(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 1])
	name = 'mteResource'

class mteTrigger(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2])
	name = 'mteTrigger'

class mteObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 3])
	name = 'mteObjects'

class mteEvent(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 4])
	name = 'mteEvent'

class dismanEventMIBNotificationPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 2])
	name = 'dismanEventMIBNotificationPrefix'

class dismanEventMIBNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 2, 0])
	name = 'dismanEventMIBNotifications'

class dismanEventMIBNotificationObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 2, 1])
	name = 'dismanEventMIBNotificationObjects'

class dismanEventMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 3])
	name = 'dismanEventMIBConformance'

class dismanEventMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 3, 1])
	name = 'dismanEventMIBCompliances'

class dismanEventMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 3, 2])
	name = 'dismanEventMIBGroups'


# macros
# types 

class FailureReason(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(-6, 'sampleOverrun'), Enum(-5, 'badType'), Enum(-4, 'noResponse'), Enum(-3, 'destinationUnreachable'), Enum(-2, 'badDestination'), Enum(-1, 'localResourceLack'), Enum(0, 'noError'), Enum(1, 'tooBig'), Enum(2, 'noSuchName'), Enum(3, 'badValue'), Enum(4, 'readOnly'), Enum(5, 'genErr'), Enum(6, 'noAccess'), Enum(7, 'wrongType'), Enum(8, 'wrongLength'), Enum(9, 'wrongEncoding'), Enum(10, 'wrongValue'), Enum(11, 'noCreation'), Enum(12, 'inconsistentValue'), Enum(13, 'resourceUnavailable'), Enum(14, 'commitFailed'), Enum(15, 'undoFailed'), Enum(16, 'authorizationError'), Enum(17, 'notWritable'), Enum(18, 'inconsistentName')]

# scalars 
class mteResourceSampleMinimum(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'seconds'


class mteResourceSampleInstanceMaximum(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'instances'


class mteResourceSampleInstances(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'instances'


class mteResourceSampleInstancesHigh(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'instances'


class mteResourceSampleInstanceLacks(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'instances'


class mteTriggerFailures(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'failures'


class mteEventFailures(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 4, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mteHotTrigger(ScalarObject):
	access = 3
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 2, 1, 1])
	syntaxobject = SnmpAdminString


class mteHotTargetName(ScalarObject):
	access = 3
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 2, 1, 2])
	syntaxobject = SnmpAdminString


class mteHotContextName(ScalarObject):
	access = 3
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 2, 1, 3])
	syntaxobject = SnmpAdminString


class mteHotOID(ScalarObject):
	access = 3
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class mteHotValue(ScalarObject):
	access = 3
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mteFailedReason(ScalarObject):
	access = 3
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 2, 1, 6])
	syntaxobject = FailureReason


# columns
class mteOwner(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 1])
	syntaxobject = SnmpAdminString


class mteTriggerName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 2])
	syntaxobject = SnmpAdminString


class mteTriggerComment(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 3])
	syntaxobject = SnmpAdminString


class mteTriggerTest(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class mteTriggerSampleType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'absoluteValue'), Enum(2, 'deltaValue')]


class mteTriggerValueID(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class mteTriggerValueIDWildcard(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class mteTriggerTargetTag(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 8])
	syntaxobject = SnmpTagValue


class mteTriggerContextName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 9])
	syntaxobject = SnmpAdminString


class mteTriggerContextNameWildcard(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class mteTriggerFrequency(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'seconds'


class mteTriggerObjectsOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 12])
	syntaxobject = SnmpAdminString


class mteTriggerObjects(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 13])
	syntaxobject = SnmpAdminString


class mteTriggerEnabled(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class mteTriggerEntryStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class mteTriggerDeltaDiscontinuityID(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class mteTriggerDeltaDiscontinuityIDWildcard(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class mteTriggerDeltaDiscontinuityIDType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'timeTicks'), Enum(2, 'timeStamp'), Enum(3, 'dateAndTime')]


class mteTriggerExistenceTest(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class mteTriggerExistenceStartup(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class mteTriggerExistenceObjectsOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 3])
	syntaxobject = SnmpAdminString


class mteTriggerExistenceObjects(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 4])
	syntaxobject = SnmpAdminString


class mteTriggerExistenceEventOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 5])
	syntaxobject = SnmpAdminString


class mteTriggerExistenceEvent(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 6])
	syntaxobject = SnmpAdminString


class mteTriggerBooleanComparison(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unequal'), Enum(2, 'equal'), Enum(3, 'less'), Enum(4, 'lessOrEqual'), Enum(5, 'greater'), Enum(6, 'greaterOrEqual')]


class mteTriggerBooleanValue(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mteTriggerBooleanStartup(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class mteTriggerBooleanObjectsOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 4])
	syntaxobject = SnmpAdminString


class mteTriggerBooleanObjects(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 5])
	syntaxobject = SnmpAdminString


class mteTriggerBooleanEventOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 6])
	syntaxobject = SnmpAdminString


class mteTriggerBooleanEvent(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 7])
	syntaxobject = SnmpAdminString


class mteTriggerThresholdStartup(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'rising'), Enum(2, 'falling'), Enum(3, 'risingOrFalling')]


class mteTriggerThresholdRising(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mteTriggerThresholdFalling(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mteTriggerThresholdDeltaRising(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mteTriggerThresholdDeltaFalling(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mteTriggerThresholdObjectsOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 6])
	syntaxobject = SnmpAdminString


class mteTriggerThresholdObjects(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 7])
	syntaxobject = SnmpAdminString


class mteTriggerThresholdRisingEventOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 8])
	syntaxobject = SnmpAdminString


class mteTriggerThresholdRisingEvent(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 9])
	syntaxobject = SnmpAdminString


class mteTriggerThresholdFallingEventOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 10])
	syntaxobject = SnmpAdminString


class mteTriggerThresholdFallingEvent(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 11])
	syntaxobject = SnmpAdminString


class mteTriggerThresholdDeltaRisingEventOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 12])
	syntaxobject = SnmpAdminString


class mteTriggerThresholdDeltaRisingEvent(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 13])
	syntaxobject = SnmpAdminString


class mteTriggerThresholdDeltaFallingEventOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 14])
	syntaxobject = SnmpAdminString


class mteTriggerThresholdDeltaFallingEvent(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 15])
	syntaxobject = SnmpAdminString


class mteObjectsName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 1])
	syntaxobject = SnmpAdminString


class mteObjectsIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class mteObjectsID(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class mteObjectsIDWildcard(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class mteObjectsEntryStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class mteEventName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 1])
	syntaxobject = SnmpAdminString


class mteEventComment(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 2])
	syntaxobject = SnmpAdminString


class mteEventActions(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class mteEventEnabled(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class mteEventEntryStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class mteEventNotification(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 4, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class mteEventNotificationObjectsOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 4, 3, 1, 2])
	syntaxobject = SnmpAdminString


class mteEventNotificationObjects(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 4, 3, 1, 3])
	syntaxobject = SnmpAdminString


class mteEventSetObject(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class mteEventSetObjectWildcard(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class mteEventSetValue(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mteEventSetTargetTag(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 4])
	syntaxobject = SnmpTagValue


class mteEventSetContextName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 5])
	syntaxobject = SnmpAdminString


class mteEventSetContextNameWildcard(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


# rows 
class mteTriggerEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mteOwner, mteTriggerName], True)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1])
	access = 2
	rowstatus = mteTriggerEntryStatus
	columns = {'mteOwner': mteOwner, 'mteTriggerName': mteTriggerName, 'mteTriggerComment': mteTriggerComment, 'mteTriggerTest': mteTriggerTest, 'mteTriggerSampleType': mteTriggerSampleType, 'mteTriggerValueID': mteTriggerValueID, 'mteTriggerValueIDWildcard': mteTriggerValueIDWildcard, 'mteTriggerTargetTag': mteTriggerTargetTag, 'mteTriggerContextName': mteTriggerContextName, 'mteTriggerContextNameWildcard': mteTriggerContextNameWildcard, 'mteTriggerFrequency': mteTriggerFrequency, 'mteTriggerObjectsOwner': mteTriggerObjectsOwner, 'mteTriggerObjects': mteTriggerObjects, 'mteTriggerEnabled': mteTriggerEnabled, 'mteTriggerEntryStatus': mteTriggerEntryStatus}


class mteTriggerDeltaEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mteOwner, mteTriggerName], True)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 3, 1])
	access = 2
	columns = {'mteTriggerDeltaDiscontinuityID': mteTriggerDeltaDiscontinuityID, 'mteTriggerDeltaDiscontinuityIDWildcard': mteTriggerDeltaDiscontinuityIDWildcard, 'mteTriggerDeltaDiscontinuityIDType': mteTriggerDeltaDiscontinuityIDType}


class mteTriggerExistenceEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mteOwner, mteTriggerName], True)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1])
	access = 2
	columns = {'mteTriggerExistenceTest': mteTriggerExistenceTest, 'mteTriggerExistenceStartup': mteTriggerExistenceStartup, 'mteTriggerExistenceObjectsOwner': mteTriggerExistenceObjectsOwner, 'mteTriggerExistenceObjects': mteTriggerExistenceObjects, 'mteTriggerExistenceEventOwner': mteTriggerExistenceEventOwner, 'mteTriggerExistenceEvent': mteTriggerExistenceEvent}


class mteTriggerBooleanEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mteOwner, mteTriggerName], True)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1])
	access = 2
	columns = {'mteTriggerBooleanComparison': mteTriggerBooleanComparison, 'mteTriggerBooleanValue': mteTriggerBooleanValue, 'mteTriggerBooleanStartup': mteTriggerBooleanStartup, 'mteTriggerBooleanObjectsOwner': mteTriggerBooleanObjectsOwner, 'mteTriggerBooleanObjects': mteTriggerBooleanObjects, 'mteTriggerBooleanEventOwner': mteTriggerBooleanEventOwner, 'mteTriggerBooleanEvent': mteTriggerBooleanEvent}


class mteTriggerThresholdEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mteOwner, mteTriggerName], True)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1])
	access = 2
	columns = {'mteTriggerThresholdStartup': mteTriggerThresholdStartup, 'mteTriggerThresholdRising': mteTriggerThresholdRising, 'mteTriggerThresholdFalling': mteTriggerThresholdFalling, 'mteTriggerThresholdDeltaRising': mteTriggerThresholdDeltaRising, 'mteTriggerThresholdDeltaFalling': mteTriggerThresholdDeltaFalling, 'mteTriggerThresholdObjectsOwner': mteTriggerThresholdObjectsOwner, 'mteTriggerThresholdObjects': mteTriggerThresholdObjects, 'mteTriggerThresholdRisingEventOwner': mteTriggerThresholdRisingEventOwner, 'mteTriggerThresholdRisingEvent': mteTriggerThresholdRisingEvent, 'mteTriggerThresholdFallingEventOwner': mteTriggerThresholdFallingEventOwner, 'mteTriggerThresholdFallingEvent': mteTriggerThresholdFallingEvent, 'mteTriggerThresholdDeltaRisingEventOwner': mteTriggerThresholdDeltaRisingEventOwner, 'mteTriggerThresholdDeltaRisingEvent': mteTriggerThresholdDeltaRisingEvent, 'mteTriggerThresholdDeltaFallingEventOwner': mteTriggerThresholdDeltaFallingEventOwner, 'mteTriggerThresholdDeltaFallingEvent': mteTriggerThresholdDeltaFallingEvent}


class mteObjectsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mteOwner, mteObjectsName, mteObjectsIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1])
	access = 2
	rowstatus = mteObjectsEntryStatus
	columns = {'mteObjectsName': mteObjectsName, 'mteObjectsIndex': mteObjectsIndex, 'mteObjectsID': mteObjectsID, 'mteObjectsIDWildcard': mteObjectsIDWildcard, 'mteObjectsEntryStatus': mteObjectsEntryStatus}


class mteEventEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mteOwner, mteEventName], True)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1])
	access = 2
	rowstatus = mteEventEntryStatus
	columns = {'mteEventName': mteEventName, 'mteEventComment': mteEventComment, 'mteEventActions': mteEventActions, 'mteEventEnabled': mteEventEnabled, 'mteEventEntryStatus': mteEventEntryStatus}


class mteEventNotificationEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mteOwner, mteEventName], True)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 4, 3, 1])
	access = 2
	columns = {'mteEventNotification': mteEventNotification, 'mteEventNotificationObjectsOwner': mteEventNotificationObjectsOwner, 'mteEventNotificationObjects': mteEventNotificationObjects}


class mteEventSetEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mteOwner, mteEventName], True)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1])
	access = 2
	columns = {'mteEventSetObject': mteEventSetObject, 'mteEventSetObjectWildcard': mteEventSetObjectWildcard, 'mteEventSetValue': mteEventSetValue, 'mteEventSetTargetTag': mteEventSetTargetTag, 'mteEventSetContextName': mteEventSetContextName, 'mteEventSetContextNameWildcard': mteEventSetContextNameWildcard}


# notifications (traps) 
class mteTriggerFired(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 2, 0, 1])

class mteTriggerRising(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 2, 0, 2])

class mteTriggerFalling(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 2, 0, 3])

class mteTriggerFailure(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 2, 0, 4])

class mteEventSetFailure(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 2, 0, 5])

# groups 
class dismanEventResourceGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 3, 2, 1])
	group = [mteResourceSampleMinimum, mteResourceSampleInstanceMaximum, mteResourceSampleInstances, mteResourceSampleInstancesHigh, mteResourceSampleInstanceLacks]

class dismanEventTriggerGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 3, 2, 2])
	group = [mteTriggerFailures, mteTriggerComment, mteTriggerTest, mteTriggerSampleType, mteTriggerValueID, mteTriggerValueIDWildcard, mteTriggerTargetTag, mteTriggerContextName, mteTriggerContextNameWildcard, mteTriggerFrequency, mteTriggerObjectsOwner, mteTriggerObjects, mteTriggerEnabled, mteTriggerEntryStatus, mteTriggerDeltaDiscontinuityID, mteTriggerDeltaDiscontinuityIDWildcard, mteTriggerDeltaDiscontinuityIDType, mteTriggerExistenceTest, mteTriggerExistenceStartup, mteTriggerExistenceObjectsOwner, mteTriggerExistenceObjects, mteTriggerExistenceEventOwner, mteTriggerExistenceEvent, mteTriggerBooleanComparison, mteTriggerBooleanValue, mteTriggerBooleanStartup, mteTriggerBooleanObjectsOwner, mteTriggerBooleanObjects, mteTriggerBooleanEventOwner, mteTriggerBooleanEvent, mteTriggerThresholdStartup, mteTriggerThresholdObjectsOwner, mteTriggerThresholdObjects, mteTriggerThresholdRising, mteTriggerThresholdFalling, mteTriggerThresholdDeltaRising, mteTriggerThresholdDeltaFalling, mteTriggerThresholdRisingEventOwner, mteTriggerThresholdRisingEvent, mteTriggerThresholdFallingEventOwner, mteTriggerThresholdFallingEvent, mteTriggerThresholdDeltaRisingEventOwner, mteTriggerThresholdDeltaRisingEvent, mteTriggerThresholdDeltaFallingEventOwner, mteTriggerThresholdDeltaFallingEvent]

class dismanEventObjectsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 3, 2, 3])
	group = [mteObjectsID, mteObjectsIDWildcard, mteObjectsEntryStatus]

class dismanEventEventGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 3, 2, 4])
	group = [mteEventFailures, mteEventComment, mteEventActions, mteEventEnabled, mteEventEntryStatus, mteEventNotification, mteEventNotificationObjectsOwner, mteEventNotificationObjects, mteEventSetObject, mteEventSetObjectWildcard, mteEventSetValue, mteEventSetTargetTag, mteEventSetContextName, mteEventSetContextNameWildcard]

class dismanEventNotificationObjectGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 3, 2, 5])
	group = [mteHotTrigger, mteHotTargetName, mteHotContextName, mteHotOID, mteHotValue, mteFailedReason]

class dismanEventNotificationGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 88, 3, 2, 6])
	group = [mteTriggerFired, mteTriggerRising, mteTriggerFalling, mteTriggerFailure, mteEventSetFailure]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
