# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, mib_2, Gauge32
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SNMPv2_TC import TEXTUAL_CONVENTION, RowStatus, TimeStamp, RowPointer, StorageType
from IF_MIB import ifIndex, InterfaceIndex

class CIRCUIT_IF_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/CIRCUIT-IF-MIB'
	conformance = 3
	name = 'CIRCUIT-IF-MIB'
	language = 2
	description = 'The MIB module to allow insertion of selected circuit into\nthe ifTable.'

# nodes
class circuitIfMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94])
	name = 'circuitIfMIB'

class ciObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94, 1])
	name = 'ciObjects'

class ciCapabilities(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94, 2])
	name = 'ciCapabilities'

class ciConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94, 3])
	name = 'ciConformance'

class ciMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94, 3, 1])
	name = 'ciMIBGroups'

class ciMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94, 3, 2])
	name = 'ciMIBCompliances'


# macros
# types 

class CiFlowDirection(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'transmit'), Enum(2, 'receive'), Enum(3, 'both')]

# scalars 
class ciIfLastChange(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class ciIfNumActive(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


# columns
class ciCircuitObject(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


class ciCircuitFlow(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 2])
	syntaxobject = CiFlowDirection


class ciCircuitStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class ciCircuitIfIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 4])
	syntaxobject = InterfaceIndex


class ciCircuitCreateTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class ciCircuitStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class ciIfMapObject(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


class ciIfMapFlow(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94, 1, 2, 1, 2])
	syntaxobject = CiFlowDirection


# rows 
class ciCircuitEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ciCircuitObject, ciCircuitFlow], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94, 1, 1, 1])
	access = 2
	rowstatus = ciCircuitStatus
	columns = {'ciCircuitObject': ciCircuitObject, 'ciCircuitFlow': ciCircuitFlow, 'ciCircuitStatus': ciCircuitStatus, 'ciCircuitIfIndex': ciCircuitIfIndex, 'ciCircuitCreateTime': ciCircuitCreateTime, 'ciCircuitStorageType': ciCircuitStorageType}


class ciIfMapEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94, 1, 2, 1])
	access = 2
	columns = {'ciIfMapObject': ciIfMapObject, 'ciIfMapFlow': ciIfMapFlow}


# notifications (traps) 
# groups 
class ciCircuitGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94, 3, 1, 1])
	group = [ciCircuitStatus, ciCircuitIfIndex, ciCircuitCreateTime, ciCircuitStorageType]

class ciIfMapGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94, 3, 1, 2])
	group = [ciIfMapObject, ciIfMapFlow]

class ciStatsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 94, 3, 1, 3])
	group = [ciIfLastChange, ciIfNumActive]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
