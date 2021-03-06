# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, Unsigned32, Integer32, transmission
from SNMPv2_TC import TEXTUAL_CONVENTION

class MPLS_TC_STD_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/MPLS-TC-STD-MIB'
	conformance = 4
	name = 'MPLS-TC-STD-MIB'
	language = 2
	description = 'Copyright (C) The Internet Society (2004). The\ninitial version of this MIB module was published\nin RFC 3811. For full legal notices see the RFC\nitself or see:\nhttp://www.ietf.org/copyrights/ianamib.html\n\nThis MIB module defines TEXTUAL-CONVENTIONs\nfor concepts used in Multiprotocol Label\nSwitching (MPLS) networks.'

# nodes
class mplsStdMIB(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166])
	name = 'mplsStdMIB'

class mplsTCStdMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 1])
	name = 'mplsTCStdMIB'


# macros
# types 

class MplsAtmVcIdentifier(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(32, 65535))
	format = 'd'


class MplsBitRate(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(0, -1))
	format = 'd'


class MplsBurstSize(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(0, -1))
	format = 'd'


class MplsExtendedTunnelId(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(0, -1))


class MplsLabel(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(0, -1))


class MplsLabelDistributionMethod(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'downstreamOnDemand'), Enum(2, 'downstreamUnsolicited')]


class MplsLdpIdentifier(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(6, 6))
	format = '1d.1d.1d.1d:2d'


class MplsLsrIdentifier(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(4, 4))


class MplsLdpLabelType(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'generic'), Enum(2, 'atm'), Enum(3, 'frameRelay')]


class MplsLSPID(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(2, 2), Range(6, 6))


class MplsLspType(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'unknown'), Enum(2, 'terminatingLsp'), Enum(3, 'originatingLsp'), Enum(4, 'crossConnectingLsp')]


class MplsOwner(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'unknown'), Enum(2, 'other'), Enum(3, 'snmp'), Enum(4, 'ldp'), Enum(5, 'crldp'), Enum(6, 'rsvpTe'), Enum(7, 'policyAgent')]


class MplsPathIndexOrZero(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(0, -1))


class MplsPathIndex(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(1, -1))


class MplsRetentionMode(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'conservative'), Enum(2, 'liberal')]


class MplsTunnelAffinity(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(0, -1))


class MplsTunnelIndex(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(0, 65535))


class MplsTunnelInstanceIndex(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(0, -1))


class TeHopAddressType(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(0, 'unknown'), Enum(1, 'ipv4'), Enum(2, 'ipv6'), Enum(3, 'asnumber'), Enum(4, 'unnum'), Enum(5, 'lspid')]


class TeHopAddress(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 32))


class TeHopAddressAS(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(4, 4))


class TeHopAddressUnnum(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(4, 4))

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
