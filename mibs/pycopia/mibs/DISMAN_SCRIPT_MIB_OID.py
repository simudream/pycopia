# python
# This file is generated by a program (mib2py). 

import DISMAN_SCRIPT_MIB

OIDMAP = {
'1.3.6.1.2.1.64': DISMAN_SCRIPT_MIB.scriptMIB,
'1.3.6.1.2.1.64.1': DISMAN_SCRIPT_MIB.smObjects,
'1.3.6.1.2.1.64.1.3': DISMAN_SCRIPT_MIB.smScriptObjects,
'1.3.6.1.2.1.64.1.4': DISMAN_SCRIPT_MIB.smRunObjects,
'1.3.6.1.2.1.64.2': DISMAN_SCRIPT_MIB.smNotifications,
'1.3.6.1.2.1.64.2.0': DISMAN_SCRIPT_MIB.smTraps,
'1.3.6.1.2.1.64.3': DISMAN_SCRIPT_MIB.smConformance,
'1.3.6.1.2.1.64.3.1': DISMAN_SCRIPT_MIB.smCompliances,
'1.3.6.1.2.1.64.3.2': DISMAN_SCRIPT_MIB.smGroups,
'1.3.6.1.2.1.64.1.1.1.1': DISMAN_SCRIPT_MIB.smLangIndex,
'1.3.6.1.2.1.64.1.1.1.2': DISMAN_SCRIPT_MIB.smLangLanguage,
'1.3.6.1.2.1.64.1.1.1.3': DISMAN_SCRIPT_MIB.smLangVersion,
'1.3.6.1.2.1.64.1.1.1.4': DISMAN_SCRIPT_MIB.smLangVendor,
'1.3.6.1.2.1.64.1.1.1.5': DISMAN_SCRIPT_MIB.smLangRevision,
'1.3.6.1.2.1.64.1.1.1.6': DISMAN_SCRIPT_MIB.smLangDescr,
'1.3.6.1.2.1.64.1.2.1.1': DISMAN_SCRIPT_MIB.smExtsnIndex,
'1.3.6.1.2.1.64.1.2.1.2': DISMAN_SCRIPT_MIB.smExtsnExtension,
'1.3.6.1.2.1.64.1.2.1.3': DISMAN_SCRIPT_MIB.smExtsnVersion,
'1.3.6.1.2.1.64.1.2.1.4': DISMAN_SCRIPT_MIB.smExtsnVendor,
'1.3.6.1.2.1.64.1.2.1.5': DISMAN_SCRIPT_MIB.smExtsnRevision,
'1.3.6.1.2.1.64.1.2.1.6': DISMAN_SCRIPT_MIB.smExtsnDescr,
'1.3.6.1.2.1.64.1.3.1.1.1': DISMAN_SCRIPT_MIB.smScriptOwner,
'1.3.6.1.2.1.64.1.3.1.1.2': DISMAN_SCRIPT_MIB.smScriptName,
'1.3.6.1.2.1.64.1.3.1.1.3': DISMAN_SCRIPT_MIB.smScriptDescr,
'1.3.6.1.2.1.64.1.3.1.1.4': DISMAN_SCRIPT_MIB.smScriptLanguage,
'1.3.6.1.2.1.64.1.3.1.1.5': DISMAN_SCRIPT_MIB.smScriptSource,
'1.3.6.1.2.1.64.1.3.1.1.6': DISMAN_SCRIPT_MIB.smScriptAdminStatus,
'1.3.6.1.2.1.64.1.3.1.1.7': DISMAN_SCRIPT_MIB.smScriptOperStatus,
'1.3.6.1.2.1.64.1.3.1.1.8': DISMAN_SCRIPT_MIB.smScriptStorageType,
'1.3.6.1.2.1.64.1.3.1.1.9': DISMAN_SCRIPT_MIB.smScriptRowStatus,
'1.3.6.1.2.1.64.1.3.1.1.10': DISMAN_SCRIPT_MIB.smScriptError,
'1.3.6.1.2.1.64.1.3.1.1.11': DISMAN_SCRIPT_MIB.smScriptLastChange,
'1.3.6.1.2.1.64.1.3.2.1.1': DISMAN_SCRIPT_MIB.smCodeIndex,
'1.3.6.1.2.1.64.1.3.2.1.2': DISMAN_SCRIPT_MIB.smCodeText,
'1.3.6.1.2.1.64.1.3.2.1.3': DISMAN_SCRIPT_MIB.smCodeRowStatus,
'1.3.6.1.2.1.64.1.4.1.1.1': DISMAN_SCRIPT_MIB.smLaunchOwner,
'1.3.6.1.2.1.64.1.4.1.1.2': DISMAN_SCRIPT_MIB.smLaunchName,
'1.3.6.1.2.1.64.1.4.1.1.3': DISMAN_SCRIPT_MIB.smLaunchScriptOwner,
'1.3.6.1.2.1.64.1.4.1.1.4': DISMAN_SCRIPT_MIB.smLaunchScriptName,
'1.3.6.1.2.1.64.1.4.1.1.5': DISMAN_SCRIPT_MIB.smLaunchArgument,
'1.3.6.1.2.1.64.1.4.1.1.6': DISMAN_SCRIPT_MIB.smLaunchMaxRunning,
'1.3.6.1.2.1.64.1.4.1.1.7': DISMAN_SCRIPT_MIB.smLaunchMaxCompleted,
'1.3.6.1.2.1.64.1.4.1.1.8': DISMAN_SCRIPT_MIB.smLaunchLifeTime,
'1.3.6.1.2.1.64.1.4.1.1.9': DISMAN_SCRIPT_MIB.smLaunchExpireTime,
'1.3.6.1.2.1.64.1.4.1.1.10': DISMAN_SCRIPT_MIB.smLaunchStart,
'1.3.6.1.2.1.64.1.4.1.1.11': DISMAN_SCRIPT_MIB.smLaunchControl,
'1.3.6.1.2.1.64.1.4.1.1.12': DISMAN_SCRIPT_MIB.smLaunchAdminStatus,
'1.3.6.1.2.1.64.1.4.1.1.13': DISMAN_SCRIPT_MIB.smLaunchOperStatus,
'1.3.6.1.2.1.64.1.4.1.1.14': DISMAN_SCRIPT_MIB.smLaunchRunIndexNext,
'1.3.6.1.2.1.64.1.4.1.1.15': DISMAN_SCRIPT_MIB.smLaunchStorageType,
'1.3.6.1.2.1.64.1.4.1.1.16': DISMAN_SCRIPT_MIB.smLaunchRowStatus,
'1.3.6.1.2.1.64.1.4.1.1.17': DISMAN_SCRIPT_MIB.smLaunchError,
'1.3.6.1.2.1.64.1.4.1.1.18': DISMAN_SCRIPT_MIB.smLaunchLastChange,
'1.3.6.1.2.1.64.1.4.1.1.19': DISMAN_SCRIPT_MIB.smLaunchRowExpireTime,
'1.3.6.1.2.1.64.1.4.2.1.1': DISMAN_SCRIPT_MIB.smRunIndex,
'1.3.6.1.2.1.64.1.4.2.1.2': DISMAN_SCRIPT_MIB.smRunArgument,
'1.3.6.1.2.1.64.1.4.2.1.3': DISMAN_SCRIPT_MIB.smRunStartTime,
'1.3.6.1.2.1.64.1.4.2.1.4': DISMAN_SCRIPT_MIB.smRunEndTime,
'1.3.6.1.2.1.64.1.4.2.1.5': DISMAN_SCRIPT_MIB.smRunLifeTime,
'1.3.6.1.2.1.64.1.4.2.1.6': DISMAN_SCRIPT_MIB.smRunExpireTime,
'1.3.6.1.2.1.64.1.4.2.1.7': DISMAN_SCRIPT_MIB.smRunExitCode,
'1.3.6.1.2.1.64.1.4.2.1.8': DISMAN_SCRIPT_MIB.smRunResult,
'1.3.6.1.2.1.64.1.4.2.1.9': DISMAN_SCRIPT_MIB.smRunControl,
'1.3.6.1.2.1.64.1.4.2.1.10': DISMAN_SCRIPT_MIB.smRunState,
'1.3.6.1.2.1.64.1.4.2.1.11': DISMAN_SCRIPT_MIB.smRunError,
'1.3.6.1.2.1.64.1.4.2.1.12': DISMAN_SCRIPT_MIB.smRunResultTime,
'1.3.6.1.2.1.64.1.4.2.1.13': DISMAN_SCRIPT_MIB.smRunErrorTime,
'1.3.6.1.2.1.64.2.0.1': DISMAN_SCRIPT_MIB.smScriptAbort,
'1.3.6.1.2.1.64.2.0.2': DISMAN_SCRIPT_MIB.smScriptResult,
'1.3.6.1.2.1.64.2.0.3': DISMAN_SCRIPT_MIB.smScriptException,
'1.3.6.1.2.1.64.3.2.1': DISMAN_SCRIPT_MIB.smLanguageGroup,
'1.3.6.1.2.1.64.3.2.2': DISMAN_SCRIPT_MIB.smScriptGroup,
'1.3.6.1.2.1.64.3.2.3': DISMAN_SCRIPT_MIB.smCodeGroup,
'1.3.6.1.2.1.64.3.2.4': DISMAN_SCRIPT_MIB.smLaunchGroup,
'1.3.6.1.2.1.64.3.2.5': DISMAN_SCRIPT_MIB.smRunGroup,
'1.3.6.1.2.1.64.3.2.6': DISMAN_SCRIPT_MIB.smNotificationsGroup,
'1.3.6.1.2.1.64.3.2.7': DISMAN_SCRIPT_MIB.smScriptGroup2,
'1.3.6.1.2.1.64.3.2.8': DISMAN_SCRIPT_MIB.smLaunchGroup2,
'1.3.6.1.2.1.64.3.2.9': DISMAN_SCRIPT_MIB.smRunGroup2,
'1.3.6.1.2.1.64.3.2.10': DISMAN_SCRIPT_MIB.smNotificationsGroup2,
}
