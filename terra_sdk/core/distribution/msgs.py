"""Distribution module message types."""

from __future__ import annotations

import attr
from terra_proto.cosmos.distribution.v1beta1 import (
    MsgFundCommunityPool as MsgFundCommunityPool_pb,
)
from terra_proto.cosmos.distribution.v1beta1 import (
    MsgSetWithdrawAddress as MsgSetWithdrawAddress_pb,
)
from terra_proto.cosmos.distribution.v1beta1 import (
    MsgWithdrawDelegatorReward as MsgWithdrawDelegatorReward_pb,
)
from terra_proto.cosmos.distribution.v1beta1 import (
    MsgWithdrawValidatorCommission as MsgWithdrawValidatorCommission_pb,
)

from terra_sdk.core import AccAddress, Coins, ValAddress
from terra_sdk.core.msg import Msg

__all__ = [
    "MsgSetWithdrawAddress",
    "MsgWithdrawDelegationReward",
    "MsgWithdrawValidatorCommission",
    "MsgFundCommunityPool",
]


@attr.s
class MsgSetWithdrawAddress(Msg):
    """Modify the Withdraw Address of a delegator.

    Args:
        delegator_address: delegator
        withdraw_address: new withdraw address
    """

    type_amino = "distribution/MsgSetWithdrawAddress"
    """"""
    type_url = "/cosmos.distribution.v1beta1.MsgSetWithdrawAddress"
    """"""
    action = "set_withdraw_address"
    """"""

    delegator_address: AccAddress = attr.ib()
    withdraw_address: AccAddress = attr.ib()

    def to_amino(self) -> dict:
        return {
            "type": self.type_amino,
            "value": {
                "delegator_address": self.delegator_address,
                "withdraw_address": self.withdraw_address,
            },
        }

    def to_data(self) -> dict:
        return {
            "@type": self.type_url,
            "delegator_address": self.delegator_address,
            "withdraw_address": self.withdraw_address,
        }

    @classmethod
    def from_data(cls, data: dict) -> MsgSetWithdrawAddress:
        return cls(
            delegator_address=data["delegator_address"],
            withdraw_address=data["withdraw_address"],
        )

    def to_proto(self) -> MsgSetWithdrawAddress_pb:
        return MsgSetWithdrawAddress_pb(
            delegator_address=self.delegator_address,
            withdraw_address=self.withdraw_address,
        )

    @classmethod
    def from_proto(cls, data: MsgSetWithdrawAddress_pb) -> MsgSetWithdrawAddress:
        return cls(
            delegator_address=data["delegator_address"],
            withdraw_address=data["withdraw_address"],
        )


@attr.s
class MsgWithdrawDelegationReward(Msg):
    """Withdraw rewards for a delegation specified by a (delegator, validator) pair.

    Args:
        delegator_address: delegator
        validator_address: validator
    """

    type_amino = "distribution/MsgWithdrawDelegationReward"
    """"""
    type_url = "/cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward"
    """"""
    action = "withdraw_delegation_reward"
    """"""

    delegator_address: AccAddress = attr.ib()
    validator_address: ValAddress = attr.ib()

    def to_amino(self) -> dict:
        return {
            "type": self.type_amino,
            "value": {
                "delegator_address": self.delegator_address,
                "withdraw_address": self.withdraw_address,
            },
        }

    def to_data(self) -> dict:
        return {
            "@type": self.type_url,
            "delegator_address": self.delegator_address,
            "withdraw_address": self.withdraw_address,
        }

    @classmethod
    def from_data(cls, data: dict) -> MsgWithdrawDelegationReward:
        return cls(
            delegator_address=data["delegator_address"],
            validator_address=data["validator_address"],
        )

    def to_proto(self) -> MsgWithdrawDelegatorReward_pb:
        return MsgWithdrawDelegatorReward_pb(
            delegator_address=self.delegator_address,
            validator_address=self.validator_address,
        )

    @classmethod
    def from_proto(
        cls, data: MsgWithdrawDelegatorReward_pb
    ) -> MsgWithdrawDelegationReward:
        return cls(
            delegator_address=data["delegator_address"],
            validator_address=data["validator_address"],
        )


@attr.s
class MsgWithdrawValidatorCommission(Msg):
    """Withdraw rewards accrued for a validator gained through commissions.

    Args:
        validator_address: validator operator address
    """

    type_amino = "distribution/MsgWithdrawValidatorCommission"
    """"""
    type_url = "/cosmos.distribution.v1beta1.MsgWithdrawValidatorCommission"
    """"""
    action = "withdraw_validator_commission"
    """"""

    validator_address: ValAddress = attr.ib()

    def to_amino(self) -> dict:
        return {
            "type": self.type_amino,
            "value": {"validator_address": self.validator_address},
        }

    def to_data(self) -> dict:
        return {"@type": self.type_url, "validator_address": self.validator_address}

    @classmethod
    def from_data(cls, data: dict) -> MsgWithdrawValidatorCommission:
        return cls(validator_address=data["validator_address"])

    def to_proto(self) -> MsgWithdrawValidatorCommission_pb:
        return MsgWithdrawValidatorCommission_pb(
            validator_address=self.validator_address
        )

    @classmethod
    def from_proto(
        cls, data: MsgWithdrawValidatorCommission_pb
    ) -> MsgWithdrawValidatorCommission:
        return cls(validator_address=data["validator_address"])


@attr.s
class MsgFundCommunityPool(Msg):
    """Deposit assets to the Community Pool.

    Args:
        depositor (AccAddress): sender
        amount (Coins): amount to fund community pool with
    """

    type_amino = "distribution/MsgFundCommunityPool"
    """"""
    type_url = "/cosmos.distribution.v1beta1.MsgFundCommunityPool"
    """"""

    depositor: AccAddress = attr.ib()
    amount: Coins = attr.ib(converter=Coins)

    def to_amino(self) -> dict:
        return {
            "type": self.type_amino,
            "value": {"depositor": self.depositor, "amount": self.amount.to_amino()},
        }

    def to_data(self) -> dict:
        return {
            "@type": self.type_url,
            "depositor": self.depositor,
            "amount": self.amount.to_data(),
        }

    @classmethod
    def from_data(cls, data: dict) -> MsgFundCommunityPool:
        return cls(depositor=data["depositor"], amount=Coins.from_data(data["amount"]))

    def to_proto(self) -> MsgFundCommunityPool_pb:
        return MsgFundCommunityPool_pb(
            depositor=self.depositor, amount=self.amount.to_proto()
        )

    @classmethod
    def from_proto(cls, data: MsgFundCommunityPool_pb) -> MsgFundCommunityPool:
        return cls(depositor=data["depositor"], amount=Coins.from_proto(data["amount"]))
