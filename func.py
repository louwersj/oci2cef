import io
import json
import sys

__author__ = "Johan Louwers"
__copyright__ = "Copyright 2020, Johan Louwers"
__license__ = "Apache License 2.0"
__email__ = "louwersj@gmail.com"

''' 
    This example code is intended to showcase the integration between Oracle Cloud (OCI) events and a third party SIEM 
    solution where communication is based upon the CEF (Common Event Format) format. Intended deployment target is 
    OCI Functions which acts as a PaaS solution for Fn Projects based functions and allows for serverless computing. 
    
    DO NOTE: this project is in no way or form an official Oracle released project and is in no way or form officially 
    related to the Oracle corporation. It is purely intended as an private code example to showcase potential 
    capabilities of using CEF as an integration format.  
'''

from fdk import response


# noinspection SyntaxError
def handler(ctx, data: io.BytesIO=None):
    """
    Generic (main) handler to handle the incoming request and associated payload file and to ensure a proper response
    is provided to the caller. The Python function "handler" is the default Python function used for a Fn Project
    function and is derived from the default boilerplate template.
    """

    # Generic flag which is used to indicate if the oci2cef Fn function succeeded.
    oci2cefProcessStatus = "OK"

   # ociEventEventID = "" #catch OCI event payload; eventID
   # name = "World"


    sys.stderr.write("THIS IS A TEST TO WRITE TO PAPERTRAIL LOG FROM OCI\n")

    try:
        body = json.loads(data.getvalue())

        ociEventEventID = body.get("eventID")        #catch OCI event payload value for eventID
        ociEventEventTime = body.get("eventTime")    #catch OCI event payload value for eventTime
        ociEventEventType = body.get("eventType")    #catch OCI event payload value for eventType

        ociCefVersion = "0"
        ociCefDeviceVendor = "Oracle Oci"
        ociCefDeviceProduct = body.get("source")
        ociCefDeviceVersion = body.get("eventTypeVersion")
        ociCefEventType = body.get("eventType")
        ociCefEventName = body.get("data.additionalDetails.displayName")
        ociCefEventSeverity = "1"




        sys.stderr.write("THIS IS A TEST TO WRITE TO PAPERTRAIL LOG FROM OCI" + ociEventEventID)
        cefHeader = cefHeaderConstructor(ociCefVersion,ociCefDeviceVendor,ociCefDeviceProduct,ociCefDeviceVersion,ociCefEventType,ociCefEventName,ociCefEventSeverity)

    except (Exception, ValueError) as ex:
        print(str(ex))

    return response.Response(
        ctx, response_data=json.dumps(
            {"status": ociCefEventName}),
        headers={"Content-Type": "application/json"}
    )


def cefHeaderConstructor(cefVersion, cefDeviceVendor, cefDeviceProduct, cefDeviceVersion, cefEventType, cefEventName, cefEventSeverity):
    """
    This function is used to construct the CEF header based upon the information provided to the Python function and it
    will return a proper formatted CEF format header. This holds that the full CEF payload to be send to a third party
    application is not yet ready. Only the header is constructed in this specific Python function

    :param cefVersion:
    :param cefDeviceVendor:
    :param cefDeviceProduct:
    :param cefDeviceVersion:
    :param cefEventType:
    :param cefEventName:
    :param cefEventSeverity:


    :return: proper formatted CEF message header
    """

    return cefHeaderResponse


def cefExtensionConstructor(x1, x2):
    """

    :param x1:
    :param x2:
    :return: proper formatted CEF message extension
    """

    return cefExtensionResponse


def cefMessageConstructor(cefHeader, cefBody):
    """
    This function is used to construct the CEF message, in effect stitch the header and the extension together and
    inspect it for proper formatting. CEF header is constructed in the Python Function cefHeaderConstructor and the
    extension is constructed in the cefExtensionConstructor as two individual parts.

    :param cefHeader:
    :param cefBody:
    :return: proper formatted CEF message (header and extension)
    """

    return cefMessageResponse


def cefMessagePrePublisher(cefMessage, cefPublisher):
    """
    This function is used as a (pre)publisher of the event towards a third party SIEM solution. we PREpublish it to
    another Fn Project function so we can ensure that the logic of the SIEM integration is segregated from the more
    (generic) CEF message construction. In an actual implementation the integration (publishing) to a SIEM will be a
    case by case like codebase while the message construction can stay the same. Hence... splitting into two functions.

    :param cefMessage:
    :param cefPublisher: FQDN pointer to the Fn Project function; cefPublisher.
    :return: 
    """