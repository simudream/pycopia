# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Counter32
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_SMI import ciscoMgmt
from SNMPv2_TC import TruthValue
from ATM_MIB import aal5VccEntry

class CISCO_ATM_EXT_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-ATM-EXT-MIB'
	name = 'CISCO-ATM-EXT-MIB'
	language = 2
	description = 'An extension to the Cisco ATM MIB module for managing\nATM implementations'

# nodes
class ciscoAtmExtMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 88])
	name = 'ciscoAtmExtMIB'

class cAal5VccExtMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 88, 1])
	name = 'cAal5VccExtMIBObjects'

class ciscoAal5ExtMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 88, 3])
	name = 'ciscoAal5ExtMIBConformance'

class ciscoAal5ExtMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 88, 3, 1])
	name = 'ciscoAal5ExtMIBCompliances'

class ciscoAal5ExtMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 88, 3, 2])
	name = 'ciscoAal5ExtMIBGroups'


# macros
# types 
# scalars 
# columns
class cAal5VccExtCompEnabled(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cAal5VccExtVoice(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cAal5VccExtInF5OamCells(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cAal5VccExtOutF5OamCells(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# rows 
from IF_MIB import ifIndex
from ATM_MIB import aal5VccVpi
from ATM_MIB import aal5VccVci
class cAal5VccExtEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, aal5VccVpi, aal5VccVci], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 1, 1])
	access = 2
	columns = {'cAal5VccExtCompEnabled': cAal5VccExtCompEnabled, 'cAal5VccExtVoice': cAal5VccExtVoice, 'cAal5VccExtInF5OamCells': cAal5VccExtInF5OamCells, 'cAal5VccExtOutF5OamCells': cAal5VccExtOutF5OamCells}


# notifications (traps) 
# groups 
class ciscoAal5ExtMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 88, 3, 2, 1])
	group = [cAal5VccExtCompEnabled, cAal5VccExtVoice, cAal5VccExtInF5OamCells, cAal5VccExtOutF5OamCells]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
