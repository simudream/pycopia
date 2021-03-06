# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Integer32, mib_2
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from BRIDGE_MIB import dot1dStp, dot1dStpPortEntry
from SNMPv2_TC import TruthValue

class RSTP_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/RSTP-MIB'
	name = 'RSTP-MIB'
	language = 2
	description = 'The Bridge MIB Extension module for managing devices\nthat support the Rapid Spanning Tree Protocol defined\nby IEEE 802.1w.\n\nCopyright (C) The Internet Society (2005).  This version of\nthis MIB module is part of RFC 4318; See the RFC itself for\nfull legal notices.'

# nodes
class rstpMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 134])
	name = 'rstpMIB'

class rstpNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 134, 0])
	name = 'rstpNotifications'

class rstpObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 134, 1])
	name = 'rstpObjects'

class rstpConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 134, 2])
	name = 'rstpConformance'

class rstpGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 134, 2, 1])
	name = 'rstpGroups'

class rstpCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 134, 2, 2])
	name = 'rstpCompliances'


# macros
# types 
# scalars 
class dot1dStpVersion(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 2, 16])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(0, 'stpCompatible'), Enum(2, 'rstp')]


class dot1dStpTxHoldCount(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 2, 17])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# columns
class dot1dStpPortProtocolMigration(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class dot1dStpPortAdminEdgePort(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class dot1dStpPortOperEdgePort(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class dot1dStpPortAdminPointToPoint(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(0, 'forceTrue'), Enum(1, 'forceFalse'), Enum(2, 'auto')]


class dot1dStpPortOperPointToPoint(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class dot1dStpPortAdminPathCost(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# rows 
from BRIDGE_MIB import dot1dStpPort
class dot1dStpExtPortEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dot1dStpPort], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 2, 19, 1])
	access = 2
	columns = {'dot1dStpPortProtocolMigration': dot1dStpPortProtocolMigration, 'dot1dStpPortAdminEdgePort': dot1dStpPortAdminEdgePort, 'dot1dStpPortOperEdgePort': dot1dStpPortOperEdgePort, 'dot1dStpPortAdminPointToPoint': dot1dStpPortAdminPointToPoint, 'dot1dStpPortOperPointToPoint': dot1dStpPortOperPointToPoint, 'dot1dStpPortAdminPathCost': dot1dStpPortAdminPathCost}


# notifications (traps) 
# groups 
class rstpBridgeGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 134, 2, 1, 1])
	group = [dot1dStpVersion, dot1dStpTxHoldCount]

class rstpPortGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 134, 2, 1, 2])
	group = [dot1dStpPortProtocolMigration, dot1dStpPortAdminEdgePort, dot1dStpPortOperEdgePort, dot1dStpPortAdminPointToPoint, dot1dStpPortOperPointToPoint, dot1dStpPortAdminPathCost]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
