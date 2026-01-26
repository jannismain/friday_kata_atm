from collections import Counter, defaultdict

import pytest

CoinSetID = str


class CoinSetRegistry:
    standard_coins = [200, 100, 50, 20, 10, 5, 2, 1]

    def __init__(self, custom_sets: dict[CoinSetID, list[int]] = {}):
        self.coin_sets = {"": self.standard_coins, **custom_sets}

    def get_available_coins(self, coin_set_id: CoinSetID = ""):
        return self.coin_sets[coin_set_id]


class ATM:
    def __init__(self, coin_set_registry: CoinSetRegistry = CoinSetRegistry()):
        self.registry = coin_set_registry

    def get_minimal_coins(
        self, total_amount_in_cents: int, coin_set_id: str = ""
    ) -> dict[int, int]:
        if total_amount_in_cents < 0:
            raise ValueError("only positive amounts are supported")

        returned_coins = defaultdict(lambda: 0)
        remaining_amount = total_amount_in_cents

        for coin in self.registry.get_available_coins(coin_set_id):
            while remaining_amount >= coin:
                returned_coins[coin] += 1
                remaining_amount -= coin

        return returned_coins


def test_should_get_no_coins_for_zero_amount():
    assert ATM().get_minimal_coins(0) == {}, "no money is returned"


def test_should_raise_error_when_negative_value_is_given():
    with pytest.raises(ValueError):
        ATM().get_minimal_coins(-1)


def test_should_get_single_coin_when_coin_with_that_value_exists():
    for amount in CoinSetRegistry.standard_coins:
        assert ATM().get_minimal_coins(amount) == {amount: 1}, (
            f"{amount} should return a single coin"
        )


def test_should_return_multiple_coins_with_different_values():
    result = ATM().get_minimal_coins(3)
    assert len(result) == 2
    assert result == {1: 1, 2: 1}


def test_should_return_multiple_coins_with_same_value_when_required():
    # assert get_minimal_coins(4) == {2: 2}
    assert_get_minimal_coins_returns([2, 2], 4)


def test_should_support_custom_coin_sets():
    assert ATM(CoinSetRegistry({"custom": [100, 33, 1]})).get_minimal_coins(
        133, "custom"
    ) == {
        100: 1,
        33: 1,
    }


def assert_get_minimal_coins_returns(expected_coins: list[int], amount_in_cents: int):
    expected_coins_dict = Counter(expected_coins)
    result = ATM().get_minimal_coins(amount_in_cents)
    assert result == expected_coins_dict


if __name__ == "__main__":
    import sys

    total_value = int(sys.argv[1])
    coins = dict(ATM().get_minimal_coins(total_value))
    [
        print((f"{k:2d} Cent" if k < 100 else f"{k // 100:2d} Euro") + f": {v}")
        for k, v in coins.items()
    ]
