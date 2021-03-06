# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, Counter32, Gauge32
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_SMI import ciscoMgmt
from SNMPv2_TC import TruthValue, TimeStamp
from SNMP_REPEATER_MIB import rptrPortEntry

class CISCO_REPEATER_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-REPEATER-MIB'
	conformance = 4
	name = 'CISCO-REPEATER-MIB'
	language = 2
	description = ''

# nodes
class ciscoRptrMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22])
	name = 'ciscoRptrMIB'

class ciscoRptrMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 1])
	name = 'ciscoRptrMIBObjects'

class ciscoRptrMIBglobal(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 2])
	name = 'ciscoRptrMIBglobal'

class ciscoRptrMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 2])
	name = 'ciscoRptrMIBConformance'

class ciscoRptrMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 2, 1])
	name = 'ciscoRptrMIBCompliances'

class ciscoRptrMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 2, 2])
	name = 'ciscoRptrMIBGroups'

class ciscoRptrMIBTrapPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 3])
	name = 'ciscoRptrMIBTrapPrefix'

class ciscoRptrMIBTraps(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 3, 0])
	name = 'ciscoRptrMIBTraps'


# macros
# types 
# scalars 
class ciscoRptrTrapAlgorithm(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 2, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'once'), Enum(2, 'decay')]


# columns
class ciscoRptrPortMDIStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'normal'), Enum(2, 'crossover'), Enum(3, 'notSwitchable')]


class ciscoRptrPortLinkTestEnabled(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class ciscoRptrPortLinkTestFailed(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class ciscoRptrPortAutoPolarityEnabled(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class ciscoRptrPortAutoPolarityCorrected(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class ciscoRptrPortSrcAddrCtrl(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class ciscoRptrPortAllowedSrcAddr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class ciscoRptrPortAllowedSrcAddrStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'allowedSrcAddrConfig'), Enum(2, 'allowedSrcAddrLearn'), Enum(3, 'allowedSrcAddrUndefined')]


class ciscoRptrPortLastIllegalSrcAddr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class ciscoRptrPortIllegalAddrTrapAcked(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'acked'), Enum(2, 'no-acked-sending'), Enum(3, 'no-acked-no-sending')]


class ciscoRptrPortIllegalAddrTrapEnabled(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class ciscoRptrPortIllegalAddrFirstHeard(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class ciscoRptrPortIllegalAddrLastHeard(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class ciscoRptrPortLastIllegalAddrCount(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class ciscoRptrPortIllegalAddrTotalCount(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# rows 
from SNMP_REPEATER_MIB import rptrPortGroupIndex
from SNMP_REPEATER_MIB import rptrPortIndex
class ciscoRptrPortEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([rptrPortGroupIndex, rptrPortIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1])
	access = 2
	columns = {'ciscoRptrPortMDIStatus': ciscoRptrPortMDIStatus, 'ciscoRptrPortLinkTestEnabled': ciscoRptrPortLinkTestEnabled, 'ciscoRptrPortLinkTestFailed': ciscoRptrPortLinkTestFailed, 'ciscoRptrPortAutoPolarityEnabled': ciscoRptrPortAutoPolarityEnabled, 'ciscoRptrPortAutoPolarityCorrected': ciscoRptrPortAutoPolarityCorrected, 'ciscoRptrPortSrcAddrCtrl': ciscoRptrPortSrcAddrCtrl, 'ciscoRptrPortAllowedSrcAddr': ciscoRptrPortAllowedSrcAddr, 'ciscoRptrPortAllowedSrcAddrStatus': ciscoRptrPortAllowedSrcAddrStatus, 'ciscoRptrPortLastIllegalSrcAddr': ciscoRptrPortLastIllegalSrcAddr, 'ciscoRptrPortIllegalAddrTrapAcked': ciscoRptrPortIllegalAddrTrapAcked, 'ciscoRptrPortIllegalAddrTrapEnabled': ciscoRptrPortIllegalAddrTrapEnabled, 'ciscoRptrPortIllegalAddrFirstHeard': ciscoRptrPortIllegalAddrFirstHeard, 'ciscoRptrPortIllegalAddrLastHeard': ciscoRptrPortIllegalAddrLastHeard, 'ciscoRptrPortLastIllegalAddrCount': ciscoRptrPortLastIllegalAddrCount, 'ciscoRptrPortIllegalAddrTotalCount': ciscoRptrPortIllegalAddrTotalCount}


# notifications (traps) 
class ciscoRptrIllegalSrcAddrTrap(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 3, 0, 1])

# groups 
class ciscoRptrMIBPortGroupV11R01(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 2, 2, 2])
	group = [ciscoRptrPortMDIStatus, ciscoRptrPortLinkTestEnabled, ciscoRptrPortLinkTestFailed, ciscoRptrPortAutoPolarityEnabled, ciscoRptrPortAutoPolarityCorrected, ciscoRptrPortSrcAddrCtrl, ciscoRptrPortAllowedSrcAddr, ciscoRptrPortAllowedSrcAddrStatus, ciscoRptrPortLastIllegalSrcAddr, ciscoRptrPortIllegalAddrTrapAcked, ciscoRptrPortIllegalAddrTrapEnabled, ciscoRptrPortIllegalAddrFirstHeard, ciscoRptrPortIllegalAddrLastHeard, ciscoRptrPortLastIllegalAddrCount, ciscoRptrPortIllegalAddrTotalCount]

class ciscoRptrMIBGlobalsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 22, 2, 2, 3])
	group = [ciscoRptrTrapAlgorithm]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
