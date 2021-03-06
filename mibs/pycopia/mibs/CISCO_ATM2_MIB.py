# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Counter32
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_SMI import ciscoExperiment
from IF_MIB import ifIndex
from ATM_MIB import atmInterfaceConfEntry

class CISCO_ATM2_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-ATM2-MIB'
	conformance = 5
	name = 'CISCO-ATM2-MIB'
	language = 2
	description = 'This MIB Module is a supplement to the\nATM-MIB [1]. It is an adaptation of a \n\tportion of the ATOMMIB supplemental MIB.'

# nodes
class ciscoAtm2MIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23])
	name = 'ciscoAtm2MIB'

class ciscoatm2MIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1])
	name = 'ciscoatm2MIBObjects'

class ciscoatm2MIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 3])
	name = 'ciscoatm2MIBConformance'

class ciscoatm2MIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 3, 1])
	name = 'ciscoatm2MIBGroups'

class ciscoatm2MIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 3, 2])
	name = 'ciscoatm2MIBCompliances'


# macros
# types 
# scalars 
# columns
class ciscoatmSigSSCOPConEvents(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoatmSigSSCOPErrdPdus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoatmSigDetectSetupAttempts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoatmSigEmitSetupAttempts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoatmSigDetectUnavailRoutes(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoatmSigEmitUnavailRoutes(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoatmSigDetectUnavailResrcs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoatmSigEmitUnavailResrcs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoatmSigDetectCldPtyEvents(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoatmSigEmitCldPtyEvents(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoatmSigDetectMsgErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoatmSigEmitMsgErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoatmSigDetectClgPtyEvents(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoatmSigEmitClgPtyEvents(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoatmSigDetectTimerExpireds(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoatmSigEmitTimerExpireds(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 20])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoatmSigDetectRestarts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 21])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoatmSigEmitRestarts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 22])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoatmSigInEstabls(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 23])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoatmSigOutEstabls(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 24])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ciscoatmSigSupportClgPtyNumDel(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled')]


class ciscoatmSigSupportClgPtySubAddr(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled')]


class ciscoatmSigSupportCldPtySubAddr(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled')]


class ciscoatmSigSupportHiLyrInfo(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled')]


class ciscoatmSigSupportLoLyrInfo(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled')]


class ciscoatmSigSupportBlliRepeatInd(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled')]


class ciscoatmSigSupportAALInfo(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled')]


class ciscoatmSigSupportUnknownIe(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled')]


class ciscoatmInterfaceConfMaxSvpcVpi(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 3, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ciscoatmInterfaceCurrentMaxSvpcVpi(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 3, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ciscoatmInterfaceConfMaxSvccVpi(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 3, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ciscoatmInterfaceCurrentMaxSvccVpi(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 3, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ciscoatmInterfaceConfMinSvccVci(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 3, 1, 20])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ciscoatmInterfaceCurrentMinSvccVci(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 3, 1, 21])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# rows 
class ciscoatmSigStatEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1])
	access = 2
	columns = {'ciscoatmSigSSCOPConEvents': ciscoatmSigSSCOPConEvents, 'ciscoatmSigSSCOPErrdPdus': ciscoatmSigSSCOPErrdPdus, 'ciscoatmSigDetectSetupAttempts': ciscoatmSigDetectSetupAttempts, 'ciscoatmSigEmitSetupAttempts': ciscoatmSigEmitSetupAttempts, 'ciscoatmSigDetectUnavailRoutes': ciscoatmSigDetectUnavailRoutes, 'ciscoatmSigEmitUnavailRoutes': ciscoatmSigEmitUnavailRoutes, 'ciscoatmSigDetectUnavailResrcs': ciscoatmSigDetectUnavailResrcs, 'ciscoatmSigEmitUnavailResrcs': ciscoatmSigEmitUnavailResrcs, 'ciscoatmSigDetectCldPtyEvents': ciscoatmSigDetectCldPtyEvents, 'ciscoatmSigEmitCldPtyEvents': ciscoatmSigEmitCldPtyEvents, 'ciscoatmSigDetectMsgErrors': ciscoatmSigDetectMsgErrors, 'ciscoatmSigEmitMsgErrors': ciscoatmSigEmitMsgErrors, 'ciscoatmSigDetectClgPtyEvents': ciscoatmSigDetectClgPtyEvents, 'ciscoatmSigEmitClgPtyEvents': ciscoatmSigEmitClgPtyEvents, 'ciscoatmSigDetectTimerExpireds': ciscoatmSigDetectTimerExpireds, 'ciscoatmSigEmitTimerExpireds': ciscoatmSigEmitTimerExpireds, 'ciscoatmSigDetectRestarts': ciscoatmSigDetectRestarts, 'ciscoatmSigEmitRestarts': ciscoatmSigEmitRestarts, 'ciscoatmSigInEstabls': ciscoatmSigInEstabls, 'ciscoatmSigOutEstabls': ciscoatmSigOutEstabls}


class ciscoatmSigSupportEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 2, 1])
	access = 2
	columns = {'ciscoatmSigSupportClgPtyNumDel': ciscoatmSigSupportClgPtyNumDel, 'ciscoatmSigSupportClgPtySubAddr': ciscoatmSigSupportClgPtySubAddr, 'ciscoatmSigSupportCldPtySubAddr': ciscoatmSigSupportCldPtySubAddr, 'ciscoatmSigSupportHiLyrInfo': ciscoatmSigSupportHiLyrInfo, 'ciscoatmSigSupportLoLyrInfo': ciscoatmSigSupportLoLyrInfo, 'ciscoatmSigSupportBlliRepeatInd': ciscoatmSigSupportBlliRepeatInd, 'ciscoatmSigSupportAALInfo': ciscoatmSigSupportAALInfo, 'ciscoatmSigSupportUnknownIe': ciscoatmSigSupportUnknownIe}


from IF_MIB import ifIndex
class ciscoatmInterfaceExtEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 3, 1])
	access = 2
	columns = {'ciscoatmInterfaceConfMaxSvpcVpi': ciscoatmInterfaceConfMaxSvpcVpi, 'ciscoatmInterfaceCurrentMaxSvpcVpi': ciscoatmInterfaceCurrentMaxSvpcVpi, 'ciscoatmInterfaceConfMaxSvccVpi': ciscoatmInterfaceConfMaxSvccVpi, 'ciscoatmInterfaceCurrentMaxSvccVpi': ciscoatmInterfaceCurrentMaxSvccVpi, 'ciscoatmInterfaceConfMinSvccVci': ciscoatmInterfaceConfMinSvccVci, 'ciscoatmInterfaceCurrentMinSvccVci': ciscoatmInterfaceCurrentMinSvccVci}


# notifications (traps) 
# groups 
class ciscoAtmSwitchServcHostGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 3, 1, 1])
	group = [ciscoatmSigSSCOPConEvents, ciscoatmSigSSCOPErrdPdus, ciscoatmSigDetectSetupAttempts, ciscoatmSigEmitSetupAttempts, ciscoatmSigDetectUnavailRoutes, ciscoatmSigEmitUnavailRoutes, ciscoatmSigDetectUnavailResrcs, ciscoatmSigEmitUnavailResrcs, ciscoatmSigDetectCldPtyEvents, ciscoatmSigEmitCldPtyEvents, ciscoatmSigDetectMsgErrors, ciscoatmSigEmitMsgErrors, ciscoatmSigDetectClgPtyEvents, ciscoatmSigEmitClgPtyEvents, ciscoatmSigDetectTimerExpireds, ciscoatmSigEmitTimerExpireds, ciscoatmSigDetectRestarts, ciscoatmSigEmitRestarts, ciscoatmSigInEstabls, ciscoatmSigOutEstabls]

class ciscoAtmSwitchServcGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 3, 1, 3])
	group = [ciscoatmSigSupportClgPtyNumDel, ciscoatmSigSupportClgPtySubAddr, ciscoatmSigSupportCldPtySubAddr, ciscoatmSigSupportHiLyrInfo, ciscoatmSigSupportLoLyrInfo, ciscoatmSigSupportBlliRepeatInd, ciscoatmSigSupportAALInfo, ciscoatmSigSupportUnknownIe]

class ciscoAtmSwitchServcHostGroup2(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 23, 3, 1, 4])
	group = [ciscoatmInterfaceConfMaxSvpcVpi, ciscoatmInterfaceCurrentMaxSvpcVpi, ciscoatmInterfaceConfMaxSvccVpi, ciscoatmInterfaceCurrentMaxSvccVpi, ciscoatmInterfaceConfMinSvccVci, ciscoatmInterfaceCurrentMinSvccVci]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
