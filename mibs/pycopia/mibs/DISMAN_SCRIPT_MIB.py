# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, Integer32, Unsigned32, mib_2
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP, NOTIFICATION_GROUP
from SNMPv2_TC import RowStatus, TimeInterval, DateAndTime, StorageType, DisplayString
from SNMP_FRAMEWORK_MIB import SnmpAdminString

class DISMAN_SCRIPT_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/DISMAN-SCRIPT-MIB'
	conformance = 5
	name = 'DISMAN-SCRIPT-MIB'
	language = 2
	description = 'This MIB module defines a set of objects that allow to\ndelegate management scripts to distributed managers.'

# nodes
class scriptMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64])
	name = 'scriptMIB'

class smObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1])
	name = 'smObjects'

class smScriptObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 3])
	name = 'smScriptObjects'

class smRunObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4])
	name = 'smRunObjects'

class smNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 2])
	name = 'smNotifications'

class smTraps(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 2, 0])
	name = 'smTraps'

class smConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 3])
	name = 'smConformance'

class smCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 3, 1])
	name = 'smCompliances'

class smGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 3, 2])
	name = 'smGroups'


# macros
# types 
# scalars 
# columns
class smLangIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class smLangLanguage(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class smLangVersion(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 3])
	syntaxobject = SnmpAdminString


class smLangVendor(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class smLangRevision(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 5])
	syntaxobject = SnmpAdminString


class smLangDescr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 6])
	syntaxobject = SnmpAdminString


class smExtsnIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class smExtsnExtension(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class smExtsnVersion(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 3])
	syntaxobject = SnmpAdminString


class smExtsnVendor(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class smExtsnRevision(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 5])
	syntaxobject = SnmpAdminString


class smExtsnDescr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 6])
	syntaxobject = SnmpAdminString


class smScriptOwner(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 1])
	syntaxobject = SnmpAdminString


class smScriptName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 2])
	syntaxobject = SnmpAdminString


class smScriptDescr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 3])
	syntaxobject = SnmpAdminString


class smScriptLanguage(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class smScriptSource(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class smScriptAdminStatus(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled'), Enum(3, 'editing')]


class smScriptOperStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled'), Enum(3, 'editing'), Enum(4, 'retrieving'), Enum(5, 'compiling'), Enum(6, 'noSuchScript'), Enum(7, 'accessDenied'), Enum(8, 'wrongLanguage'), Enum(9, 'wrongVersion'), Enum(10, 'compilationFailed'), Enum(11, 'noResourcesLeft'), Enum(12, 'unknownProtocol'), Enum(13, 'protocolFailure'), Enum(14, 'genericError')]


class smScriptStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class smScriptRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class smScriptError(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 10])
	syntaxobject = SnmpAdminString


class smScriptLastChange(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.DateAndTime


class smCodeIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 3, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class smCodeText(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 3, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class smCodeRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 3, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class smLaunchOwner(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 1])
	syntaxobject = SnmpAdminString


class smLaunchName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 2])
	syntaxobject = SnmpAdminString


class smLaunchScriptOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 3])
	syntaxobject = SnmpAdminString


class smLaunchScriptName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 4])
	syntaxobject = SnmpAdminString


class smLaunchArgument(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class smLaunchMaxRunning(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class smLaunchMaxCompleted(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class smLaunchLifeTime(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval
	access = 5
	units = 'centi-seconds'


class smLaunchExpireTime(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval
	access = 5
	units = 'centi-seconds'


class smLaunchStart(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class smLaunchControl(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'abort'), Enum(2, 'suspend'), Enum(3, 'resume'), Enum(4, 'nop')]


class smLaunchAdminStatus(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled'), Enum(3, 'autostart')]


class smLaunchOperStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled'), Enum(3, 'expired')]


class smLaunchRunIndexNext(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class smLaunchStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class smLaunchRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class smLaunchError(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 17])
	syntaxobject = SnmpAdminString


class smLaunchLastChange(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.DateAndTime


class smLaunchRowExpireTime(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval
	access = 5
	units = 'centi-seconds'


class smRunIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class smRunArgument(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class smRunStartTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DateAndTime


class smRunEndTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DateAndTime


class smRunLifeTime(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval
	access = 5
	units = 'centi-seconds'


class smRunExpireTime(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval
	access = 5
	units = 'centi-seconds'


class smRunExitCode(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'noError'), Enum(2, 'halted'), Enum(3, 'lifeTimeExceeded'), Enum(4, 'noResourcesLeft'), Enum(5, 'languageError'), Enum(6, 'runtimeError'), Enum(7, 'invalidArgument'), Enum(8, 'securityViolation'), Enum(9, 'genericError')]


class smRunResult(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class smRunControl(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'abort'), Enum(2, 'suspend'), Enum(3, 'resume'), Enum(4, 'nop')]


class smRunState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'initializing'), Enum(2, 'executing'), Enum(3, 'suspending'), Enum(4, 'suspended'), Enum(5, 'resuming'), Enum(6, 'aborting'), Enum(7, 'terminated')]


class smRunError(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 11])
	syntaxobject = SnmpAdminString


class smRunResultTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.DateAndTime


class smRunErrorTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.DateAndTime


# rows 
class smLangEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([smLangIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 1, 1])
	access = 2
	columns = {'smLangIndex': smLangIndex, 'smLangLanguage': smLangLanguage, 'smLangVersion': smLangVersion, 'smLangVendor': smLangVendor, 'smLangRevision': smLangRevision, 'smLangDescr': smLangDescr}


class smExtsnEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([smLangIndex, smExtsnIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 2, 1])
	access = 2
	columns = {'smExtsnIndex': smExtsnIndex, 'smExtsnExtension': smExtsnExtension, 'smExtsnVersion': smExtsnVersion, 'smExtsnVendor': smExtsnVendor, 'smExtsnRevision': smExtsnRevision, 'smExtsnDescr': smExtsnDescr}


class smScriptEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([smScriptOwner, smScriptName], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1])
	access = 2
	rowstatus = smScriptRowStatus
	columns = {'smScriptOwner': smScriptOwner, 'smScriptName': smScriptName, 'smScriptDescr': smScriptDescr, 'smScriptLanguage': smScriptLanguage, 'smScriptSource': smScriptSource, 'smScriptAdminStatus': smScriptAdminStatus, 'smScriptOperStatus': smScriptOperStatus, 'smScriptStorageType': smScriptStorageType, 'smScriptRowStatus': smScriptRowStatus, 'smScriptError': smScriptError, 'smScriptLastChange': smScriptLastChange}


class smCodeEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([smScriptOwner, smScriptName, smCodeIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 3, 2, 1])
	access = 2
	rowstatus = smCodeRowStatus
	columns = {'smCodeIndex': smCodeIndex, 'smCodeText': smCodeText, 'smCodeRowStatus': smCodeRowStatus}


class smLaunchEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([smLaunchOwner, smLaunchName], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1])
	access = 2
	rowstatus = smLaunchRowStatus
	columns = {'smLaunchOwner': smLaunchOwner, 'smLaunchName': smLaunchName, 'smLaunchScriptOwner': smLaunchScriptOwner, 'smLaunchScriptName': smLaunchScriptName, 'smLaunchArgument': smLaunchArgument, 'smLaunchMaxRunning': smLaunchMaxRunning, 'smLaunchMaxCompleted': smLaunchMaxCompleted, 'smLaunchLifeTime': smLaunchLifeTime, 'smLaunchExpireTime': smLaunchExpireTime, 'smLaunchStart': smLaunchStart, 'smLaunchControl': smLaunchControl, 'smLaunchAdminStatus': smLaunchAdminStatus, 'smLaunchOperStatus': smLaunchOperStatus, 'smLaunchRunIndexNext': smLaunchRunIndexNext, 'smLaunchStorageType': smLaunchStorageType, 'smLaunchRowStatus': smLaunchRowStatus, 'smLaunchError': smLaunchError, 'smLaunchLastChange': smLaunchLastChange, 'smLaunchRowExpireTime': smLaunchRowExpireTime}


class smRunEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([smLaunchOwner, smLaunchName, smRunIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1])
	access = 2
	columns = {'smRunIndex': smRunIndex, 'smRunArgument': smRunArgument, 'smRunStartTime': smRunStartTime, 'smRunEndTime': smRunEndTime, 'smRunLifeTime': smRunLifeTime, 'smRunExpireTime': smRunExpireTime, 'smRunExitCode': smRunExitCode, 'smRunResult': smRunResult, 'smRunControl': smRunControl, 'smRunState': smRunState, 'smRunError': smRunError, 'smRunResultTime': smRunResultTime, 'smRunErrorTime': smRunErrorTime}


# notifications (traps) 
class smScriptAbort(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 2, 0, 1])

class smScriptResult(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 2, 0, 2])

class smScriptException(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 2, 0, 3])

# groups 
class smLanguageGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 3, 2, 1])
	group = [smLangLanguage, smLangVersion, smLangVendor, smLangRevision, smLangDescr, smExtsnExtension, smExtsnVersion, smExtsnVendor, smExtsnRevision, smExtsnDescr]

class smScriptGroup(GroupObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 3, 2, 2])
	group = [smScriptDescr, smScriptLanguage, smScriptSource, smScriptAdminStatus, smScriptOperStatus, smScriptStorageType, smScriptRowStatus]

class smCodeGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 3, 2, 3])
	group = [smCodeText, smCodeRowStatus]

class smLaunchGroup(GroupObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 3, 2, 4])
	group = [smLaunchScriptOwner, smLaunchScriptName, smLaunchArgument, smLaunchMaxRunning, smLaunchMaxCompleted, smLaunchLifeTime, smLaunchExpireTime, smLaunchStart, smLaunchControl, smLaunchAdminStatus, smLaunchOperStatus, smLaunchRunIndexNext, smLaunchStorageType, smLaunchRowStatus]

class smRunGroup(GroupObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 3, 2, 5])
	group = [smRunArgument, smRunStartTime, smRunEndTime, smRunLifeTime, smRunExpireTime, smRunExitCode, smRunResult, smRunState, smRunControl, smRunError]

class smNotificationsGroup(GroupObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 3, 2, 6])
	group = [smScriptAbort, smScriptResult]

class smScriptGroup2(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 3, 2, 7])
	group = [smScriptDescr, smScriptLanguage, smScriptSource, smScriptAdminStatus, smScriptOperStatus, smScriptStorageType, smScriptRowStatus, smScriptError, smScriptLastChange]

class smLaunchGroup2(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 3, 2, 8])
	group = [smLaunchScriptOwner, smLaunchScriptName, smLaunchArgument, smLaunchMaxRunning, smLaunchMaxCompleted, smLaunchLifeTime, smLaunchExpireTime, smLaunchStart, smLaunchControl, smLaunchAdminStatus, smLaunchOperStatus, smLaunchRunIndexNext, smLaunchStorageType, smLaunchRowStatus, smLaunchError, smLaunchLastChange, smLaunchRowExpireTime]

class smRunGroup2(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 3, 2, 9])
	group = [smRunArgument, smRunStartTime, smRunEndTime, smRunLifeTime, smRunExpireTime, smRunExitCode, smRunResult, smRunState, smRunControl, smRunError, smRunResultTime, smRunErrorTime]

class smNotificationsGroup2(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 64, 3, 2, 10])
	group = [smScriptAbort, smScriptResult, smScriptException]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
