import io
import json

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
    name = "World"
    try:
        body = json.loads(data.getvalue())
        name = body.get("name")
    except (Exception, ValueError) as ex:
        print(str(ex))

    return response.Response(
        ctx, response_data=json.dumps(
            {"message": "Hello {0}".format(name)}),
        headers={"Content-Type": "application/json"}
    )


def cefHeaderConstructor(cefVersion, cefDeviceVendor, cefDeviceProduct, cefDeviceVersion, cefEventType, cefEventName, cefEventSeverity):
    """
    This function is used to construct the CEF header based upon the information provided to the Python function and it
    will return a proper formatted CEF format header. This holds that the full CEF payload to be send to a third party
    application is not yet ready. Only the header is constructed in this specific Python function

    :param cefVersion: version of the CEF format (current default is 0)
    :param cefDeviceVendor: Name of the vendor (current default is Oracle OCI)
    :param cefDeviceProduct: Name of the product (mapping on OCI "service" name)
    :param cefDeviceVersion: Version of the service (default should be "latest")
    :param cefEventType: original CEF name "Device Event Class ID"
    :param cefEventName: short name / description of the event
    :param cefEventSeverity: severity of the event 0(low) till 10(very high)


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


def cefMessagePublisher(cefMessage):
    """
    
    :param cefMessage: 
    :return: 
    """