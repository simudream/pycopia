# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP, NOTIFICATION_GROUP
from FC_MGMT_MIB import fcmInstanceIndex, fcmSwitchIndex, FcDomainIdOrZero, FcNameIdOrZero
from IF_MIB import ifIndex
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, Unsigned32, Counter32, Gauge32, mib_2
from T11_TC_MIB import T11FabricIndex
from SNMPv2_TC import TEXTUAL_CONVENTION, TruthValue, RowStatus

class T11_FC_FABRIC_ADDR_MGR_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/T11-FC-FABRIC-ADDR-MGR-MIB'
	name = 'T11-FC-FABRIC-ADDR-MGR-MIB'
	language = 2
	description = "The MIB module for the Fabric Address management\nfunctionality defined by the Fibre Channel standards.  For\nthe purposes of this MIB, Fabric Address Manager refers to\nthe functionality of acquiring DomainID(s) as specified in\nFC-SW-3, and managing Fibre Channel Identifiers as specified\nin FC-FS.  An instance of 'Fabric Address Manager' software\nfunctionality executes in the Principal Switch, and in each\nother switch.\n\nAfter an agent reboot, the values of read-write objects\ndefined in this MIB module are implementation-dependent.\n\nCopyright (C) The Internet Society (2006).  This version of\nthis MIB module is part of RFC 4439;  see the RFC itself for\nfull legal notices."

# nodes
class t11FcFabricAddrMgrMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137])
	name = 't11FcFabricAddrMgrMIB'

class t11FamNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 0])
	name = 't11FamNotifications'

class t11FamMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1])
	name = 't11FamMIBObjects'

class t11FamConfiguration(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1])
	name = 't11FamConfiguration'

class t11FamInfo(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 2])
	name = 't11FamInfo'

class t11FamNotifyControl(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 3])
	name = 't11FamNotifyControl'

class t11FamMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 2])
	name = 't11FamMIBConformance'

class t11FamMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 2, 1])
	name = 't11FamMIBCompliances'

class t11FamMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 2, 2])
	name = 't11FamMIBGroups'


# macros
# types 

class T11FamDomainPriority(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(1, 255))
	format = 'd'


class T11FamDomainInterfaceRole(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'nonPrincipal'), Enum(2, 'principalUpstream'), Enum(3, 'principalDownsteam'), Enum(4, 'isolated'), Enum(5, 'down'), Enum(6, 'unknown')]


class T11FamState(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'other'), Enum(2, 'starting'), Enum(3, 'unconfigured'), Enum(4, 'principalSwitchSelection'), Enum(5, 'domainIdDistribution'), Enum(6, 'buildFabricPhase'), Enum(7, 'reconfigureFabricPhase'), Enum(8, 'stable'), Enum(9, 'stableWithNoEports'), Enum(10, 'noDomains'), Enum(11, 'disabled'), Enum(12, 'unknown')]

# scalars 
class t11FamMaxFcIdCacheSize(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 2, 3])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class t11FamNotifyFabricIndex(ScalarObject):
	access = 3
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 3, 1])
	syntaxobject = T11FabricIndex


# columns
class t11FamFabricIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 1])
	syntaxobject = T11FabricIndex


class t11FamConfigDomainId(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 2])
	syntaxobject = FcDomainIdOrZero


class t11FamConfigDomainIdType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'preferred'), Enum(2, 'insistent'), Enum(3, 'static')]


class t11FamAutoReconfigure(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class t11FamContiguousAllocation(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class t11FamPriority(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 6])
	syntaxobject = T11FamDomainPriority


class t11FamPrincipalSwitchWwn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 7])
	syntaxobject = FcNameIdOrZero


class t11FamLocalSwitchWwn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 8])
	syntaxobject = FcNameIdOrZero


class t11FamAssignedAreaIdList(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class t11FamGrantedFcIds(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class t11FamRecoveredFcIds(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class t11FamFreeFcIds(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class t11FamAssignedFcIds(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class t11FamAvailableFcIds(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class t11FamRunningPriority(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 15])
	syntaxobject = T11FamDomainPriority


class t11FamPrincSwRunningPriority(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 16])
	syntaxobject = T11FamDomainPriority


class t11FamState(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 17])
	syntaxobject = T11FamState


class t11FamLocalPrincipalSwitchSlctns(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class t11FamPrincipalSwitchSelections(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class t11FamBuildFabrics(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 20])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class t11FamFabricReconfigures(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 21])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class t11FamDomainId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 22])
	syntaxobject = FcDomainIdOrZero


class t11FamSticky(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 23])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class t11FamRestart(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 24])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'nonDisruptive'), Enum(2, 'disruptive'), Enum(3, 'noOp')]


class t11FamRcFabricNotifyEnable(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 25])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class t11FamEnable(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 26])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class t11FamFabricName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 27])
	syntaxobject = FcNameIdOrZero


class t11FamIfRcfReject(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class t11FamIfRole(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 2, 1, 2])
	syntaxobject = T11FamDomainInterfaceRole


class t11FamIfRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class t11FamAreaAreaId(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class t11FamAreaAssignedPortIdList(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class t11FamDatabaseDomainId(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 2, 2, 1, 1])
	syntaxobject = FcDomainIdOrZero


class t11FamDatabaseSwitchWwn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 2, 2, 1, 2])
	syntaxobject = FcNameIdOrZero


class t11FamFcIdCacheWwn(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 2, 4, 1, 1])
	syntaxobject = FcNameIdOrZero


class t11FamFcIdCacheAreaIdPortId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 2, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class t11FamFcIdCachePortIds(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 2, 4, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


# rows 
class t11FamEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([fcmInstanceIndex, fcmSwitchIndex, t11FamFabricIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1])
	access = 2
	columns = {'t11FamFabricIndex': t11FamFabricIndex, 't11FamConfigDomainId': t11FamConfigDomainId, 't11FamConfigDomainIdType': t11FamConfigDomainIdType, 't11FamAutoReconfigure': t11FamAutoReconfigure, 't11FamContiguousAllocation': t11FamContiguousAllocation, 't11FamPriority': t11FamPriority, 't11FamPrincipalSwitchWwn': t11FamPrincipalSwitchWwn, 't11FamLocalSwitchWwn': t11FamLocalSwitchWwn, 't11FamAssignedAreaIdList': t11FamAssignedAreaIdList, 't11FamGrantedFcIds': t11FamGrantedFcIds, 't11FamRecoveredFcIds': t11FamRecoveredFcIds, 't11FamFreeFcIds': t11FamFreeFcIds, 't11FamAssignedFcIds': t11FamAssignedFcIds, 't11FamAvailableFcIds': t11FamAvailableFcIds, 't11FamRunningPriority': t11FamRunningPriority, 't11FamPrincSwRunningPriority': t11FamPrincSwRunningPriority, 't11FamState': t11FamState, 't11FamLocalPrincipalSwitchSlctns': t11FamLocalPrincipalSwitchSlctns, 't11FamPrincipalSwitchSelections': t11FamPrincipalSwitchSelections, 't11FamBuildFabrics': t11FamBuildFabrics, 't11FamFabricReconfigures': t11FamFabricReconfigures, 't11FamDomainId': t11FamDomainId, 't11FamSticky': t11FamSticky, 't11FamRestart': t11FamRestart, 't11FamRcFabricNotifyEnable': t11FamRcFabricNotifyEnable, 't11FamEnable': t11FamEnable, 't11FamFabricName': t11FamFabricName}


class t11FamIfEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([fcmInstanceIndex, fcmSwitchIndex, t11FamFabricIndex, ifIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 1, 2, 1])
	access = 2
	rowstatus = t11FamIfRowStatus
	columns = {'t11FamIfRcfReject': t11FamIfRcfReject, 't11FamIfRole': t11FamIfRole, 't11FamIfRowStatus': t11FamIfRowStatus}


class t11FamAreaEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([fcmInstanceIndex, fcmSwitchIndex, t11FamFabricIndex, t11FamAreaAreaId], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 2, 1, 1])
	access = 2
	columns = {'t11FamAreaAreaId': t11FamAreaAreaId, 't11FamAreaAssignedPortIdList': t11FamAreaAssignedPortIdList}


class t11FamDatabaseEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([fcmInstanceIndex, fcmSwitchIndex, t11FamFabricIndex, t11FamDatabaseDomainId], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 2, 2, 1])
	access = 2
	columns = {'t11FamDatabaseDomainId': t11FamDatabaseDomainId, 't11FamDatabaseSwitchWwn': t11FamDatabaseSwitchWwn}


class t11FamFcIdCacheEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([fcmInstanceIndex, fcmSwitchIndex, t11FamFabricIndex, t11FamFcIdCacheWwn], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 1, 2, 4, 1])
	access = 2
	columns = {'t11FamFcIdCacheWwn': t11FamFcIdCacheWwn, 't11FamFcIdCacheAreaIdPortId': t11FamFcIdCacheAreaIdPortId, 't11FamFcIdCachePortIds': t11FamFcIdCachePortIds}


# notifications (traps) 
class t11FamDomainIdNotAssignedNotify(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 0, 1])

class t11FamNewPrincipalSwitchNotify(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 0, 2])

class t11FamFabricChangeNotify(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 0, 3])

# groups 
class t11FamGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 2, 2, 1])
	group = [t11FamConfigDomainId, t11FamConfigDomainIdType, t11FamAutoReconfigure, t11FamContiguousAllocation, t11FamPriority, t11FamPrincipalSwitchWwn, t11FamLocalSwitchWwn, t11FamAssignedAreaIdList, t11FamGrantedFcIds, t11FamRecoveredFcIds, t11FamFreeFcIds, t11FamAssignedFcIds, t11FamAvailableFcIds, t11FamRunningPriority, t11FamPrincSwRunningPriority, t11FamState, t11FamLocalPrincipalSwitchSlctns, t11FamPrincipalSwitchSelections, t11FamBuildFabrics, t11FamFabricReconfigures, t11FamDomainId, t11FamSticky, t11FamRestart, t11FamRcFabricNotifyEnable, t11FamEnable, t11FamFabricName, t11FamIfRcfReject, t11FamIfRole, t11FamIfRowStatus, t11FamNotifyFabricIndex]

class t11FamCommandGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 2, 2, 2])
	group = [t11FamRestart]

class t11FamDatabaseGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 2, 2, 3])
	group = [t11FamDatabaseSwitchWwn]

class t11FamAreaGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 2, 2, 4])
	group = [t11FamAreaAssignedPortIdList]

class t11FamCacheGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 2, 2, 5])
	group = [t11FamMaxFcIdCacheSize, t11FamFcIdCacheAreaIdPortId, t11FamFcIdCachePortIds]

class t11FamNotificationGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 137, 2, 2, 6])
	group = [t11FamDomainIdNotAssignedNotify, t11FamNewPrincipalSwitchNotify, t11FamFabricChangeNotify]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
