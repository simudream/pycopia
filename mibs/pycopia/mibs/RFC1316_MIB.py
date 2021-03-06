# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from RFC_1212 import OBJECT_TYPE
from RFC1213_MIB import DisplayString, mib_2
from RFC1155_SMI import Counter, TimeTicks, Gauge

class RFC1316_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/RFC1316-MIB'
	conformance = 2
	name = 'RFC1316-MIB'
	language = 1

# nodes
class char(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19])
	name = 'char'

class wellKnownProtocols(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 4])
	name = 'wellKnownProtocols'

class protocolOther(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 4, 1])
	name = 'protocolOther'

class protocolTelnet(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 4, 2])
	name = 'protocolTelnet'

class protocolRlogin(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 4, 3])
	name = 'protocolRlogin'

class protocolLat(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 4, 4])
	name = 'protocolLat'

class protocolX29(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 4, 5])
	name = 'protocolX29'

class protocolVtp(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 4, 6])
	name = 'protocolVtp'


# macros
# types 
AutonomousType = pycopia.SMI.Basetypes.AutonomousType
InstancePointer = pycopia.SMI.Basetypes.InstancePointer
# scalars 
class charNumber(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# columns
class charPortIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class charPortName(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class charPortType(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'physical'), Enum(2, 'virtual')]


class charPortHardware(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.AutonomousType


class charPortReset(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'ready'), Enum(2, 'execute')]


class charPortAdminStatus(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled'), Enum(3, 'off'), Enum(4, 'maintenance')]


class charPortOperStatus(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'up'), Enum(2, 'down'), Enum(3, 'maintenance'), Enum(4, 'absent'), Enum(5, 'active')]


class charPortLastChange(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class charPortInFlowType(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'none'), Enum(2, 'xonXoff'), Enum(3, 'hardware'), Enum(4, 'ctsRts'), Enum(5, 'dsrDtr')]


class charPortOutFlowType(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 2, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'none'), Enum(2, 'xonXoff'), Enum(3, 'hardware'), Enum(4, 'ctsRts'), Enum(5, 'dsrDtr')]


class charPortInFlowState(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 2, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'none'), Enum(2, 'unknown'), Enum(3, 'stop'), Enum(4, 'go')]


class charPortOutFlowState(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 2, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'none'), Enum(2, 'unknown'), Enum(3, 'stop'), Enum(4, 'go')]


class charPortInCharacters(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 2, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class charPortOutCharacters(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 2, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class charPortAdminOrigin(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 2, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'dynamic'), Enum(2, 'network'), Enum(3, 'local'), Enum(4, 'none')]


class charPortSessionMaximum(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 2, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class charPortSessionNumber(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 2, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class charPortSessionIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 2, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class charSessPortIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class charSessIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class charSessKill(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'ready'), Enum(2, 'execute')]


class charSessState(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'connecting'), Enum(2, 'connected'), Enum(3, 'disconnecting')]


class charSessProtocol(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.AutonomousType


class charSessOperOrigin(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unknown'), Enum(2, 'network'), Enum(3, 'local')]


class charSessInCharacters(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class charSessOutCharacters(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 3, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class charSessConnectionId(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 3, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.InstancePointer


class charSessStartTime(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 3, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


# rows 
class charPortEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([charPortIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 2, 1])
	access = 2
	columns = {'charPortIndex': charPortIndex, 'charPortName': charPortName, 'charPortType': charPortType, 'charPortHardware': charPortHardware, 'charPortReset': charPortReset, 'charPortAdminStatus': charPortAdminStatus, 'charPortOperStatus': charPortOperStatus, 'charPortLastChange': charPortLastChange, 'charPortInFlowType': charPortInFlowType, 'charPortOutFlowType': charPortOutFlowType, 'charPortInFlowState': charPortInFlowState, 'charPortOutFlowState': charPortOutFlowState, 'charPortInCharacters': charPortInCharacters, 'charPortOutCharacters': charPortOutCharacters, 'charPortAdminOrigin': charPortAdminOrigin, 'charPortSessionMaximum': charPortSessionMaximum, 'charPortSessionNumber': charPortSessionNumber, 'charPortSessionIndex': charPortSessionIndex}


class charSessEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([charSessPortIndex, charSessIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 19, 3, 1])
	access = 2
	columns = {'charSessPortIndex': charSessPortIndex, 'charSessIndex': charSessIndex, 'charSessKill': charSessKill, 'charSessState': charSessState, 'charSessProtocol': charSessProtocol, 'charSessOperOrigin': charSessOperOrigin, 'charSessInCharacters': charSessInCharacters, 'charSessOutCharacters': charSessOutCharacters, 'charSessConnectionId': charSessConnectionId, 'charSessStartTime': charSessStartTime}


# notifications (traps) 
# groups 
# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
