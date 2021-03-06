# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, NOTIFICATION_GROUP, OBJECT_GROUP
from IF_MIB import ifIndex, ifCounterDiscontinuityGroup
from SNMP_FRAMEWORK_MIB import SnmpAdminString
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Integer32, Unsigned32, Gauge32, Counter64, TimeTicks, mib_2, NOTIFICATION_TYPE
from INET_ADDRESS_MIB import InetAddressType, InetAddress, InetPortNumber
from SNMPv2_TC import TEXTUAL_CONVENTION, StorageType, RowStatus

class NAT_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/NAT-MIB'
	conformance = 5
	name = 'NAT-MIB'
	language = 2
	description = 'This MIB module defines the generic managed objects\nfor NAT.\n\nCopyright (C) The Internet Society (2005).  This version\nof this MIB module is part of RFC 4008;  see the RFC\nitself for full legal notices.'

# nodes
class natMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123])
	name = 'natMIB'

class natMIBNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 0])
	name = 'natMIBNotifications'

class natMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1])
	name = 'natMIBObjects'

class natDefTimeouts(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 1])
	name = 'natDefTimeouts'

class natNotifCtrl(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 2])
	name = 'natNotifCtrl'

class natMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 2])
	name = 'natMIBConformance'

class natMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 2, 1])
	name = 'natMIBGroups'

class natMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 2, 2])
	name = 'natMIBCompliances'


# macros
# types 

class NatProtocolType(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'none'), Enum(2, 'other'), Enum(3, 'icmp'), Enum(4, 'udp'), Enum(5, 'tcp')]


class NatProtocolMap(pycopia.SMI.Basetypes.BITS):
	status = 1
	enumerations = [Enum(0, 'other'), Enum(1, 'icmp'), Enum(2, 'udp'), Enum(3, 'tcp')]


class NatAddrMapId(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(1, -1))
	format = 'd'


class NatBindIdOrZero(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(0, -1))
	format = 'd'


class NatBindId(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(1, -1))
	format = 'd'


class NatSessionId(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(1, -1))
	format = 'd'


class NatBindMode(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'addressBind'), Enum(2, 'addressPortBind')]


class NatAssociationType(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'static'), Enum(2, 'dynamic')]


class NatTranslationEntity(pycopia.SMI.Basetypes.BITS):
	status = 1
	enumerations = [Enum(0, 'inboundSrcEndPoint'), Enum(1, 'outboundDstEndPoint'), Enum(2, 'inboundDstEndPoint'), Enum(3, 'outboundSrcEndPoint')]

# scalars 
class natBindDefIdleTimeout(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'seconds'


class natUdpDefIdleTimeout(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'seconds'


class natIcmpDefIdleTimeout(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'seconds'


class natOtherDefIdleTimeout(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'seconds'


class natTcpDefIdleTimeout(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'seconds'


class natTcpDefNegTimeout(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'seconds'


class natNotifThrottlingInterval(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 2, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'seconds'


class natAddrBindNumberOfEntries(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class natAddrPortBindNumberOfEntries(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


# columns
class natInterfaceRealm(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'private'), Enum(2, 'public')]


class natInterfaceServiceType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class natInterfaceInTranslates(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class natInterfaceOutTranslates(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class natInterfaceDiscards(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class natInterfaceStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class natInterfaceRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class natAddrMapIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 1])
	syntaxobject = NatAddrMapId


class natAddrMapName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 2])
	syntaxobject = SnmpAdminString


class natAddrMapEntryType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 3])
	syntaxobject = NatAssociationType


class natAddrMapTranslationEntity(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 4])
	syntaxobject = NatTranslationEntity


class natAddrMapLocalAddrType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 5])
	syntaxobject = InetAddressType


class natAddrMapLocalAddrFrom(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 6])
	syntaxobject = InetAddress


class natAddrMapLocalAddrTo(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 7])
	syntaxobject = InetAddress


class natAddrMapLocalPortFrom(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 8])
	syntaxobject = InetPortNumber


class natAddrMapLocalPortTo(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 9])
	syntaxobject = InetPortNumber


class natAddrMapGlobalAddrType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 10])
	syntaxobject = InetAddressType


class natAddrMapGlobalAddrFrom(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 11])
	syntaxobject = InetAddress


class natAddrMapGlobalAddrTo(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 12])
	syntaxobject = InetAddress


class natAddrMapGlobalPortFrom(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 13])
	syntaxobject = InetPortNumber


class natAddrMapGlobalPortTo(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 14])
	syntaxobject = InetPortNumber


class natAddrMapProtocol(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 15])
	syntaxobject = NatProtocolMap


class natAddrMapInTranslates(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class natAddrMapOutTranslates(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class natAddrMapDiscards(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class natAddrMapAddrUsed(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class natAddrMapStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 20])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class natAddrMapRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 21])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class natAddrBindLocalAddrType(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 1])
	syntaxobject = InetAddressType


class natAddrBindLocalAddr(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 2])
	syntaxobject = InetAddress


class natAddrBindGlobalAddrType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 3])
	syntaxobject = InetAddressType


class natAddrBindGlobalAddr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 4])
	syntaxobject = InetAddress


class natAddrBindId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 5])
	syntaxobject = NatBindId


class natAddrBindTranslationEntity(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 6])
	syntaxobject = NatTranslationEntity


class natAddrBindType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 7])
	syntaxobject = NatAssociationType


class natAddrBindMapIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 8])
	syntaxobject = NatAddrMapId


class natAddrBindSessions(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class natAddrBindMaxIdleTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class natAddrBindCurrentIdleTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class natAddrBindInTranslates(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class natAddrBindOutTranslates(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class natAddrPortBindLocalAddrType(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 1])
	syntaxobject = InetAddressType


class natAddrPortBindLocalAddr(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 2])
	syntaxobject = InetAddress


class natAddrPortBindLocalPort(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 3])
	syntaxobject = InetPortNumber


class natAddrPortBindProtocol(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 4])
	syntaxobject = NatProtocolType


class natAddrPortBindGlobalAddrType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 5])
	syntaxobject = InetAddressType


class natAddrPortBindGlobalAddr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 6])
	syntaxobject = InetAddress


class natAddrPortBindGlobalPort(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 7])
	syntaxobject = InetPortNumber


class natAddrPortBindId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 8])
	syntaxobject = NatBindId


class natAddrPortBindTranslationEntity(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 9])
	syntaxobject = NatTranslationEntity


class natAddrPortBindType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 10])
	syntaxobject = NatAssociationType


class natAddrPortBindMapIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 11])
	syntaxobject = NatAddrMapId


class natAddrPortBindSessions(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class natAddrPortBindMaxIdleTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class natAddrPortBindCurrentIdleTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class natAddrPortBindInTranslates(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class natAddrPortBindOutTranslates(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class natSessionIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 1])
	syntaxobject = NatSessionId


class natSessionPrivateSrcEPBindId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 2])
	syntaxobject = NatBindIdOrZero


class natSessionPrivateSrcEPBindMode(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 3])
	syntaxobject = NatBindMode


class natSessionPrivateDstEPBindId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 4])
	syntaxobject = NatBindIdOrZero


class natSessionPrivateDstEPBindMode(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 5])
	syntaxobject = NatBindMode


class natSessionDirection(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'inbound'), Enum(2, 'outbound')]


class natSessionUpTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class natSessionAddrMapIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 8])
	syntaxobject = NatAddrMapId


class natSessionProtocolType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 9])
	syntaxobject = NatProtocolType


class natSessionPrivateAddrType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 10])
	syntaxobject = InetAddressType


class natSessionPrivateSrcAddr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 11])
	syntaxobject = InetAddress


class natSessionPrivateSrcPort(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 12])
	syntaxobject = InetPortNumber


class natSessionPrivateDstAddr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 13])
	syntaxobject = InetAddress


class natSessionPrivateDstPort(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 14])
	syntaxobject = InetPortNumber


class natSessionPublicAddrType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 15])
	syntaxobject = InetAddressType


class natSessionPublicSrcAddr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 16])
	syntaxobject = InetAddress


class natSessionPublicSrcPort(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 17])
	syntaxobject = InetPortNumber


class natSessionPublicDstAddr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 18])
	syntaxobject = InetAddress


class natSessionPublicDstPort(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 19])
	syntaxobject = InetPortNumber


class natSessionMaxIdleTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 20])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class natSessionCurrentIdleTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 21])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class natSessionInTranslates(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 22])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class natSessionOutTranslates(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 23])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class natProtocol(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 10, 1, 1])
	syntaxobject = NatProtocolType


class natProtocolInTranslates(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 10, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class natProtocolOutTranslates(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 10, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class natProtocolDiscards(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 10, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


# rows 
class natInterfaceEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 3, 1])
	access = 2
	rowstatus = natInterfaceRowStatus
	columns = {'natInterfaceRealm': natInterfaceRealm, 'natInterfaceServiceType': natInterfaceServiceType, 'natInterfaceInTranslates': natInterfaceInTranslates, 'natInterfaceOutTranslates': natInterfaceOutTranslates, 'natInterfaceDiscards': natInterfaceDiscards, 'natInterfaceStorageType': natInterfaceStorageType, 'natInterfaceRowStatus': natInterfaceRowStatus}


class natAddrMapEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, natAddrMapIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 4, 1])
	access = 2
	rowstatus = natAddrMapRowStatus
	columns = {'natAddrMapIndex': natAddrMapIndex, 'natAddrMapName': natAddrMapName, 'natAddrMapEntryType': natAddrMapEntryType, 'natAddrMapTranslationEntity': natAddrMapTranslationEntity, 'natAddrMapLocalAddrType': natAddrMapLocalAddrType, 'natAddrMapLocalAddrFrom': natAddrMapLocalAddrFrom, 'natAddrMapLocalAddrTo': natAddrMapLocalAddrTo, 'natAddrMapLocalPortFrom': natAddrMapLocalPortFrom, 'natAddrMapLocalPortTo': natAddrMapLocalPortTo, 'natAddrMapGlobalAddrType': natAddrMapGlobalAddrType, 'natAddrMapGlobalAddrFrom': natAddrMapGlobalAddrFrom, 'natAddrMapGlobalAddrTo': natAddrMapGlobalAddrTo, 'natAddrMapGlobalPortFrom': natAddrMapGlobalPortFrom, 'natAddrMapGlobalPortTo': natAddrMapGlobalPortTo, 'natAddrMapProtocol': natAddrMapProtocol, 'natAddrMapInTranslates': natAddrMapInTranslates, 'natAddrMapOutTranslates': natAddrMapOutTranslates, 'natAddrMapDiscards': natAddrMapDiscards, 'natAddrMapAddrUsed': natAddrMapAddrUsed, 'natAddrMapStorageType': natAddrMapStorageType, 'natAddrMapRowStatus': natAddrMapRowStatus}


class natAddrBindEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, natAddrBindLocalAddrType, natAddrBindLocalAddr], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 6, 1])
	access = 2
	columns = {'natAddrBindLocalAddrType': natAddrBindLocalAddrType, 'natAddrBindLocalAddr': natAddrBindLocalAddr, 'natAddrBindGlobalAddrType': natAddrBindGlobalAddrType, 'natAddrBindGlobalAddr': natAddrBindGlobalAddr, 'natAddrBindId': natAddrBindId, 'natAddrBindTranslationEntity': natAddrBindTranslationEntity, 'natAddrBindType': natAddrBindType, 'natAddrBindMapIndex': natAddrBindMapIndex, 'natAddrBindSessions': natAddrBindSessions, 'natAddrBindMaxIdleTime': natAddrBindMaxIdleTime, 'natAddrBindCurrentIdleTime': natAddrBindCurrentIdleTime, 'natAddrBindInTranslates': natAddrBindInTranslates, 'natAddrBindOutTranslates': natAddrBindOutTranslates}


class natAddrPortBindEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, natAddrPortBindLocalAddrType, natAddrPortBindLocalAddr, natAddrPortBindLocalPort, natAddrPortBindProtocol], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 8, 1])
	access = 2
	columns = {'natAddrPortBindLocalAddrType': natAddrPortBindLocalAddrType, 'natAddrPortBindLocalAddr': natAddrPortBindLocalAddr, 'natAddrPortBindLocalPort': natAddrPortBindLocalPort, 'natAddrPortBindProtocol': natAddrPortBindProtocol, 'natAddrPortBindGlobalAddrType': natAddrPortBindGlobalAddrType, 'natAddrPortBindGlobalAddr': natAddrPortBindGlobalAddr, 'natAddrPortBindGlobalPort': natAddrPortBindGlobalPort, 'natAddrPortBindId': natAddrPortBindId, 'natAddrPortBindTranslationEntity': natAddrPortBindTranslationEntity, 'natAddrPortBindType': natAddrPortBindType, 'natAddrPortBindMapIndex': natAddrPortBindMapIndex, 'natAddrPortBindSessions': natAddrPortBindSessions, 'natAddrPortBindMaxIdleTime': natAddrPortBindMaxIdleTime, 'natAddrPortBindCurrentIdleTime': natAddrPortBindCurrentIdleTime, 'natAddrPortBindInTranslates': natAddrPortBindInTranslates, 'natAddrPortBindOutTranslates': natAddrPortBindOutTranslates}


class natSessionEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, natSessionIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 9, 1])
	access = 2
	columns = {'natSessionIndex': natSessionIndex, 'natSessionPrivateSrcEPBindId': natSessionPrivateSrcEPBindId, 'natSessionPrivateSrcEPBindMode': natSessionPrivateSrcEPBindMode, 'natSessionPrivateDstEPBindId': natSessionPrivateDstEPBindId, 'natSessionPrivateDstEPBindMode': natSessionPrivateDstEPBindMode, 'natSessionDirection': natSessionDirection, 'natSessionUpTime': natSessionUpTime, 'natSessionAddrMapIndex': natSessionAddrMapIndex, 'natSessionProtocolType': natSessionProtocolType, 'natSessionPrivateAddrType': natSessionPrivateAddrType, 'natSessionPrivateSrcAddr': natSessionPrivateSrcAddr, 'natSessionPrivateSrcPort': natSessionPrivateSrcPort, 'natSessionPrivateDstAddr': natSessionPrivateDstAddr, 'natSessionPrivateDstPort': natSessionPrivateDstPort, 'natSessionPublicAddrType': natSessionPublicAddrType, 'natSessionPublicSrcAddr': natSessionPublicSrcAddr, 'natSessionPublicSrcPort': natSessionPublicSrcPort, 'natSessionPublicDstAddr': natSessionPublicDstAddr, 'natSessionPublicDstPort': natSessionPublicDstPort, 'natSessionMaxIdleTime': natSessionMaxIdleTime, 'natSessionCurrentIdleTime': natSessionCurrentIdleTime, 'natSessionInTranslates': natSessionInTranslates, 'natSessionOutTranslates': natSessionOutTranslates}


class natProtocolEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([natProtocol], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 1, 10, 1])
	access = 2
	columns = {'natProtocol': natProtocol, 'natProtocolInTranslates': natProtocolInTranslates, 'natProtocolOutTranslates': natProtocolOutTranslates, 'natProtocolDiscards': natProtocolDiscards}


# notifications (traps) 
class natPacketDiscard(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 0, 1])

# groups 
class natConfigGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 2, 1, 1])
	group = [natInterfaceRealm, natInterfaceServiceType, natInterfaceStorageType, natInterfaceRowStatus, natAddrMapName, natAddrMapEntryType, natAddrMapTranslationEntity, natAddrMapLocalAddrType, natAddrMapLocalAddrFrom, natAddrMapLocalAddrTo, natAddrMapLocalPortFrom, natAddrMapLocalPortTo, natAddrMapGlobalAddrType, natAddrMapGlobalAddrFrom, natAddrMapGlobalAddrTo, natAddrMapGlobalPortFrom, natAddrMapGlobalPortTo, natAddrMapProtocol, natAddrMapStorageType, natAddrMapRowStatus, natBindDefIdleTimeout, natUdpDefIdleTimeout, natIcmpDefIdleTimeout, natOtherDefIdleTimeout, natTcpDefIdleTimeout, natTcpDefNegTimeout, natNotifThrottlingInterval]

class natTranslationGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 2, 1, 2])
	group = [natAddrBindNumberOfEntries, natAddrBindGlobalAddrType, natAddrBindGlobalAddr, natAddrBindId, natAddrBindTranslationEntity, natAddrBindType, natAddrBindMapIndex, natAddrBindSessions, natAddrBindMaxIdleTime, natAddrBindCurrentIdleTime, natAddrBindInTranslates, natAddrBindOutTranslates, natAddrPortBindNumberOfEntries, natAddrPortBindGlobalAddrType, natAddrPortBindGlobalAddr, natAddrPortBindGlobalPort, natAddrPortBindId, natAddrPortBindTranslationEntity, natAddrPortBindType, natAddrPortBindMapIndex, natAddrPortBindSessions, natAddrPortBindMaxIdleTime, natAddrPortBindCurrentIdleTime, natAddrPortBindInTranslates, natAddrPortBindOutTranslates, natSessionPrivateSrcEPBindId, natSessionPrivateSrcEPBindMode, natSessionPrivateDstEPBindId, natSessionPrivateDstEPBindMode, natSessionDirection, natSessionUpTime, natSessionAddrMapIndex, natSessionProtocolType, natSessionPrivateAddrType, natSessionPrivateSrcAddr, natSessionPrivateSrcPort, natSessionPrivateDstAddr, natSessionPrivateDstPort, natSessionPublicAddrType, natSessionPublicSrcAddr, natSessionPublicSrcPort, natSessionPublicDstAddr, natSessionPublicDstPort, natSessionMaxIdleTime, natSessionCurrentIdleTime, natSessionInTranslates, natSessionOutTranslates]

class natStatsInterfaceGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 2, 1, 3])
	group = [natInterfaceInTranslates, natInterfaceOutTranslates, natInterfaceDiscards]

class natStatsProtocolGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 2, 1, 4])
	group = [natProtocolInTranslates, natProtocolOutTranslates, natProtocolDiscards]

class natStatsAddrMapGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 2, 1, 5])
	group = [natAddrMapInTranslates, natAddrMapOutTranslates, natAddrMapDiscards, natAddrMapAddrUsed]

class natMIBNotificationGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 123, 2, 1, 6])
	group = [natPacketDiscard]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
