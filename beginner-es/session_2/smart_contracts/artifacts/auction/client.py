# flake8: noqa
# fmt: off
# mypy: disable-error-code="no-any-return, no-untyped-call"
# This file was automatically generated by algokit-client-generator.
# DO NOT MODIFY IT BY HAND.
# requires: algokit-utils@^1.2.0
import base64
import dataclasses
import decimal
import typing
from abc import ABC, abstractmethod

import algokit_utils
import algosdk
from algosdk.atomic_transaction_composer import (
    AtomicTransactionComposer,
    AtomicTransactionResponse,
    TransactionSigner,
    TransactionWithSigner
)

_APP_SPEC_JSON = r"""{
    "hints": {
        "optin_to_asset(pay,asset)void": {
            "call_config": {
                "no_op": "CALL"
            }
        },
        "start(uint64,uint64,axfer)void": {
            "call_config": {
                "no_op": "CALL"
            }
        },
        "bid(pay,account)void": {
            "call_config": {
                "no_op": "CALL"
            }
        },
        "claim_asset(asset)void": {
            "call_config": {
                "no_op": "CALL"
            }
        },
        "claim_bid()void": {
            "call_config": {
                "no_op": "CALL"
            }
        },
        "get_time()uint64": {
            "call_config": {
                "no_op": "CALL"
            }
        }
    },
    "source": {
        "approval": "I3ByYWdtYSB2ZXJzaW9uIDgKaW50Y2Jsb2NrIDAgMSA0CmJ5dGVjYmxvY2sgMHg2ODY5Njc2ODY1NzM3NDVmNjI2OTY0IDB4Nzc2OTZlNmU2NTcyIDB4NjE3MzYxNWY2OTY0IDB4NjE3NTYzNzQ2OTZmNmU1ZjY1NmU2NCAweAp0eG4gTnVtQXBwQXJncwppbnRjXzAgLy8gMAo9PQpibnogbWFpbl9sMTQKdHhuYSBBcHBsaWNhdGlvbkFyZ3MgMApwdXNoYnl0ZXMgMHg3ZGNlY2VlZSAvLyAib3B0aW5fdG9fYXNzZXQocGF5LGFzc2V0KXZvaWQiCj09CmJueiBtYWluX2wxMwp0eG5hIEFwcGxpY2F0aW9uQXJncyAwCnB1c2hieXRlcyAweDA5YTVhNzkwIC8vICJzdGFydCh1aW50NjQsdWludDY0LGF4ZmVyKXZvaWQiCj09CmJueiBtYWluX2wxMgp0eG5hIEFwcGxpY2F0aW9uQXJncyAwCnB1c2hieXRlcyAweDM5MDQyYWVlIC8vICJiaWQocGF5LGFjY291bnQpdm9pZCIKPT0KYm56IG1haW5fbDExCnR4bmEgQXBwbGljYXRpb25BcmdzIDAKcHVzaGJ5dGVzIDB4MWVjMTJiZWYgLy8gImNsYWltX2Fzc2V0KGFzc2V0KXZvaWQiCj09CmJueiBtYWluX2wxMAp0eG5hIEFwcGxpY2F0aW9uQXJncyAwCnB1c2hieXRlcyAweGI1ODkwNjg2IC8vICJjbGFpbV9iaWQoKXZvaWQiCj09CmJueiBtYWluX2w5CnR4bmEgQXBwbGljYXRpb25BcmdzIDAKcHVzaGJ5dGVzIDB4ZTY1NTIyZmQgLy8gImdldF90aW1lKCl1aW50NjQiCj09CmJueiBtYWluX2w4CmVycgptYWluX2w4Ogp0eG4gT25Db21wbGV0aW9uCmludGNfMCAvLyBOb09wCj09CnR4biBBcHBsaWNhdGlvbklECmludGNfMCAvLyAwCiE9CiYmCmFzc2VydApjYWxsc3ViIGdldHRpbWVjYXN0ZXJfMTIKaW50Y18xIC8vIDEKcmV0dXJuCm1haW5fbDk6CnR4biBPbkNvbXBsZXRpb24KaW50Y18wIC8vIE5vT3AKPT0KdHhuIEFwcGxpY2F0aW9uSUQKaW50Y18wIC8vIDAKIT0KJiYKYXNzZXJ0CmNhbGxzdWIgY2xhaW1iaWRjYXN0ZXJfMTEKaW50Y18xIC8vIDEKcmV0dXJuCm1haW5fbDEwOgp0eG4gT25Db21wbGV0aW9uCmludGNfMCAvLyBOb09wCj09CnR4biBBcHBsaWNhdGlvbklECmludGNfMCAvLyAwCiE9CiYmCmFzc2VydApjYWxsc3ViIGNsYWltYXNzZXRjYXN0ZXJfMTAKaW50Y18xIC8vIDEKcmV0dXJuCm1haW5fbDExOgp0eG4gT25Db21wbGV0aW9uCmludGNfMCAvLyBOb09wCj09CnR4biBBcHBsaWNhdGlvbklECmludGNfMCAvLyAwCiE9CiYmCmFzc2VydApjYWxsc3ViIGJpZGNhc3Rlcl85CmludGNfMSAvLyAxCnJldHVybgptYWluX2wxMjoKdHhuIE9uQ29tcGxldGlvbgppbnRjXzAgLy8gTm9PcAo9PQp0eG4gQXBwbGljYXRpb25JRAppbnRjXzAgLy8gMAohPQomJgphc3NlcnQKY2FsbHN1YiBzdGFydGNhc3Rlcl84CmludGNfMSAvLyAxCnJldHVybgptYWluX2wxMzoKdHhuIE9uQ29tcGxldGlvbgppbnRjXzAgLy8gTm9PcAo9PQp0eG4gQXBwbGljYXRpb25JRAppbnRjXzAgLy8gMAohPQomJgphc3NlcnQKY2FsbHN1YiBvcHRpbnRvYXNzZXRjYXN0ZXJfNwppbnRjXzEgLy8gMQpyZXR1cm4KbWFpbl9sMTQ6CnR4biBPbkNvbXBsZXRpb24KaW50Y18wIC8vIE5vT3AKPT0KYm56IG1haW5fbDE2CmVycgptYWluX2wxNjoKdHhuIEFwcGxpY2F0aW9uSUQKaW50Y18wIC8vIDAKPT0KYXNzZXJ0CmNhbGxzdWIgY3JlYXRlXzAKaW50Y18xIC8vIDEKcmV0dXJuCgovLyBjcmVhdGUKY3JlYXRlXzA6CnByb3RvIDAgMApieXRlY18yIC8vICJhc2FfaWQiCmludGNfMCAvLyAwCmFwcF9nbG9iYWxfcHV0CmJ5dGVjXzMgLy8gImF1Y3Rpb25fZW5kIgppbnRjXzAgLy8gMAphcHBfZ2xvYmFsX3B1dApieXRlY18wIC8vICJoaWdoZXN0X2JpZCIKaW50Y18wIC8vIDAKYXBwX2dsb2JhbF9wdXQKYnl0ZWNfMSAvLyAid2lubmVyIgpieXRlYyA0IC8vICIiCmFwcF9nbG9iYWxfcHV0CnJldHN1YgoKLy8gb3B0aW5fdG9fYXNzZXQKb3B0aW50b2Fzc2V0XzE6CnByb3RvIDIgMApmcmFtZV9kaWcgLTIKZ3R4bnMgUmVjZWl2ZXIKZ2xvYmFsIEN1cnJlbnRBcHBsaWNhdGlvbkFkZHJlc3MKPT0KYXNzZXJ0CmJ5dGVjXzIgLy8gImFzYV9pZCIKZnJhbWVfZGlnIC0xCnR4bmFzIEFzc2V0cwphcHBfZ2xvYmFsX3B1dAppdHhuX2JlZ2luCmludGNfMiAvLyBheGZlcgppdHhuX2ZpZWxkIFR5cGVFbnVtCmdsb2JhbCBDdXJyZW50QXBwbGljYXRpb25BZGRyZXNzCml0eG5fZmllbGQgQXNzZXRSZWNlaXZlcgppbnRjXzAgLy8gMAppdHhuX2ZpZWxkIEFzc2V0QW1vdW50CmZyYW1lX2RpZyAtMQp0eG5hcyBBc3NldHMKaXR4bl9maWVsZCBYZmVyQXNzZXQKaW50Y18wIC8vIDAKaXR4bl9maWVsZCBGZWUKaXR4bl9zdWJtaXQKcmV0c3ViCgovLyBzdGFydApzdGFydF8yOgpwcm90byAzIDAKYnl0ZWNfMCAvLyAiaGlnaGVzdF9iaWQiCmZyYW1lX2RpZyAtMgphcHBfZ2xvYmFsX3B1dApieXRlY18zIC8vICJhdWN0aW9uX2VuZCIKZ2xvYmFsIExhdGVzdFRpbWVzdGFtcApmcmFtZV9kaWcgLTMKKwphcHBfZ2xvYmFsX3B1dApyZXRzdWIKCi8vIGJpZApiaWRfMzoKcHJvdG8gMiAwCmZyYW1lX2RpZyAtMgpndHhucyBBbW91bnQKYnl0ZWNfMCAvLyAiaGlnaGVzdF9iaWQiCmFwcF9nbG9iYWxfZ2V0Cj4KYXNzZXJ0CmJ5dGVjXzEgLy8gIndpbm5lciIKYXBwX2dsb2JhbF9nZXQKYnl0ZWMgNCAvLyAiIgohPQpieiBiaWRfM19sMgppdHhuX2JlZ2luCmludGNfMSAvLyBwYXkKaXR4bl9maWVsZCBUeXBlRW51bQpieXRlY18xIC8vICJ3aW5uZXIiCmFwcF9nbG9iYWxfZ2V0Cml0eG5fZmllbGQgUmVjZWl2ZXIKYnl0ZWNfMCAvLyAiaGlnaGVzdF9iaWQiCmFwcF9nbG9iYWxfZ2V0Cml0eG5fZmllbGQgQW1vdW50CmludGNfMCAvLyAwCml0eG5fZmllbGQgRmVlCml0eG5fc3VibWl0CmJpZF8zX2wyOgpieXRlY18xIC8vICJ3aW5uZXIiCmZyYW1lX2RpZyAtMgpndHhucyBTZW5kZXIKYXBwX2dsb2JhbF9wdXQKYnl0ZWNfMCAvLyAiaGlnaGVzdF9iaWQiCmZyYW1lX2RpZyAtMgpndHhucyBBbW91bnQKYXBwX2dsb2JhbF9wdXQKcmV0c3ViCgovLyBjbGFpbV9hc3NldApjbGFpbWFzc2V0XzQ6CnByb3RvIDEgMAppdHhuX2JlZ2luCmludGNfMiAvLyBheGZlcgppdHhuX2ZpZWxkIFR5cGVFbnVtCmJ5dGVjXzEgLy8gIndpbm5lciIKYXBwX2dsb2JhbF9nZXQKaXR4bl9maWVsZCBBc3NldFJlY2VpdmVyCmludGNfMSAvLyAxCml0eG5fZmllbGQgQXNzZXRBbW91bnQKYnl0ZWNfMiAvLyAiYXNhX2lkIgphcHBfZ2xvYmFsX2dldAppdHhuX2ZpZWxkIFhmZXJBc3NldAppbnRjXzAgLy8gMAppdHhuX2ZpZWxkIEZlZQppdHhuX3N1Ym1pdApyZXRzdWIKCi8vIGNsYWltX2JpZApjbGFpbWJpZF81Ogpwcm90byAwIDAKaXR4bl9iZWdpbgppbnRjXzEgLy8gcGF5Cml0eG5fZmllbGQgVHlwZUVudW0KZ2xvYmFsIENyZWF0b3JBZGRyZXNzCml0eG5fZmllbGQgUmVjZWl2ZXIKYnl0ZWNfMCAvLyAiaGlnaGVzdF9iaWQiCmFwcF9nbG9iYWxfZ2V0Cml0eG5fZmllbGQgQW1vdW50CmludGNfMCAvLyAwCml0eG5fZmllbGQgRmVlCml0eG5fc3VibWl0CnJldHN1YgoKLy8gZ2V0X3RpbWUKZ2V0dGltZV82Ogpwcm90byAwIDEKaW50Y18wIC8vIDAKZ2xvYmFsIExhdGVzdFRpbWVzdGFtcApmcmFtZV9idXJ5IDAKcmV0c3ViCgovLyBvcHRpbl90b19hc3NldF9jYXN0ZXIKb3B0aW50b2Fzc2V0Y2FzdGVyXzc6CnByb3RvIDAgMAppbnRjXzAgLy8gMApkdXAKdHhuYSBBcHBsaWNhdGlvbkFyZ3MgMQppbnRjXzAgLy8gMApnZXRieXRlCmZyYW1lX2J1cnkgMQp0eG4gR3JvdXBJbmRleAppbnRjXzEgLy8gMQotCmZyYW1lX2J1cnkgMApmcmFtZV9kaWcgMApndHhucyBUeXBlRW51bQppbnRjXzEgLy8gcGF5Cj09CmFzc2VydApmcmFtZV9kaWcgMApmcmFtZV9kaWcgMQpjYWxsc3ViIG9wdGludG9hc3NldF8xCnJldHN1YgoKLy8gc3RhcnRfY2FzdGVyCnN0YXJ0Y2FzdGVyXzg6CnByb3RvIDAgMAppbnRjXzAgLy8gMApkdXBuIDIKdHhuYSBBcHBsaWNhdGlvbkFyZ3MgMQpidG9pCmZyYW1lX2J1cnkgMAp0eG5hIEFwcGxpY2F0aW9uQXJncyAyCmJ0b2kKZnJhbWVfYnVyeSAxCnR4biBHcm91cEluZGV4CmludGNfMSAvLyAxCi0KZnJhbWVfYnVyeSAyCmZyYW1lX2RpZyAyCmd0eG5zIFR5cGVFbnVtCmludGNfMiAvLyBheGZlcgo9PQphc3NlcnQKZnJhbWVfZGlnIDAKZnJhbWVfZGlnIDEKZnJhbWVfZGlnIDIKY2FsbHN1YiBzdGFydF8yCnJldHN1YgoKLy8gYmlkX2Nhc3RlcgpiaWRjYXN0ZXJfOToKcHJvdG8gMCAwCmludGNfMCAvLyAwCmR1cAp0eG5hIEFwcGxpY2F0aW9uQXJncyAxCmludGNfMCAvLyAwCmdldGJ5dGUKZnJhbWVfYnVyeSAxCnR4biBHcm91cEluZGV4CmludGNfMSAvLyAxCi0KZnJhbWVfYnVyeSAwCmZyYW1lX2RpZyAwCmd0eG5zIFR5cGVFbnVtCmludGNfMSAvLyBwYXkKPT0KYXNzZXJ0CmZyYW1lX2RpZyAwCmZyYW1lX2RpZyAxCmNhbGxzdWIgYmlkXzMKcmV0c3ViCgovLyBjbGFpbV9hc3NldF9jYXN0ZXIKY2xhaW1hc3NldGNhc3Rlcl8xMDoKcHJvdG8gMCAwCmludGNfMCAvLyAwCnR4bmEgQXBwbGljYXRpb25BcmdzIDEKaW50Y18wIC8vIDAKZ2V0Ynl0ZQpmcmFtZV9idXJ5IDAKZnJhbWVfZGlnIDAKY2FsbHN1YiBjbGFpbWFzc2V0XzQKcmV0c3ViCgovLyBjbGFpbV9iaWRfY2FzdGVyCmNsYWltYmlkY2FzdGVyXzExOgpwcm90byAwIDAKY2FsbHN1YiBjbGFpbWJpZF81CnJldHN1YgoKLy8gZ2V0X3RpbWVfY2FzdGVyCmdldHRpbWVjYXN0ZXJfMTI6CnByb3RvIDAgMAppbnRjXzAgLy8gMApjYWxsc3ViIGdldHRpbWVfNgpmcmFtZV9idXJ5IDAKcHVzaGJ5dGVzIDB4MTUxZjdjNzUgLy8gMHgxNTFmN2M3NQpmcmFtZV9kaWcgMAppdG9iCmNvbmNhdApsb2cKcmV0c3Vi",
        "clear": "I3ByYWdtYSB2ZXJzaW9uIDgKcHVzaGludCAwIC8vIDAKcmV0dXJu"
    },
    "state": {
        "global": {
            "num_byte_slices": 1,
            "num_uints": 3
        },
        "local": {
            "num_byte_slices": 0,
            "num_uints": 0
        }
    },
    "schema": {
        "global": {
            "declared": {
                "asa_id": {
                    "type": "uint64",
                    "key": "asa_id",
                    "descr": "Este es el ID del asset a subastarse, si es cero, la subasta aun no inicia."
                },
                "auction_end": {
                    "type": "uint64",
                    "key": "auction_end",
                    "descr": "Duracion de la subasta, si es cero, la subasta aun no ha iniciado"
                },
                "highest_bid": {
                    "type": "uint64",
                    "key": "highest_bid",
                    "descr": "Apuesta mayor hasta el momento"
                },
                "winner": {
                    "type": "bytes",
                    "key": "winner",
                    "descr": "Cuenta del apostador mayor, ganador hasta ese momento, si es vacio, no hay ganador a\u00fan"
                }
            },
            "reserved": {}
        },
        "local": {
            "declared": {},
            "reserved": {}
        }
    },
    "contract": {
        "name": "auction",
        "methods": [
            {
                "name": "optin_to_asset",
                "args": [
                    {
                        "type": "pay",
                        "name": "payment_to_contract"
                    },
                    {
                        "type": "asset",
                        "name": "asset"
                    }
                ],
                "returns": {
                    "type": "void"
                }
            },
            {
                "name": "start",
                "args": [
                    {
                        "type": "uint64",
                        "name": "length"
                    },
                    {
                        "type": "uint64",
                        "name": "min"
                    },
                    {
                        "type": "axfer",
                        "name": "axfer"
                    }
                ],
                "returns": {
                    "type": "void"
                }
            },
            {
                "name": "bid",
                "args": [
                    {
                        "type": "pay",
                        "name": "payment"
                    },
                    {
                        "type": "account",
                        "name": "prewinner"
                    }
                ],
                "returns": {
                    "type": "void"
                }
            },
            {
                "name": "claim_asset",
                "args": [
                    {
                        "type": "asset",
                        "name": "asset"
                    }
                ],
                "returns": {
                    "type": "void"
                }
            },
            {
                "name": "claim_bid",
                "args": [],
                "returns": {
                    "type": "void"
                }
            },
            {
                "name": "get_time",
                "args": [],
                "returns": {
                    "type": "uint64"
                }
            }
        ],
        "networks": {}
    },
    "bare_call_config": {
        "no_op": "CREATE"
    }
}"""
APP_SPEC = algokit_utils.ApplicationSpecification.from_json(_APP_SPEC_JSON)
_TReturn = typing.TypeVar("_TReturn")


class _ArgsBase(ABC, typing.Generic[_TReturn]):
    @staticmethod
    @abstractmethod
    def method() -> str:
        ...


_TArgs = typing.TypeVar("_TArgs", bound=_ArgsBase[typing.Any])


@dataclasses.dataclass(kw_only=True)
class _TArgsHolder(typing.Generic[_TArgs]):
    args: _TArgs


def _filter_none(value: dict | typing.Any) -> dict | typing.Any:
    if isinstance(value, dict):
        return {k: _filter_none(v) for k, v in value.items() if v is not None}
    return value


def _as_dict(data: typing.Any, *, convert_all: bool = True) -> dict[str, typing.Any]:
    if data is None:
        return {}
    if not dataclasses.is_dataclass(data):
        raise TypeError(f"{data} must be a dataclass")
    if convert_all:
        result = dataclasses.asdict(data)
    else:
        result = {f.name: getattr(data, f.name) for f in dataclasses.fields(data)}
    return _filter_none(result)


def _convert_transaction_parameters(
    transaction_parameters: algokit_utils.TransactionParameters | None,
) -> algokit_utils.CommonCallParametersDict:
    return typing.cast(algokit_utils.CommonCallParametersDict, _as_dict(transaction_parameters))


def _convert_call_transaction_parameters(
    transaction_parameters: algokit_utils.TransactionParameters | None,
) -> algokit_utils.OnCompleteCallParametersDict:
    return typing.cast(algokit_utils.OnCompleteCallParametersDict, _as_dict(transaction_parameters))


def _convert_create_transaction_parameters(
    transaction_parameters: algokit_utils.TransactionParameters | None,
    on_complete: algokit_utils.OnCompleteActionName,
) -> algokit_utils.CreateCallParametersDict:
    result = typing.cast(algokit_utils.CreateCallParametersDict, _as_dict(transaction_parameters))
    on_complete_enum = on_complete.replace("_", " ").title().replace(" ", "") + "OC"
    result["on_complete"] = getattr(algosdk.transaction.OnComplete, on_complete_enum)
    return result


def _convert_deploy_args(
    deploy_args: algokit_utils.DeployCallArgs | None,
) -> algokit_utils.ABICreateCallArgsDict | None:
    if deploy_args is None:
        return None

    deploy_args_dict = typing.cast(algokit_utils.ABICreateCallArgsDict, _as_dict(deploy_args))
    if isinstance(deploy_args, _TArgsHolder):
        deploy_args_dict["args"] = _as_dict(deploy_args.args)
        deploy_args_dict["method"] = deploy_args.args.method()

    return deploy_args_dict


@dataclasses.dataclass(kw_only=True)
class OptinToAssetArgs(_ArgsBase[None]):
    payment_to_contract: TransactionWithSigner
    asset: int

    @staticmethod
    def method() -> str:
        return "optin_to_asset(pay,asset)void"


@dataclasses.dataclass(kw_only=True)
class StartArgs(_ArgsBase[None]):
    length: int
    min: int
    axfer: TransactionWithSigner

    @staticmethod
    def method() -> str:
        return "start(uint64,uint64,axfer)void"


@dataclasses.dataclass(kw_only=True)
class BidArgs(_ArgsBase[None]):
    payment: TransactionWithSigner
    prewinner: str | bytes

    @staticmethod
    def method() -> str:
        return "bid(pay,account)void"


@dataclasses.dataclass(kw_only=True)
class ClaimAssetArgs(_ArgsBase[None]):
    asset: int

    @staticmethod
    def method() -> str:
        return "claim_asset(asset)void"


@dataclasses.dataclass(kw_only=True)
class ClaimBidArgs(_ArgsBase[None]):
    @staticmethod
    def method() -> str:
        return "claim_bid()void"


@dataclasses.dataclass(kw_only=True)
class GetTimeArgs(_ArgsBase[int]):
    @staticmethod
    def method() -> str:
        return "get_time()uint64"


class ByteReader:
    def __init__(self, data: bytes):
        self._data = data

    @property
    def as_bytes(self) -> bytes:
        return self._data

    @property
    def as_str(self) -> str:
        return self._data.decode("utf8")

    @property
    def as_base64(self) -> str:
        return base64.b64encode(self._data).decode("utf8")

    @property
    def as_hex(self) -> str:
        return self._data.hex()


class GlobalState:
    def __init__(self, data: dict[bytes, bytes | int]):
        self.asa_id = typing.cast(int, data.get(b"asa_id"))
        """Este es el ID del asset a subastarse, si es cero, la subasta aun no inicia."""
        self.auction_end = typing.cast(int, data.get(b"auction_end"))
        """Duracion de la subasta, si es cero, la subasta aun no ha iniciado"""
        self.highest_bid = typing.cast(int, data.get(b"highest_bid"))
        """Apuesta mayor hasta el momento"""
        self.winner = ByteReader(typing.cast(bytes, data.get(b"winner")))
        """Cuenta del apostador mayor, ganador hasta ese momento, si es vacio, no hay ganador aún"""


class Composer:

    def __init__(self, app_client: algokit_utils.ApplicationClient, atc: AtomicTransactionComposer):
        self.app_client = app_client
        self.atc = atc

    def build(self) -> AtomicTransactionComposer:
        return self.atc

    def execute(self) -> AtomicTransactionResponse:
        return self.app_client.execute_atc(self.atc)

    def optin_to_asset(
        self,
        *,
        payment_to_contract: TransactionWithSigner,
        asset: int,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
    ) -> "Composer":
        """Adds a call to `optin_to_asset(pay,asset)void` ABI method
        
        :param TransactionWithSigner payment_to_contract: The `payment_to_contract` ABI parameter
        :param int asset: The `asset` ABI parameter
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns Composer: This Composer instance"""

        args = OptinToAssetArgs(
            payment_to_contract=payment_to_contract,
            asset=asset,
        )
        self.app_client.compose_call(
            self.atc,
            call_abi_method=args.method(),
            transaction_parameters=_convert_call_transaction_parameters(transaction_parameters),
            **_as_dict(args, convert_all=True),
        )
        return self

    def start(
        self,
        *,
        length: int,
        min: int,
        axfer: TransactionWithSigner,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
    ) -> "Composer":
        """Adds a call to `start(uint64,uint64,axfer)void` ABI method
        
        :param int length: The `length` ABI parameter
        :param int min: The `min` ABI parameter
        :param TransactionWithSigner axfer: The `axfer` ABI parameter
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns Composer: This Composer instance"""

        args = StartArgs(
            length=length,
            min=min,
            axfer=axfer,
        )
        self.app_client.compose_call(
            self.atc,
            call_abi_method=args.method(),
            transaction_parameters=_convert_call_transaction_parameters(transaction_parameters),
            **_as_dict(args, convert_all=True),
        )
        return self

    def bid(
        self,
        *,
        payment: TransactionWithSigner,
        prewinner: str | bytes,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
    ) -> "Composer":
        """Adds a call to `bid(pay,account)void` ABI method
        
        :param TransactionWithSigner payment: The `payment` ABI parameter
        :param str | bytes prewinner: The `prewinner` ABI parameter
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns Composer: This Composer instance"""

        args = BidArgs(
            payment=payment,
            prewinner=prewinner,
        )
        self.app_client.compose_call(
            self.atc,
            call_abi_method=args.method(),
            transaction_parameters=_convert_call_transaction_parameters(transaction_parameters),
            **_as_dict(args, convert_all=True),
        )
        return self

    def claim_asset(
        self,
        *,
        asset: int,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
    ) -> "Composer":
        """Adds a call to `claim_asset(asset)void` ABI method
        
        :param int asset: The `asset` ABI parameter
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns Composer: This Composer instance"""

        args = ClaimAssetArgs(
            asset=asset,
        )
        self.app_client.compose_call(
            self.atc,
            call_abi_method=args.method(),
            transaction_parameters=_convert_call_transaction_parameters(transaction_parameters),
            **_as_dict(args, convert_all=True),
        )
        return self

    def claim_bid(
        self,
        *,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
    ) -> "Composer":
        """Adds a call to `claim_bid()void` ABI method
        
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns Composer: This Composer instance"""

        args = ClaimBidArgs()
        self.app_client.compose_call(
            self.atc,
            call_abi_method=args.method(),
            transaction_parameters=_convert_call_transaction_parameters(transaction_parameters),
            **_as_dict(args, convert_all=True),
        )
        return self

    def get_time(
        self,
        *,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
    ) -> "Composer":
        """Adds a call to `get_time()uint64` ABI method
        
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns Composer: This Composer instance"""

        args = GetTimeArgs()
        self.app_client.compose_call(
            self.atc,
            call_abi_method=args.method(),
            transaction_parameters=_convert_call_transaction_parameters(transaction_parameters),
            **_as_dict(args, convert_all=True),
        )
        return self

    def create_bare(
        self,
        *,
        on_complete: typing.Literal["no_op"] = "no_op",
        transaction_parameters: algokit_utils.CreateTransactionParameters | None = None,
    ) -> "Composer":
        """Adds a call to create an application using the no_op bare method
        
        :param typing.Literal[no_op] on_complete: On completion type to use
        :param algokit_utils.CreateTransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns Composer: This Composer instance"""

        self.app_client.compose_create(
            self.atc,
            call_abi_method=False,
            transaction_parameters=_convert_create_transaction_parameters(transaction_parameters, on_complete),
        )
        return self

    def clear_state(
        self,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
        app_args: list[bytes] | None = None,
    ) -> "Composer":
        """Adds a call to the application with on completion set to ClearState
    
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :param list[bytes] | None app_args: (optional) Application args to pass"""
    
        self.app_client.compose_clear_state(self.atc, _convert_transaction_parameters(transaction_parameters), app_args)
        return self


class AuctionClient:
    """A class for interacting with the auction app providing high productivity and
    strongly typed methods to deploy and call the app"""

    @typing.overload
    def __init__(
        self,
        algod_client: algosdk.v2client.algod.AlgodClient,
        *,
        app_id: int = 0,
        signer: TransactionSigner | algokit_utils.Account | None = None,
        sender: str | None = None,
        suggested_params: algosdk.transaction.SuggestedParams | None = None,
        template_values: algokit_utils.TemplateValueMapping | None = None,
        app_name: str | None = None,
    ) -> None:
        ...

    @typing.overload
    def __init__(
        self,
        algod_client: algosdk.v2client.algod.AlgodClient,
        *,
        creator: str | algokit_utils.Account,
        indexer_client: algosdk.v2client.indexer.IndexerClient | None = None,
        existing_deployments: algokit_utils.AppLookup | None = None,
        signer: TransactionSigner | algokit_utils.Account | None = None,
        sender: str | None = None,
        suggested_params: algosdk.transaction.SuggestedParams | None = None,
        template_values: algokit_utils.TemplateValueMapping | None = None,
        app_name: str | None = None,
    ) -> None:
        ...

    def __init__(
        self,
        algod_client: algosdk.v2client.algod.AlgodClient,
        *,
        creator: str | algokit_utils.Account | None = None,
        indexer_client: algosdk.v2client.indexer.IndexerClient | None = None,
        existing_deployments: algokit_utils.AppLookup | None = None,
        app_id: int = 0,
        signer: TransactionSigner | algokit_utils.Account | None = None,
        sender: str | None = None,
        suggested_params: algosdk.transaction.SuggestedParams | None = None,
        template_values: algokit_utils.TemplateValueMapping | None = None,
        app_name: str | None = None,
    ) -> None:
        """
        AuctionClient can be created with an app_id to interact with an existing application, alternatively
        it can be created with a creator and indexer_client specified to find existing applications by name and creator.
        
        :param AlgodClient algod_client: AlgoSDK algod client
        :param int app_id: The app_id of an existing application, to instead find the application by creator and name
        use the creator and indexer_client parameters
        :param str | Account creator: The address or Account of the app creator to resolve the app_id
        :param IndexerClient indexer_client: AlgoSDK indexer client, only required if deploying or finding app_id by
        creator and app name
        :param AppLookup existing_deployments:
        :param TransactionSigner | Account signer: Account or signer to use to sign transactions, if not specified and
        creator was passed as an Account will use that.
        :param str sender: Address to use as the sender for all transactions, will use the address associated with the
        signer if not specified.
        :param TemplateValueMapping template_values: Values to use for TMPL_* template variables, dictionary keys should
        *NOT* include the TMPL_ prefix
        :param str | None app_name: Name of application to use when deploying, defaults to name defined on the
        Application Specification
            """

        self.app_spec = APP_SPEC
        
        # calling full __init__ signature, so ignoring mypy warning about overloads
        self.app_client = algokit_utils.ApplicationClient(  # type: ignore[call-overload, misc]
            algod_client=algod_client,
            app_spec=self.app_spec,
            app_id=app_id,
            creator=creator,
            indexer_client=indexer_client,
            existing_deployments=existing_deployments,
            signer=signer,
            sender=sender,
            suggested_params=suggested_params,
            template_values=template_values,
            app_name=app_name,
        )

    @property
    def algod_client(self) -> algosdk.v2client.algod.AlgodClient:
        return self.app_client.algod_client

    @property
    def app_id(self) -> int:
        return self.app_client.app_id

    @app_id.setter
    def app_id(self, value: int) -> None:
        self.app_client.app_id = value

    @property
    def app_address(self) -> str:
        return self.app_client.app_address

    @property
    def sender(self) -> str | None:
        return self.app_client.sender

    @sender.setter
    def sender(self, value: str) -> None:
        self.app_client.sender = value

    @property
    def signer(self) -> TransactionSigner | None:
        return self.app_client.signer

    @signer.setter
    def signer(self, value: TransactionSigner) -> None:
        self.app_client.signer = value

    @property
    def suggested_params(self) -> algosdk.transaction.SuggestedParams | None:
        return self.app_client.suggested_params

    @suggested_params.setter
    def suggested_params(self, value: algosdk.transaction.SuggestedParams | None) -> None:
        self.app_client.suggested_params = value

    def get_global_state(self) -> GlobalState:
        """Returns the application's global state wrapped in a strongly typed class with options to format the stored value"""

        state = typing.cast(dict[bytes, bytes | int], self.app_client.get_global_state(raw=True))
        return GlobalState(state)

    def optin_to_asset(
        self,
        *,
        payment_to_contract: TransactionWithSigner,
        asset: int,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
    ) -> algokit_utils.ABITransactionResponse[None]:
        """Calls `optin_to_asset(pay,asset)void` ABI method
        
        :param TransactionWithSigner payment_to_contract: The `payment_to_contract` ABI parameter
        :param int asset: The `asset` ABI parameter
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns algokit_utils.ABITransactionResponse[None]: The result of the transaction"""

        args = OptinToAssetArgs(
            payment_to_contract=payment_to_contract,
            asset=asset,
        )
        result = self.app_client.call(
            call_abi_method=args.method(),
            transaction_parameters=_convert_call_transaction_parameters(transaction_parameters),
            **_as_dict(args, convert_all=True),
        )
        return result

    def start(
        self,
        *,
        length: int,
        min: int,
        axfer: TransactionWithSigner,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
    ) -> algokit_utils.ABITransactionResponse[None]:
        """Calls `start(uint64,uint64,axfer)void` ABI method
        
        :param int length: The `length` ABI parameter
        :param int min: The `min` ABI parameter
        :param TransactionWithSigner axfer: The `axfer` ABI parameter
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns algokit_utils.ABITransactionResponse[None]: The result of the transaction"""

        args = StartArgs(
            length=length,
            min=min,
            axfer=axfer,
        )
        result = self.app_client.call(
            call_abi_method=args.method(),
            transaction_parameters=_convert_call_transaction_parameters(transaction_parameters),
            **_as_dict(args, convert_all=True),
        )
        return result

    def bid(
        self,
        *,
        payment: TransactionWithSigner,
        prewinner: str | bytes,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
    ) -> algokit_utils.ABITransactionResponse[None]:
        """Calls `bid(pay,account)void` ABI method
        
        :param TransactionWithSigner payment: The `payment` ABI parameter
        :param str | bytes prewinner: The `prewinner` ABI parameter
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns algokit_utils.ABITransactionResponse[None]: The result of the transaction"""

        args = BidArgs(
            payment=payment,
            prewinner=prewinner,
        )
        result = self.app_client.call(
            call_abi_method=args.method(),
            transaction_parameters=_convert_call_transaction_parameters(transaction_parameters),
            **_as_dict(args, convert_all=True),
        )
        return result

    def claim_asset(
        self,
        *,
        asset: int,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
    ) -> algokit_utils.ABITransactionResponse[None]:
        """Calls `claim_asset(asset)void` ABI method
        
        :param int asset: The `asset` ABI parameter
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns algokit_utils.ABITransactionResponse[None]: The result of the transaction"""

        args = ClaimAssetArgs(
            asset=asset,
        )
        result = self.app_client.call(
            call_abi_method=args.method(),
            transaction_parameters=_convert_call_transaction_parameters(transaction_parameters),
            **_as_dict(args, convert_all=True),
        )
        return result

    def claim_bid(
        self,
        *,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
    ) -> algokit_utils.ABITransactionResponse[None]:
        """Calls `claim_bid()void` ABI method
        
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns algokit_utils.ABITransactionResponse[None]: The result of the transaction"""

        args = ClaimBidArgs()
        result = self.app_client.call(
            call_abi_method=args.method(),
            transaction_parameters=_convert_call_transaction_parameters(transaction_parameters),
            **_as_dict(args, convert_all=True),
        )
        return result

    def get_time(
        self,
        *,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
    ) -> algokit_utils.ABITransactionResponse[int]:
        """Calls `get_time()uint64` ABI method
        
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns algokit_utils.ABITransactionResponse[int]: The result of the transaction"""

        args = GetTimeArgs()
        result = self.app_client.call(
            call_abi_method=args.method(),
            transaction_parameters=_convert_call_transaction_parameters(transaction_parameters),
            **_as_dict(args, convert_all=True),
        )
        return result

    def create_bare(
        self,
        *,
        on_complete: typing.Literal["no_op"] = "no_op",
        transaction_parameters: algokit_utils.CreateTransactionParameters | None = None,
    ) -> algokit_utils.TransactionResponse:
        """Creates an application using the no_op bare method
        
        :param typing.Literal[no_op] on_complete: On completion type to use
        :param algokit_utils.CreateTransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns algokit_utils.TransactionResponse: The result of the transaction"""

        result = self.app_client.create(
            call_abi_method=False,
            transaction_parameters=_convert_create_transaction_parameters(transaction_parameters, on_complete),
        )
        return result

    def clear_state(
        self,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
        app_args: list[bytes] | None = None,
    ) -> algokit_utils.TransactionResponse:
        """Calls the application with on completion set to ClearState
    
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :param list[bytes] | None app_args: (optional) Application args to pass
        :returns algokit_utils.TransactionResponse: The result of the transaction"""
    
        return self.app_client.clear_state(_convert_transaction_parameters(transaction_parameters), app_args)

    def deploy(
        self,
        version: str | None = None,
        *,
        signer: TransactionSigner | None = None,
        sender: str | None = None,
        allow_update: bool | None = None,
        allow_delete: bool | None = None,
        on_update: algokit_utils.OnUpdate = algokit_utils.OnUpdate.Fail,
        on_schema_break: algokit_utils.OnSchemaBreak = algokit_utils.OnSchemaBreak.Fail,
        template_values: algokit_utils.TemplateValueMapping | None = None,
        create_args: algokit_utils.DeployCallArgs | None = None,
        update_args: algokit_utils.DeployCallArgs | None = None,
        delete_args: algokit_utils.DeployCallArgs | None = None,
    ) -> algokit_utils.DeployResponse:
        """Deploy an application and update client to reference it.
        
        Idempotently deploy (create, update/delete if changed) an app against the given name via the given creator
        account, including deploy-time template placeholder substitutions.
        To understand the architecture decisions behind this functionality please see
        <https://github.com/algorandfoundation/algokit-cli/blob/main/docs/architecture-decisions/2023-01-12_smart-contract-deployment.md>
        
        ```{note}
        If there is a breaking state schema change to an existing app (and `on_schema_break` is set to
        'ReplaceApp' the existing app will be deleted and re-created.
        ```
        
        ```{note}
        If there is an update (different TEAL code) to an existing app (and `on_update` is set to 'ReplaceApp')
        the existing app will be deleted and re-created.
        ```
        
        :param str version: version to use when creating or updating app, if None version will be auto incremented
        :param algosdk.atomic_transaction_composer.TransactionSigner signer: signer to use when deploying app
        , if None uses self.signer
        :param str sender: sender address to use when deploying app, if None uses self.sender
        :param bool allow_delete: Used to set the `TMPL_DELETABLE` template variable to conditionally control if an app
        can be deleted
        :param bool allow_update: Used to set the `TMPL_UPDATABLE` template variable to conditionally control if an app
        can be updated
        :param OnUpdate on_update: Determines what action to take if an application update is required
        :param OnSchemaBreak on_schema_break: Determines what action to take if an application schema requirements
        has increased beyond the current allocation
        :param dict[str, int|str|bytes] template_values: Values to use for `TMPL_*` template variables, dictionary keys
        should *NOT* include the TMPL_ prefix
        :param algokit_utils.DeployCallArgs | None create_args: Arguments used when creating an application
        :param algokit_utils.DeployCallArgs | None update_args: Arguments used when updating an application
        :param algokit_utils.DeployCallArgs | None delete_args: Arguments used when deleting an application
        :return DeployResponse: details action taken and relevant transactions
        :raises DeploymentError: If the deployment failed"""

        return self.app_client.deploy(
            version,
            signer=signer,
            sender=sender,
            allow_update=allow_update,
            allow_delete=allow_delete,
            on_update=on_update,
            on_schema_break=on_schema_break,
            template_values=template_values,
            create_args=_convert_deploy_args(create_args),
            update_args=_convert_deploy_args(update_args),
            delete_args=_convert_deploy_args(delete_args),
        )

    def compose(self, atc: AtomicTransactionComposer | None = None) -> Composer:
        return Composer(self.app_client, atc or AtomicTransactionComposer())