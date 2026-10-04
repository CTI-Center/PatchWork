---
title: "🔀 subtechniques"
source: https://gtidocs.virustotal.com/reference/subtechniques
slug: subtechniques
section: reference
group: "API OBJECTS"
updatedAt: 2025-12-01T16:16:08.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Attack Techniques](../object-attack-techniques.md) › 🔀 subtechniques

---

# 🔀-subtechniques

Attack technique's sub-techniques.

The *subtechniques* relationship returns the list of ***sub-techniques of the technique***.

This relationship can be retrieved using the [relationships API](../../03-ioc-investigation/attack-techniques/attack_techniqueidrelationship.md) endpoint. The response contains a list of [Attack Technique](../object-attack-techniques.md) objects.

```json /attack_techniques/{id}/subtechniques
{
  "data": [
    <ATTACK_TECHNIQUE_OBJECT>,
    <ATTACK_TECHNIQUE_OBJECT>,
    ...
  ],
  "links": {
    "next": <string>,
    "self": <string>
  },
  "meta": {
    "count": <int>,
    "cursor": <string>
  }
}
```
```json Example
{
  "meta": {
    "count": 4
  },
  "data": [
    {
      "attributes": {
        "info": {
          "x_mitre_platforms": [
            "Linux",
            "macOS"
          ],
          "x_mitre_is_subtechnique": true,
          "x_mitre_permissions_required": [
            "User"
          ],
          "x_mitre_version": "1.0",
          "x_mitre_data_sources": [
            "File monitoring",
            "Process monitoring",
            "Process command-line parameters"
          ],
          "x_mitre_detection": "Monitor the file system for files that have the setuid or setgid bits set. Monitor for execution of utilities, like chmod, and their command-line arguments to look for setuid or setguid bits being set."
        },
        "revoked": false,
        "name": "Setuid and Setgid",
        "creation_date": 1580393501,
        "link": "https://attack.mitre.org/techniques/T1548/001/",
        "stix_id": "attack-pattern--6831414d-bb70-42b7-8030-d4e06b2660c9",
        "last_modification_date": 1585269838,
        "description": "An adversary may perform shell escapes or exploit vulnerabilities in an application with the setsuid or setgid bits to get code running in a different user’s context. On Linux or macOS, when the setuid or setgid bits are set for an application, the application will run with the privileges of the owning user or group respectively. . Normally an application is run in the current user’s context, regardless of which user or group owns the application. However, there are instances where programs need to be executed in an elevated context to function properly, but the user running them doesn’t need the elevated privileges.\nInstead of creating an entry in the sudoers file, which must be done by root, any user can specify the setuid or setgid flag to be set for their own applications. These bits are indicated with an \"s\" instead of an \"x\" when viewing a file's attributes via ls -l. The chmod program can set these bits with via bitmasking, chmod 4777 [file] or via shorthand naming, chmod u+s [file].\nAdversaries can use this mechanism on their own malware to make sure they're able to execute in elevated contexts in the future.."
      },
      "type": "attack_technique",
      "id": "T1548.001",
      "links": {
        "self": "https://www.virustotal.com/api/v3/attack_techniques/T1548.001"
      }
    },
    {
      "attributes": {
        "info": {
          "x_mitre_contributors": [
            "Stefan Kanthak",
            "Casey Smith"
          ],
          "x_mitre_defense_bypassed": [
            "Windows User Account Control"
          ],
          "x_mitre_platforms": [
            "Windows"
          ],
          "x_mitre_is_subtechnique": true,
          "x_mitre_permissions_required": [
            "Administrator",
            "User"
          ],
          "x_mitre_effective_permissions": [
            "Administrator"
          ],
          "x_mitre_version": "2.0",
          "x_mitre_data_sources": [
            "Windows Registry",
            "Process command-line parameters",
            "Process monitoring"
          ],
          "x_mitre_detection": "There are many ways to perform UAC bypasses when a user is in the local administrator group on a system, so it may be difficult to target detection on all variations. Efforts should likely be placed on mitigation and collecting enough information on process launches and actions that could be performed before and after a UAC bypass is performed. Monitor process API calls for behavior that may be indicative of Process Injection and unusual loaded DLLs through DLL Search Order Hijacking, which indicate attempts to gain access to higher privileged processes.\nSome UAC bypass methods rely on modifying specific, user-accessible Registry settings. For example:\n\n\nThe eventvwr.exe bypass uses the [HKEY_CURRENT_USER]\\Software\\Classes\\mscfile\\shell\\open\\command Registry key.\n\n\nThe sdclt.exe bypass uses the [HKEY_CURRENT_USER]\\Software\\Microsoft\\Windows\\CurrentVersion\\App Paths\\control.exe and [HKEY_CURRENT_USER]\\Software\\Classes\\exefile\\shell\\runas\\command\\isolatedCommand Registry keys.\n\n\nAnalysts should monitor these Registry settings for unauthorized changes."
        },
        "revoked": false,
        "name": "Bypass User Account Control",
        "creation_date": 1580394274,
        "link": "https://attack.mitre.org/techniques/T1548/002/",
        "stix_id": "attack-pattern--120d5519-3098-4e1c-9191-2aa61232f073",
        "last_modification_date": 1595453812,
        "description": "Adversaries may bypass UAC mechanisms to elevate process privileges on system. Windows User Account Control (UAC) allows a program to elevate its privileges (tracked as integrity levels ranging from low to high) to perform a task under administrator-level permissions, possibly by prompting the user for confirmation. The impact to the user ranges from denying the operation under high enforcement to allowing the user to perform the action if they are in the local administrators group and click through the prompt or allowing them to enter an administrator password to complete the action. \nIf the UAC protection level of a computer is set to anything but the highest level, certain Windows programs can elevate privileges or execute some elevated Component Object Model objects without prompting the user through the UAC notification box.   An example of this is use of Rundll32 to load a specifically crafted DLL which loads an auto-elevated Component Object Model object and performs a file operation in a protected directory which would typically require elevated access. Malicious software may also be injected into a trusted process to gain elevated privileges without prompting a user.\nMany methods have been discovered to bypass UAC. The Github readme page for UACME contains an extensive list of methods that have been discovered and implemented, but may not be a comprehensive list of bypasses. Additional bypass methods are regularly discovered and some used in the wild, such as:\n\neventvwr.exe can auto-elevate and execute a specified binary or script.\n\nAnother bypass is possible through some lateral movement techniques if credentials for an account with administrator privileges are known, since UAC is a single system security mechanism, and the privilege or integrity of a process running on one system will be unknown on remote systems and default to high integrity."
      },
      "type": "attack_technique",
      "id": "T1548.002",
      "links": {
        "self": "https://www.virustotal.com/api/v3/attack_techniques/T1548.002"
      }
    },
    {
      "attributes": {
        "info": {
          "x_mitre_platforms": [
            "Linux",
            "macOS"
          ],
          "x_mitre_is_subtechnique": true,
          "x_mitre_permissions_required": [
            "User"
          ],
          "x_mitre_effective_permissions": [
            "root"
          ],
          "x_mitre_version": "1.0",
          "x_mitre_data_sources": [
            "File monitoring",
            "Process command-line parameters"
          ],
          "x_mitre_detection": "On Linux, auditd can alert every time a user's actual ID and effective ID are different (this is what happens when you sudo). This technique is abusing normal functionality in macOS and Linux systems, but sudo has the ability to log all input and output based on the LOG_INPUT and LOG_OUTPUT directives in the /etc/sudoers file."
        },
        "revoked": false,
        "name": "Sudo and Sudo Caching",
        "creation_date": 1580394884,
        "link": "https://attack.mitre.org/techniques/T1548/003/",
        "stix_id": "attack-pattern--1365fe3b-0f50-455d-b4da-266ce31c23b0",
        "last_modification_date": 1585271006,
        "description": "Adversaries may perform sudo caching and/or use the suoders file to elevate privileges. Adversaries may do this to execute commands as other users or spawn processes with higher privileges.\nWithin Linux and MacOS systems, sudo (sometimes referred to as \"superuser do\") allows users to perform commands from terminals with elevated privileges and to control who can perform these commands on the system. The sudo command \"allows a system administrator to delegate authority to give certain users (or groups of users) the ability to run some (or all) commands as root or another user while providing an audit trail of the commands and their arguments.\" Since sudo was made for the system administrator, it has some useful configuration features such as a timestamp_timeout, which is the amount of time in minutes between instances of sudo before it will re-prompt for a password. This is because sudo has the ability to cache credentials for a period of time. Sudo creates (or touches) a file at /var/db/sudo with a timestamp of when sudo was last run to determine this timeout. Additionally, there is a tty_tickets variable that treats each new tty (terminal session) in isolation. This means that, for example, the sudo timeout of one tty will not affect another tty (you will have to type the password again).\nThe sudoers file, /etc/sudoers, describes which users can run which commands and from which terminals. This also describes which commands users can run as other users or groups. This provides the principle of least privilege such that users are running in their lowest possible permissions for most of the time and only elevate to other users or permissions as needed, typically by prompting for a password. However, the sudoers file can also specify when to not prompt users for passwords with a line like user1 ALL=(ALL) NOPASSWD: ALL . Elevated privileges are required to edit this file though.\nAdversaries can also abuse poor configurations of these mechanisms to escalate privileges without needing the user's password. For example, /var/db/sudo's timestamp can be monitored to see if it falls within the timestamp_timeout range. If it does, then malware can execute sudo commands without needing to supply the user's password. Additional, if tty_tickets is disabled, adversaries can do this from any tty for that user.\nIn the wild, malware has disabled tty_tickets to potentially make scripting easier by issuing echo \\'Defaults !tty_tickets\\' >> /etc/sudoers . In order for this change to be reflected, the malware also issued killall Terminal. As of macOS Sierra, the sudoers file has tty_tickets enabled by default."
      },
      "type": "attack_technique",
      "id": "T1548.003",
      "links": {
        "self": "https://www.virustotal.com/api/v3/attack_techniques/T1548.003"
      }
    },
    {
      "attributes": {
        "info": {
          "x_mitre_contributors": [
            "Jimmy Astle, @AstleJimmy, Carbon Black",
            "Erika Noerenberg, @gutterchurl, Carbon Black"
          ],
          "x_mitre_platforms": [
            "macOS"
          ],
          "x_mitre_is_subtechnique": true,
          "x_mitre_permissions_required": [
            "Administrator",
            "User"
          ],
          "x_mitre_effective_permissions": [
            "root"
          ],
          "x_mitre_version": "1.0",
          "x_mitre_data_sources": [
            "API monitoring",
            "Process monitoring",
            "File monitoring"
          ],
          "x_mitre_detection": "Consider monitoring for /usr/libexec/security_authtrampoline executions which may indicate that AuthorizationExecuteWithPrivileges is being executed. MacOS system logs may also indicate when AuthorizationExecuteWithPrivileges is being called. Monitoring OS API callbacks for the execution can also be a way to detect this behavior but requires specialized security tooling."
        },
        "revoked": false,
        "name": "Elevated Execution with Prompt",
        "creation_date": 1580395220,
        "link": "https://attack.mitre.org/techniques/T1548/004/",
        "stix_id": "attack-pattern--b84903f0-c7d5-435d-a69e-de47cc3578c0",
        "last_modification_date": 1585310677,
        "description": "Adversaries may leverage the AuthorizationExecuteWithPrivileges API to escalate privileges by prompting the user for credentials. The purpose of this API is to give application developers an easy way to perform operations with root privileges, such as for application installation or updating. This API does not validate that the program requesting root privileges comes from a reputable source or has been maliciously modified. \nAlthough this API is deprecated, it still fully functions in the latest releases of macOS. When calling this API, the user will be prompted to enter their credentials but no checks on the origin or integrity of the program are made. The program calling the API may also load world writable files which can be modified to perform malicious behavior with elevated privileges.\nAdversaries may abuse AuthorizationExecuteWithPrivileges to obtain root privileges in order to install malicious software on victims and install persistence mechanisms. This technique may be combined with Masquerading to trick the user into granting escalated privileges to malicious code. This technique has also been shown to work by modifying legitimate programs present on the machine that make use of this API."
      },
      "type": "attack_technique",
      "id": "T1548.004",
      "links": {
        "self": "https://www.virustotal.com/api/v3/attack_techniques/T1548.004"
      }
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/attack_techniques/T1548/subtechniques?limit=10"
  }
}
```

---

← [🔀 revoking_technique](revoking_technique.md) · [up](../README.md) · [🔀 threat_actors](attack-techniques-threat_actors.md) →

*Archived from <https://gtidocs.virustotal.com/reference/subtechniques>.*
