# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Integer32, IpAddress
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_SMI import ciscoExperiment
from SNMPv2_TC import DisplayString

class CISCO_SIBU_FLASH_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-SIBU-FLASH-MIB'
	conformance = 132
	name = 'CISCO-SIBU-FLASH-MIB'
	language = 2
	description = 'The MIB module that provides a simple mechanism\nto support firmware upgrade on Cisco low end\ndevices.'

# nodes
class ciscoSibuFlashMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 45])
	name = 'ciscoSibuFlashMIB'

class ciscoSibuFlashMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 45, 1])
	name = 'ciscoSibuFlashMIBObjects'

class csfUpgrade(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1])
	name = 'csfUpgrade'

class ciscoSibuFlashMIBNotificationsPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 45, 2])
	name = 'ciscoSibuFlashMIBNotificationsPrefix'

class ciscoSibuFlashMIBNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 45, 2, 0])
	name = 'ciscoSibuFlashMIBNotifications'

class ciscoSibuFlashMIBComformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 45, 3])
	name = 'ciscoSibuFlashMIBComformance'

class ciscoSibuFlashMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 1])
	name = 'ciscoSibuFlashMIBCompliances'

class ciscoSibuFlashMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 2])
	name = 'ciscoSibuFlashMIBGroups'


# macros
# types 
# scalars 
class csfUpgradeFirmwareVersion(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class csfUpgradeFlashSize(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 4
	units = 'kbytes'


class csfUpgradeTFTPServerAddress(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class csfUpgradeTFTPLoadFilename(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class csfUpgradeTFTPInitiate(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'upgrade'), Enum(2, 'noUpgrade')]


class csfUpgradeFlashMode(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'permanent'), Enum(2, 'temporary')]


class csfUpgradeFirmwareStatus(ScalarObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'none'), Enum(2, 'inProgress'), Enum(3, 'succeeded'), Enum(4, 'failed')]


# columns
# rows 
# notifications (traps) 
# groups 
class ciscoSibuFlashMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 2, 1])
	group = [csfUpgradeFirmwareVersion, csfUpgradeFlashSize, csfUpgradeTFTPServerAddress, csfUpgradeTFTPLoadFilename, csfUpgradeTFTPInitiate, csfUpgradeFlashMode, csfUpgradeFirmwareStatus]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
