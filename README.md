# oci2cef
WIP......

## CEF Format
The CEF standard format is an open log management standard that simplifies log management. CEF allows third parties to create their own device schemas that are compatible with a standard that is used industry-wide for normalizing security events. Technology companies and customers can use the standardized CEF format to facilitate data collection and aggregation, for later analysis by an enterprise management system. 

### CEF Header
The CEF Header consists out of a predefined and prefixed format as shown in the example below. The "Extensions" section is used for the required additional information related to the event. 
```
CEF:Version|Device Vendor|Device Product|Device Version|Device Event Class ID|Name|Severity|[Extension]
```

Version is  an integer and identifies the version of the CEF format. Event consumers use this information to determine what the following fields represent. The current CEF version is 0 (CEF:0). 

Device Vendor, Device Product and Device Version are strings that uniquely identify the type of sending device. No two products may use the same device-vendor and device-product pair. There is no central authority managing these pairs. Event producers must ensure that they assign unique name pairs.

Device Event Class ID is  a unique identifier per event-type. This can be a string or an integer. Device Event Class ID identifies the type of event reported. In the intrusion detection system (IDS)world, each signature or rule that detects certain activity has a unique Device Event Class ID assigned. This is    a   requirement for other types of devices as   well, and helps correlation enginesprocess the events. Also known as Signature ID.

Name is a string representing a human-readable and understandable description of the event. The event name should not contain information that is specifically mentioned in other fields. For example: "Port scan from 10.0.0.1 targeting 20.1.1.1" is not a good event name. It should be: "Portscan". The other information is redundant and can be picked up from the other fields.

Severity is a string or integer and reflects the importance of the event. The valid string values are Unknown, Low, Medium, High, and Very-High. The valid integer values are 0-3=Low, 4-6=Medium, 7- 8=High, and 9-10=Very-High.

### CEF Extention(s)
