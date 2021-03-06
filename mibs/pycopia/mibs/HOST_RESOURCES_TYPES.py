# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_IDENTITY
from HOST_RESOURCES_MIB import hrMIBAdminInfo, hrStorage, hrDevice

class HOST_RESOURCES_TYPES(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/HOST-RESOURCES-TYPES'
	conformance = 4
	name = 'HOST-RESOURCES-TYPES'
	language = 2
	description = 'This MIB module registers type definitions for\nstorage types, device types, and file system types.\nAfter the initial revision, this module will be\nmaintained by IANA.'

# nodes
class hrStorageTypes(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 2, 1])
	name = 'hrStorageTypes'

class hrStorageOther(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 2, 1, 1])
	name = 'hrStorageOther'

class hrStorageRam(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 2, 1, 2])
	name = 'hrStorageRam'

class hrStorageVirtualMemory(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 2, 1, 3])
	name = 'hrStorageVirtualMemory'

class hrStorageFixedDisk(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 2, 1, 4])
	name = 'hrStorageFixedDisk'

class hrStorageRemovableDisk(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 2, 1, 5])
	name = 'hrStorageRemovableDisk'

class hrStorageFloppyDisk(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 2, 1, 6])
	name = 'hrStorageFloppyDisk'

class hrStorageCompactDisc(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 2, 1, 7])
	name = 'hrStorageCompactDisc'

class hrStorageRamDisk(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 2, 1, 8])
	name = 'hrStorageRamDisk'

class hrStorageFlashMemory(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 2, 1, 9])
	name = 'hrStorageFlashMemory'

class hrStorageNetworkDisk(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 2, 1, 10])
	name = 'hrStorageNetworkDisk'

class hrDeviceTypes(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 1])
	name = 'hrDeviceTypes'

class hrDeviceOther(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 1, 1])
	name = 'hrDeviceOther'

class hrDeviceUnknown(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 1, 2])
	name = 'hrDeviceUnknown'

class hrDeviceProcessor(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 1, 3])
	name = 'hrDeviceProcessor'

class hrDeviceNetwork(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 1, 4])
	name = 'hrDeviceNetwork'

class hrDevicePrinter(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 1, 5])
	name = 'hrDevicePrinter'

class hrDeviceDiskStorage(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 1, 6])
	name = 'hrDeviceDiskStorage'

class hrDeviceVideo(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 1, 10])
	name = 'hrDeviceVideo'

class hrDeviceAudio(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 1, 11])
	name = 'hrDeviceAudio'

class hrDeviceCoprocessor(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 1, 12])
	name = 'hrDeviceCoprocessor'

class hrDeviceKeyboard(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 1, 13])
	name = 'hrDeviceKeyboard'

class hrDeviceModem(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 1, 14])
	name = 'hrDeviceModem'

class hrDeviceParallelPort(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 1, 15])
	name = 'hrDeviceParallelPort'

class hrDevicePointing(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 1, 16])
	name = 'hrDevicePointing'

class hrDeviceSerialPort(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 1, 17])
	name = 'hrDeviceSerialPort'

class hrDeviceTape(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 1, 18])
	name = 'hrDeviceTape'

class hrDeviceClock(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 1, 19])
	name = 'hrDeviceClock'

class hrDeviceVolatileMemory(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 1, 20])
	name = 'hrDeviceVolatileMemory'

class hrDeviceNonVolatileMemory(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 1, 21])
	name = 'hrDeviceNonVolatileMemory'

class hrFSTypes(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9])
	name = 'hrFSTypes'

class hrFSOther(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 1])
	name = 'hrFSOther'

class hrFSUnknown(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 2])
	name = 'hrFSUnknown'

class hrFSBerkeleyFFS(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 3])
	name = 'hrFSBerkeleyFFS'

class hrFSSys5FS(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 4])
	name = 'hrFSSys5FS'

class hrFSFat(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 5])
	name = 'hrFSFat'

class hrFSHPFS(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 6])
	name = 'hrFSHPFS'

class hrFSHFS(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 7])
	name = 'hrFSHFS'

class hrFSMFS(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 8])
	name = 'hrFSMFS'

class hrFSNTFS(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 9])
	name = 'hrFSNTFS'

class hrFSVNode(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 10])
	name = 'hrFSVNode'

class hrFSJournaled(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 11])
	name = 'hrFSJournaled'

class hrFSiso9660(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 12])
	name = 'hrFSiso9660'

class hrFSRockRidge(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 13])
	name = 'hrFSRockRidge'

class hrFSNFS(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 14])
	name = 'hrFSNFS'

class hrFSNetware(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 15])
	name = 'hrFSNetware'

class hrFSAFS(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 16])
	name = 'hrFSAFS'

class hrFSDFS(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 17])
	name = 'hrFSDFS'

class hrFSAppleshare(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 18])
	name = 'hrFSAppleshare'

class hrFSRFS(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 19])
	name = 'hrFSRFS'

class hrFSDGCFS(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 20])
	name = 'hrFSDGCFS'

class hrFSBFS(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 21])
	name = 'hrFSBFS'

class hrFSFAT32(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 22])
	name = 'hrFSFAT32'

class hrFSLinuxExt2(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 3, 9, 23])
	name = 'hrFSLinuxExt2'

class hostResourcesTypesModule(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 25, 7, 4])
	name = 'hostResourcesTypesModule'


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
