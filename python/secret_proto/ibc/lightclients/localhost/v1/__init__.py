# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ibc/lightclients/localhost/v1/localhost.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class ClientState(betterproto.Message):
    """
    ClientState defines a loopback (localhost) client. It requires (read-only)
    access to keys outside the client prefix.
    """

    # self chain ID
    chain_id: str = betterproto.string_field(1)
    # self latest block height
    height: "___core_client_v1__.Height" = betterproto.message_field(2)


from ....core.client import v1 as ___core_client_v1__
