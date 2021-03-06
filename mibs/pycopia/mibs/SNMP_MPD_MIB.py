# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, snmpModules, Counter32

class SNMP_MPD_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/SNMP-MPD-MIB'
	name = 'SNMP-MPD-MIB'
	language = 2
	description = 'The MIB for Message Processing and Dispatching\n\nCopyright (C) The Internet Society (2002). This\nversion of this MIB module is part of RFC 3412;\nsee the RFC itself for full legal notices.'

# nodes
class snmpMPDMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 11])
	name = 'snmpMPDMIB'

class snmpMPDAdmin(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 11, 1])
	name = 'snmpMPDAdmin'

class snmpMPDMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 11, 2])
	name = 'snmpMPDMIBObjects'

class snmpMPDStats(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 11, 2, 1])
	name = 'snmpMPDStats'

class snmpMPDMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 11, 3])
	name = 'snmpMPDMIBConformance'

class snmpMPDMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 11, 3, 1])
	name = 'snmpMPDMIBCompliances'

class snmpMPDMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 11, 3, 2])
	name = 'snmpMPDMIBGroups'


# macros
# types 
# scalars 
class snmpUnknownSecurityModels(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 11, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInvalidMsgs(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 11, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpUnknownPDUHandlers(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 11, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# columns
# rows 
# notifications (traps) 
# groups 
class snmpMPDGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 11, 3, 2, 1])
	group = [snmpUnknownSecurityModels, snmpInvalidMsgs, snmpUnknownPDUHandlers]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
