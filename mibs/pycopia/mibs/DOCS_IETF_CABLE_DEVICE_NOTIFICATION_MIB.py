# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, mib_2
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP, NOTIFICATION_GROUP
from IF_MIB import ifPhysAddress
from DOCS_CABLE_DEVICE_MIB import docsDevEvLevel, docsDevEvId, docsDevEvText, docsDevSwFilename, docsDevSwServer, docsDevServerDhcp, docsDevServerTime
from DOCS_IF_MIB import docsIfCmCmtsAddress, docsIfCmtsCmStatusMacAddress, docsIfDocsisBaseCapability, docsIfCmStatusDocsisOperMode, docsIfCmStatusModulationType, docsIfCmtsCmStatusDocsisRegMode, docsIfCmtsCmStatusModulationType

class DOCS_IETF_CABLE_DEVICE_NOTIFICATION_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB'
	conformance = 5
	name = 'DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB'
	language = 2
	description = 'The Event Notification MIB is an extension of the\nCABLE DEVICE MIB.  It defines various notification\nobjects for both cable modem and cable modem termination\nsystems.  Two groups of SNMP notification objects are\ndefined.  One group is for notifying cable modem events,\nand one group is for notifying cable modem termination\nsystem events.\n\nDOCSIS defines numerous events, and each event is\nassigned to a functional category.  This MIB defines\na notification object for each functional category.\nThe varbinding list of each notification includes\ninformation about the event that occurred on the\ndevice.\n\nCopyright (C) The Internet Society (2006).  This version\nof this MIB module is part of RFC 4547; see the RFC\nitself for full legal notices.'

# nodes
class docsDevNotifMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132])
	name = 'docsDevNotifMIB'

class docsDevNotifControl(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 1])
	name = 'docsDevNotifControl'

class docsDevCmNotifs(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 2, 0])
	name = 'docsDevCmNotifs'

class docsDevCmtsNotifs(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 3, 0])
	name = 'docsDevCmtsNotifs'

class docsDevNotifConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 4])
	name = 'docsDevNotifConformance'

class docsDevNotifGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 4, 1])
	name = 'docsDevNotifGroups'

class docsDevNotifCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 4, 2])
	name = 'docsDevNotifCompliances'


# macros
# types 
# scalars 
class docsDevCmNotifControl(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class docsDevCmtsNotifControl(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.BITS


# columns
# rows 
# notifications (traps) 
class docsDevCmInitTLVUnknownNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 2, 0, 1])

class docsDevCmDynServReqFailNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 2, 0, 2])

class docsDevCmDynServRspFailNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 2, 0, 3])

class docsDevCmDynServAckFailNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 2, 0, 4])

class docsDevCmBpiInitNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 2, 0, 5])

class docsDevCmBPKMNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 2, 0, 6])

class docsDevCmDynamicSANotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 2, 0, 7])

class docsDevCmDHCPFailNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 2, 0, 8])

class docsDevCmSwUpgradeInitNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 2, 0, 9])

class docsDevCmSwUpgradeFailNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 2, 0, 10])

class docsDevCmSwUpgradeSuccessNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 2, 0, 11])

class docsDevCmSwUpgradeCVCFailNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 2, 0, 12])

class docsDevCmTODFailNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 2, 0, 13])

class docsDevCmDCCReqFailNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 2, 0, 14])

class docsDevCmDCCRspFailNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 2, 0, 15])

class docsDevCmDCCAckFailNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 2, 0, 16])

class docsDevCmtsInitRegReqFailNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 3, 0, 1])

class docsDevCmtsInitRegRspFailNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 3, 0, 2])

class docsDevCmtsInitRegAckFailNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 3, 0, 3])

class docsDevCmtsDynServReqFailNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 3, 0, 4])

class docsDevCmtsDynServRspFailNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 3, 0, 5])

class docsDevCmtsDynServAckFailNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 3, 0, 6])

class docsDevCmtsBpiInitNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 3, 0, 7])

class docsDevCmtsBPKMNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 3, 0, 8])

class docsDevCmtsDynamicSANotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 3, 0, 9])

class docsDevCmtsDCCReqFailNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 3, 0, 10])

class docsDevCmtsDCCRspFailNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 3, 0, 11])

class docsDevCmtsDCCAckFailNotif(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 3, 0, 12])

# groups 
class docsDevCmNotifControlGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 4, 1, 1])
	group = [docsDevCmNotifControl]

class docsDevCmNotificationGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 4, 1, 2])
	group = [docsDevCmInitTLVUnknownNotif, docsDevCmDynServReqFailNotif, docsDevCmDynServRspFailNotif, docsDevCmDynServAckFailNotif, docsDevCmBpiInitNotif, docsDevCmBPKMNotif, docsDevCmDynamicSANotif, docsDevCmDHCPFailNotif, docsDevCmSwUpgradeInitNotif, docsDevCmSwUpgradeFailNotif, docsDevCmSwUpgradeSuccessNotif, docsDevCmSwUpgradeCVCFailNotif, docsDevCmTODFailNotif, docsDevCmDCCReqFailNotif, docsDevCmDCCRspFailNotif, docsDevCmDCCAckFailNotif]

class docsDevCmtsNotifControlGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 4, 1, 3])
	group = [docsDevCmtsNotifControl]

class docsDevCmtsNotificationGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 132, 4, 1, 4])
	group = [docsDevCmtsInitRegReqFailNotif, docsDevCmtsInitRegRspFailNotif, docsDevCmtsInitRegAckFailNotif, docsDevCmtsDynServReqFailNotif, docsDevCmtsDynServRspFailNotif, docsDevCmtsDynServAckFailNotif, docsDevCmtsBpiInitNotif, docsDevCmtsBPKMNotif, docsDevCmtsDynamicSANotif, docsDevCmtsDCCReqFailNotif, docsDevCmtsDCCRspFailNotif, docsDevCmtsDCCAckFailNotif]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
