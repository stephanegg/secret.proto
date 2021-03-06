# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ibc/applications/transfer/v1/genesis.proto, ibc/applications/transfer/v1/query.proto, ibc/applications/transfer/v1/transfer.proto, ibc/applications/transfer/v1/tx.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


@dataclass(eq=False, repr=False)
class MsgTransfer(betterproto.Message):
    """
    MsgTransfer defines a msg to transfer fungible tokens (i.e Coins) between
    ICS20 enabled chains. See ICS Spec here:
    https://github.com/cosmos/ics/tree/master/spec/ics-020-fungible-token-
    transfer#data-structures
    """

    # the port on which the packet will be sent
    source_port: str = betterproto.string_field(1)
    # the channel by which the packet will be sent
    source_channel: str = betterproto.string_field(2)
    # the tokens to be transferred
    token: "____cosmos_base_v1_beta1__.Coin" = betterproto.message_field(3)
    # the sender address
    sender: str = betterproto.string_field(4)
    # the recipient address on the destination chain
    receiver: str = betterproto.string_field(5)
    # Timeout height relative to the current block height. The timeout is
    # disabled when set to 0.
    timeout_height: "___core_client_v1__.Height" = betterproto.message_field(6)
    # Timeout timestamp (in nanoseconds) relative to the current block timestamp.
    # The timeout is disabled when set to 0.
    timeout_timestamp: int = betterproto.uint64_field(7)


@dataclass(eq=False, repr=False)
class MsgTransferResponse(betterproto.Message):
    """MsgTransferResponse defines the Msg/Transfer response type."""

    pass


@dataclass(eq=False, repr=False)
class FungibleTokenPacketData(betterproto.Message):
    """
    FungibleTokenPacketData defines a struct for the packet payload See
    FungibleTokenPacketData spec:
    https://github.com/cosmos/ics/tree/master/spec/ics-020-fungible-token-
    transfer#data-structures
    """

    # the token denomination to be transferred
    denom: str = betterproto.string_field(1)
    # the token amount to be transferred
    amount: int = betterproto.uint64_field(2)
    # the sender address
    sender: str = betterproto.string_field(3)
    # the recipient address on the destination chain
    receiver: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class DenomTrace(betterproto.Message):
    """
    DenomTrace contains the base denomination for ICS20 fungible tokens and the
    source tracing information path.
    """

    # path defines the chain of port/channel identifiers used for tracing the
    # source of the fungible token.
    path: str = betterproto.string_field(1)
    # base denomination of the relayed fungible token.
    base_denom: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """
    Params defines the set of IBC transfer parameters. NOTE: To prevent a
    single token from being transferred, set the TransfersEnabled parameter to
    true and then set the bank module's SendEnabled parameter for the
    denomination to false.
    """

    # send_enabled enables or disables all cross-chain token transfers from this
    # chain.
    send_enabled: bool = betterproto.bool_field(1)
    # receive_enabled enables or disables all cross-chain token transfers to this
    # chain.
    receive_enabled: bool = betterproto.bool_field(2)


@dataclass(eq=False, repr=False)
class QueryDenomTraceRequest(betterproto.Message):
    """
    QueryDenomTraceRequest is the request type for the Query/DenomTrace RPC
    method
    """

    # hash (in hex format) of the denomination trace information.
    hash: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryDenomTraceResponse(betterproto.Message):
    """
    QueryDenomTraceResponse is the response type for the Query/DenomTrace RPC
    method.
    """

    # denom_trace returns the requested denomination trace information.
    denom_trace: "DenomTrace" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryDenomTracesRequest(betterproto.Message):
    """
    QueryConnectionsRequest is the request type for the Query/DenomTraces RPC
    method
    """

    # pagination defines an optional pagination for the request.
    pagination: "____cosmos_base_query_v1_beta1__.PageRequest" = (
        betterproto.message_field(1)
    )


@dataclass(eq=False, repr=False)
class QueryDenomTracesResponse(betterproto.Message):
    """
    QueryConnectionsResponse is the response type for the Query/DenomTraces RPC
    method.
    """

    # denom_traces returns all denominations trace information.
    denom_traces: List["DenomTrace"] = betterproto.message_field(1)
    # pagination defines the pagination in the response.
    pagination: "____cosmos_base_query_v1_beta1__.PageResponse" = (
        betterproto.message_field(2)
    )


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """
    QueryParamsRequest is the request type for the Query/Params RPC method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """
    QueryParamsResponse is the response type for the Query/Params RPC method.
    """

    # params defines the parameters of the module.
    params: "Params" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the ibc-transfer genesis state"""

    port_id: str = betterproto.string_field(1)
    denom_traces: List["DenomTrace"] = betterproto.message_field(2)
    params: "Params" = betterproto.message_field(3)


class MsgStub(betterproto.ServiceStub):
    async def transfer(
        self,
        *,
        source_port: str = "",
        source_channel: str = "",
        token: "____cosmos_base_v1_beta1__.Coin" = None,
        sender: str = "",
        receiver: str = "",
        timeout_height: "___core_client_v1__.Height" = None,
        timeout_timestamp: int = 0
    ) -> "MsgTransferResponse":

        request = MsgTransfer()
        request.source_port = source_port
        request.source_channel = source_channel
        if token is not None:
            request.token = token
        request.sender = sender
        request.receiver = receiver
        if timeout_height is not None:
            request.timeout_height = timeout_height
        request.timeout_timestamp = timeout_timestamp

        return await self._unary_unary(
            "/ibc.applications.transfer.v1.Msg/Transfer", request, MsgTransferResponse
        )


class QueryStub(betterproto.ServiceStub):
    async def denom_trace(self, *, hash: str = "") -> "QueryDenomTraceResponse":

        request = QueryDenomTraceRequest()
        request.hash = hash

        return await self._unary_unary(
            "/ibc.applications.transfer.v1.Query/DenomTrace",
            request,
            QueryDenomTraceResponse,
        )

    async def denom_traces(
        self, *, pagination: "____cosmos_base_query_v1_beta1__.PageRequest" = None
    ) -> "QueryDenomTracesResponse":

        request = QueryDenomTracesRequest()
        if pagination is not None:
            request.pagination = pagination

        return await self._unary_unary(
            "/ibc.applications.transfer.v1.Query/DenomTraces",
            request,
            QueryDenomTracesResponse,
        )

    async def params(self) -> "QueryParamsResponse":

        request = QueryParamsRequest()

        return await self._unary_unary(
            "/ibc.applications.transfer.v1.Query/Params", request, QueryParamsResponse
        )


class MsgBase(ServiceBase):
    async def transfer(
        self,
        source_port: str,
        source_channel: str,
        token: "____cosmos_base_v1_beta1__.Coin",
        sender: str,
        receiver: str,
        timeout_height: "___core_client_v1__.Height",
        timeout_timestamp: int,
    ) -> "MsgTransferResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_transfer(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "source_port": request.source_port,
            "source_channel": request.source_channel,
            "token": request.token,
            "sender": request.sender,
            "receiver": request.receiver,
            "timeout_height": request.timeout_height,
            "timeout_timestamp": request.timeout_timestamp,
        }

        response = await self.transfer(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/ibc.applications.transfer.v1.Msg/Transfer": grpclib.const.Handler(
                self.__rpc_transfer,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgTransfer,
                MsgTransferResponse,
            ),
        }


class QueryBase(ServiceBase):
    async def denom_trace(self, hash: str) -> "QueryDenomTraceResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def denom_traces(
        self, pagination: "____cosmos_base_query_v1_beta1__.PageRequest"
    ) -> "QueryDenomTracesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def params(self) -> "QueryParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_denom_trace(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "hash": request.hash,
        }

        response = await self.denom_trace(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_denom_traces(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "pagination": request.pagination,
        }

        response = await self.denom_traces(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_params(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.params(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/ibc.applications.transfer.v1.Query/DenomTrace": grpclib.const.Handler(
                self.__rpc_denom_trace,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryDenomTraceRequest,
                QueryDenomTraceResponse,
            ),
            "/ibc.applications.transfer.v1.Query/DenomTraces": grpclib.const.Handler(
                self.__rpc_denom_traces,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryDenomTracesRequest,
                QueryDenomTracesResponse,
            ),
            "/ibc.applications.transfer.v1.Query/Params": grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
        }


from .....cosmos.base import v1beta1 as ____cosmos_base_v1_beta1__
from .....cosmos.base.query import v1beta1 as ____cosmos_base_query_v1_beta1__
from ....core.client import v1 as ___core_client_v1__
