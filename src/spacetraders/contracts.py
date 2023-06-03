"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from spacetraders import utils
from spacetraders.models import operations
from typing import Optional

class Contracts:
    r"""Contracts"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def accept_contract(self, request: operations.AcceptContractRequest, security: operations.AcceptContractSecurity) -> operations.AcceptContractResponse:
        r"""Accept Contract
        Accept a contract.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.AcceptContractRequest, base_url, '/my/contracts/{contractId}/accept', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('POST', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.AcceptContractResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.AcceptContract200ApplicationJSON])
                res.accept_contract_200_application_json_object = out

        return res

    
    def deliver_contract(self, request: operations.DeliverContractRequest, security: operations.DeliverContractSecurity) -> operations.DeliverContractResponse:
        r"""Deliver Contract
        Deliver cargo on a given contract.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeliverContractRequest, base_url, '/my/contracts/{contractId}/deliver', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeliverContractResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeliverContract200ApplicationJSON])
                res.deliver_contract_200_application_json_object = out

        return res

    
    def fulfill_contract(self, request: operations.FulfillContractRequest, security: operations.FulfillContractSecurity) -> operations.FulfillContractResponse:
        r"""Fulfill Contract
        Fulfill a contract
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.FulfillContractRequest, base_url, '/my/contracts/{contractId}/fulfill', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('POST', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.FulfillContractResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.FulfillContract200ApplicationJSON])
                res.fulfill_contract_200_application_json_object = out

        return res

    
    def get_contract(self, request: operations.GetContractRequest, security: operations.GetContractSecurity) -> operations.GetContractResponse:
        r"""Get Contract
        Get the details of a contract by ID.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetContractRequest, base_url, '/my/contracts/{contractId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetContractResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetContract200ApplicationJSON])
                res.get_contract_200_application_json_object = out

        return res

    
    def get_contracts(self, request: operations.GetContractsRequest, security: operations.GetContractsSecurity) -> operations.GetContractsResponse:
        r"""List Contracts
        List all of your contracts.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/my/contracts'
        headers = {}
        query_params = utils.get_query_params(operations.GetContractsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetContractsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetContracts200ApplicationJSON])
                res.get_contracts_200_application_json_object = out

        return res

    