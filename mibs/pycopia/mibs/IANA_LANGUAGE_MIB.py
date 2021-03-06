# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_IDENTITY, mib_2

class IANA_LANGUAGE_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/iana/IANA-LANGUAGE-MIB'
	name = 'IANA-LANGUAGE-MIB'
	language = 2
	description = "The MIB module registers object identifier values for\nwell-known programming and scripting languages. Every\nlanguage registration MUST describe the format used\nwhen transferring scripts written in this language.\n\nAny additions or changes to the contents of this MIB\nmodule require Designated Expert Review as defined in\nthe Guidelines for Writing IANA Considerations Section\ndocument. The Designated Expert will be selected by\nthe IESG Area Director of the OPS Area.\n\nNote, this module does not have to register all possible\nlanguages since languages are identified by object\nidentifier values. It is therefore possible to registered \nlanguages in private OID trees. The references given below are not\nnormative with regard to the language version. Other\nreferences might be better suited to describe some newer \nversions of this language. The references are only\nprovided as `a pointer into the right direction'."

# nodes
class ianaLanguages(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 73])
	name = 'ianaLanguages'

class ianaLangJavaByteCode(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 73, 1])
	name = 'ianaLangJavaByteCode'

class ianaLangTcl(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 73, 2])
	name = 'ianaLangTcl'

class ianaLangPerl(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 73, 3])
	name = 'ianaLangPerl'

class ianaLangScheme(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 73, 4])
	name = 'ianaLangScheme'

class ianaLangSRSL(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 73, 5])
	name = 'ianaLangSRSL'

class ianaLangPSL(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 73, 6])
	name = 'ianaLangPSL'

class ianaLangSMSL(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 73, 7])
	name = 'ianaLangSMSL'


# macros
# types 
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
