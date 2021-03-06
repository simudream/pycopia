# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from RFC1155_SMI import mgmt, OBJECT_TYPE, NetworkAddress, IpAddress, Counter, Gauge, TimeTicks

class RFC1158_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/RFC1158-MIB'
	conformance = 2
	name = 'RFC1158-MIB'
	language = 1

# nodes
class nullSpecific(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([0, 0])
	name = 'nullSpecific'

class mib_2(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1])
	name = 'mib-2'

class system(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1])
	name = 'system'

class interfaces(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2])
	name = 'interfaces'

class at(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 3])
	name = 'at'

class ip(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4])
	name = 'ip'

class icmp(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5])
	name = 'icmp'

class tcp(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6])
	name = 'tcp'

class udp(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 7])
	name = 'udp'

class egp(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8])
	name = 'egp'

class transmission(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10])
	name = 'transmission'

class snmp(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11])
	name = 'snmp'


# macros
# types 
DisplayString = pycopia.SMI.Basetypes.DisplayString
# scalars 
class sysDescr(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class sysObjectID(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class sysUpTime(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class sysContact(ScalarObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class sysName(ScalarObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class sysLocation(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class sysServices(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ifNumber(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ifIndex(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ifDescr(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class ifType(ScalarObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'regular1822'), Enum(3, 'hdh1822'), Enum(4, 'ddn-x25'), Enum(5, 'rfc877-x25'), Enum(6, 'ethernet-csmacd'), Enum(7, 'iso88023-csmacd'), Enum(8, 'iso88024-tokenBus'), Enum(9, 'iso88025-tokenRing'), Enum(10, 'iso88026-man'), Enum(11, 'starLan'), Enum(12, 'proteon-10Mbit'), Enum(13, 'proteon-80Mbit'), Enum(14, 'hyperchannel'), Enum(15, 'fddi'), Enum(16, 'lapb'), Enum(17, 'sdlc'), Enum(18, 't1-carrier'), Enum(19, 'cept'), Enum(20, 'basicISDN'), Enum(21, 'primaryISDN'), Enum(22, 'propPointToPointSerial'), Enum(23, 'terminalServer-asyncPort'), Enum(24, 'softwareLoopback'), Enum(25, 'eon'), Enum(26, 'ethernet-3Mbit'), Enum(27, 'nsip'), Enum(28, 'slip')]


class ifMtu(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ifSpeed(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class ifPhysAddress(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class ifAdminStatus(ScalarObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'up'), Enum(2, 'down'), Enum(3, 'testing')]


class ifOperStatus(ScalarObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'up'), Enum(2, 'down'), Enum(3, 'testing')]


class ifLastChange(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class ifInOctets(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ifInUcastPkts(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ifInNUcastPkts(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ifInDiscards(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ifInErrors(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ifInUnknownProtos(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ifOutOctets(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ifOutUcastPkts(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ifOutNUcastPkts(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ifOutDiscards(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ifOutErrors(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 20])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ifOutQLen(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 21])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class ifSpecific(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1, 22])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class ipForwarding(ScalarObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'gateway'), Enum(2, 'host')]


class ipDefaultTTL(ScalarObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ipInReceives(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipInHdrErrors(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipInAddrErrors(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipForwDatagrams(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipInUnknownProtos(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipInDiscards(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipInDelivers(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipOutRequests(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipOutDiscards(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipOutNoRoutes(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipReasmTimeout(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 13])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ipReasmReqds(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipReasmOKs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipReasmFails(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipFragOKs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipFragFails(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipFragCreates(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 19])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipAdEntAddr(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 20, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class ipAdEntIfIndex(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 20, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ipAdEntNetMask(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 20, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class ipAdEntBcastAddr(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 20, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ipAdEntReasmMaxSize(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 20, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ipRouteDest(ScalarObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 21, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class ipRouteIfIndex(ScalarObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 21, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ipRouteMetric1(ScalarObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 21, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ipRouteMetric2(ScalarObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 21, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ipRouteMetric3(ScalarObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 21, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ipRouteMetric4(ScalarObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 21, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ipRouteNextHop(ScalarObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 21, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class ipRouteType(ScalarObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 21, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'invalid'), Enum(3, 'direct'), Enum(4, 'remote')]


class ipRouteProto(ScalarObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 21, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'local'), Enum(3, 'netmgmt'), Enum(4, 'icmp'), Enum(5, 'egp'), Enum(6, 'ggp'), Enum(7, 'hello'), Enum(8, 'rip'), Enum(9, 'is-is'), Enum(10, 'es-is'), Enum(11, 'ciscoIgrp'), Enum(12, 'bbnSpfIgp'), Enum(13, 'ospf'), Enum(14, 'bgp')]


class ipRouteAge(ScalarObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 21, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ipRouteMask(ScalarObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 21, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class ipNetToMediaIfIndex(ScalarObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 22, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ipNetToMediaPhysAddress(ScalarObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 22, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class ipNetToMediaNetAddress(ScalarObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 22, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class ipNetToMediaType(ScalarObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 22, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'invalid'), Enum(3, 'dynamic'), Enum(4, 'static')]


class icmpInMsgs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpInErrors(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpInDestUnreachs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpInTimeExcds(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpInParmProbs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpInSrcQuenchs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpInRedirects(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpInEchos(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpInEchoReps(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpInTimestamps(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpInTimestampReps(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpInAddrMasks(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpInAddrMaskReps(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpOutMsgs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpOutErrors(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpOutDestUnreachs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpOutTimeExcds(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpOutParmProbs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpOutSrcQuenchs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 19])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpOutRedirects(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 20])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpOutEchos(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 21])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpOutEchoReps(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 22])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpOutTimestamps(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 23])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpOutTimestampReps(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 24])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpOutAddrMasks(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 25])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class icmpOutAddrMaskReps(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 5, 26])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class tcpRtoAlgorithm(ScalarObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'constant'), Enum(3, 'rsre'), Enum(4, 'vanj')]


class tcpRtoMin(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class tcpRtoMax(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class tcpMaxConn(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class tcpActiveOpens(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class tcpPassiveOpens(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class tcpAttemptFails(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class tcpEstabResets(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class tcpCurrEstab(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6, 9])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class tcpInSegs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class tcpOutSegs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class tcpRetransSegs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class tcpConnState(ScalarObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6, 13, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'closed'), Enum(2, 'listen'), Enum(3, 'synSent'), Enum(4, 'synReceived'), Enum(5, 'established'), Enum(6, 'finWait1'), Enum(7, 'finWait2'), Enum(8, 'closeWait'), Enum(9, 'lastAck'), Enum(10, 'closing'), Enum(11, 'timeWait')]


class tcpConnLocalAddress(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6, 13, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class tcpConnLocalPort(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6, 13, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class tcpConnRemAddress(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6, 13, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class tcpConnRemPort(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6, 13, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class tcpInErrs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class tcpOutRsts(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class udpInDatagrams(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 7, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class udpNoPorts(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 7, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class udpInErrors(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 7, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class udpOutDatagrams(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 7, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class udpLocalAddress(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 7, 5, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class udpLocalPort(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 7, 5, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class egpInMsgs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class egpInErrors(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class egpOutMsgs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class egpOutErrors(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class egpNeighState(ScalarObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 5, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'idle'), Enum(2, 'acquisition'), Enum(3, 'down'), Enum(4, 'up'), Enum(5, 'cease')]


class egpNeighAddr(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 5, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class egpNeighAs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 5, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class egpNeighInMsgs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 5, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class egpNeighInErrs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 5, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class egpNeighOutMsgs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 5, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class egpNeighOutErrs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 5, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class egpNeighInErrMsgs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 5, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class egpNeighOutErrMsgs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 5, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class egpNeighStateUps(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 5, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class egpNeighStateDowns(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 5, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class egpNeighIntervalHello(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 5, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class egpNeighIntervalPoll(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 5, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class egpNeighMode(ScalarObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 5, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'active'), Enum(2, 'passive')]


class egpNeighEventTrigger(ScalarObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 5, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'start'), Enum(2, 'stop')]


class egpAs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snmpInPkts(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpOutPkts(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInBadVersions(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInBadCommunityNames(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInBadCommunityUses(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInASNParseErrs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInBadTypes(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInTooBigs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInNoSuchNames(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInBadValues(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInReadOnlys(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInGenErrs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInTotalReqVars(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInTotalSetVars(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInGetRequests(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInGetNexts(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInSetRequests(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInGetResponses(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInTraps(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 19])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpOutTooBigs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 20])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpOutNoSuchNames(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 21])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpOutBadValues(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 22])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpOutReadOnlys(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 23])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpOutGenErrs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 24])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpOutGetRequests(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 25])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpOutGetNexts(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 26])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpOutSetRequests(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 27])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpOutGetResponses(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 28])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpOutTraps(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 29])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpEnableAuthTraps(ScalarObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 30])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled')]


# columns
# rows 
class ifEntry(RowObject):
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 2, 2, 1])
	access = 4
	columns = {}


class ipAddrEntry(RowObject):
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 20, 1])
	access = 4
	columns = {}


class ipRouteEntry(RowObject):
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 21, 1])
	access = 5
	columns = {}


class ipNetToMediaEntry(RowObject):
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 4, 22, 1])
	access = 5
	columns = {}


class tcpConnEntry(RowObject):
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 6, 13, 1])
	access = 4
	columns = {}


class udpEntry(RowObject):
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 7, 5, 1])
	access = 4
	columns = {}


class egpNeighEntry(RowObject):
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 8, 5, 1])
	access = 4
	columns = {}


# notifications (traps) 
# groups 
# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
