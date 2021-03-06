# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Counter32, Gauge32, Unsigned32, TimeTicks, mib_2
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from INET_ADDRESS_MIB import InetAddressIPv6
from SNMPv2_TC import RowStatus, TruthValue
from IF_MIB import InterfaceIndex, InterfaceIndexOrZero

class IPV6_MLD_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/IPV6-MLD-MIB'
	conformance = 5
	name = 'IPV6-MLD-MIB'
	language = 2
	description = 'The MIB module for MLD Management.'

# nodes
class mldMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91])
	name = 'mldMIB'

class mldMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1])
	name = 'mldMIBObjects'

class mldMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 2])
	name = 'mldMIBConformance'

class mldMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 2, 1])
	name = 'mldMIBCompliances'

class mldMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 2, 2])
	name = 'mldMIBGroups'


# macros
# types 
# scalars 
# columns
class mldInterfaceIfIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 1])
	syntaxobject = InterfaceIndex


class mldInterfaceQueryInterval(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'seconds'


class mldInterfaceStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class mldInterfaceVersion(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class mldInterfaceQuerier(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 5])
	syntaxobject = InetAddressIPv6


class mldInterfaceQueryMaxResponseDelay(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'seconds'


class mldInterfaceJoins(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mldInterfaceGroups(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class mldInterfaceRobustness(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class mldInterfaceLastListenQueryIntvl(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'seconds'


class mldInterfaceProxyIfIndex(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 11])
	syntaxobject = InterfaceIndexOrZero


class mldInterfaceQuerierUpTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class mldInterfaceQuerierExpiryTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class mldCacheAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 1])
	syntaxobject = InetAddressIPv6


class mldCacheIfIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 2])
	syntaxobject = InterfaceIndex


class mldCacheSelf(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class mldCacheLastReporter(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 4])
	syntaxobject = InetAddressIPv6


class mldCacheUpTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class mldCacheExpiryTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class mldCacheStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


# rows 
class mldInterfaceEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mldInterfaceIfIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 1, 1])
	access = 2
	rowstatus = mldInterfaceStatus
	columns = {'mldInterfaceIfIndex': mldInterfaceIfIndex, 'mldInterfaceQueryInterval': mldInterfaceQueryInterval, 'mldInterfaceStatus': mldInterfaceStatus, 'mldInterfaceVersion': mldInterfaceVersion, 'mldInterfaceQuerier': mldInterfaceQuerier, 'mldInterfaceQueryMaxResponseDelay': mldInterfaceQueryMaxResponseDelay, 'mldInterfaceJoins': mldInterfaceJoins, 'mldInterfaceGroups': mldInterfaceGroups, 'mldInterfaceRobustness': mldInterfaceRobustness, 'mldInterfaceLastListenQueryIntvl': mldInterfaceLastListenQueryIntvl, 'mldInterfaceProxyIfIndex': mldInterfaceProxyIfIndex, 'mldInterfaceQuerierUpTime': mldInterfaceQuerierUpTime, 'mldInterfaceQuerierExpiryTime': mldInterfaceQuerierExpiryTime}


class mldCacheEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mldCacheAddress, mldCacheIfIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 1, 2, 1])
	access = 2
	rowstatus = mldCacheStatus
	columns = {'mldCacheAddress': mldCacheAddress, 'mldCacheIfIndex': mldCacheIfIndex, 'mldCacheSelf': mldCacheSelf, 'mldCacheLastReporter': mldCacheLastReporter, 'mldCacheUpTime': mldCacheUpTime, 'mldCacheExpiryTime': mldCacheExpiryTime, 'mldCacheStatus': mldCacheStatus}


# notifications (traps) 
# groups 
class mldBaseMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 2, 2, 1])
	group = [mldCacheSelf, mldCacheStatus, mldInterfaceStatus]

class mldRouterMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 2, 2, 2])
	group = [mldCacheUpTime, mldCacheExpiryTime, mldInterfaceQueryInterval, mldInterfaceJoins, mldInterfaceGroups, mldCacheLastReporter, mldInterfaceQuerierUpTime, mldInterfaceQuerierExpiryTime, mldInterfaceQuerier, mldInterfaceVersion, mldInterfaceQueryMaxResponseDelay, mldInterfaceRobustness, mldInterfaceLastListenQueryIntvl]

class mldHostMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 2, 2, 3])
	group = [mldInterfaceQuerier]

class mldProxyMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 91, 2, 2, 4])
	group = [mldInterfaceProxyIfIndex]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
