# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, Gauge32, Integer32
from CISCO_SMI import ciscoModules, ciscoProducts
from SNMPv2_TC import TEXTUAL_CONVENTION

class CISCO_TC(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-TC-NO-U32'
	conformance = 3
	name = 'CISCO-TC'
	language = 2
	description = 'This module defines textual conventions used throughout\ncisco enterprise mibs.'

# nodes
class ciscoTextualConventions(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 12, 1])
	name = 'ciscoTextualConventions'


# macros
# types 

class CiscoNetworkProtocol(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'ip'), Enum(2, 'decnet'), Enum(3, 'pup'), Enum(4, 'chaos'), Enum(5, 'xns'), Enum(6, 'x121'), Enum(7, 'appletalk'), Enum(8, 'clns'), Enum(9, 'lat'), Enum(10, 'vines'), Enum(11, 'cons'), Enum(12, 'apollo'), Enum(13, 'stun'), Enum(14, 'novell'), Enum(15, 'qllc'), Enum(16, 'snapshot'), Enum(17, 'bstun'), Enum(18, 'x25pvc')]


class CiscoNetworkAddress(pycopia.SMI.Basetypes.OctetString):
	status = 1
	format = '1x:'


class InterfaceIndexOrZero(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 2147483647))
	format = 'd'

# scalars 
# columns
# rows 
# notifications (traps) 
# groups 
# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
